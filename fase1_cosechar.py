#!/usr/bin/env python3
"""
Fase 1 - Cosecha resultados de agentes desde el journal de un workflow.

Los workflows pueden morir a medias (p.ej. limite de sesion). El journal guarda
una linea {"type":"result", "result":{...}} por CADA agente que SI termino, asi
que ningun lote completado se pierde aunque el workflow global falle.

Uso:
  python fase1_cosechar.py <run_id> <clave_array> <archivo_salida.json>

  clave_array: 'clasificaciones' | 'veredictos' | 'auditorias'

Es idempotente y acumulativo: fusiona sobre lo que ya hubiera en el archivo de
salida, indexando por el campo 'id'.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path(
    r"C:\Users\gcastillo\.claude\projects\C--Users-gcastillo-Desktop-Ordenanzas"
    r"\dbd02721-f7e2-40b5-8e1d-94bc520a24fa\subagents\workflows"
)


def main() -> int:
    if len(sys.argv) != 4:
        print(__doc__)
        return 1
    run_id, clave, salida = sys.argv[1], sys.argv[2], Path(sys.argv[3])

    journal = BASE / run_id / "journal.jsonl"
    if not journal.exists():
        print(f"ERROR: no existe {journal}", file=sys.stderr)
        return 1

    acum: dict = {}
    if salida.exists():
        acum = json.loads(salida.read_text(encoding="utf-8"))
    previos = len(acum)

    n_result = 0
    for ln in journal.open(encoding="utf-8"):
        try:
            o = json.loads(ln)
        except json.JSONDecodeError:
            continue
        if o.get("type") != "result":
            continue
        n_result += 1
        r = o.get("result") or {}
        if isinstance(r, str):
            try:
                r = json.loads(r)
            except json.JSONDecodeError:
                continue
        if not isinstance(r, dict):
            continue
        for item in (r.get(clave) or []):
            if isinstance(item, dict) and item.get("id"):
                acum[item["id"]] = item

    salida.write_text(json.dumps(acum, ensure_ascii=False, indent=1),
                      encoding="utf-8")
    print(f"agentes con resultado: {n_result}")
    print(f"{salida.name}: {previos} -> {len(acum)} registros "
          f"(+{len(acum) - previos})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
