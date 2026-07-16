#!/usr/bin/env python3
"""
Fase 1 - Consolidacion final.

Fusiona las capas de decision, de menos a mas autoridad:

  1. REGEX     (fase1_features.json -> .pre)          metodo=NOMBRE|TEXTO
  2. AGENTE    (fase1_clasificacion_agentes.json)     metodo=NOMBRE|TEXTO
  3. VISUAL    (fase1_visual.json)                    metodo=VISUAL
  4. AUDITORIA de descartes (fase1_auditoria.json)    -> solo puede RESCATAR

La capa 4 es deliberadamente asimetrica: un auditor que discrepa de un descarte
NUNCA lo confirma en silencio, lo sube a ESCALAR. Un auditor no puede convertir
un SI en un NO. Asi el sesgo del pipeline apunta siempre hacia la inclusion.

Salidas:
  corpus_clasificado.csv   - todo el corpus con categoria/sirve/confianza/motivo/metodo
  lista_blanca.csv         - los sirve=SI, ordenados por comuna
  descartados.csv          - los sirve=NO, con motivo (esto lo audita el humano)
  escalados.csv            - los sirve=ESCALAR (quedaron sin resolver)
  recuperables_pendientes.csv - los no-PDF que son ordenanzas en contenedor equivocado
  fase1_cobertura.csv      - estado de las 343 comunas
"""
from __future__ import annotations

import collections
import csv
import json
import re
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent

F_FEATURES = RAIZ / "fase1_features.json"
F_MAPA = RAIZ / "fase1_mapa_ids.json"
F_AGENTES = RAIZ / "fase1_clasificacion_agentes.json"
F_VISUAL = RAIZ / "fase1_visual.json"
F_AUDIT = RAIZ / "fase1_auditoria.json"
F_COMUNAS = RAIZ / "comunas_chile.txt"
DIR_RECUP = RAIZ / "_recuperables_no_pdf"

CATEGORIAS_SI = {"ORDENANZA_PRC", "MODIFICACION_PRC", "ENMIENDA_PRC", "PRI_INTERCOMUNAL"}

COLS = ["comuna", "familia", "ruta", "nombre", "paginas", "paginas_texto",
        "paginas_escaneadas", "veredicto", "categoria", "sirve", "confianza",
        "motivo", "metodo", "rutas_copias"]


def slug(s: str) -> str:
    s = unicodedata.normalize("NFKD", s.strip().lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-z0-9]+", "_", s)
    return re.sub(r"_+", "_", s).strip("_")


def comunas_oficiales() -> list[str]:
    """OJO: comunas_chile.txt trae lineas de comentario con '#' (marcan la region).
    Si no se filtran, se cuelan como comunas fantasma en el informe de cobertura."""
    out = []
    for linea in F_COMUNAS.read_text(encoding="utf-8", errors="replace").splitlines():
        linea = linea.strip()
        if not linea or linea.startswith("#"):
            continue
        out.append(slug(linea))
    return out


