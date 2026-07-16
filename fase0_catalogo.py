"""
FASE 0 — Catálogo maestro del corpus de ordenanzas
==================================================
Recorre las TRES copias del corpus, y por cada PDF registra:

  - identidad      : ruta, carpeta origen, comuna inferida, hash SHA-256, bytes
  - estructura     : número de páginas
  - capa de texto  : caracteres NO-ESPACIO **por página** (no por documento)
  - imágenes       : páginas con imagen raster grande (>= 40% del área de página)
  - veredicto      : TEXTO / MIXTO / ESCANEADO / VACIO / ILEGIBLE

Por qué por página y cruzado con imágenes
-----------------------------------------
El caso Caldera (decreto 1718, texto refundido, 61 MB) está en la carpeta
"OCR ok" pero NUNCA fue OCR'd: sus páginas 12-57 —donde viven TODAS las tablas
de zonas— son JPEG. La capa de texto solo trae el encabezado de LeyChile
(~130 caracteres por página). Un contador por documento lo declara "con texto"
y lo deja pasar en silencio. Por eso el detector mira cada página y la contrasta
con la superficie de imagen: página con imagen grande + poco texto = escaneada,
aunque el documento como un todo parezca legible.

Salidas (en la raíz del proyecto):
  catalogo_maestro.csv    — una fila por PDF
  catalogo_paginas.json   — detalle por página (chars + imagen) de cada PDF
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuración
# ---------------------------------------------------------------------------

RAIZ = Path(__file__).resolve().parent

CARPETAS = {
    "descargas": RAIZ / "descargas",
    "descargadas": RAIZ / "Ordenanzas Descargadas",
    "ordenadas": RAIZ / "Ordenanzas ordenadas",
}

POPPLER = Path(
    r"C:\Users\gcastillo\AppData\Local\Microsoft\WinGet\Packages"
    r"\oschwartz10612.Poppler_Microsoft.Winget.Source_8wekyb3d8bbwe"
    r"\poppler-25.07.0\Library\bin"
)

PDFTOTEXT = str(POPPLER / "pdftotext.exe")
PDFINFO = str(POPPLER / "pdfinfo.exe")
PDFIMAGES = str(POPPLER / "pdfimages.exe")

SALIDA_CSV = RAIZ / "catalogo_maestro.csv"
SALIDA_PAGINAS = RAIZ / "catalogo_paginas.json"

# Umbral de caracteres bajo el cual una página se considera SIN texto útil.
# Calibrado con el caso Caldera: el boilerplate de LeyChile aporta ~130 chars
# a una página cuyo contenido real es una imagen. Se deja holgura.
UMBRAL_CHARS_PAGINA = 300

# Una imagen es "de contenido" (un escaneo) y no un logo/firma si supera este
# número de píxeles. Calibrado con Caldera: el logo de LeyChile tiene 59 mil px;
# la tabla escaneada de la página 20 tiene 7,5 millones. El área NO sirve como
# criterio: esa misma tabla es una franja alta y angosta que cubre solo el 24%
# de la página y un umbral por área la dejaba pasar como si fuera un adorno.
UMBRAL_PIXELES_IMAGEN = 400_000

# Criterio secundario: una imagen que cubre buena parte de la página también
# es contenido, aunque tenga pocos píxeles (escaneos de baja resolución).
UMBRAL_AREA_IMAGEN = 0.35

# Un documento es MIXTO si tiene páginas con texto Y páginas escaneadas,
# y las escaneadas superan esta fracción del total.
UMBRAL_MIXTO = 0.10

HILOS = 8
TIEMPO_LIMITE = 180  # segundos por comando

# Prefijos de carpeta que no son comuna
NO_COMUNA = {"diario_oficial", "ordenanzas", "proactiva", "buscador", "1-600",
             "600-1200", "1200 x", "OCR ok", ".venv", "__pycache__"}


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------

def ejecutar(comando: list[str]) -> str:
    """Corre un binario de poppler y devuelve su stdout (vacío si falla)."""
    try:
        resultado = subprocess.run(
            comando,
            capture_output=True,
            timeout=TIEMPO_LIMITE,
            check=False,
        )
        return resultado.stdout.decode("utf-8", errors="replace")
    except (subprocess.TimeoutExpired, OSError):
        return ""


def detectar_tipo(ruta: Path) -> str:
    """
    Tipo REAL del archivo según sus bytes de cabecera, no según su extensión.

    El bot de descarga guardó cientos de respuestas HTML (la landing de LeyChile,
    páginas de error del portal) con extensión .pdf. Confiar en la extensión hace
    que esos archivos aparezcan como "PDF ilegible" y contaminen todo el conteo.
    """
    try:
        with ruta.open("rb") as manejador:
            cabecera = manejador.read(1024)
    except OSError:
        return "ERROR"

    if not cabecera:
        return "VACIO"

    inicio = cabecera.lstrip()[:512].lower()

    if cabecera[:5] == b"%PDF-" or b"%pdf-" in cabecera[:1024].lower()[:20]:
        return "PDF"
    if inicio.startswith(b"<!doctype html") or inicio.startswith(b"<html") or b"<html" in inicio[:200]:
        return "HTML"
    if cabecera[:4] == b"PK\x03\x04":
        return "ZIP_OFFICE"          # .docx/.xlsx o un zip renombrado
    if cabecera[:4] == b"\xd0\xcf\x11\xe0":
        return "OFFICE_ANTIGUO"      # .doc/.xls
    if cabecera[:3] == b"\xff\xd8\xff":
        return "IMAGEN"
    if cabecera[:4] == b"Rar!":
        return "RAR"
    return "OTRO"


def calcular_hash(ruta: Path) -> str:
    """SHA-256 del archivo completo, para detectar duplicados exactos."""
    digestor = hashlib.sha256()
    try:
        with ruta.open("rb") as manejador:
            for bloque in iter(lambda: manejador.read(1 << 20), b""):
                digestor.update(bloque)
        return digestor.hexdigest()
    except OSError:
        return ""


def inferir_comuna(ruta: Path, carpeta_origen: str) -> str:
    """
    Deduce el slug de comuna.
      - en `descargas/` la comuna es la primera subcarpeta
      - en las otras el nombre del archivo empieza con el slug
    """
    if carpeta_origen == "descargas":
        try:
            partes = ruta.relative_to(CARPETAS["descargas"]).parts
            if partes and partes[0] not in NO_COMUNA:
                return partes[0]
        except ValueError:
            pass

    nombre = ruta.stem.lower()
    # El slug es lo anterior al primer token que parece número de decreto o palabra clave
    corte = re.split(
        r"_(?:\d|decreto|resolucion|ordenanza|acuerdo|atribuciones|plan|"
        r"consulta|informe|potestades|otras|sn|orden)",
        nombre,
        maxsplit=1,
    )
    slug = corte[0].strip("_")
    return slug if slug else "desconocido"


def numero_paginas(ruta: Path) -> int:
    salida = ejecutar([PDFINFO, str(ruta)])
    coincidencia = re.search(r"^Pages:\s+(\d+)", salida, re.MULTILINE)
    return int(coincidencia.group(1)) if coincidencia else 0


def tamanos_pagina(ruta: Path) -> tuple[float, float]:
    """Ancho y alto de la página en puntos (para calcular el área)."""
    salida = ejecutar([PDFINFO, str(ruta)])
    coincidencia = re.search(r"^Page size:\s+([\d.]+) x ([\d.]+)", salida, re.MULTILINE)
    if coincidencia:
        return float(coincidencia.group(1)), float(coincidencia.group(2))
    return 612.0, 792.0  # carta por defecto


def chars_por_pagina(ruta: Path, paginas: int) -> list[int]:
    """
    Caracteres no-espacio de CADA página.
    Una sola llamada a pdftotext; las páginas vienen separadas por form-feed.
    """
    salida = ejecutar([PDFTOTEXT, "-q", str(ruta), "-"])
    if not salida:
        return [0] * paginas

    trozos = salida.split("\f")
    # pdftotext deja un form-feed final: se recorta a la cantidad real de páginas
    conteos = [len(re.sub(r"\s", "", t)) for t in trozos[:paginas]]
    conteos += [0] * (paginas - len(conteos))
    return conteos


def paginas_con_imagen_grande(ruta: Path, paginas: int, ancho_pt: float, alto_pt: float) -> set[int]:
    """
    Páginas donde una imagen raster cubre >= UMBRAL_AREA_IMAGEN del área.
    Señal de que el contenido de la página es un escaneo, no texto.
    """
    salida = ejecutar([PDFIMAGES, "-list", str(ruta)])
    if not salida:
        return set()

    grandes: set[int] = set()
    area_pagina_pt = ancho_pt * alto_pt

    for linea in salida.splitlines()[2:]:
        campos = linea.split()
        if len(campos) < 14:
            continue
        try:
            pagina = int(campos[0])
            ancho_px = int(campos[3])
            alto_px = int(campos[4])
            ppi_x = float(campos[12])
            ppi_y = float(campos[13])
        except (ValueError, IndexError):
            continue

        # Criterio principal: masa de píxeles. Distingue una tabla o página
        # escaneada (millones de px) de un logo o una firma (decenas de miles).
        if ancho_px * alto_px >= UMBRAL_PIXELES_IMAGEN:
            grandes.add(pagina)
            continue

        # Criterio secundario: cobertura de la página, para escaneos de baja
        # resolución que no alcanzan el umbral de píxeles.
        if ppi_x > 0 and ppi_y > 0 and area_pagina_pt > 0:
            ancho_img_pt = (ancho_px / ppi_x) * 72.0
            alto_img_pt = (alto_px / ppi_y) * 72.0
            if (ancho_img_pt * alto_img_pt) / area_pagina_pt >= UMBRAL_AREA_IMAGEN:
                grandes.add(pagina)

    return grandes


def dictaminar(
    paginas: int, conteos: list[int], con_imagen: set[int]
) -> tuple[str, int, int, int]:
    """
    Veredicto del documento y conteo de páginas por tipo.

    Cada página cae en exactamente una de tres categorías:
      - con texto : supera el umbral de caracteres
      - escaneada : poco texto Y una imagen de contenido encima
      - vacía     : poco texto y sin imagen (portadas, separadores, hojas en blanco)

    Ninguna página queda sin clasificar: las "vacías" se cuentan aparte en vez
    de desaparecer del balance, para que un veredicto optimista no oculte
    páginas que en realidad nadie miró.
    """
    if paginas == 0:
        return "ILEGIBLE", 0, 0, 0

    con_texto = 0
    escaneadas = 0
    vacias = 0

    for indice in range(paginas):
        numero = indice + 1
        chars = conteos[indice] if indice < len(conteos) else 0

        if chars >= UMBRAL_CHARS_PAGINA:
            con_texto += 1
        elif numero in con_imagen:
            escaneadas += 1
        else:
            vacias += 1

    if con_texto == 0 and escaneadas == 0:
        return "VACIO", con_texto, escaneadas, vacias
    if con_texto == 0:
        return "ESCANEADO", con_texto, escaneadas, vacias
    if escaneadas / paginas >= UMBRAL_MIXTO:
        return "MIXTO", con_texto, escaneadas, vacias
    return "TEXTO", con_texto, escaneadas, vacias


# ---------------------------------------------------------------------------
# Procesamiento de un PDF
# ---------------------------------------------------------------------------

def analizar(ruta: Path, carpeta_origen: str) -> dict:
    registro: dict = {
        "ruta": str(ruta.relative_to(RAIZ)),
        "carpeta_origen": carpeta_origen,
        "nombre": ruta.name,
        "comuna": inferir_comuna(ruta, carpeta_origen),
        "tipo_archivo": "ERROR",
        "bytes": 0,
        "sha256": "",
        "paginas": 0,
        "chars_total": 0,
        "paginas_texto": 0,
        "paginas_escaneadas": 0,
        "paginas_vacias": 0,
        "veredicto": "ILEGIBLE",
        "_chars_pagina": [],
        "_paginas_imagen": [],
    }

    try:
        registro["bytes"] = ruta.stat().st_size
    except OSError:
        return registro

    registro["tipo_archivo"] = detectar_tipo(ruta)
    registro["sha256"] = calcular_hash(ruta)

    # Si no es un PDF de verdad, no se le corre poppler: se marca y se sale.
    if registro["tipo_archivo"] != "PDF":
        registro["veredicto"] = "NO_ES_PDF"
        return registro

    paginas = numero_paginas(ruta)
    registro["paginas"] = paginas
    if paginas == 0:
        return registro

    ancho, alto = tamanos_pagina(ruta)
    conteos = chars_por_pagina(ruta, paginas)
    con_imagen = paginas_con_imagen_grande(ruta, paginas, ancho, alto)

    veredicto, con_texto, escaneadas, vacias = dictaminar(paginas, conteos, con_imagen)

    registro["chars_total"] = sum(conteos)
    registro["paginas_texto"] = con_texto
    registro["paginas_escaneadas"] = escaneadas
    registro["paginas_vacias"] = vacias
    registro["veredicto"] = veredicto
    registro["_chars_pagina"] = conteos
    registro["_paginas_imagen"] = sorted(con_imagen)

    return registro


# ---------------------------------------------------------------------------
# Principal
# ---------------------------------------------------------------------------

def recolectar_pdfs() -> list[tuple[Path, str]]:
    pendientes: list[tuple[Path, str]] = []
    for etiqueta, carpeta in CARPETAS.items():
        if not carpeta.is_dir():
            print(f"AVISO: no existe {carpeta}")
            continue
        for ruta in carpeta.rglob("*"):
            if ruta.suffix.lower() != ".pdf" or not ruta.is_file():
                continue
            if ".venv" in ruta.parts or "__pycache__" in ruta.parts:
                continue
            pendientes.append((ruta, etiqueta))
    return pendientes


def main() -> None:
    if not Path(PDFTOTEXT).exists():
        sys.exit(f"No se encontró poppler en {POPPLER}")

    pendientes = recolectar_pdfs()
    total = len(pendientes)
    print(f"PDFs a catalogar: {total}")

    registros: list[dict] = []

    with ThreadPoolExecutor(max_workers=HILOS) as ejecutor:
        futuros = {
            ejecutor.submit(analizar, ruta, origen): ruta
            for ruta, origen in pendientes
        }
        for hechos, futuro in enumerate(as_completed(futuros), start=1):
            try:
                registros.append(futuro.result())
            except Exception as error:  # noqa: BLE001 — un PDF roto no detiene el censo
                ruta = futuros[futuro]
                print(f"FALLO {ruta.name}: {error}")
            if hechos % 50 == 0 or hechos == total:
                print(f"  {hechos}/{total}", flush=True)

    registros.sort(key=lambda r: (r["comuna"], r["nombre"]))

    columnas = ["ruta", "carpeta_origen", "comuna", "nombre", "tipo_archivo",
                "bytes", "sha256", "paginas", "chars_total", "paginas_texto",
                "paginas_escaneadas", "paginas_vacias", "veredicto"]

    with SALIDA_CSV.open("w", newline="", encoding="utf-8") as manejador:
        escritor = csv.DictWriter(manejador, fieldnames=columnas, extrasaction="ignore")
        escritor.writeheader()
        escritor.writerows(registros)

    detalle = {
        r["ruta"]: {"chars": r["_chars_pagina"], "img": r["_paginas_imagen"]}
        for r in registros
    }
    SALIDA_PAGINAS.write_text(
        json.dumps(detalle, ensure_ascii=False), encoding="utf-8"
    )

    # ---- Resumen en consola -------------------------------------------------
    por_veredicto: dict[str, int] = {}
    for r in registros:
        por_veredicto[r["veredicto"]] = por_veredicto.get(r["veredicto"], 0) + 1

    hashes = {}
    for r in registros:
        if r["sha256"]:
            hashes.setdefault(r["sha256"], []).append(r["ruta"])
    unicos = len(hashes)
    duplicados = len(registros) - unicos

    por_tipo: dict[str, int] = {}
    for r in registros:
        por_tipo[r["tipo_archivo"]] = por_tipo.get(r["tipo_archivo"], 0) + 1

    print("\n=== CATÁLOGO MAESTRO ===")
    print(f"Archivos .pdf hallados : {len(registros)}")
    print(f"Únicos por hash        : {unicos}  (duplicados exactos: {duplicados})")

    print("\nTipo REAL del archivo (por bytes de cabecera, no por extensión):")
    for tipo, cantidad in sorted(por_tipo.items(), key=lambda x: -x[1]):
        marca = "" if tipo == "PDF" else "   <-- no es un PDF"
        print(f"  {tipo:15s} {cantidad:5d}{marca}")

    print("\nVeredicto de capa de texto:")
    for veredicto, cantidad in sorted(por_veredicto.items(), key=lambda x: -x[1]):
        print(f"  {veredicto:10s} {cantidad:5d}")

    mixtos = [r for r in registros if r["veredicto"] == "MIXTO"]
    print(f"\nDocumentos MIXTOS (texto + tablas escaneadas): {len(mixtos)}")
    print("Los 10 con más páginas escaneadas ocultas:")
    for r in sorted(mixtos, key=lambda x: -x["paginas_escaneadas"])[:10]:
        print(f"  {r['paginas_escaneadas']:4d}/{r['paginas']:4d} pág. esc. | "
              f"{r['comuna'][:18]:18s} | {r['nombre'][:60]}")

    print(f"\nCSV     : {SALIDA_CSV}")
    print(f"Páginas : {SALIDA_PAGINAS}")


if __name__ == "__main__":
    main()
