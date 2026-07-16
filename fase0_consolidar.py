"""
FASE 0 (paso 2) — Consolidación del corpus
==========================================
Toma `catalogo_maestro.csv` (las tres copias del corpus, con su veredicto de
capa de texto) y produce UN corpus único deduplicado, más el mapa de cobertura
por comuna.

Dos niveles de duplicado, y hay que distinguirlos:

  1. Copia exacta      — mismo SHA-256. El mismo archivo en dos carpetas.
  2. Misma obra        — mismo documento pero bytes distintos, típicamente
                         porque una copia pasó por el bot de OCR y la otra no.
                         El hash NO las agrupa; hay que agrupar por nombre.

Para (2) se usa una "familia": el nombre del archivo normalizado (sin el prefijo
de comuna, sin sufijos de OCR, sin extensión). Dentro de cada familia se elige
UNA copia canónica con este criterio, en orden:

    a) la que tiene MÁS páginas con texto real (una copia OCR'd le gana a la
       escaneada; pero ojo: `paginas_texto` ya se midió por página, así que un
       "OCR ok" falso como Caldera no gana solo por estar en esa carpeta)
    b) a igualdad, la de más páginas totales (evita quedarse con un extracto)
    c) a igualdad, la más pesada

Salidas:
  corpus_unico.csv        — una fila por documento único (el canónico)
  cobertura_comunas.csv   — qué tiene cada una de las 343 comunas
"""

from __future__ import annotations

import csv
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent

ENTRADA = RAIZ / "catalogo_maestro.csv"
SALIDA_CORPUS = RAIZ / "corpus_unico.csv"
SALIDA_COBERTURA = RAIZ / "cobertura_comunas.csv"
LISTA_COMUNAS = RAIZ / "comunas_chile.txt"

# Prioridad de carpeta solo como criterio de DESEMPATE final, nunca antes que
# la evidencia medida. "OCR ok" no es garantía de nada — lo probó Caldera.
PRIORIDAD_CARPETA = {"ordenadas": 0, "descargadas": 1, "descargas": 2}


def slug(texto: str) -> str:
    """
    'Cerro Navia' -> 'cerro_navia'; 'Conchalí' -> 'conchali'.

    `comunas_chile.txt` guarda nombres propios con mayúsculas y tildes, mientras
    que las carpetas y archivos usan slugs. Sin esta normalización la cobertura
    daba 0 coincidencias y las 343 comunas aparecían todas como "sin material".
    """
    sin_tilde = unicodedata.normalize("NFKD", texto)
    sin_tilde = "".join(c for c in sin_tilde if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "_", sin_tilde.lower()).strip("_")


def cargar_comunas_oficiales() -> list[str]:
    """Slugs de las 343 comunas, ordenados de más largo a más corto."""
    if not LISTA_COMUNAS.exists():
        return []
    slugs = []
    for linea in LISTA_COMUNAS.read_text(encoding="utf-8").splitlines():
        linea = linea.strip()
        if linea and not linea.startswith("#"):
            slugs.append(slug(linea))
    # El orden importa: 'san_jose_de_maipo' debe intentarse ANTES que 'san_jose',
    # y 'la_serena' antes que 'la_' — si no, el prefijo corto gana y trunca.
    return sorted(set(slugs), key=len, reverse=True)


def inferir_comuna(ruta: str, oficiales: list[str]) -> str:
    """
    Comuna de un documento, emparejando contra la lista OFICIAL.

    Se abandonó el enfoque anterior (cortar el nombre en el primer número o
    palabra clave) porque destrozaba nombres legítimos: 'las_condes_n_8_30MAY1995'
    quedaba como comuna 'las_condes_n', y 'el_quisco_informacion...' como
    'el_quisco_inform' — cada corte inventaba una comuna nueva y vaciaba la real.

    Dos fuentes, en orden de confianza:
      1. La carpeta: en `descargas/<comuna>/...` la comuna es explícita.
      2. El nombre : prefijo más largo que coincida con una comuna oficial.
    """
    partes = Path(ruta).parts

    # 1. Carpeta explícita (descargas/<comuna>/...)
    if partes and partes[0] == "descargas" and len(partes) > 1:
        candidato = slug(partes[1])
        if candidato in oficiales:
            return candidato

    # 2. Prefijo del nombre de archivo contra la lista oficial
    nombre = slug(Path(ruta).stem)
    for comuna in oficiales:  # ya vienen de más largo a más corto
        if nombre == comuna or nombre.startswith(comuna + "_"):
            return comuna

    return "SIN_COMUNA"


