#!/usr/bin/env python3
"""
Fase 1 - Preparacion de lotes para los agentes.

Toma `fase1_features.json` y lo parte en lotes de ~28 documentos AGRUPADOS POR
COMUNA (un agente que ve juntos todos los documentos de una comuna distingue
mucho mejor cual es la ordenanza y cuales son decretos satelite).

Escribe fase1_lotes/lote_XX.json y emite en stdout la lista de rutas.
"""
from __future__ import annotations

import json
import shutil
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
FEATURES = RAIZ / "fase1_features.json"
DIR_LOTES = RAIZ / "fase1_lotes"

TAM_LOTE = 28
SNIPPET_AGENTE = 1500


def compactar(doc_id: str, v: dict) -> dict:
    """Registro compacto que ve el agente. Solo evidencia, sin veredicto previo
    presentado como verdad: el `pre` va como 'sugerencia_regex' para que el
    agente pueda contradecirlo."""
    rn = v["reglas_nombre"]
    tx = v.get("texto") or {}
    return {
        "id": doc_id,
        "comuna": v["comuna"],
        "nombre_documento": v["familia"],
        "archivo": v["nombre"],
        "veredicto_capa_texto": v["veredicto"],
        "paginas": v["paginas"],
        "paginas_escaneadas": v["paginas_escaneadas"],
        "tipo_real": v["tipo_real"],
        "regex_descarte": [d["patron"] for d in rn["descarte"]],
        "regex_valor": [d["patron"] for d in rn["valor"]],
        "nombre_opaco": rn["opaco"],
        "senales_normativas": tx.get("senales_normativas", {}),
        "senales_tramite": tx.get("senales_tramite", {}),
        "codigos_zona": tx.get("codigos_zona", []),
        "puntaje_normativo": tx.get("puntaje_normativo", 0),
        "sugerencia_regex": v["pre"],
        "texto_primeras_paginas": (v.get("snippet") or "")[:SNIPPET_AGENTE],
    }


def main() -> None:
    feats = json.loads(FEATURES.read_text(encoding="utf-8"))

    # id estable por ruta
    docs = {}
    for i, (ruta, v) in enumerate(sorted(feats.items())):
        docs[f"d{i:04d}"] = (ruta, v)

    # agrupar por comuna
    por_comuna: dict[str, list[str]] = {}
    for did, (ruta, v) in docs.items():
        por_comuna.setdefault(v["comuna"], []).append(did)

    # armar lotes: llenar con comunas completas hasta TAM_LOTE
    lotes: list[list[str]] = []
    actual: list[str] = []
    for comuna in sorted(por_comuna):
        ids = por_comuna[comuna]
        # una comuna con muchos documentos se parte sola
        if len(ids) > TAM_LOTE:
            if actual:
                lotes.append(actual)
                actual = []
            for j in range(0, len(ids), TAM_LOTE):
                lotes.append(ids[j:j + TAM_LOTE])
            continue
        if len(actual) + len(ids) > TAM_LOTE:
            lotes.append(actual)
            actual = []
        actual.extend(ids)
    if actual:
        lotes.append(actual)

    if DIR_LOTES.exists():
        shutil.rmtree(DIR_LOTES)
    DIR_LOTES.mkdir()

    # mapa id -> ruta, para consolidar despues
    mapa = {did: ruta for did, (ruta, _) in docs.items()}
    (RAIZ / "fase1_mapa_ids.json").write_text(
        json.dumps(mapa, ensure_ascii=False, indent=1), encoding="utf-8")

    rutas = []
    for n, ids in enumerate(lotes, 1):
        registros = [compactar(did, docs[did][1]) for did in ids]
        p = DIR_LOTES / f"lote_{n:02d}.json"
        p.write_text(json.dumps(registros, ensure_ascii=False, indent=1),
                     encoding="utf-8")
        rutas.append(str(p))

    print(json.dumps(rutas, ensure_ascii=False))
    import sys
    print(f"\n{len(docs)} documentos -> {len(lotes)} lotes "
          f"(promedio {len(docs)/len(lotes):.1f} docs/lote)", file=sys.stderr)


if __name__ == "__main__":
    main()
