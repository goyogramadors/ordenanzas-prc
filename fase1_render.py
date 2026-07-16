#!/usr/bin/env python3
"""
Fase 1 - Paso 3: renderizado BARATO para los documentos que quedaron indeterminados.

Renderiza 1-2 paginas a 100 dpi (NO el documento entero: eso es Fase 3 y ya hay
un mapa de paginas para hacerlo dirigido).

  pagina 1  -> portada / titulo del decreto: dice QUE es el documento
  pagina X  -> ~35% del documento: es donde suelen vivir los cuadros de zonas

Uso:
  python fase1_render.py --ids fase1_visual_pendientes.json
Escribe fase1_render/<id>_p<N>.png y un indice fase1_render/indice.json
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
FEATURES = RAIZ / "fase1_features.json"
MAPA = RAIZ / "fase1_mapa_ids.json"
DIR_OUT = RAIZ / "fase1_render"

POPPLER = Path(
    r"C:\Users\gcastillo\AppData\Local\Microsoft\WinGet\Packages"
    r"\oschwartz10612.Poppler_Microsoft.Winget.Source_8wekyb3d8bbwe"
    r"\poppler-25.07.0\Library\bin"
)
PDFTOPPM = POPPLER / "pdftoppm.exe"
DPI = 100


def paginas_a_mirar(n_pag: int) -> list[int]:
    """Pagina 1 siempre (dice que es). Y una del cuerpo, donde viven las tablas."""
    if n_pag <= 1:
        return [1]
    if n_pag <= 3:
        return [1, n_pag]
    # ~35% adentro: pasada la portada y los vistos, entrando en el articulado
    return [1, max(2, int(n_pag * 0.35))]


def render(pdf: Path, pagina: int, destino_base: Path) -> Path | None:
    try:
        subprocess.run(
            [str(PDFTOPPM), "-f", str(pagina), "-l", str(pagina), "-r", str(DPI),
             "-png", "-singlefile", str(pdf), str(destino_base)],
            capture_output=True, timeout=120, check=False,
        )
    except (subprocess.TimeoutExpired, OSError) as e:
        print(f"  fallo {destino_base.name}: {e}", file=sys.stderr)
        return None
    p = destino_base.with_suffix(".png")
    return p if p.exists() and p.stat().st_size > 0 else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ids", required=True, help="JSON con la lista de ids a renderizar")
    ap.add_argument("--limpiar", action="store_true")
    args = ap.parse_args()

    if not PDFTOPPM.exists():
        print(f"ERROR: no encuentro pdftoppm en {PDFTOPPM}", file=sys.stderr)
        return 1

    feats = json.loads(FEATURES.read_text(encoding="utf-8"))
    mapa = json.loads(MAPA.read_text(encoding="utf-8"))
    ids = json.loads(Path(args.ids).read_text(encoding="utf-8"))

    if args.limpiar and DIR_OUT.exists():
        shutil.rmtree(DIR_OUT)
    DIR_OUT.mkdir(exist_ok=True)

    indice = {}
    fallos = []
    for k, did in enumerate(ids, 1):
        ruta_rel = mapa.get(did)
        if not ruta_rel:
            fallos.append({"id": did, "error": "id desconocido"})
            continue
        v = feats[ruta_rel]
        pdf = RAIZ / ruta_rel
        if not pdf.exists():
            fallos.append({"id": did, "error": "el pdf no existe en disco"})
            continue

        pngs = []
        for pag in paginas_a_mirar(v["paginas"]):
            base = DIR_OUT / f"{did}_p{pag}"
            if base.with_suffix(".png").exists():
                pngs.append(str(base.with_suffix(".png")))
                continue
            p = render(pdf, pag, base)
            if p:
                pngs.append(str(p))

        if not pngs:
            fallos.append({"id": did, "error": "no se pudo renderizar ninguna pagina"})
            continue

        indice[did] = {
            "comuna": v["comuna"],
            "nombre_documento": v["familia"],
            "veredicto_capa_texto": v["veredicto"],
            "paginas": v["paginas"],
            "imagenes": pngs,
        }
        if k % 25 == 0:
            print(f"  {k}/{len(ids)} ...", flush=True)

    (DIR_OUT / "indice.json").write_text(
        json.dumps(indice, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"\nrenderizados: {len(indice)} documentos "
          f"({sum(len(v['imagenes']) for v in indice.values())} imagenes a {DPI} dpi)")
    if fallos:
        print(f"fallos: {len(fallos)}")
        for f in fallos[:10]:
            print("  ", f)
        (DIR_OUT / "fallos.json").write_text(
            json.dumps(fallos, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
