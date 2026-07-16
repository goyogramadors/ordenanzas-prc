"""
FASE 0 (paso 3) — Limpieza de los .pdf que no son PDF
=====================================================
El bot de descarga guardó respuestas HTML del portal (landing de LeyChile,
páginas de error) con extensión .pdf. Este script las elimina.

Dos comportamientos DISTINTOS según el tipo real del archivo:

  HTML  -> SE BORRA. No tiene contenido recuperable: es una página web.

  ZIP / OFFICE / IMAGEN / RAR / OTRO -> SE MUEVE a `_recuperables_no_pdf/`,
        NO se borra. Muchos son ordenanzas de verdad en el contenedor
        equivocado (Doñihue trae el plan regulador en un ZIP de 5 MB; Papudo,
        "aprueba plano regulador y ordenanza local" en 6,5 MB; Lonquimay en
        .doc; Catemu y Villarrica como imagen). Para varias de esas comunas es
        el ÚNICO material que existe: borrarlos sería destruir la fuente.

Seguridad: antes de tocar cada archivo se releen sus bytes de cabecera. Si el
archivo ya no es lo que decía el catálogo, se deja intacto y se reporta. El
catálogo puede estar desactualizado; los bytes en disco, no.

Uso:
    python fase0_limpiar_html.py            # simulacro, no toca nada
    python fase0_limpiar_html.py --ejecutar # aplica los cambios
"""

from __future__ import annotations

import argparse
import csv
import shutil
from datetime import datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
CATALOGO = RAIZ / "catalogo_maestro.csv"
CUARENTENA = RAIZ / "_recuperables_no_pdf"
REGISTRO = RAIZ / "fase0_limpieza_registro.csv"

TIPOS_A_BORRAR = {"HTML"}
TIPOS_A_RESCATAR = {"ZIP_OFFICE", "OFFICE_ANTIGUO", "IMAGEN", "RAR", "OTRO"}

# Extensión real sugerida para cada tipo, al mover a cuarentena.
EXTENSION_REAL = {
    "ZIP_OFFICE": ".zip",
    "OFFICE_ANTIGUO": ".doc",
    "IMAGEN": ".jpg",
    "RAR": ".rar",
    "OTRO": ".bin",
}


def tipo_real(ruta: Path) -> str:
    """Relee los bytes en disco. No se confía en lo que dice el catálogo."""
    try:
        with ruta.open("rb") as manejador:
            cabecera = manejador.read(1024)
    except OSError:
        return "ERROR"

    if not cabecera:
        return "VACIO"

    inicio = cabecera.lstrip()[:512].lower()

    if cabecera[:5] == b"%PDF-":
        return "PDF"
    if inicio.startswith(b"<!doctype html") or inicio.startswith(b"<html") or b"<html" in inicio[:200]:
        return "HTML"
    if cabecera[:4] == b"PK\x03\x04":
        return "ZIP_OFFICE"
    if cabecera[:4] == b"\xd0\xcf\x11\xe0":
        return "OFFICE_ANTIGUO"
    if cabecera[:3] == b"\xff\xd8\xff":
        return "IMAGEN"
    if cabecera[:4] == b"Rar!":
        return "RAR"
    return "OTRO"


def destino_cuarentena(ruta: Path, tipo: str) -> Path:
    """Ruta en cuarentena, con la extensión REAL y sin colisiones de nombre."""
    extension = EXTENSION_REAL.get(tipo, ".bin")
    base = ruta.stem  # el .pdf mentiroso se descarta
    candidato = CUARENTENA / f"{base}{extension}"

    contador = 2
    while candidato.exists():
        candidato = CUARENTENA / f"{base}__{contador}{extension}"
        contador += 1
    return candidato


