"""
FASE 5 — Generador de la cola de trabajo (unidad = COMUNA)
=========================================================
A diferencia de las fases anteriores (unidad = documento), aquí la unidad es
la COMUNA: cada ítem produce UN archivo JSON `NormativaPRC` que agrega todos
los Markdown de esa comuna generados en Fase 4.

Aplica tres filtros y clasifica en buckets:

  1. GEOJSON (regla del usuario: sin capa GeoJSON no se procesa). El manifiesto
     `Web/public/geo-data/comunas.manifest.json` da la región y el archivo
     GeoJSON de cada comuna. Comuna sin entrada = SIN_GEOJSON, excluida.
  2. BASE: la comuna necesita al menos un documento ORDENANZA_PRC con zonas
     transcritas. Solo con enmiendas/modificaciones NO se puede armar una ficha
     completa (falta la ordenanza base) -> bucket SIN_BASE (hueco de descarga).
  3. EXISTENTE: si ya hay un JSON en `norma-data` CON PARAMETROS REALES (al
     menos una zona con algun campo numerico de edificacion no nulo), es
     perfeccionamiento (aplicar modificaciones a la ficha existente) -> bucket
     PERFECCIONAR, al final. Un JSON "existente" cuyas zonas son 100% nulas
     (ingesta de la capa GeoJSON con solo nombre+usos, sin ningun COS/altura/
     predial extraido de la ordenanza) NO cuenta como existente para este
     filtro -- se trata como si no existiera y sigue el flujo normal hacia
     PROCESAR. Sin este chequeo de contenido, una comuna con ficha 100% nula
     queda enterrada en PERFECCIONAR (que ademas ni siquiera se escribe en
     fase5_cola.json, solo se reporta por consola) y nunca se vuelve a tocar.

Los que pasan los tres -> bucket PROCESAR, ordenados por PRIORIDAD:
  tier 0: ciudad grande (lista curada CIUDADES_GRANDES, editable)
  tier 1: región prioritaria (RM 13, Valparaíso 05, Biobío 08, Araucanía 09,
          Los Lagos 10)
  tier 2: resto
Dentro de cada tier, más zonas primero (fichas más ricas antes).

Peñalolén y Las Condes se dejan explícitamente para el final (instrucción del
usuario: son perfeccionamiento, revisar al cierre).

Salida: `fase5_cola.json` (solo el bucket PROCESAR) + reporte de todos los
buckets por consola.

Uso:
    python fase5_cola.py
"""

from __future__ import annotations

import collections
import csv
import glob
import json
import os
import re
import unicodedata
from datetime import datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
WEB = Path(os.environ.get("ARCHIBLOCKS_WEB_PUBLIC", RAIZ.parent / "projectbook" / "Web" / "public"))
MANIFEST = WEB / "geo-data" / "comunas.manifest.json"
GEODIR = WEB / "geo-data"
NORMADIR = WEB / "norma-data"

COLA_FASE4 = RAIZ / "fase4_cola.json"
LISTA_BLANCA = RAIZ / "lista_blanca.csv"
SALIDA = RAIZ / "fase5_cola.json"

REGIONES_PRIORITARIAS = {"13", "05", "08", "09", "10"}

# Campos numericos de edificacion cuya presencia (no-nula) en al menos una zona
# distingue una ficha "real" (con trabajo de extraccion de la ordenanza) de un
# stub de ingesta GeoJSON (solo nombre+usos, todo lo demas null).
CAMPOS_PARAMETRO_REAL = (
    "coef_constructibilidad", "cos_primer_piso", "cos_pisos_superiores",
    "altura_maxima_metros", "altura_maxima_pisos",
    "superficie_predial_minima_m2", "densidad_maxima_hab_ha",
)

# Comunas que se dejan para el final por decisión del usuario (perfeccionamiento
# de fichas ya desarrolladas). Slugs del corpus.
DIFERIR_AL_FINAL = {"penalolen", "las_condes"}

