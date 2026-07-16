"""
FASE 4 — Generador de la cola de trabajo
========================================
Construye `fase4_cola.json`: los documentos que SÍ tienen tablas de normas
localizadas en Fase 3 (`fase3_rangos.csv`, columna tiene_tablas=si), listos
para que una sesión renderice exactamente ese rango de páginas y transcriba
las tablas a Markdown.

Cada ítem lleva el contexto que dejó Fase 3 (rango, confianza, método, nota)
para que la sesión no tenga que releer el PDF entero ni redescubrir las
trampas ya documentadas (Caldera, LeyChile, Diario Oficial nativo con tablas
en imagen, decreto pegado).

La cola es ESTABLE: usa el mismo id que Fase 3 (derivado de la ruta), así que
regenerar la cola no invalida el avance de Fase 4.

Orden: de menos páginas a más (barato primero), y dentro de eso por comuna
(un agente que procesa varios documentos de la misma comuna seguidos
reconoce mejor si son la ordenanza base o modificaciones satélite).

Uso:
    python fase4_cola.py
"""

from __future__ import annotations

import ast
import csv
import hashlib
import json
from datetime import datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
RANGOS = RAIZ / "fase3_rangos.csv"
SALIDA = RAIZ / "fase4_cola.json"


def parsear_rangos(texto: str) -> list[list[int]]:
    """'23-33,41' -> [[23,33],[41,41]]"""
    rangos = []
    for trozo in texto.split(","):
        trozo = trozo.strip()
        if not trozo:
            continue
        if "-" in trozo:
            a, b = trozo.split("-")
            rangos.append([int(a), int(b)])
        else:
            rangos.append([int(trozo), int(trozo)])
    return rangos


def main() -> None:
    if not RANGOS.exists():
        raise SystemExit(f"Falta {RANGOS.name}. Corre antes Fase 3 (fase3_registro.py consolidar).")

    with RANGOS.open(encoding="utf-8-sig") as manejador:
        filas = list(csv.DictReader(manejador))

    items = []
    for fila in filas:
        if fila["tiene_tablas"] != "si":
            continue
        if not fila["rangos"].strip():
            continue

        rangos = parsear_rangos(fila["rangos"])
        items.append({
            "id": fila["id"],
            "comuna": fila["comuna"],
            "ruta": fila["ruta"],
            "veredicto": fila["veredicto"],
            "paginas_documento": int(fila["paginas"]),
            "rangos": rangos,
            "paginas_utiles": int(fila["paginas_utiles"]),
            "confianza_fase3": fila["confianza"],
            "metodo_fase3": fila["metodo"],
            "nota_fase3": fila["nota"],
        })

    items.sort(key=lambda i: (i["paginas_utiles"], i["comuna"], i["id"]))

    contenido = {
        "generado": datetime.now().isoformat(timespec="seconds"),
        "total": len(items),
        "items": items,
    }
    SALIDA.write_text(json.dumps(contenido, ensure_ascii=False), encoding="utf-8")

    total_paginas = sum(i["paginas_utiles"] for i in items)
    por_comuna = len({i["comuna"] for i in items})

    print(f"Cola generada: {SALIDA.name}")
    print(f"Documentos a transcribir: {len(items)}")
    print(f"Comunas involucradas: {por_comuna}")
    print(f"Páginas totales a renderizar/transcribir: {total_paginas}")
    print()
    print("Distribución por tamaño (páginas útiles por documento):")
    tramos = [(1, 1), (2, 3), (4, 6), (7, 15), (16, 999)]
    for lo, hi in tramos:
        n = sum(1 for i in items if lo <= i["paginas_utiles"] <= hi)
        print(f"  {lo:3d}-{hi if hi < 999 else '+':<3} páginas: {n} documentos")


if __name__ == "__main__":
    main()
