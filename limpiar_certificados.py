#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Elimina de la carpeta descargas/ los PDF que son "Certificado de Informes
Previos" / "Certificado de Informaciones Previas" (CIP), que no son ordenanzas
ni modificaciones del Plan Regulador y se colaron en descargas anteriores.

Coincide de forma conservadora: solo borra si el nombre del archivo contiene
"certificad... (de) inform(es|aciones)... previ..." (previos/previas/previa).
NO borra otros documentos que solo mencionan "certificado" (p. ej. certificado
de exposicion del plan regulador, antecedentes previos, cartas certificadas).

Uso:
    python limpiar_certificados.py            # ELIMINA (mostrando cada archivo)
    python limpiar_certificados.py --dry-run  # solo muestra, no borra
"""

import argparse
import re
import sys
import unicodedata
from pathlib import Path

DIR = Path(__file__).parent
DESCARGAS = DIR / "descargas"

# La frase que define a un Certificado de Informaciones/Informes Previos (CIP):
# "informes previos" / "informaciones previas" (con o sin separador, porque a
# veces el nombre viene pegado en camelCase, ej. "InformacionesPreviasN125").
# Es lo bastante especifica para no borrar ordenanzas del plan regulador.
PATRON_CIP = re.compile(
    r"inform(?:e|aci[oó]?n)[a-z]*\s*previ",
    re.I,
)


def normaliza(nombre: str) -> str:
    """Minusculas, sin acentos, con separadores (_, -, espacios) como espacio."""
    t = unicodedata.normalize("NFKD", nombre).encode("ascii", "ignore").decode()
    t = re.sub(r"[^\w]+", " ", t)
    t = re.sub(r"_+", " ", t)
    t = re.sub(r"\s+", " ", t)
    return t.lower().strip()


def es_cip(pdf: Path) -> bool:
    return bool(PATRON_CIP.search(normaliza(pdf.stem)))


def main() -> int:
    ap = argparse.ArgumentParser(description="Elimina PDFs de Certificado de Informaciones/Informes Previos")
    ap.add_argument("--dry-run", action="store_true",
                     help="Solo muestra que borraria, sin eliminar nada")
    args = ap.parse_args()

    if not DESCARGAS.exists():
        print(f"No existe la carpeta {DESCARGAS}")
        return 1

    encontrados = [p for p in DESCARGAS.rglob("*.pdf") if es_cip(p)]
    if not encontrados:
        print("No se encontraron PDFs de 'certificado de informes/informaciones previas'.")
        return 0

    total_bytes = 0
    modo = "[DRY-RUN] se borraria" if args.dry_run else "eliminado"
    # agrupa por comuna (primer nivel bajo descargas/) para un resumen legible
    por_comuna = {}
    for p in encontrados:
        try:
            rel = p.relative_to(DESCARGAS)
            comuna = rel.parts[0]
        except Exception:
            comuna = "?"
        por_comuna.setdefault(comuna, []).append(p)

    for comuna in sorted(por_comuna):
        archivos = por_comuna[comuna]
        print(f"\n== {comuna} ({len(archivos)}) ==")
        for p in archivos:
            try:
                size = p.stat().st_size
            except OSError:
                size = 0
            total_bytes += size
            print(f"  {modo}: {p.name}  ({size // 1024} KB)")
            if not args.dry_run:
                try:
                    p.unlink()
                except OSError as e:
                    print(f"    !! no se pudo borrar: {e}")

    accion = "Se borrarian" if args.dry_run else "Eliminados"
    print(f"\n{accion} {len(encontrados)} archivo(s), "
          f"{total_bytes // (1024*1024)} MB en {len(por_comuna)} comuna(s).")
    if args.dry_run:
        print("(dry-run: no se borro nada; corre sin --dry-run para eliminar)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