def normalizar_familia(nombre: str, comuna: str) -> str:
    """
    Clave que agrupa la MISMA obra aunque los bytes difieran.

    Quita: extensión, sufijo .ocr, el prefijo de comuna, y el sufijo aleatorio
    que el portal agrega tras el doble guion bajo (`__Exportar`, `__view`,
    `__3f01n`, hashes largos...). Ese sufijo cambia entre descargas del mismo
    documento y rompería el agrupamiento.
    """
    base = re.sub(r"\.pdf$", "", nombre, flags=re.IGNORECASE)
    base = re.sub(r"\.ocr$", "", base, flags=re.IGNORECASE)
    base = base.lower()

    # Fuera el prefijo de comuna
    if comuna and base.startswith(comuna + "_"):
        base = base[len(comuna) + 1:]

    # Fuera el sufijo de descarga tras el doble guion bajo
    base = base.split("__")[0]

    # Normalización final
    base = re.sub(r"[^a-z0-9]+", "_", base).strip("_")
    return base or nombre.lower()


def leer_catalogo() -> tuple[list[dict], list[dict]]:
    """Devuelve (pdfs_reales, basura). La basura son los .pdf que no son PDF."""
    with ENTRADA.open(encoding="utf-8") as manejador:
        filas = list(csv.DictReader(manejador))

    for fila in filas:
        for campo in ("bytes", "paginas", "chars_total", "paginas_texto",
                      "paginas_escaneadas", "paginas_vacias"):
            fila[campo] = int(fila.get(campo) or 0)

    pdfs = [f for f in filas if f.get("tipo_archivo") == "PDF"]
    basura = [f for f in filas if f.get("tipo_archivo") != "PDF"]
    return pdfs, basura


def elegir_canonico(copias: list[dict]) -> dict:
    """La mejor copia de una familia: la que más contenido legible aporta."""
    return max(
        copias,
        key=lambda f: (
            f["paginas_texto"],
            f["paginas"],
            f["bytes"],
            -PRIORIDAD_CARPETA.get(f["carpeta_origen"], 9),
        ),
    )


