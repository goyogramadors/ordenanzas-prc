"""
FASE 4 — Registro de trabajo compartido entre sesiones
======================================================
Coordina VARIAS sesiones de Claude transcribiendo tablas de normas en
paralelo, sin pisarse. Mismo mecanismo que `fase3_registro.py`: reclamo
atómico por creación exclusiva de archivo, un JSON por documento.

Comandos
--------
  tomar      --sesion S1 [--n 3] [--comuna x]
             Reclama los próximos documentos libres (incluye rango de
             páginas y todo el contexto que dejó Fase 3).
  completar  <id> --archivo "ruta/al/markdown.md" --zonas 12
             --zonas-codigos "ZC-1,ZC-2,ZH-1,..." [--confianza ALTA]
             [--nota "..."]
  fallar     <id> --motivo "..."
  liberar    <id>
  estado     [--sesion S1]
  consolidar                  (genera fase4_extraccion.csv)

Diferencia clave con Fase 3: aquí `completar` exige `--archivo` (el .md
producido) y `--zonas` (cuántas zonas se transcribieron). Sirve para
auditar después si un documento "se completó" pero con menos zonas de las
que su propio rango sugería — el mismo error que costó caro en el proyecto
hermano (ordenanza-a-json): zonas omitidas en silencio quedan sin ficha.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from datetime import datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
COLA = RAIZ / "fase4_cola.json"
CARPETA_REGISTRO = RAIZ / "fase4_registro"
CONSOLIDADO = RAIZ / "fase4_extraccion.csv"
CARPETA_MARKDOWN = RAIZ / "extraccion_normas"

HORAS_HUERFANO = 3

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except AttributeError:
    pass


def ahora() -> str:
    return datetime.now().isoformat(timespec="seconds")


def cargar_cola() -> list[dict]:
    if not COLA.exists():
        raise SystemExit(f"Falta {COLA.name}. Genera la cola:  python fase4_cola.py")
    return json.loads(COLA.read_text(encoding="utf-8"))["items"]


def ruta_registro(id_doc: str) -> Path:
    if not re.fullmatch(r"[a-z0-9_]+", id_doc):
        raise SystemExit(f"Id inválido: {id_doc!r}")
    return CARPETA_REGISTRO / f"{id_doc}.json"


def leer_registro(id_doc: str) -> dict:
    ruta = ruta_registro(id_doc)
    if not ruta.exists():
        raise SystemExit(f"El documento {id_doc} no está reclamado por nadie.")
    return json.loads(ruta.read_text(encoding="utf-8"))


def escribir_registro(id_doc: str, datos: dict) -> None:
    ruta_registro(id_doc).write_text(
        json.dumps(datos, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def horas_desde(marca: str) -> float:
    try:
        return (datetime.now() - datetime.fromisoformat(marca)).total_seconds() / 3600
    except ValueError:
        return 0.0


# ---------------------------------------------------------------------------
# tomar
# ---------------------------------------------------------------------------

def cmd_tomar(argumentos: argparse.Namespace) -> None:
    CARPETA_REGISTRO.mkdir(exist_ok=True)
    items = cargar_cola()

    if argumentos.comuna:
        items = [i for i in items if i["comuna"] == argumentos.comuna]

    reclamados: list[dict] = []

    for item in items:
        if len(reclamados) >= argumentos.n:
            break

        ruta = ruta_registro(item["id"])
        reclamo = {
            "id": item["id"],
            "comuna": item["comuna"],
            "ruta": item["ruta"],
            "rangos": item["rangos"],
            "paginas_utiles": item["paginas_utiles"],
            "nota_fase3": item["nota_fase3"],
            "confianza_fase3": item["confianza_fase3"],
            "metodo_fase3": item["metodo_fase3"],
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
                          "mensaje": "No quedan documentos libres con ese filtro."},
                         ensure_ascii=False))
        return

    print(json.dumps({"reclamados": len(reclamados), "sesion": argumentos.sesion,
                      "items": reclamados}, ensure_ascii=False, indent=1))


# ---------------------------------------------------------------------------
# completar / fallar / liberar
# ---------------------------------------------------------------------------

def cmd_completar(argumentos: argparse.Namespace) -> None:
    registro = leer_registro(argumentos.id)

    if registro["estado"] == "HECHO":
        raise SystemExit(f"{argumentos.id} ya está HECHO (por {registro['sesion']}). "
                         "Si quieres rehacerlo: liberar y tomar de nuevo.")

    ruta_md = Path(argumentos.archivo)
    if not ruta_md.is_absolute():
        ruta_md = RAIZ / argumentos.archivo
    if not ruta_md.is_file():
        raise SystemExit(f"El archivo {argumentos.archivo} no existe. "
                         "Guarda el markdown antes de completar.")

    zonas_codigos = [z.strip() for z in (argumentos.zonas_codigos or "").split(",") if z.strip()]
    if zonas_codigos and len(zonas_codigos) != argumentos.zonas:
        raise SystemExit(f"--zonas ({argumentos.zonas}) no coincide con la cantidad de códigos "
                         f"en --zonas-codigos ({len(zonas_codigos)}).")

    registro.update({
        "estado": "HECHO",
        "fin": ahora(),
        "resultado": {
            "archivo": str(ruta_md.relative_to(RAIZ)) if ruta_md.is_relative_to(RAIZ) else str(ruta_md),
            "zonas": argumentos.zonas,
            "zonas_codigos": zonas_codigos,
            "confianza": argumentos.confianza,
            "nota": argumentos.nota,
        },
    })
    escribir_registro(argumentos.id, registro)
    print(f"HECHO {argumentos.id}: {argumentos.zonas} zonas -> {argumentos.archivo}")


def cmd_fallar(argumentos: argparse.Namespace) -> None:
    registro = leer_registro(argumentos.id)
    registro.update({
        "estado": "FALLIDO",
        "fin": ahora(),
        "resultado": {"motivo": argumentos.motivo},
    })
    escribir_registro(argumentos.id, registro)
    print(f"FALLIDO {argumentos.id}: {argumentos.motivo}")


def cmd_liberar(argumentos: argparse.Namespace) -> None:
    ruta = ruta_registro(argumentos.id)
    if not ruta.exists():
        raise SystemExit(f"{argumentos.id} no estaba reclamado.")
    estado = json.loads(ruta.read_text(encoding="utf-8")).get("estado")
    ruta.unlink()
    print(f"LIBERADO {argumentos.id} (estaba {estado}); vuelve a la cola.")


# ---------------------------------------------------------------------------
# estado / consolidar
# ---------------------------------------------------------------------------

def cmd_estado(argumentos: argparse.Namespace) -> None:
    items = {i["id"]: i for i in cargar_cola()}
    CARPETA_REGISTRO.mkdir(exist_ok=True)

    registros = []
    for ruta in sorted(CARPETA_REGISTRO.glob("*.json")):
        try:
            registros.append(json.loads(ruta.read_text(encoding="utf-8")))
        except json.JSONDecodeError:
            print(f"AVISO: registro corrupto: {ruta.name}")

    if argumentos.sesion:
        registros = [r for r in registros if r.get("sesion") == argumentos.sesion]

    por_estado: dict[str, list[dict]] = {"EN_PROCESO": [], "HECHO": [], "FALLIDO": []}
    for r in registros:
        por_estado.setdefault(r.get("estado", "?"), []).append(r)

    hechos = por_estado.get("HECHO", [])
    total_zonas = sum((r.get("resultado") or {}).get("zonas", 0) for r in hechos)

    print(f"=== FASE 4 — TABLERO ({ahora()}) ===")
    print(f"Cola total          : {len(items)}")
    print(f"Reclamados          : {len(registros)}")
    print(f"  HECHO             : {len(hechos)}  (zonas transcritas: {total_zonas})")
    print(f"  EN_PROCESO        : {len(por_estado.get('EN_PROCESO', []))}")
    print(f"  FALLIDO           : {len(por_estado.get('FALLIDO', []))}")
    print(f"Libres en cola      : {len(items) - len(registros)}")

    por_sesion: dict[str, int] = {}
    for r in registros:
        por_sesion[r.get("sesion", "?")] = por_sesion.get(r.get("sesion", "?"), 0) + 1
    if por_sesion:
        print("\nPor sesión:", "  ".join(f"{s}={n}" for s, n in sorted(por_sesion.items())))

    en_proceso = por_estado.get("EN_PROCESO", [])
    if en_proceso:
        print("\nEN_PROCESO ahora:")
        for r in sorted(en_proceso, key=lambda x: x["inicio"]):
            edad = horas_desde(r["inicio"])
            marca = "  <-- HUÉRFANO?" if edad > HORAS_HUERFANO else ""
            print(f"  {r['sesion']:6s} {edad:5.1f}h  {r['id']:32s} "
                  f"{r.get('comuna','?')[:16]:16s}{marca}")

    fallidos = por_estado.get("FALLIDO", [])
    if fallidos:
        print("\nFALLIDOS (revisar / liberar para reintentar):")
        for r in fallidos[:15]:
            print(f"  {r['id']:32s} {(r.get('resultado') or {}).get('motivo','')[:60]}")


def cmd_consolidar(argumentos: argparse.Namespace) -> None:
    CARPETA_REGISTRO.mkdir(exist_ok=True)
    filas = []
    for ruta in sorted(CARPETA_REGISTRO.glob("*.json")):
        registro = json.loads(ruta.read_text(encoding="utf-8"))
        if registro.get("estado") != "HECHO":
            continue
        resultado = registro.get("resultado") or {}
        filas.append({
            "id": registro["id"],
            "comuna": registro["comuna"],
            "ruta": registro["ruta"],
            "archivo_md": resultado.get("archivo", ""),
            "zonas": resultado.get("zonas", 0),
            "zonas_codigos": ",".join(resultado.get("zonas_codigos", [])),
            "confianza": resultado.get("confianza", ""),
            "nota": resultado.get("nota", ""),
            "sesion": registro.get("sesion", ""),
            "fin": registro.get("fin", ""),
        })

    if not filas:
        print("Aún no hay documentos HECHO que consolidar.")
        return

    filas.sort(key=lambda f: (f["comuna"], f["id"]))
    with CONSOLIDADO.open("w", newline="", encoding="utf-8") as manejador:
        escritor = csv.DictWriter(manejador, fieldnames=list(filas[0].keys()))
        escritor.writeheader()
        escritor.writerows(filas)

    print(f"Consolidado: {CONSOLIDADO.name} ({len(filas)} documentos, "
          f"{sum(f['zonas'] for f in filas)} zonas transcritas)")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    analizador = argparse.ArgumentParser(description="Registro compartido de la Fase 4.")
    subcomandos = analizador.add_subparsers(dest="comando", required=True)

    p = subcomandos.add_parser("tomar", help="Reclama documentos libres de la cola.")
    p.add_argument("--sesion", required=True, help="Nombre de TU sesión (S1, S2, S3...)")
    p.add_argument("--n", type=int, default=3)
    p.add_argument("--comuna")
    p.set_defaults(funcion=cmd_tomar)

    p = subcomandos.add_parser("completar", help="Marca un documento como HECHO.")
    p.add_argument("id")
    p.add_argument("--archivo", required=True, help="Ruta al .md producido")
    p.add_argument("--zonas", type=int, required=True, help="Cantidad de zonas transcritas")
    p.add_argument("--zonas-codigos", help="Códigos de zona separados por coma, ej: ZC-1,ZC-2,ZH-1")
    p.add_argument("--confianza", choices=["ALTA", "MEDIA", "BAJA"], default="ALTA")
    p.add_argument("--nota", default="")
    p.set_defaults(funcion=cmd_completar)

    p = subcomandos.add_parser("fallar", help="Marca un documento como FALLIDO.")
    p.add_argument("id")
    p.add_argument("--motivo", required=True)
    p.set_defaults(funcion=cmd_fallar)

    p = subcomandos.add_parser("liberar", help="Devuelve un documento a la cola.")
    p.add_argument("id")
    p.set_defaults(funcion=cmd_liberar)

    p = subcomandos.add_parser("estado", help="Tablero en vivo.")
    p.add_argument("--sesion")
    p.set_defaults(funcion=cmd_estado)

    p = subcomandos.add_parser("consolidar", help="Genera fase4_extraccion.csv.")
    p.set_defaults(funcion=cmd_consolidar)

    argumentos = analizador.parse_args()
    argumentos.funcion(argumentos)


if __name__ == "__main__":
    main()