# Alias entre el slug del corpus y la clave del manifiesto GeoJSON, para los
# casos en que no coinciden por slug directo.
ALIAS_MANIFEST = {
    "saavedra": "puertosaavedra",
    "quinta_de_tilcoco": "qtatilcoco",
}

# Lista CURADA y EDITABLE de "ciudades grandes" (slugs del corpus). Son las que
# el usuario quiere priorizar aunque su región no esté en REGIONES_PRIORITARIAS
# (p. ej. Valdivia, capital regional de Los Ríos-14). Ajústala libremente.
CIUDADES_GRANDES = {
    # Capitales regionales y grandes metros fuera de las regiones prioritarias
    "antofagasta", "calama", "iquique", "arica", "la_serena", "coquimbo",
    "copiapo", "rancagua", "curico", "talca", "chillan", "valdivia",
    "punta_arenas", "coyhaique",
    # Grandes urbes DENTRO de las regiones prioritarias (para que suban por
    # encima de comunas chicas de la misma región)
    "santiago", "puente_alto", "maipu", "la_florida", "san_bernardo", "nunoa",
    "providencia", "penaflor", "quilicura", "pudahuel",
    "valparaiso", "vina_del_mar", "quilpue", "san_antonio", "quillota",
    "concepcion", "talcahuano", "los_angeles", "coronel", "chiguayante",
    "san_pedro_de_la_paz", "hualpen",
    "temuco", "padre_las_casas", "angol", "villarrica",
    "puerto_montt", "osorno", "castro", "ancud",
}


def slug_plano(t: str) -> str:
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "", t.lower())


def clave_manifest(comuna: str, manifest: dict) -> str | None:
    sp = slug_plano(comuna)
    if sp in manifest:
        return sp
    if comuna in ALIAS_MANIFEST and ALIAS_MANIFEST[comuna] in manifest:
        return ALIAS_MANIFEST[comuna]
    return None


