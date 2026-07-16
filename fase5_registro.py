"""
FASE 5 — Registro de trabajo compartido entre sesiones (unidad = COMUNA)
=======================================================================
Coordina varias sesiones generando los JSON `NormativaPRC`, una comuna cada
una, sin pisarse. Mismo reclamo atómico que las fases anteriores.

Lo distintivo de Fase 5: `completar` NO solo registra — VALIDA el JSON
producido contra la capa GeoJSON de la comuna:
  - el archivo parsea y es un array no vacío
  - extrae los `zona_codigo` del JSON y los `ZONA` del GeoJSON
  - reporta cobertura y, sobre todo, las zonas del GeoJSON que quedaron SIN
    ficha (el error Ñuñoa: puntos que caen a "parámetros estimados").
  El emparejamiento tolera el prefijo 'Z' inicial (GeoJSON 'ICH1' <-> ficha
  'ZICH1'), igual que el matcher de la app.

Si quedan zonas del GeoJSON sin ficha, `completar` AVISA pero no bloquea —
la sesión decide si son omisiones reales (rehacer) o zonas legítimamente
ausentes de la ordenanza (dejar constancia en --nota).

Comandos: tomar / completar / fallar / liberar / estado / consolidar
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
WEB = Path(os.environ.get("ARCHIBLOCKS_WEB_PUBLIC", RAIZ.parent / "projectbook" / "Web" / "public"))
GEODIR = WEB / "geo-data"
NORMADIR = WEB / "norma-data"
COLA = RAIZ / "fase5_cola.json"
CARPETA_REGISTRO = RAIZ / "fase5_registro"
CONSOLIDADO = RAIZ / "fase5_produccion.csv"

HORAS_HUERFANO = 4  # una comuna toma más que un documento; margen mayor

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except AttributeError:
    pass


def ahora() -> str:
    return datetime.now().isoformat(timespec="seconds")


def cargar_cola() -> list[dict]:
    if not COLA.exists():
        raise SystemExit(f"Falta {COLA.name}. Genera la cola:  python fase5_cola.py")
    return json.loads(COLA.read_text(encoding="utf-8"))["items"]


def ruta_registro(comuna: str) -> Path:
    if not re.fullmatch(r"[a-z0-9_]+", comuna):
        raise SystemExit(f"Comuna inválida: {comuna!r}")
    return CARPETA_REGISTRO / f"{comuna}.json"


def leer_registro(comuna: str) -> dict:
    ruta = ruta_registro(comuna)
    if not ruta.exists():
        raise SystemExit(f"La comuna {comuna} no está reclamada por nadie.")
    return json.loads(ruta.read_text(encoding="utf-8"))


def escribir_registro(comuna: str, datos: dict) -> None:
    ruta_registro(comuna).write_text(
        json.dumps(datos, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def horas_desde(marca: str) -> float:
    try:
        return (datetime.now() - datetime.fromisoformat(marca)).total_seconds() / 3600
    except ValueError:
        return 0.0


def normalizar_codigo(c: str) -> str:
    """Normaliza para el matcher: mayúsculas, sin espacios, tolera prefijo Z."""
    c = re.sub(r"[\s]", "", str(c).upper())
    c = re.sub(r"^Z[-_]?", "", c)  # tolera Z / Z- / Z_
    return c


def codigos_geojson(geojson_file: str) -> set[str]:
    ruta = GEODIR / geojson_file
    if not ruta.is_file():
        return set()
    data = json.loads(ruta.read_text(encoding="utf-8"))
    codigos = set()
    for feat in data.get("features", []):
        z = (feat.get("properties") or {}).get("ZONA")
        if z:
            codigos.add(normalizar_codigo(z))
    return codigos


# ---------------------------------------------------------------------------
# tomar
# ---------------------------------------------------------------------------

def cmd_tomar(argumentos: argparse.Namespace) -> None:
    CARPETA_REGISTRO.mkdir(exist_ok=True)
    items = cargar_cola()

    reclamados: list[dict] = []
    for item in items:
        if len(reclamados) >= argumentos.n:
            break
        ruta = ruta_registro(item["comuna"])
        reclamo = {
            "comuna": item["comuna"],
            "region": item["region"],
            "geojson_file": item["geojson_file"],
            "salida_json": item["salida_json"],
            "markdowns": item["markdowns"],
            "estado": "EN_PROCESO",
            "sesion": argumentos.sesion,
            "inicio": ahora(),
            "fin": None,
            "resultado": None,
        }
        try:
            with ruta.open("x", encoding="utf-8") as manejador:
                json.dump(reclamo, manejador, ensure_ascii=False, indent=2)
        except FileExistsError:
            continue
        reclamados.append(item)

    if not reclamados:
        print(json.dumps({"reclamados": 0, "items": [],
                          "mensaje": "No quedan comunas libres."}, ensure_ascii=False))
        return
    print(json.dumps({"reclamados": len(reclamados), "sesion": argumentos.sesion,
                      "items": reclamados}, ensure_ascii=False, indent=1))


# ---------------------------------------------------------------------------
# completar (con validación GeoJSON)
# ---------------------------------------------------------------------------

def cmd_completar(argumentos: argparse.Namespace) -> None:
    registro = leer_registro(argumentos.comuna)
    if registro["estado"] == "HECHO":
        raise SystemExit(f"{argumentos.comuna} ya está HECHO. Libera y toma de nuevo si quieres rehacer.")

    # El JSON debe estar guardado en norma-data con el nombre esperado
    ruta_json = NORMADIR / registro["salida_json"]
    if not ruta_json.is_file():
        raise SystemExit(f"No existe {ruta_json}. Guarda el JSON en norma-data antes de completar.")

    try:
        data = json.loads(ruta_json.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise SystemExit(f"El JSON no parsea: {e}. Corrígelo antes de completar.")

    if not isinstance(data, list) or not data:
        raise SystemExit("El JSON debe ser un array no vacío de zonas.")

    # Códigos de zona en la ficha vs en el GeoJSON
    fichas = {normalizar_codigo(z.get("zona_codigo", "")) for z in data if z.get("zona_codigo")}
    geo = codigos_geojson(registro["geojson_file"])

    sin_ficha = sorted(geo - fichas)      # zonas del GeoJSON que quedaron sin ficha (Ñuñoa)
    sin_geojson = sorted(fichas - geo)    # fichas que no tienen polígono (subzonas, patrimonial)
    cubiertas = len(geo & fichas)

    registro.update({
        "estado": "HECHO",
        "fin": ahora(),
        "resultado": {
            "archivo_json": registro["salida_json"],
            "zonas_ficha": len(data),
            "zonas_geojson": len(geo),
            "zonas_cubiertas": cubiertas,
            "geojson_sin_ficha": sin_ficha,
            "ficha_sin_geojson": sin_geojson,
            "confianza": argumentos.confianza,
            "nota": argumentos.nota,
        },
    })
    escribir_registro(argumentos.comuna, registro)

    print(f"HECHO {argumentos.comuna}: {len(data)} zonas en la ficha")
    print(f"  cobertura GeoJSON: {cubiertas}/{len(geo)} zonas del plano tienen ficha")
    if sin_ficha:
        print(f"  ⚠ {len(sin_ficha)} zonas del GeoJSON SIN ficha (revisar si son omisiones): "
              f"{', '.join(sin_ficha[:15])}{' ...' if len(sin_ficha) > 15 else ''}")
    if sin_geojson:
        print(f"  · {len(sin_geojson)} fichas sin polígono en el GeoJSON (normal en subzonas/patrimonio): "
              f"{', '.join(sin_geojson[:15])}{' ...' if len(sin_geojson) > 15 else ''}")


def cmd_fallar(argumentos: argparse.Namespace) -> None:
    registro = leer_registro(argumentos.comuna)
    registro.update({"estado": "FALLIDO", "fin": ahora(),
                     "resultado": {"motivo": argumentos.motivo}})
    escribir_registro(argumentos.comuna, registro)
    print(f"FALLIDO {argumentos.comuna}: {argumentos.motivo}")


def cmd_liberar(argumentos: argparse.Namespace) -> None:
    ruta = ruta_registro(argumentos.comuna)
    if not ruta.exists():
        raise SystemExit(f"{argumentos.comuna} no estaba reclamada.")
    estado = json.loads(ruta.read_text(encoding="utf-8")).get("estado")
    ruta.unlink()
    print(f"LIBERADA {argumentos.comuna} (estaba {estado}); vuelve a la cola.")


# ---------------------------------------------------------------------------
# estado / consolidar
# ---------------------------------------------------------------------------

def cmd_estado(argumentos: argparse.Namespace) -> None:
    items = {i["comuna"]: i for i in cargar_cola()}
    CARPETA_REGISTRO.mkdir(exist_ok=True)
    registros = []
    for ruta in sorted(CARPETA_REGISTRO.glob("*.json")):
        try:
            registros.append(json.loads(ruta.read_text(encoding="utf-8")))
        except json.JSONDecodeError:
            print(f"AVISO: registro corrupto: {ruta.name}")
    if argumentos.sesion:
        registros = [r for r in registros if r.get("sesion") == argumentos.sesion]

    por_estado = collections_defaultdict(registros)
    hechos = por_estado.get("HECHO", [])
    zonas = sum((r.get("resultado") or {}).get("zonas_ficha", 0) for r in hechos)

    print(f"=== FASE 5 — TABLERO ({ahora()}) ===")
    print(f"Cola (PROCESAR)     : {len(items)}")
    print(f"Reclamadas          : {len(registros)}")
    print(f"  HECHO             : {len(hechos)}  (zonas producidas: {zonas})")
    print(f"  EN_PROCESO        : {len(por_estado.get('EN_PROCESO', []))}")
    print(f"  FALLIDO           : {len(por_estado.get('FALLIDO', []))}")
    print(f"Libres en cola      : {len(items) - len(registros)}")

    por_sesion = {}
    for r in registros:
        por_sesion[r.get("sesion", "?")] = por_sesion.get(r.get("sesion", "?"), 0) + 1
    if por_sesion:
        print("\nPor sesión:", "  ".join(f"{s}={n}" for s, n in sorted(por_sesion.items())))

    en_proc = por_estado.get("EN_PROCESO", [])
    if en_proc:
        print("\nEN_PROCESO ahora:")
        for r in sorted(en_proc, key=lambda x: x["inicio"]):
            edad = horas_desde(r["inicio"])
            marca = "  <-- HUÉRFANO?" if edad > HORAS_HUERFANO else ""
            print(f"  {r['sesion']:6s} {edad:5.1f}h  {r['comuna']:20s}{marca}")

    # avisos de cobertura en los completados
    con_hueco = [r for r in hechos if (r.get("resultado") or {}).get("geojson_sin_ficha")]
    if con_hueco:
        print("\nHECHAS con zonas del GeoJSON sin ficha (revisar):")
        for r in con_hueco:
            res = r["resultado"]
            print(f"  {r['comuna']:20s} {len(res['geojson_sin_ficha'])} zonas sin ficha: "
                  f"{', '.join(res['geojson_sin_ficha'][:10])}")

    fallidos = por_estado.get("FALLIDO", [])
    if fallidos:
        print("\nFALLIDAS:")
        for r in fallidos:
            print(f"  {r['comuna']:20s} {(r.get('resultado') or {}).get('motivo','')[:60]}")


def collections_defaultdict(registros):
    d = {"EN_PROCESO": [], "HECHO": [], "FALLIDO": []}
    for r in registros:
        d.setdefault(r.get("estado", "?"), []).append(r)
    return d


def cmd_consolidar(argumentos: argparse.Namespace) -> None:
    CARPETA_REGISTRO.mkdir(exist_ok=True)
    filas = []
    for ruta in sorted(CARPETA_REGISTRO.glob("*.json")):
        registro = json.loads(ruta.read_text(encoding="utf-8"))
        if registro.get("estado") != "HECHO":
            continue
        r = registro.get("resultado") or {}
        filas.append({
            "comuna": registro["comuna"],
            "region": registro["region"],
            "archivo_json": r.get("archivo_json", ""),
            "zonas_ficha": r.get("zonas_ficha", 0),
            "zonas_geojson": r.get("zonas_geojson", 0),
            "zonas_cubiertas": r.get("zonas_cubiertas", 0),
            "geojson_sin_ficha": " ".join(r.get("geojson_sin_ficha", [])),
            "confianza": r.get("confianza", ""),
            "nota": r.get("nota", ""),
            "sesion": registro.get("sesion", ""),
            "fin": registro.get("fin", ""),
        })
    if not filas:
        print("Aún no hay comunas HECHO que consolidar.")
        return
    filas.sort(key=lambda f: (f["region"], f["comuna"]))
    with CONSOLIDADO.open("w", newline="", encoding="utf-8") as manejador:
        escritor = csv.DictWriter(manejador, fieldnames=list(filas[0].keys()))
        escritor.writeheader()
        escritor.writerows(filas)
    print(f"Consolidado: {CONSOLIDADO.name} ({len(filas)} comunas, "
          f"{sum(f['zonas_ficha'] for f in filas)} zonas)")


def main() -> None:
    a = argparse.ArgumentParser(description="Registro compartido de la Fase 5.")
    sub = a.add_subparsers(dest="comando", required=True)

    p = sub.add_parser("tomar")
    p.add_argument("--sesion", required=True)
    p.add_argument("--n", type=int, default=1)
    p.set_defaults(funcion=cmd_tomar)

    p = sub.add_parser("completar")
    p.add_argument("comuna")
    p.add_argument("--confianza", choices=["ALTA", "MEDIA", "BAJA"], default="ALTA")
    p.add_argument("--nota", default="")
    p.set_defaults(funcion=cmd_completar)

    p = sub.add_parser("fallar")
    p.add_argument("comuna")
    p.add_argument("--motivo", required=True)
    p.set_defaults(funcion=cmd_fallar)

    p = sub.add_parser("liberar")
    p.add_argument("comuna")
    p.set_defaults(funcion=cmd_liberar)

    p = sub.add_parser("estado")
    p.add_argument("--sesion")
    p.set_defaults(funcion=cmd_estado)

    p = sub.add_parser("consolidar")
    p.set_defaults(funcion=cmd_consolidar)

    args = a.parse_args()
    args.funcion(args)


if __name__ == "__main__":
    main()
