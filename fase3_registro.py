"""
FASE 3 — Registro de trabajo compartido entre sesiones
======================================================
Coordina VARIAS sesiones de Claude trabajando en paralelo sobre la misma cola
(`fase3_cola.json`) sin pisarse, con un registro en vivo de quién hace qué.

Cómo se evita la colisión
-------------------------
Un archivo por documento en `fase3_registro/<id>.json`. Reclamar un documento
es CREAR su archivo con bandera de creación exclusiva (open 'x'): el sistema
de archivos garantiza que solo una sesión puede crearlo — si dos lo intentan a
la vez, una falla y pasa al siguiente ítem de la cola. No hay archivo central
de estado que se corrompa con escrituras concurrentes: cada documento tiene el
suyo, y solo la sesión dueña lo modifica.

Comandos
--------
  tomar      --sesion S1 [--n 5] [--veredicto TEXTO] [--comuna x]
             Reclama los próximos N documentos libres y los imprime en JSON
             (incluye el mapa de páginas de cada uno).
  completar  <id> --rangos "23-33,41" [--confianza ALTA] [--metodo ...] [--nota ...]
  completar  <id> --sin-tablas --nota "..."      (el doc no contiene tablas)
  fallar     <id> --motivo "..."                 (no se pudo procesar)
  liberar    <id>                                (devuelve el doc a la cola)
  estado     [--sesion S1]                       (tablero en vivo)
  consolidar                                     (genera fase3_rangos.csv)

Regla de convivencia: una sesión SOLO modifica los documentos que ella reclamó.
Si al partir ves reclamos tuyos de una corrida anterior (caída), termínalos o
libéralos tú; los reclamos EN_PROCESO de OTRA sesión con más de 3 horas se
consideran huérfanos y `estado` los denuncia — libéralos solo si esa sesión ya
no existe.
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
COLA = RAIZ / "fase3_cola.json"
CARPETA_REGISTRO = RAIZ / "fase3_registro"
CONSOLIDADO = RAIZ / "fase3_rangos.csv"

HORAS_HUERFANO = 3

# La consola de Windows puede venir en cp1252: forzamos utf-8 para no morir
# imprimiendo nombres de comunas con tildes.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except AttributeError:
    pass


def ahora() -> str:
    return datetime.now().isoformat(timespec="seconds")


def cargar_cola() -> list[dict]:
    if not COLA.exists():
        raise SystemExit(f"Falta {COLA.name}. Genera la cola:  python fase3_cola.py")
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

    if argumentos.veredicto:
        items = [i for i in items if i["veredicto"] == argumentos.veredicto]
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
            "nombre": item["nombre"],
            "veredicto": item["veredicto"],
            "paginas": item["paginas"],
            "estado": "EN_PROCESO",
            "sesion": argumentos.sesion,
            "inicio": ahora(),
            "fin": None,
            "resultado": None,
        }
        try:
            # Creación EXCLUSIVA: aquí vive toda la exclusión mutua.
            with ruta.open("x", encoding="utf-8") as manejador:
                json.dump(reclamo, manejador, ensure_ascii=False, indent=2)
        except FileExistsError:
            continue  # otra sesión llegó primero: siguiente ítem

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

def parsear_rangos(texto: str, tope: int) -> list[list[int]]:
    """'23-33,41' -> [[23,33],[41,41]] con validación contra el total de páginas."""
    rangos = []
    for trozo in texto.split(","):
        trozo = trozo.strip()
        coincidencia = re.fullmatch(r"(\d+)(?:-(\d+))?", trozo)
        if not coincidencia:
            raise SystemExit(f"Rango ilegible: {trozo!r} (formato: '23-33,41')")
        desde = int(coincidencia.group(1))
        hasta = int(coincidencia.group(2) or desde)
        if desde < 1 or hasta < desde or (tope and hasta > tope):
            raise SystemExit(f"Rango fuera de documento: {trozo!r} (tiene {tope} páginas)")
        rangos.append([desde, hasta])
    return sorted(rangos)


def cmd_completar(argumentos: argparse.Namespace) -> None:
    registro = leer_registro(argumentos.id)

    if registro["estado"] == "HECHO":
        raise SystemExit(f"{argumentos.id} ya está HECHO (por {registro['sesion']}). "
                         "Si quieres rehacerlo: liberar y tomar de nuevo.")

    if bool(argumentos.rangos) == bool(argumentos.sin_tablas):
        raise SystemExit("Indica --rangos O --sin-tablas (exactamente uno).")

    rangos = []
    if argumentos.rangos:
        rangos = parsear_rangos(argumentos.rangos, registro.get("paginas", 0))

    registro.update({
        "estado": "HECHO",
        "fin": ahora(),
        "resultado": {
            "tiene_tablas": bool(argumentos.rangos),
            "rangos": rangos,
            "paginas_utiles": sum(b - a + 1 for a, b in rangos),
            "confianza": argumentos.confianza,
            "metodo": argumentos.metodo,
            "nota": argumentos.nota,
        },
    })
    escribir_registro(argumentos.id, registro)
    descripcion = f"rangos {rangos}" if rangos else "SIN tablas de normas"
    print(f"HECHO {argumentos.id}: {descripcion}")


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
    con_tablas = sum(1 for r in hechos if (r.get("resultado") or {}).get("tiene_tablas"))
    paginas_utiles = sum((r.get("resultado") or {}).get("paginas_utiles", 0) for r in hechos)

    print(f"=== FASE 3 — TABLERO ({ahora()}) ===")
    print(f"Cola total          : {len(items)}")
    print(f"Reclamados          : {len(registros)}")
    print(f"  HECHO             : {len(hechos)}  "
          f"(con tablas: {con_tablas}, sin tablas: {len(hechos) - con_tablas}; "
          f"páginas útiles localizadas: {paginas_utiles})")
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
            "veredicto": registro["veredicto"],
            "paginas": registro["paginas"],
            "tiene_tablas": "si" if resultado.get("tiene_tablas") else "no",
            "rangos": ",".join(f"{a}-{b}" for a, b in resultado.get("rangos", [])),
            "paginas_utiles": resultado.get("paginas_utiles", 0),
            "confianza": resultado.get("confianza", ""),
            "metodo": resultado.get("metodo", ""),
            "nota": resultado.get("nota", ""),
            "sesion": registro.get("sesion", ""),
            "fin": registro.get("fin", ""),
        })

    if not filas:
        print("Aún no hay documentos HECHO que consolidar.")
        return

    filas.sort(key=lambda f: (f["comuna"], f["id"]))
    with CONSOLIDADO.open("w", newline="", encoding="utf-8") as manejador:
        escritor = csv.DictWriter(manejador, fieldnames=list(filas[0]))
        escritor.writeheader()
        escritor.writerows(filas)

    print(f"Consolidado: {CONSOLIDADO.name} ({len(filas)} documentos HECHO, "
          f"{sum(int(f['paginas_utiles']) for f in filas)} páginas útiles localizadas)")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    analizador = argparse.ArgumentParser(description="Registro compartido de la Fase 3.")
    subcomandos = analizador.add_subparsers(dest="comando", required=True)

    p = subcomandos.add_parser("tomar", help="Reclama documentos libres de la cola.")
    p.add_argument("--sesion", required=True, help="Nombre de TU sesión (S1, S2, S3...)")
    p.add_argument("--n", type=int, default=5)
    p.add_argument("--veredicto", choices=["TEXTO", "MIXTO", "ESCANEADO"])
    p.add_argument("--comuna")
    p.set_defaults(funcion=cmd_tomar)

    p = subcomandos.add_parser("completar", help="Marca un documento como HECHO.")
    p.add_argument("id")
    p.add_argument("--rangos", help="Páginas con tablas, ej: '23-33,41'")
    p.add_argument("--sin-tablas", action="store_true", dest="sin_tablas")
    p.add_argument("--confianza", choices=["ALTA", "MEDIA", "BAJA"], default="MEDIA")
    p.add_argument("--metodo", default="", help="TEXTO / VISUAL / TEXTO+VISUAL")
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

    p = subcomandos.add_parser("consolidar", help="Genera fase3_rangos.csv.")
    p.set_defaults(funcion=cmd_consolidar)

    argumentos = analizador.parse_args()
    argumentos.funcion(argumentos)


if __name__ == "__main__":
    main()
