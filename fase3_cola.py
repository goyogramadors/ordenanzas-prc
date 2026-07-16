"""
FASE 3 — Generador de la cola de trabajo
========================================
Construye `fase3_cola.json`: la lista de documentos a los que hay que
localizarles el rango de páginas con tablas de normas urbanísticas.

Cada ítem lleva el MAPA DE PÁGINAS del documento (caracteres por página y
páginas con imagen grande, calculados en Fase 0), para que la sesión que lo
tome sepa de antemano qué páginas puede leer con pdftotext y cuáles debe
mirar visualmente — sin volver a escanear el PDF.

Fuentes:
  - corpus_unico.csv        (Fase 0 — documentos deduplicados con veredicto)
  - catalogo_paginas.json   (Fase 0 — detalle página a página)
  - lista_blanca.csv        (Fase 1 — si existe, manda; si no, se aplica un
                             filtro provisional por nombre y se avisa)

La cola es ESTABLE: el id de cada documento se deriva de su ruta, así que
regenerar la cola no cambia los ids ni invalida el registro de avance.

Uso:
    python fase3_cola.py
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
from datetime import datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parent

CORPUS = RAIZ / "corpus_unico.csv"
PAGINAS = RAIZ / "catalogo_paginas.json"
LISTA_BLANCA = RAIZ / "lista_blanca.csv"
SALIDA = RAIZ / "fase3_cola.json"

# Veredictos que entran a la cola. VACIO e ILEGIBLE no tienen nada que localizar.
VEREDICTOS_UTILES = {"TEXTO", "MIXTO", "ESCANEADO"}

# Orden de procesamiento: primero lo barato (texto), al final lo caro (escaneado).
ORDEN_VEREDICTO = {"TEXTO": 0, "MIXTO": 1, "ESCANEADO": 2}

# Filtro PROVISIONAL por nombre, solo si aún no existe la lista blanca de Fase 1.
# Es deliberadamente conservador: descarta únicamente lo inconfundible.
# Ante la duda el documento ENTRA a la cola (los errores no son simétricos:
# procesar un trámite de más cuesta centavos; botar una ordenanza, una comuna).
DESCARTE_PROVISIONAL = re.compile(
    r"atribuciones_esenciales|potestades_competencias|consulta_publica"
    r"|iniciese_el_proceso|inicio_del?_proceso|postergacion|posterga_por"
    r"|deja_sin_efecto|audiencias_publicas|adjudicase|autoriza_compra"
    r"|insercion_prensa|solicito_|estimados_|a_quien_corresponda"
    r"|certificado_de_inform(?:e|acion)e?s_previas",
    re.IGNORECASE,
)


def identificador(comuna: str, ruta: str) -> str:
    """Id estable y corto: la ruta canónica no cambia entre regeneraciones."""
    resumen = hashlib.sha1(ruta.encode("utf-8")).hexdigest()[:10]
    # Siempre minúsculas: 'SIN_COMUNA' generaba ids que la validación del
    # registro (regex de solo minúsculas) rechazaba.
    return f"{comuna}_{resumen}".lower()


def main() -> None:
    for requisito in (CORPUS, PAGINAS):
        if not requisito.exists():
            raise SystemExit(f"Falta {requisito.name}. Corre antes la Fase 0.")

    with CORPUS.open(encoding="utf-8") as manejador:
        docs = list(csv.DictReader(manejador))

    detalle_paginas = json.loads(PAGINAS.read_text(encoding="utf-8"))

    # --- Selección ------------------------------------------------------------
    rutas_blancas: set[str] | None = None
    if LISTA_BLANCA.exists():
        with LISTA_BLANCA.open(encoding="utf-8") as manejador:
            rutas_blancas = {f["ruta"] for f in csv.DictReader(manejador)}
        modo = f"lista_blanca ({len(rutas_blancas)} rutas)"
    else:
        modo = "PROVISIONAL por nombre (Fase 1 pendiente)"

    items = []
    descartados_nombre = 0
    sin_detalle = 0

    for doc in docs:
        if doc["veredicto"] not in VEREDICTOS_UTILES:
            continue

        if rutas_blancas is not None:
            if doc["ruta"] not in rutas_blancas:
                continue
        elif DESCARTE_PROVISIONAL.search(doc["nombre"]):
            descartados_nombre += 1
            continue

        mapa = detalle_paginas.get(doc["ruta"])
        if mapa is None:
            sin_detalle += 1
            mapa = {"chars": [], "img": []}

        items.append({
            "id": identificador(doc["comuna"], doc["ruta"]),
            "comuna": doc["comuna"],
            "ruta": doc["ruta"],
            "nombre": doc["nombre"],
            "veredicto": doc["veredicto"],
            "paginas": int(doc["paginas"]),
            "paginas_texto": int(doc["paginas_texto"]),
            "paginas_escaneadas": int(doc["paginas_escaneadas"]),
            # Mapa de páginas de Fase 0 (índice 0 = página 1):
            "chars_por_pagina": mapa["chars"],
            "paginas_con_imagen": mapa["img"],
        })

    items.sort(key=lambda i: (ORDEN_VEREDICTO.get(i["veredicto"], 9), i["comuna"], i["id"]))

    contenido = {
        "generado": datetime.now().isoformat(timespec="seconds"),
        "modo_seleccion": modo,
        "total": len(items),
        "items": items,
    }
    SALIDA.write_text(json.dumps(contenido, ensure_ascii=False), encoding="utf-8")

    # --- Resumen ---------------------------------------------------------------
    por_veredicto: dict[str, int] = {}
    for item in items:
        por_veredicto[item["veredicto"]] = por_veredicto.get(item["veredicto"], 0) + 1

    print(f"Cola generada: {SALIDA.name}")
    print(f"Modo de selección : {modo}")
    if rutas_blancas is None:
        print(f"  (descartados por nombre provisional: {descartados_nombre} — "
              f"cuando exista lista_blanca.csv, regenera la cola)")
    print(f"Documentos en cola: {len(items)}")
    for veredicto, cantidad in sorted(por_veredicto.items()):
        print(f"  {veredicto:10s} {cantidad:5d}")
    if sin_detalle:
        print(f"AVISO: {sin_detalle} documentos sin mapa de páginas "
              f"(catalogo_paginas.json desactualizado; considera regenerar Fase 0)")


if __name__ == "__main__":
    main()