def cargar(p: Path):
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def main() -> None:
    feats = cargar(F_FEATURES)
    mapa = cargar(F_MAPA)                      # id -> ruta
    if not feats or not mapa:
        raise SystemExit("faltan fase1_features.json / fase1_mapa_ids.json")
    inv = {ruta: did for did, ruta in mapa.items()}   # ruta -> id

    agentes = cargar(F_AGENTES) or {}
    visual = cargar(F_VISUAL) or {}
    audit = cargar(F_AUDIT) or {}

    corpus = {r["ruta"]: r for r in
              csv.DictReader(open(RAIZ / "corpus_unico.csv", encoding="utf-8"))}

    filas = []
    trazas = []
    for ruta, v in feats.items():
        did = inv[ruta]
        pre = v["pre"]

        # --- capa 1: regex ---
        dec = dict(categoria=pre["categoria"], sirve=pre["sirve"],
                   confianza=pre["confianza"], motivo=pre["motivo"],
                   metodo=pre["metodo"], fuente="REGEX")

        # --- capa 2: agente sobre nombre+texto ---
        a = agentes.get(did)
        if a:
            dec = dict(categoria=a["categoria"], sirve=a["sirve"],
                       confianza=a["confianza"], motivo=a["motivo"],
                       metodo=a["metodo"], fuente="AGENTE")

        # --- capa 3: lectura visual ---
        vi = visual.get(did)
        if vi:
            dec = dict(categoria=vi["categoria"], sirve=vi["sirve"],
                       confianza=vi["confianza"], motivo=vi["motivo"],
                       metodo="VISUAL", fuente="VISUAL")

        # --- capa 4: auditoria de descartes (solo rescata, nunca descarta) ---
        au = audit.get(did)
        if au and dec["sirve"] == "NO":
            if au.get("rescatar"):
                dec = dict(
                    categoria=au.get("categoria") or "INDETERMINADO",
                    sirve="ESCALAR",
                    confianza="BAJA",
                    motivo=f"RESCATADO POR AUDITORIA: {au.get('motivo','')} "
                           f"[descarte previo: {dec['motivo']}]",
                    metodo=dec["metodo"], fuente="AUDITORIA",
                )
            else:
                dec["motivo"] = f"{dec['motivo']} [descarte confirmado por auditor independiente]"
                if dec["confianza"] != "ALTA":
                    dec["confianza"] = "ALTA"

        # coherencia: la categoria manda sobre sirve, salvo ESCALAR
        if dec["sirve"] == "SI" and dec["categoria"] not in CATEGORIAS_SI:
            dec["sirve"] = "ESCALAR"
            dec["motivo"] += " [incoherencia categoria/sirve -> escalado]"
        if dec["sirve"] == "NO" and dec["categoria"] in CATEGORIAS_SI:
            dec["sirve"] = "ESCALAR"
            dec["motivo"] += " [incoherencia categoria/sirve -> escalado]"

        base = corpus[ruta]
        filas.append({
            "comuna": base["comuna"], "familia": base["familia"], "ruta": ruta,
            "nombre": base["nombre"], "paginas": base["paginas"],
            "paginas_texto": base["paginas_texto"],
            "paginas_escaneadas": base["paginas_escaneadas"],
            "veredicto": base["veredicto"],
            "categoria": dec["categoria"], "sirve": dec["sirve"],
            "confianza": dec["confianza"], "motivo": dec["motivo"],
            "metodo": dec["metodo"], "rutas_copias": base["rutas_copias"],
        })
        trazas.append({"id": did, "ruta": ruta, "fuente_final": dec["fuente"]})

    filas.sort(key=lambda r: (r["comuna"], r["familia"]))

    def escribir(nombre: str, rows: list[dict]) -> None:
        with open(RAIZ / nombre, "w", newline="", encoding="utf-8-sig") as fh:
            w = csv.DictWriter(fh, fieldnames=COLS)
            w.writeheader()
            w.writerows(rows)

    escribir("corpus_clasificado.csv", filas)
    escribir("lista_blanca.csv", [r for r in filas if r["sirve"] == "SI"])
    escribir("descartados.csv", [r for r in filas if r["sirve"] == "NO"])
    escribir("escalados.csv", [r for r in filas if r["sirve"] == "ESCALAR"])

    (RAIZ / "fase1_trazas.json").write_text(
        json.dumps(trazas, ensure_ascii=False, indent=1), encoding="utf-8")

    # ---------- recuperables (no-PDF: ordenanzas en contenedor equivocado) ----------
    recup = []
    if DIR_RECUP.exists():
        oficiales = comunas_oficiales()
        oficiales.sort(key=len, reverse=True)   # prefijo mas largo gana
        for p in sorted(DIR_RECUP.iterdir()):
            if p.is_dir():
                continue
            s = slug(p.stem)
            com = next((c for c in oficiales if s.startswith(c)), "SIN_COMUNA")
            recup.append({
                "comuna": com, "archivo": p.name,
                "extension": p.suffix.lower(),
                "bytes": p.stat().st_size,
                "estado": "PENDIENTE_CONVERSION",
            })
    if recup:
        with open(RAIZ / "recuperables_pendientes.csv", "w", newline="",
                  encoding="utf-8-sig") as fh:
            w = csv.DictWriter(fh, fieldnames=["comuna", "archivo", "extension",
                                               "bytes", "estado"])
            w.writeheader()
            w.writerows(sorted(recup, key=lambda r: r["comuna"]))

    # ---------- cobertura de las comunas oficiales ----------
    oficiales = comunas_oficiales()
    utiles = collections.Counter()
    escal = collections.Counter()
    tot = collections.Counter()
    for r in filas:
        tot[r["comuna"]] += 1
        if r["sirve"] == "SI":
            utiles[r["comuna"]] += 1
        elif r["sirve"] == "ESCALAR":
            escal[r["comuna"]] += 1
    recup_com = collections.Counter(r["comuna"] for r in recup)

    cob = []
    for c in sorted(set(oficiales)):
        cob.append({
            "comuna": c,
            "documentos": tot.get(c, 0),
            "utiles": utiles.get(c, 0),
            "escalados": escal.get(c, 0),
            "recuperables": recup_com.get(c, 0),
            "estado": ("CON_NORMA" if utiles.get(c, 0)
                       else "SOLO_ESCALADOS" if escal.get(c, 0)
                       else "SOLO_RECUPERABLES" if recup_com.get(c, 0)
                       else "SIN_NADA"),
        })
    with open(RAIZ / "fase1_cobertura.csv", "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=["comuna", "documentos", "utiles",
                                           "escalados", "recuperables", "estado"])
        w.writeheader()
        w.writerows(cob)

    # ---------- resumen ----------
    c_cat = collections.Counter(r["categoria"] for r in filas)
    c_sirve = collections.Counter(r["sirve"] for r in filas)
    c_met = collections.Counter(r["metodo"] for r in filas)
    c_fuente = collections.Counter(t["fuente_final"] for t in trazas)
    c_estado = collections.Counter(r["estado"] for r in cob)

    print("=" * 62)
    print(f"CORPUS CLASIFICADO: {len(filas)} documentos")
    print("=" * 62)
    print("\ncategoria:")
    for k, v in c_cat.most_common():
        print(f"  {k:<24} {v:>5}")
    print("\nsirve:")
    for k, v in c_sirve.most_common():
        print(f"  {k:<24} {v:>5}")
    print("\nmetodo (con que evidencia se decidio):")
    for k, v in c_met.most_common():
        print(f"  {k:<24} {v:>5}")
    print("\ncapa que puso el veredicto final:")
    for k, v in c_fuente.most_common():
        print(f"  {k:<24} {v:>5}")
    print(f"\nCOBERTURA sobre {len(cob)} comunas oficiales:")
    for k, v in c_estado.most_common():
        print(f"  {k:<24} {v:>5}")

    sin_nada = [c["comuna"] for c in cob if c["estado"] == "SIN_NADA"]
    print(f"\ncomunas SIN NADA ({len(sin_nada)}):")
    for i in range(0, len(sin_nada), 6):
        print("  " + ", ".join(sin_nada[i:i + 6]))


if __name__ == "__main__":
    main()