def main() -> None:
    if not ENTRADA.exists():
        raise SystemExit(f"Falta {ENTRADA}. Corre primero fase0_catalogo.py")

    filas, basura = leer_catalogo()
    print(f"Filas en el catálogo : {len(filas) + len(basura)}")
    print(f"PDFs reales          : {len(filas)}")
    print(f"Descartados (no PDF) : {len(basura)}")

    tipos_basura: dict[str, int] = defaultdict(int)
    for f in basura:
        tipos_basura[f.get("tipo_archivo", "?")] += 1
    for tipo, cantidad in sorted(tipos_basura.items(), key=lambda x: -x[1]):
        print(f"    {tipo:15s} {cantidad:5d}")

    # --- Reasignar comuna contra la lista oficial ---------------------------
    oficiales_ordenados = cargar_comunas_oficiales()
    if not oficiales_ordenados:
        raise SystemExit(f"Falta o está vacío {LISTA_COMUNAS}")

    for fila in filas:
        fila["comuna"] = inferir_comuna(fila["ruta"], oficiales_ordenados)

    huerfanos = sum(1 for f in filas if f["comuna"] == "SIN_COMUNA")
    print(f"PDFs sin comuna reconocible: {huerfanos}")

    # --- Agrupar por familia ------------------------------------------------
    familias: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for fila in filas:
        clave = (fila["comuna"], normalizar_familia(fila["nombre"], fila["comuna"]))
        familias[clave].append(fila)

    canonicos: list[dict] = []
    for (comuna, familia), copias in familias.items():
        elegido = elegir_canonico(copias)
        hashes = {c["sha256"] for c in copias if c["sha256"]}

        registro = dict(elegido)
        registro["familia"] = familia
        registro["copias"] = len(copias)
        registro["copias_distintas"] = len(hashes)
        registro["rutas_copias"] = " | ".join(sorted(c["ruta"] for c in copias))
        canonicos.append(registro)

    canonicos.sort(key=lambda r: (r["comuna"], r["familia"]))

    columnas = ["comuna", "familia", "ruta", "carpeta_origen", "nombre", "bytes",
                "paginas", "paginas_texto", "paginas_escaneadas", "paginas_vacias",
                "veredicto", "copias", "copias_distintas", "rutas_copias"]

    with SALIDA_CORPUS.open("w", newline="", encoding="utf-8") as manejador:
        escritor = csv.DictWriter(manejador, fieldnames=columnas, extrasaction="ignore")
        escritor.writeheader()
        escritor.writerows(canonicos)

    # --- Cobertura por comuna ----------------------------------------------
    comunas_oficiales = oficiales_ordenados

    por_comuna: dict[str, list[dict]] = defaultdict(list)
    for r in canonicos:
        por_comuna[r["comuna"]].append(r)

    oficiales = set(comunas_oficiales)

    filas_cobertura = []
    for comuna in sorted(set(por_comuna) | oficiales):
        docs = por_comuna.get(comuna, [])
        filas_cobertura.append({
            "comuna": comuna,
            "es_comuna_oficial": "si" if comuna in oficiales else "NO",
            "documentos": len(docs),
            "con_texto": sum(1 for d in docs if d["veredicto"] == "TEXTO"),
            "mixtos": sum(1 for d in docs if d["veredicto"] == "MIXTO"),
            "escaneados": sum(1 for d in docs if d["veredicto"] == "ESCANEADO"),
            "vacios_ilegibles": sum(1 for d in docs if d["veredicto"] in ("VACIO", "ILEGIBLE")),
            "paginas_totales": sum(d["paginas"] for d in docs),
            "paginas_a_ocr": sum(d["paginas_escaneadas"] for d in docs),
        })

    with SALIDA_COBERTURA.open("w", newline="", encoding="utf-8") as manejador:
        escritor = csv.DictWriter(manejador, fieldnames=list(filas_cobertura[0]))
        escritor.writeheader()
        escritor.writerows(filas_cobertura)

    # --- Resumen ------------------------------------------------------------
    veredictos: dict[str, int] = defaultdict(int)
    for r in canonicos:
        veredictos[r["veredicto"]] += 1

    mixtos = [r for r in canonicos if r["veredicto"] == "MIXTO"]
    sin_docs = [f for f in filas_cobertura
                if f["documentos"] == 0 and f["es_comuna_oficial"] == "si"]
    no_oficiales = [f for f in filas_cobertura if f["es_comuna_oficial"] == "NO"]

    print("\n=== CORPUS ÚNICO ===")
    print(f"PDFs reales              : {len(filas)}")
    print(f"Documentos únicos        : {len(canonicos)}  "
          f"(se colapsaron {len(filas) - len(canonicos)} copias)")
    print(f"Comunas oficiales cubiertas: "
          f"{len([f for f in filas_cobertura if f['es_comuna_oficial']=='si' and f['documentos']>0])}"
          f" / {len(oficiales)}")
    print(f"Comunas oficiales SIN nada : {len(sin_docs)}")
    if no_oficiales:
        print(f"Slugs NO reconocidos       : {len(no_oficiales)}  "
              f"(inferencia de comuna a revisar)")
        for f in sorted(no_oficiales, key=lambda x: -x["documentos"])[:8]:
            print(f"    {f['documentos']:4d} docs | {f['comuna'][:55]}")

    print("\nVeredicto de capa de texto (sobre el corpus único):")
    for veredicto, cantidad in sorted(veredictos.items(), key=lambda x: -x[1]):
        print(f"  {veredicto:10s} {cantidad:5d}")

    total_ocr = sum(r["paginas_escaneadas"] for r in canonicos)
    print(f"\nPáginas que requieren lectura visual: {total_ocr:,}")
    print(f"  de las cuales, ocultas en documentos MIXTOS: "
          f"{sum(r['paginas_escaneadas'] for r in mixtos):,} "
          f"(en {len(mixtos)} documentos)")

    print("\nDocumentos MIXTOS con más páginas escaneadas ocultas:")
    for r in sorted(mixtos, key=lambda x: -x["paginas_escaneadas"])[:12]:
        print(f"  {r['paginas_escaneadas']:4d}/{r['paginas']:4d} | "
              f"{r['comuna'][:16]:16s} | {r['nombre'][:58]}")

    print(f"\nCorpus    : {SALIDA_CORPUS}")
    print(f"Cobertura : {SALIDA_COBERTURA}")


if __name__ == "__main__":
    main()
