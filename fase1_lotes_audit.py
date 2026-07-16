#!/usr/bin/env python3
"""
Fase 1 - Prepara los lotes para la auditoria adversarial de descartes.

Lee descartados.csv (los sirve=NO) y arma lotes con TODA la evidencia disponible
mas el motivo del descarte, para que un auditor independiente intente refutarlo.
"""
from __future__ import annotations

import csv
import json
import shutil
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
DIR = RAIZ / "fase1_lotes_audit"
TAM = 25
SNIPPET = 1400


def main() -> None:
    feats = json.loads((RAIZ / "fase1_features.json").read_text(encoding="utf-8"))
    mapa = json.loads((RAIZ / "fase1_mapa_ids.json").read_text(encoding="utf-8"))
    inv = {ruta: did for did, ruta in mapa.items()}

    desc = list(csv.DictReader(open(RAIZ / "descartados.csv", encoding="utf-8-sig")))
    if not desc:
        print("[]")
        print("no hay descartes que auditar", file=sys.stderr)
        return

    regs = []
    for r in desc:
        ruta = r["ruta"]
        v = feats[ruta]
        tx = v.get("texto") or {}
        regs.append({
            "id": inv[ruta],
            "comuna": r["comuna"],
            "nombre_documento": r["familia"],
            "ruta": ruta,
            "veredicto_capa_texto": r["veredicto"],
            "paginas": int(r["paginas"] or 0),
            "paginas_escaneadas": int(r["paginas_escaneadas"] or 0),
            "senales_normativas": tx.get("senales_normativas", {}),
            "codigos_zona": tx.get("codigos_zona", []),
            "puntaje_normativo": tx.get("puntaje_normativo", 0),
            "categoria_asignada": r["categoria"],
            "motivo_del_descarte": r["motivo"],
            "texto_primeras_paginas": (v.get("snippet") or "")[:SNIPPET],
        })

    if DIR.exists():
        shutil.rmtree(DIR)
    DIR.mkdir()

    rutas = []
    for n in range(0, len(regs), TAM):
        p = DIR / f"audit_{n // TAM + 1:02d}.json"
        p.write_text(json.dumps(regs[n:n + TAM], ensure_ascii=False, indent=1),
                     encoding="utf-8")
        rutas.append(str(p).replace("\\", "/"))

    print(json.dumps(rutas, ensure_ascii=False))
    print(f"\n{len(regs)} descartes -> {len(rutas)} lotes de auditoria", file=sys.stderr)


if __name__ == "__main__":
    main()