def tiene_parametros_reales(ruta_json: Path) -> bool:
    """True si al menos una zona del JSON trae un parametro de edificacion no nulo.
    Distingue una ficha con trabajo real de extraccion de un stub de ingesta
    GeoJSON (solo nombre+usos, todo el resto null) -- ver nota del bucket EXISTENTE."""
    try:
        datos = json.loads(ruta_json.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return False
    if not isinstance(datos, list):
        return False
    return any(
        isinstance(zona, dict)
        and any(zona.get(campo) is not None for campo in CAMPOS_PARAMETRO_REAL)
        for zona in datos
    )


def main() -> None:
    if not MANIFEST.exists():
        raise SystemExit(f"Falta el manifiesto GeoJSON: {MANIFEST}")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    existentes = set()
    stubs_ignorados = []
    for fn in os.listdir(NORMADIR):
        m = re.match(r"\d+_(.+)\.json", fn)
        if not m:
            continue
        if tiene_parametros_reales(NORMADIR / fn):
            existentes.add(m.group(1))
        else:
            stubs_ignorados.append((m.group(1), fn))

    cola4 = json.loads(COLA_FASE4.read_text(encoding="utf-8"))
    ids_por_comuna = collections.defaultdict(list)
    id_a_ruta = {}
    for i in cola4["items"]:
        ids_por_comuna[i["comuna"]].append(i["id"])
        id_a_ruta[i["id"]] = i["ruta"]

    # Estado + resultado de Fase 4
    hecho = {}
    for f in glob.glob(str(RAIZ / "fase4_registro" / "*.json")):
        d = json.loads(Path(f).read_text(encoding="utf-8"))
        if d["estado"] == "HECHO":
            hecho[d["id"]] = d.get("resultado") or {}

    # Categoría de Fase 1 por ruta
    categoria = {r["ruta"]: r["categoria"]
                 for r in csv.DictReader(LISTA_BLANCA.open(encoding="utf-8-sig"))}

    # Comunas 100% completas en Fase 4
    listas = [c for c, ids in ids_por_comuna.items()
              if all(i in hecho for i in ids)]

    buckets = collections.defaultdict(list)
    items_procesar = []

    for comuna in listas:
        ids = ids_por_comuna[comuna]
        markdowns = []
        zonas_total = 0
        tiene_base = False
        for i in ids:
            r = hecho[i]
            z = r.get("zonas", 0)
            zonas_total += z
            cat = categoria.get(id_a_ruta[i], "?")
            if "ORDENANZA" in cat and z > 0:
                tiene_base = True
            markdowns.append({
                "id": i,
                "archivo": r.get("archivo", ""),
                "categoria": cat,
                "zonas": z,
                "zonas_codigos": r.get("zonas_codigos", []),
                "nota": r.get("nota", ""),
            })

        gk = clave_manifest(comuna, manifest)

        if gk is None:
            buckets["SIN_GEOJSON"].append((comuna, None, zonas_total))
            continue

        region = manifest[gk]["region"]
        geojson = manifest[gk]["file"]

        if slug_plano(comuna) in existentes:
            buckets["PERFECCIONAR"].append((comuna, region, zonas_total))
            continue
        if zonas_total == 0:
            buckets["REVISAR_0_ZONAS"].append((comuna, region, zonas_total))
            continue
        if not tiene_base:
            buckets["SIN_BASE"].append((comuna, region, zonas_total))
            continue

        # PROCESAR
        if comuna in CIUDADES_GRANDES:
            tier = 0
        elif region in REGIONES_PRIORITARIAS:
            tier = 1
        else:
            tier = 2
        if comuna in DIFERIR_AL_FINAL:
            tier = 9  # al final pase lo que pase

        items_procesar.append({
            "comuna": comuna,
            "region": region,
            "geojson_file": geojson,
            "geojson_existe": (GEODIR / geojson).exists(),
            "salida_json": f"{region}_{slug_plano(comuna)}.json",
            "tier": tier,
            "zonas_total": zonas_total,
            "markdowns": markdowns,
        })
        buckets["PROCESAR"].append((comuna, region, zonas_total, tier))

    items_procesar.sort(key=lambda x: (x["tier"], -x["zonas_total"], x["comuna"]))

    contenido = {
        "generado": datetime.now().isoformat(timespec="seconds"),
        "total": len(items_procesar),
        "items": items_procesar,
    }
    SALIDA.write_text(json.dumps(contenido, ensure_ascii=False, indent=1), encoding="utf-8")

    # ---- Reporte ----
    nombre_tier = {0: "ciudad grande", 1: "región prioritaria", 2: "otra región",
                   9: "diferida (perfeccionamiento)"}
    print(f"Cola Fase 5 generada: {SALIDA.name}")
    print(f"Comunas 100% completas en Fase 4: {len(listas)}")
    if stubs_ignorados:
        print(f"\nStubs de ingesta GeoJSON ignorados para el filtro EXISTENTE "
              f"({len(stubs_ignorados)}, ficha 100% nula -> tratadas como si no "
              f"existieran, siguen el flujo normal en vez de caer directo a PERFECCIONAR):")
        for slug, fn in sorted(stubs_ignorados):
            print(f"  {slug:20s} {fn}")
    print()
    print(f"=== PROCESAR (crea ficha nueva): {len(items_procesar)} ===")
    for it in items_procesar:
        print(f"  [{nombre_tier[it['tier']]:22s}] {it['comuna']:20s} "
              f"reg={it['region']} zonas={it['zonas_total']:<3d} -> {it['salida_json']}")

    for nombre, titulo in [
        ("SIN_BASE", "SIN_BASE (solo enmienda; falta ordenanza base -> re-descarga)"),
        ("PERFECCIONAR", "PERFECCIONAR (ya tiene JSON; aplicar modificaciones, al final)"),
        ("SIN_GEOJSON", "SIN_GEOJSON (excluidas por regla; ficha no usable en la app)"),
        ("REVISAR_0_ZONAS", "REVISAR (0 zonas transcritas en Fase 4)"),
    ]:
        filas = buckets.get(nombre, [])
        if filas:
            print(f"\n=== {titulo}: {len(filas)} ===")
            for tup in sorted(filas):
                c, reg = tup[0], tup[1]
                print(f"  {c:20s} reg={reg if reg else '--'}")


if __name__ == "__main__":
    main()