def main() -> None:
    analizador = argparse.ArgumentParser(
        description="Borra los HTML disfrazados de PDF y rescata el resto."
    )
    analizador.add_argument(
        "--ejecutar", action="store_true",
        help="Aplica los cambios. Sin este flag solo simula.",
    )
    argumentos = analizador.parse_args()
    simulacro = not argumentos.ejecutar

    if not CATALOGO.exists():
        raise SystemExit(f"Falta {CATALOGO}. Corre antes fase0_catalogo.py")

    with CATALOGO.open(encoding="utf-8") as manejador:
        filas = list(csv.DictReader(manejador))

    candidatos = [
        f for f in filas
        if f["tipo_archivo"] in TIPOS_A_BORRAR | TIPOS_A_RESCATAR
    ]

    print("MODO SIMULACRO — no se toca ningún archivo\n" if simulacro
          else "MODO EJECUCIÓN — se aplicarán los cambios\n")
    print(f"Candidatos según el catálogo: {len(candidatos)}")

    if not simulacro:
        CUARENTENA.mkdir(exist_ok=True)

    borrados = 0
    rescatados = 0
    intactos_por_discrepancia = 0
    no_encontrados = 0
    eventos: list[dict] = []

    for fila in candidatos:
        ruta = RAIZ / fila["ruta"]

        if not ruta.is_file():
            no_encontrados += 1
            continue

        # Verificación en disco: manda el archivo, no el catálogo.
        tipo_ahora = tipo_real(ruta)
        tipo_catalogo = fila["tipo_archivo"]

        if tipo_ahora != tipo_catalogo:
            intactos_por_discrepancia += 1
            eventos.append({
                "accion": "INTACTO_DISCREPANCIA",
                "ruta": fila["ruta"],
                "tipo_catalogo": tipo_catalogo,
                "tipo_en_disco": tipo_ahora,
                "destino": "",
            })
            print(f"  ! DISCREPANCIA, se deja intacto: catálogo dice "
                  f"{tipo_catalogo}, el disco dice {tipo_ahora} | {ruta.name[:50]}")
            continue

        if tipo_ahora in TIPOS_A_BORRAR:
            if not simulacro:
                ruta.unlink()
            borrados += 1
            eventos.append({
                "accion": "BORRADO",
                "ruta": fila["ruta"],
                "tipo_catalogo": tipo_catalogo,
                "tipo_en_disco": tipo_ahora,
                "destino": "",
            })

        elif tipo_ahora in TIPOS_A_RESCATAR:
            destino = destino_cuarentena(ruta, tipo_ahora)
            if not simulacro:
                shutil.move(str(ruta), str(destino))
            rescatados += 1
            eventos.append({
                "accion": "RESCATADO",
                "ruta": fila["ruta"],
                "tipo_catalogo": tipo_catalogo,
                "tipo_en_disco": tipo_ahora,
                "destino": str(destino.relative_to(RAIZ)),
            })

    # --- Registro -----------------------------------------------------------
    if not simulacro and eventos:
        with REGISTRO.open("w", newline="", encoding="utf-8") as manejador:
            escritor = csv.DictWriter(
                manejador,
                fieldnames=["accion", "ruta", "tipo_catalogo", "tipo_en_disco", "destino"],
            )
            escritor.writeheader()
            escritor.writerows(eventos)

    # --- Resumen ------------------------------------------------------------
    verbo = "se borrarían" if simulacro else "borrados"
    verbo2 = "se rescatarían" if simulacro else "rescatados"

    print(f"\n=== RESUMEN ({datetime.now():%Y-%m-%d %H:%M}) ===")
    print(f"HTML {verbo:16s}: {borrados}")
    print(f"No-PDF {verbo2:14s}: {rescatados}  -> {CUARENTENA.name}/")
    if intactos_por_discrepancia:
        print(f"Intactos por discrepancia: {intactos_por_discrepancia}")
    if no_encontrados:
        print(f"Ya no existían         : {no_encontrados}")

    if simulacro:
        print("\nNada fue modificado. Para aplicar:  python fase0_limpiar_html.py --ejecutar")
    else:
        print(f"\nRegistro de lo hecho: {REGISTRO}")
        print("Recuerda regenerar el catálogo:  python fase0_catalogo.py && python fase0_consolidar.py")


if __name__ == "__main__":
    main()
