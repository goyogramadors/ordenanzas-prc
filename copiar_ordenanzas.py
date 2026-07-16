# -*- coding: utf-8 -*-
"""
Copia (no mueve) todos los PDFs de descargas/<comuna>/**/*.pdf a una sola
carpeta plana "Ordenanzas Descargadas", prefijando cada archivo con el nombre
de la comuna (la carpeta de primer nivel) seguido de "_".

No elimina nada del origen. Ante colisiones de nombre en el destino, agrega un
sufijo numérico para no sobrescribir.
"""
import shutil
from pathlib import Path

BASE = Path(__file__).resolve().parent
ORIGEN = BASE / "descargas"
DESTINO = BASE / "Ordenanzas Descargadas"

def main():
    DESTINO.mkdir(exist_ok=True)

    total = 0
    copiados = 0
    saltados_existentes = 0  # ya existían idénticos en destino
    colisiones_renombradas = 0
    errores = []

    # Cada carpeta de primer nivel bajo descargas es una comuna
    comunas = sorted([p for p in ORIGEN.iterdir() if p.is_dir()])

    for comuna_dir in comunas:
        comuna = comuna_dir.name
        # Todos los PDF de la comuna, en cualquier subcarpeta
        for pdf in comuna_dir.rglob("*.pdf"):
            if not pdf.is_file():
                continue
            total += 1
            nombre_destino = f"{comuna}_{pdf.name}"
            destino_path = DESTINO / nombre_destino

            # Si ya existe un archivo con ese nombre, verificar si es el mismo
            if destino_path.exists():
                if destino_path.stat().st_size == pdf.stat().st_size:
                    # Muy probablemente ya copiado en una corrida previa
                    saltados_existentes += 1
                    continue
                # Colisión real: mismo nombre, distinto contenido -> renombrar
                stem = destino_path.stem
                suffix = destino_path.suffix
                n = 1
                while True:
                    candidato = DESTINO / f"{stem}__{n}{suffix}"
                    if not candidato.exists():
                        destino_path = candidato
                        colisiones_renombradas += 1
                        break
                    n += 1

            try:
                shutil.copy2(pdf, destino_path)
                copiados += 1
            except Exception as e:
                errores.append((str(pdf), str(e)))

    print("=" * 60)
    print(f"Comunas procesadas          : {len(comunas)}")
    print(f"PDFs encontrados en origen  : {total}")
    print(f"PDFs copiados               : {copiados}")
    print(f"Ya existían (saltados)      : {saltados_existentes}")
    print(f"Colisiones renombradas      : {colisiones_renombradas}")
    print(f"Errores                     : {len(errores)}")
    print(f"Total archivos en destino   : {len(list(DESTINO.glob('*.pdf')))}")
    print(f"Carpeta destino             : {DESTINO}")
    if errores:
        print("\n--- ERRORES ---")
        for ruta, err in errores[:20]:
            print(f"  {ruta}\n    -> {err}")

if __name__ == "__main__":
    main()
