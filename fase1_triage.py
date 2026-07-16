#!/usr/bin/env python3
"""
Fase 1 - Triage y clasificacion del corpus de ordenanzas.

Pasos implementados aqui (los baratos y deterministas):
  Paso 1: reglas de regex sobre el nombre del archivo.
  Paso 2: extraccion de texto de las primeras paginas con pdftotext y busqueda
          de senales normativas.

Produce `fase1_features.json`: un registro de evidencia por documento que luego
consumen los agentes (Paso 3 y auditoria). El script NO decide solo: marca
`preclasificacion` + `confianza`, y todo lo dudoso queda como ESCALAR.

Reanudable: guarda progreso cada 25 documentos; si se corta, relanzarlo retoma
donde quedo. Usar --rehacer para ignorar la cache.

Trampas contempladas:
  1. El tipo de archivo se detecta por bytes de cabecera, nunca por la extension.
  2. Se confia en la columna `veredicto` del catalogo, no en pdftotext a secas:
     un MIXTO "tiene texto" pero sus tablas son imagenes.
  3. La comuna viene ya resuelta en corpus_unico.csv; aqui no se recalcula.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
ENTRADA = RAIZ / "corpus_unico.csv"
SALIDA_FEATURES = RAIZ / "fase1_features.json"

POPPLER = Path(
    r"C:\Users\gcastillo\AppData\Local\Microsoft\WinGet\Packages"
    r"\oschwartz10612.Poppler_Microsoft.Winget.Source_8wekyb3d8bbwe"
    r"\poppler-25.07.0\Library\bin"
)
PDFTOTEXT = POPPLER / "pdftotext.exe"

PAGINAS_A_LEER = 6          # primeras N paginas para el Paso 2
SNIPPET_CHARS = 2600        # texto que se le pasa al agente
GUARDAR_CADA = 25


# --------------------------------------------------------------------------
# Normalizacion
# --------------------------------------------------------------------------
def sin_tildes(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c))


def norm(s: str) -> str:
    """minusculas, sin tildes, separadores unificados a _"""
    s = sin_tildes(s or "").lower()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    return re.sub(r"_+", "_", s).strip("_")


# --------------------------------------------------------------------------
# PASO 1 - reglas sobre el nombre
# --------------------------------------------------------------------------
# Cada patron: (etiqueta, categoria_sugerida, regex, motivo)
# OJO: estas reglas NO descartan por si solas de forma definitiva. Alimentan al
# agente. Solo las marcadas AUTO_SEGURO se descartan sin mirar contenido.

PAT_DESCARTE = [
    # --- solicitudes ciudadanas de transparencia (son preguntas, no normas) ---
    ("solicitud_ciudadana", "TRAMITE_ADMINISTRATIVO",
     r"(^|_)(solicito|solicitud_de_informacion|solicita_informacion|se_solicita|"
     r"estimad[oa]s?|estimadao|junto_con_saludar|quien_corresponda|a_quien_corresponda|"
     r"buenos_dias|buenas_tardes|de_mi_consideracion|por_medio_de_la_presente)",
     "el nombre es una solicitud ciudadana de transparencia, no un acto normativo"),

    # --- respuestas de atribuciones / competencia ---
    ("atribuciones", "OTRO_TEMA_MUNICIPAL",
     r"atribuciones_esenciales|potestades_competencias|potestades_y_competencias|"
     r"marco_normativo_atribuciones",
     "respuesta tipo sobre atribuciones/potestades municipales, sin normas urbanisticas"),

    # --- tramite: inicio de proceso, consulta, postergacion ---
    ("inicio_proceso", "TRAMITE_ADMINISTRATIVO",
     r"inicie?se_el_proceso|iniciese_el|inicio_del?_proceso|da[r]?_inicio|"
     r"dese_inicio|instruye_dar_inicio|inicio_de_la_tramitacion|inicio_al_procedimiento|"
     r"apruebase_el_inicio",
     "acto que solo da inicio a un proceso de PRC, sin normas"),
    ("consulta_publica", "TRAMITE_ADMINISTRATIVO",
     r"consulta_publica|participacion_ciudadana|audiencias?_publicas?|"
     r"exposicion_publica|exponer_al_publico|plebiscito|convocatoria_a_plesbicito|"
     r"convocatoria_a_plebiscito",
     "instancia de participacion/consulta publica, sin normas"),
    # ojo: hay "posterga_por", "posterga_selectivamente", "postergace" (sic) y
    # "postergacion". Un prefijo amplio los cubre todos; pedir sufijos concretos
    # se perdia 4 de 5.
    ("postergacion", "TRAMITE_ADMINISTRATIVO",
     r"posterg",
     "postergacion de permisos: acto temporal, sin normas urbanisticas"),
    ("deja_sin_efecto", "TRAMITE_ADMINISTRATIVO",
     r"deja(r|se)?_sin_efecto|dejese_sin_efecto|revoca(se)?_decreto",
     "deja sin efecto un acto previo, sin contenido normativo propio"),
    ("licitacion", "TRAMITE_ADMINISTRATIVO",
     r"adjudica(se|cion)?|llamado_a_licitacion|licitacion_publica|autoriza_compra|"
     r"insercion_(de_)?prensa|contrato_de_(estudio|consultoria)|"
     r"aprueba_bases|trato_directo|orden_de_compra|honorarios",
     "acto administrativo de contratacion/licitacion del estudio, sin normas"),
    ("cip", "OTRO_TEMA_MUNICIPAL",
     r"certificado_de_inform(e|acion)es_previas|certificado_de_informaciones",
     "certificado de informaciones previas: documento de un predio, no la ordenanza"),
    ("comision", "TRAMITE_ADMINISTRATIVO",
     r"crease_la_comision|crea(se)?_comision|designa_(a_la_)?comision|"
     r"cometido_funcionario|comision_de_servicio",
     "creacion/designacion de comision, sin normas"),

    # --- otros temas municipales ---
    ("otro_tema", "OTRO_TEMA_MUNICIPAL",
     r"derechos_munci?pales|derechos_municipales|medio_ambiente|medioambiental|"
     r"ordenanza_de_(aseo|ornato|ruidos|alcohol|mascotas|tenencia|ferias|comercio)|"
     r"becas?|subvencion|transito|estacionamientos_medidos|patentes|"
     r"gestion_hidrica|reglamento_interno|organigrama|presupuesto|"
     r"cuenta_publica|pladeco|plan_de_desarrollo_comunal",
     "materia municipal ajena al plan regulador"),

    # --- planos / laminas ---
    ("plano", "PLANO_LAMINA",
     r"(^|_)(lamina|plano)s?_(n_?\d|\d|regulador_.*\.(dwg|dxf))|"
     r"formato_dwg|archivo_dwg|(^|_)cartografia|imagen_objetivo",
     "parece un plano o lamina grafica, sin cuadro normativo"),
]

# Senales de valor en el nombre
PAT_VALOR = [
    ("ordenanza_local", "ORDENANZA_PRC",
     r"ordenanza_local|ordenanza_del?_plan_regulador|ordenanza_plan_regulador|"
     r"texto_refundido|ordenanza_municipal_del?_plan|plan_regulador_y_ordenanza|"
     r"ordenanza_prc"),
    ("aprueba_prc", "ORDENANZA_PRC",
     r"aprueba(se)?_(el_)?plan_regulador|aprueba(se)?_(el_)?plano_regulador|"
     r"aprueba(se)?_(el_)?nuevo_plan_regulador|apruebase_plan"),
    ("modificacion", "MODIFICACION_PRC",
     r"modificacion(es)?_(al?|del?)?_?plan[o]?_regulador|aprueba_modificacion|"
     r"promulga(se)?_(la_)?modificacion|modificacion_n_?\d|modificacion_prc|"
     r"promulga(se)?_modificacion|modifica_(el_)?plan_regulador"),
    ("enmienda", "ENMIENDA_PRC",
     r"enmienda"),
    ("seccional", "MODIFICACION_PRC",
     r"seccional"),
    ("intercomunal", "PRI_INTERCOMUNAL",
     r"intercomunal|metropolitano|premval|prmc|(^|_)pri(_|$)|(^|_)prm(_|$)|"
     r"plan_regulador_metropolitano"),
    ("promulga", "MODIFICACION_PRC",
     r"promulga(se)?"),
    ("prc_generico", None,
     r"plan[o]?_regulador"),
]

# Nombres opacos (8.3 truncado, hashes) -> el nombre no aporta nada
RE_NOMBRE_OPACO = re.compile(
    r"^([a-z0-9]{6}_\d|[0-9a-f]{16,}|[a-z0-9]{1,8}_?\d?)$"
)


def nombre_es_opaco(fam: str) -> bool:
    f = norm(fam)
    if RE_NOMBRE_OPACO.match(f):
        return True
    # hash hexadecimal puro
    if re.fullmatch(r"[0-9a-f]{20,}", f):
        return True
    # demasiado corto para significar algo
    if len(f) <= 8 and not re.search(r"[aeiou]{2}", f):
        return True
    return False


# --------------------------------------------------------------------------
# PASO 2 - senales normativas en el texto
# --------------------------------------------------------------------------
SENALES_TEXTO = {
    "constructibilidad": r"coeficiente\s+de\s+constructibilidad|constructibilidad",
    "ocupacion_suelo": r"coeficiente\s+de\s+ocupacion\s+de\s+suelo|ocupacion\s+de\s+suelo",
    "predial_minima": r"superficie\s+predial\s+minima|predial\s+minim",
    "altura_maxima": r"altura\s+maxima",
    "densidad": r"densidad\s+(bruta|maxima|neta|habitacional)",
    "agrupamiento": r"sistema\s+de\s+agrupamiento|aislad[oa]|pareado|continu[oa]",
    "antejardin": r"antejardin",
    "rasante": r"rasante",
    "adosamiento": r"adosamiento",
    "distanciamiento": r"distanciamiento",
    "normas_urbanisticas": r"normas?\s+urbanistic",
    "zonificacion": r"zonificacion|zonas?\s+de\s+edificacion",
    "usos_de_suelo": r"usos?\s+de\s+suelo|uso\s+permitido|usos\s+prohibidos",
    "ordenanza_local_txt": r"ordenanza\s+local",
    "articulado": r"articulo\s+\d|art\.\s*\d",
    "limite_urbano": r"limite\s+urbano",
}
RE_SENALES = {k: re.compile(v, re.I) for k, v in SENALES_TEXTO.items()}

# codigos de zona: ZC-1, ZH3, ZU-2, EC5, ICH, ZE-1, E-1...
RE_ZONAS = re.compile(
    r"\b(?:Z[A-Z]{0,3}\s?-?\s?\d{1,2}[A-Za-z]?|Z[A-Z]{1,3}|"
    r"E[CU]\s?-?\s?\d{1,2}|ICH|ZAV|ZUE)\b"
)

# senales de que es un tramite, vistas en el TEXTO
SENALES_TRAMITE = {
    "txt_solicitud": r"ley\s+de\s+transparencia|solicitud\s+de\s+acceso|"
                     r"20\.?285|derecho\s+de\s+acceso\s+a\s+la\s+informacion",
    "txt_postergacion": r"postergacion\s+de\s+(los\s+)?permisos|postergase",
    "txt_inicio": r"dese\s+inicio|iniciese\s+el\s+proceso",
    "txt_licitacion": r"adjudic|licitacion\s+publica|propuesta\s+publica",
}
RE_TRAMITE = {k: re.compile(v, re.I) for k, v in SENALES_TRAMITE.items()}


# --------------------------------------------------------------------------
# Utilidades de archivo
# --------------------------------------------------------------------------
def tipo_por_cabecera(p: Path) -> str:
    """Trampa 1: el tipo se decide por bytes, nunca por la extension."""
    try:
        with open(p, "rb") as fh:
            head = fh.read(1024)
    except OSError:
        return "NO_LEIBLE"
    if head.startswith(b"%PDF-"):
        return "PDF"
    bajo = head.lstrip().lower()
    if bajo.startswith(b"<!doctype html") or bajo.startswith(b"<html") or b"<html" in bajo[:200]:
        return "HTML"
    if head.startswith(b"PK\x03\x04"):
        return "ZIP"
    if head.startswith(b"\xd0\xcf\x11\xe0"):
        return "DOC_OLE"
    if head.startswith(b"Rar!"):
        return "RAR"
    if head[:2] in (b"\xff\xd8",) or head.startswith(b"\x89PNG"):
        return "IMAGEN"
    if head[:2] in (b"II", b"MM"):
        return "TIFF"
    return "DESCONOCIDO"


def extraer_texto(p: Path, ultima_pag: int) -> str:
    if not PDFTOTEXT.exists():
        raise FileNotFoundError(f"No existe pdftotext en {PDFTOTEXT}")
    try:
        r = subprocess.run(
            [str(PDFTOTEXT), "-f", "1", "-l", str(ultima_pag), "-enc", "UTF-8",
             str(p), "-"],
            capture_output=True, timeout=90,
        )
    except (subprocess.TimeoutExpired, OSError):
        return ""
    return r.stdout.decode("utf-8", errors="replace")


# --------------------------------------------------------------------------
# Clasificacion por reglas
# --------------------------------------------------------------------------
def reglas_nombre(familia: str, nombre: str) -> dict:
    base = norm(familia) + "_" + norm(nombre)
    hits_desc, hits_val = [], []
    for etiq, cat, rx, motivo in PAT_DESCARTE:
        if re.search(rx, base):
            hits_desc.append({"patron": etiq, "categoria": cat, "motivo": motivo})
    for etiq, cat, rx in PAT_VALOR:
        if re.search(rx, base):
            hits_val.append({"patron": etiq, "categoria": cat})
    return {"descarte": hits_desc, "valor": hits_val, "opaco": nombre_es_opaco(familia)}


def senales_de_texto(txt: str) -> dict:
    t = sin_tildes(txt)
    norm_hits = {k: len(rx.findall(t)) for k, rx in RE_SENALES.items()}
    norm_hits = {k: v for k, v in norm_hits.items() if v}
    zonas = RE_ZONAS.findall(txt)
    tram_hits = {k: len(rx.findall(t)) for k, rx in RE_TRAMITE.items()}
    tram_hits = {k: v for k, v in tram_hits.items() if v}
    # puntaje normativo: cuenta senales distintas, no repeticiones
    puntaje = len(norm_hits) + (2 if len(set(zonas)) >= 3 else 0)
    return {
        "senales_normativas": norm_hits,
        "senales_tramite": tram_hits,
        "codigos_zona": sorted(set(zonas))[:12],
        "puntaje_normativo": puntaje,
    }


def preclasificar(fila: dict, rn: dict, st: dict | None, tipo: str) -> dict:
    """Decision por reglas. Conservadora: ante la duda, ESCALAR."""
    ver = fila["veredicto"]
    cat, sirve, conf, metodo = None, None, None, "NOMBRE"
    motivos = []

    if tipo not in ("PDF",):
        return dict(categoria="INDETERMINADO", sirve="ESCALAR", confianza="BAJA",
                    motivo=f"el archivo no es un PDF real (cabecera={tipo}); requiere conversion",
                    metodo="BYTES")

    if ver in ("VACIO", "ILEGIBLE"):
        return dict(categoria="INDETERMINADO", sirve="ESCALAR", confianza="BAJA",
                    motivo=f"veredicto {ver}: PDF sin capa de texto ni imagen utilizable",
                    metodo="NOMBRE")

    desc = rn["descarte"]
    val = rn["valor"]
    val_cats = [v["categoria"] for v in val if v["categoria"]]
    val_pats = {v["patron"] for v in val}
    desc_pats = {d["patron"] for d in desc}

    # --- señal de valor fuerte gana casi siempre ---
    fuerte = val_pats & {"ordenanza_local", "aprueba_prc", "modificacion",
                         "enmienda", "intercomunal"}

    # 1) descarte claro y sin ninguna senal de valor
    if desc and not val:
        d = desc[0]
        return dict(categoria=d["categoria"], sirve="NO", confianza="ALTA",
                    motivo=d["motivo"], metodo="NOMBRE")

    # 2) descarte de solicitud ciudadana / atribuciones: gana aunque mencione el PRC
    #    (son literalmente preguntas sobre el plan regulador)
    if desc_pats & {"solicitud_ciudadana", "atribuciones", "cip"} and not fuerte:
        d = next(x for x in desc if x["patron"] in
                 {"solicitud_ciudadana", "atribuciones", "cip"})
        return dict(categoria=d["categoria"], sirve="NO", confianza="ALTA",
                    motivo=d["motivo"] + " (menciona el PRC solo como objeto de la consulta)",
                    metodo="NOMBRE")

    # 3) descarte de tramite con mencion generica al PRC
    if desc and not fuerte:
        d = desc[0]
        return dict(categoria=d["categoria"], sirve="NO", confianza="MEDIA",
                    motivo=d["motivo"], metodo="NOMBRE")

    # 4) valor fuerte
    if fuerte:
        if "intercomunal" in val_pats:
            cat = "PRI_INTERCOMUNAL"
        elif "enmienda" in val_pats:
            cat = "ENMIENDA_PRC"
        elif "ordenanza_local" in val_pats or "aprueba_prc" in val_pats:
            cat = "ORDENANZA_PRC"
        else:
            cat = "MODIFICACION_PRC"
        conf = "ALTA" if not desc else "MEDIA"
        motivo = f"el nombre declara {cat.lower().replace('_', ' ')}"
        if desc:
            motivo += f"; convive con patron de tramite '{desc[0]['patron']}' -> revisar"
        return dict(categoria=cat, sirve="SI", confianza=conf, motivo=motivo,
                    metodo="NOMBRE")

    # --- llegados aqui el nombre no decide: usar texto ---
    if st and st["puntaje_normativo"] >= 4:
        return dict(categoria="ORDENANZA_PRC", sirve="SI", confianza="MEDIA",
                    motivo=f"el texto trae {st['puntaje_normativo']} senales normativas "
                           f"({', '.join(list(st['senales_normativas'])[:4])})",
                    metodo="TEXTO")

    if st and st["puntaje_normativo"] >= 2 and "prc_generico" in val_pats:
        return dict(categoria="INDETERMINADO", sirve="ESCALAR", confianza="BAJA",
                    motivo="menciona el PRC y trae algunas senales normativas, "
                           "pero no basta para decidir",
                    metodo="TEXTO")

    return dict(categoria="INDETERMINADO", sirve="ESCALAR", confianza="BAJA",
                motivo="ni el nombre ni el texto de las primeras paginas permiten decidir",
                metodo="TEXTO" if st else "NOMBRE")


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--rehacer", action="store_true", help="ignora la cache")
    ap.add_argument("--solo-reglas", action="store_true",
                    help="recalcula reglas y preclasificacion sobre la cache, "
                         "sin volver a abrir los PDFs")
    ap.add_argument("--limite", type=int, default=0)
    args = ap.parse_args()

    if not PDFTOTEXT.exists() and not args.solo_reglas:
        print(f"ERROR: no encuentro pdftotext en {PDFTOTEXT}", file=sys.stderr)
        return 1

    filas = list(csv.DictReader(open(ENTRADA, encoding="utf-8")))
    if args.limite:
        filas = filas[: args.limite]

    cache: dict = {}
    if SALIDA_FEATURES.exists() and not args.rehacer:
        cache = json.loads(SALIDA_FEATURES.read_text(encoding="utf-8"))
        print(f"cache: {len(cache)} documentos ya procesados")

    # Recalcular reglas sobre la evidencia ya extraida (barato: no toca disco de PDFs).
    # Sirve para iterar los regex sin repetir los ~1.300 pdftotext.
    if args.solo_reglas:
        for clave, v in cache.items():
            fila = {"veredicto": v["veredicto"]}
            v["reglas_nombre"] = reglas_nombre(v["familia"], v["nombre"])
            v["pre"] = preclasificar(fila, v["reglas_nombre"], v.get("texto"),
                                     v["tipo_real"])
        SALIDA_FEATURES.write_text(
            json.dumps(cache, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"reglas recalculadas sobre {len(cache)} documentos")

    procesados = 0
    for i, fila in enumerate([] if args.solo_reglas else filas):
        clave = fila["ruta"]
        if clave in cache:
            continue

        p = RAIZ / fila["ruta"]
        tipo = tipo_por_cabecera(p) if p.exists() else "NO_EXISTE"

        rn = reglas_nombre(fila["familia"], fila["nombre"])

        st = None
        snippet = ""
        # Paso 2: solo tiene sentido si hay capa de texto (TEXTO o MIXTO).
        # En ESCANEADO igual lo intentamos: a veces trae encabezado de LeyChile
        # con el titulo del decreto, que ya es informacion util.
        if tipo == "PDF" and fila["veredicto"] in ("TEXTO", "MIXTO", "ESCANEADO"):
            txt = extraer_texto(p, PAGINAS_A_LEER)
            if txt.strip():
                st = senales_de_texto(txt)
                snippet = re.sub(r"\n{2,}", "\n", txt).strip()[:SNIPPET_CHARS]

        pre = preclasificar(fila, rn, st, tipo)

        cache[clave] = {
            "comuna": fila["comuna"],
            "familia": fila["familia"],
            "nombre": fila["nombre"],
            "ruta": fila["ruta"],
            "veredicto": fila["veredicto"],
            "paginas": int(fila["paginas"] or 0),
            "paginas_texto": int(fila["paginas_texto"] or 0),
            "paginas_escaneadas": int(fila["paginas_escaneadas"] or 0),
            "bytes": int(fila["bytes"] or 0),
            "tipo_real": tipo,
            "reglas_nombre": rn,
            "texto": st,
            "snippet": snippet,
            "pre": pre,
        }
        procesados += 1
        if procesados % GUARDAR_CADA == 0:
            SALIDA_FEATURES.write_text(
                json.dumps(cache, ensure_ascii=False, indent=1), encoding="utf-8")
            print(f"  {i+1}/{len(filas)} ...", flush=True)

    SALIDA_FEATURES.write_text(
        json.dumps(cache, ensure_ascii=False, indent=1), encoding="utf-8")

    # -------------------- resumen --------------------
    import collections
    c_cat = collections.Counter(v["pre"]["categoria"] for v in cache.values())
    c_sirve = collections.Counter(v["pre"]["sirve"] for v in cache.values())
    c_tipo = collections.Counter(v["tipo_real"] for v in cache.values())
    c_met = collections.Counter(v["pre"]["metodo"] for v in cache.values())

    print("\n=== PRECLASIFICACION POR REGLAS (Paso 1 + 2) ===")
    print(f"documentos: {len(cache)}")
    print("\ntipo real (por bytes de cabecera):")
    for k, v in c_tipo.most_common():
        print(f"  {k:<12} {v}")
    print("\ncategoria sugerida:")
    for k, v in c_cat.most_common():
        print(f"  {k:<24} {v}")
    print("\nsirve:")
    for k, v in c_sirve.most_common():
        print(f"  {k:<10} {v}")
    print("\nmetodo:")
    for k, v in c_met.most_common():
        print(f"  {k:<8} {v}")

    # que patrones de descarte disparan (verificacion, no asuncion)
    print("\npatrones de descarte que disparan:")
    cd = collections.Counter()
    for v in cache.values():
        for d in v["reglas_nombre"]["descarte"]:
            cd[d["patron"]] += 1
    for k, v in cd.most_common():
        print(f"  {k:<22} {v}")

    print("\npatrones de valor que disparan:")
    cv = collections.Counter()
    for v in cache.values():
        for d in v["reglas_nombre"]["valor"]:
            cv[d["patron"]] += 1
    for k, v in cv.most_common():
        print(f"  {k:<22} {v}")

    n_op = sum(1 for v in cache.values() if v["reglas_nombre"]["opaco"])
    print(f"\nnombres opacos (no dicen nada): {n_op}")
    print(f"\n-> {SALIDA_FEATURES.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
