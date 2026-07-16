#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prepara la ejecucion en PARALELO del bot de descarga de PRC.

Toma las comunas que AUN quedan pendientes (las que no estan marcadas 'hecho'
en NINGUN registro_*.csv), las reparte en N partes balanceadas (round-robin,
para mezclar regiones y tamaños) y genera, para cada parte:

  - comunas_lote_NN.txt   -> la lista de comunas de ese bot
  - ejecutar_lote_NN.bat  -> el .bat que corre ese bot con su propio registro

Cada bot usa su PROPIO archivo de avance (registro_NN.csv), asi no se pisan
entre ellos. Todos escriben PDFs en la misma carpeta descargas/<comuna>/, pero
como las listas son disjuntas, cada comuna la procesa un solo bot.

Uso:
    python preparar_paralelo.py            # 10 partes (por defecto)
    python preparar_paralelo.py --n 5      # 5 partes
    python preparar_paralelo.py --forzar   # re-particiona aunque ya exista

Despues, para lanzarlos todos a la vez: doble clic en ejecutar_paralelo.bat
(o abrir manualmente cada ejecutar_lote_NN.bat).
"""

import argparse
import csv
import glob
import re
import sys
import unicodedata
from pathlib import Path

DIR = Path(__file__).parent
LISTA_MAESTRA = DIR / "comunas_chile.txt"
PY_LINE = (
    'set "PY=%LOCALAPPDATA%\\Python\\pythoncore-3.14-64\\python.exe"\r\n'
    'if not exist "%PY%" set "PY=python"\r\n'
)


def slug(texto: str) -> str:
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    t = re.sub(r"[^\w\s-]", "", t).strip().lower()
    t = re.sub(r"[-\s]+", "_", t)
    return t[:120] or "sin_nombre"


def leer_comunas(ruta: Path) -> list:
    return [l.strip() for l in ruta.read_text(encoding="utf-8").splitlines()
            if l.strip() and not l.strip().startswith("#")]


def slugs_hechos() -> set:
    """Union de comunas marcadas 'hecho' en TODOS los registro_*.csv."""
    hechos = set()
    for ruta in glob.glob(str(DIR / "registro_*.csv")):
        try:
            with open(ruta, "r", newline="", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    if row.get("estado") == "hecho":
                        hechos.add(row.get("slug", ""))
        except Exception:
            pass
    return hechos


CAMPOS = ["slug", "comuna", "estado", "pdfs", "fecha_hora"]
REG_MAESTRO = DIR / "registro_progreso.csv"
RE_REG_LOTE = re.compile(r"registro_\d+\.csv$", re.I)


def consolidar_registros() -> int:
    """Vuelca todas las filas 'hecho' de los registro_NN.csv (numerados) al
    registro maestro registro_progreso.csv y luego borra esos registro_NN.csv.
    Asi cada re-reparto arranca de un unico registro de verdad y los nuevos
    bots parten con su registro_NN.csv en blanco. Devuelve cuantas filas nuevas
    consolido."""
    maestro = {}
    if REG_MAESTRO.exists():
        with REG_MAESTRO.open("r", newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                maestro[row["slug"]] = row

    lotes = [p for p in glob.glob(str(DIR / "registro_*.csv"))
             if RE_REG_LOTE.search(Path(p).name)]
    nuevas = 0
    for ruta in lotes:
        try:
            with open(ruta, "r", newline="", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    if row.get("estado") == "hecho":
                        s = row.get("slug", "")
                        if s and s not in maestro:
                            nuevas += 1
                        if s:
                            maestro[s] = row
        except Exception:
            pass

    if lotes:
        with REG_MAESTRO.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=CAMPOS)
            w.writeheader()
            for row in maestro.values():
                w.writerow({k: row.get(k, "") for k in CAMPOS})
        for ruta in lotes:
            Path(ruta).unlink(missing_ok=True)
    return nuevas


def escribir_bat(n: int, lista: str, registro: str) -> Path:
    nn = f"{n:02d}"
    ruta = DIR / f"ejecutar_lote_{nn}.bat"
    contenido = (
        "@echo off\r\n"
        "setlocal\r\n"
        'cd /d "%~dp0"\r\n'
        "set PYTHONIOENCODING=utf-8\r\n"
        "\r\n"
        + PY_LINE +
        "\r\n"
        f'title Bot {nn} - PRC\r\n'
        f"echo ================================================================\r\n"
        f"echo  BOT {nn} de descarga PRC (en paralelo)\r\n"
        f"echo  Lista:    {lista}\r\n"
        f"echo  Registro: {registro}\r\n"
        f"echo  Puedes cerrar esta ventana y volver a abrir este .bat: continua\r\n"
        f"echo  donde quedo (segun su propio registro).\r\n"
        f"echo ================================================================\r\n"
        "echo.\r\n"
        "\r\n"
        f'"%PY%" descargar_prc.py --lista {lista} --registro {registro}\r\n'
        "\r\n"
        "echo.\r\n"
        f"echo BOT {nn} termino o se pauso. Revisa {registro}.\r\n"
        "pause\r\n"
        "endlocal\r\n"
    )
    ruta.write_text(contenido, encoding="utf-8")
    return ruta


def escribir_lanzador(n_partes: int) -> Path:
    ruta = DIR / "ejecutar_paralelo.bat"
    lineas = [
        "@echo off",
        "setlocal",
        'cd /d "%~dp0"',
        "",
        "echo ================================================================",
        f"echo  Lanzando {n_partes} bots en PARALELO (una ventana por bot).",
        "echo  OJO: son %d navegadores headless a la vez; usa harta CPU/RAM." % n_partes,
        "echo  Si el equipo se pone lento, cierra algunas ventanas: cada bot",
        "echo  guarda su avance y puede reanudarse solo.",
        "echo ================================================================",
        "echo.",
        "pause",
        "",
    ]
    for n in range(1, n_partes + 1):
        nn = f"{n:02d}"
        # 'start' abre cada bot en su propia ventana, en paralelo.
        lineas.append(f'start "Bot {nn}" cmd /c ejecutar_lote_{nn}.bat')
    lineas += [
        "",
        "echo Se abrieron las ventanas de los bots. Puedes cerrar ESTA ventana.",
        "endlocal",
        "",
    ]
    ruta.write_text("\r\n".join(lineas), encoding="utf-8")
    return ruta


def main() -> int:
    ap = argparse.ArgumentParser(description="Reparte el trabajo pendiente entre N bots paralelos")
    ap.add_argument("--n", type=int, default=10, help="Cantidad de bots/partes (defecto 10)")
    ap.add_argument("--forzar", action="store_true",
                     help="Re-particiona aunque ya existan los comunas_lote_NN.txt")
    args = ap.parse_args()
    n = max(1, args.n)

    if not LISTA_MAESTRA.exists():
        print(f"No existe {LISTA_MAESTRA.name}.")
        return 1

    existentes = glob.glob(str(DIR / "comunas_lote_*.txt"))
    if existentes and not args.forzar:
        print("Ya existen archivos comunas_lote_*.txt. No re-particiono para no")
        print("desordenar bots en curso. Usa --forzar si quieres rehacer el reparto")
        print("(detén antes todos los bots).")
        return 1

    # limpia repartos previos si se fuerza
    if args.forzar:
        for f in existentes:
            Path(f).unlink(missing_ok=True)
        for f in glob.glob(str(DIR / "ejecutar_lote_*.bat")):
            Path(f).unlink(missing_ok=True)

    # Consolida el avance de bots anteriores en el registro maestro y borra los
    # registro_NN.csv, para que el nuevo reparto arranque de una sola fuente de
    # verdad y cada bot nuevo tenga su registro en blanco.
    consolidadas = consolidar_registros()
    if consolidadas:
        print(f"Consolidadas {consolidadas} comuna(s) de bots previos en {REG_MAESTRO.name}")

    todas = leer_comunas(LISTA_MAESTRA)
    hechos = slugs_hechos()
    pendientes = [c for c in todas if slug(c) not in hechos]

    print(f"Comunas totales: {len(todas)}")
    print(f"Ya hechas (todos los registros): {len(hechos)}")
    print(f"Pendientes a repartir: {len(pendientes)}")
    if not pendientes:
        print("No hay pendientes. Nada que repartir.")
        return 0

    n = min(n, len(pendientes))
    # round-robin: la parte i recibe pendientes[i], pendientes[i+n], ...
    partes = [[] for _ in range(n)]
    for idx, comuna in enumerate(pendientes):
        partes[idx % n].append(comuna)

    print(f"\nRepartiendo en {n} parte(s):")
    for i, parte in enumerate(partes, start=1):
        nn = f"{i:02d}"
        lista_f = f"comunas_lote_{nn}.txt"
        registro_f = f"registro_{nn}.csv"
        (DIR / lista_f).write_text("\n".join(parte) + "\n", encoding="utf-8")
        escribir_bat(i, lista_f, registro_f)
        print(f"  Bot {nn}: {len(parte):3d} comunas  -> {lista_f} / {registro_f}")

    lanzador = escribir_lanzador(n)
    print(f"\nGenerados: comunas_lote_01..{n:02d}.txt, ejecutar_lote_01..{n:02d}.bat")
    print(f"Lanzador:  {lanzador.name}  (doble clic para abrir los {n} bots)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
