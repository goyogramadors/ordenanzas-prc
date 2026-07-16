#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Muestra el avance combinado de todos los bots (registro_*.csv).

Uso:  python estado_paralelo.py
"""
import csv
import glob
from pathlib import Path

DIR = Path(__file__).parent


def contar(ruta):
    hecho = error = pdfs = 0
    try:
        for row in csv.DictReader(open(ruta, newline="", encoding="utf-8")):
            if row.get("estado") == "hecho":
                hecho += 1
                try:
                    pdfs += int(row.get("pdfs") or 0)
                except ValueError:
                    pass
            elif row.get("estado") == "error":
                error += 1
    except Exception:
        pass
    return hecho, error, pdfs


def tamano_slice(nn):
    f = DIR / f"comunas_lote_{nn}.txt"
    if not f.exists():
        return None
    return sum(1 for l in f.read_text(encoding="utf-8").splitlines() if l.strip())


def main():
    registros = sorted(glob.glob(str(DIR / "registro_*.csv")))
    tot_hecho = tot_error = tot_pdfs = 0
    print(f"{'registro':<24}{'hechas':>8}{'errores':>9}{'PDFs':>8}{'meta':>8}")
    print("-" * 57)
    for r in registros:
        nombre = Path(r).name
        hecho, error, pdfs = contar(r)
        nn = nombre.replace("registro_", "").replace(".csv", "")
        meta = tamano_slice(nn)
        meta_txt = str(meta) if meta is not None else "-"
        print(f"{nombre:<24}{hecho:>8}{error:>9}{pdfs:>8}{meta_txt:>8}")
        tot_hecho += hecho
        tot_error += error
        tot_pdfs += pdfs
    print("-" * 57)
    print(f"{'TOTAL':<24}{tot_hecho:>8}{tot_error:>9}{tot_pdfs:>8}")
    # meta global (comunas del pais)
    maestra = DIR / "comunas_chile.txt"
    if maestra.exists():
        total = sum(1 for l in maestra.read_text(encoding="utf-8").splitlines()
                    if l.strip() and not l.strip().startswith("#"))
        print(f"\nComunas del pais: {total} | procesadas (todos los registros): {tot_hecho}")


if __name__ == "__main__":
    main()
