#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bot de descarga de ordenanzas del Plan Regulador Comunal (PRC)
desde el Portal de Transparencia de Chile.

Para cada comuna de comunas.txt:

  1) Busca "Municipalidad de <comuna>" en el buscador del portal y entra a su
     ficha de organismo (?org=MU###).

  2) FUENTE A - Transparencia proactiva -> "Plan Regulador y sus Modificaciones":
     recorre sus subsecciones (Ordenanza, Memoria, Modificaciones, Planos...).
     Cada subseccion normalmente abre un PDF directo alojado en el sitio del
     municipio, o una tabla con enlaces a PDFs. Todo PDF que el navegador
     reciba (content-type application/pdf) se guarda automaticamente.

  3) FUENTE B - Seccion "01. Actos y documentos publicados en Diario Oficial":
     abre el panel, filtra por "plan regulador" y para cada resultado sigue el
     "Enlace" a BCN / LeyChile y descarga el PDF de la norma
     ("Descargar PDF de esta norma").

  4) FUENTE C - Seccion "07 -> Ordenanzas [-> Ordenanzas Vigentes]": igual que
     B pero en la tabla de ordenanzas vigentes de la comuna.

  5) FUENTE D - Buscador global del sitio (buscador-es?search_org=...): busca
     "plan regulador" en TODAS las secciones/subcarpetas del organismo (no
     depende de como cada municipio organice su seccion 07, que varia mucho:
     algunos la anidan por año/mes). Recorre los resultados en "rondas"
     (recarga + repagina desde cero cada vez, porque el orden de resultados
     con titulos casi idénticos no es estable) hasta agotar los relevantes.

Las Fuentes B, C y D filtran los titulos con `es_titulo_relevante()` para
descartar tramites administrativos que mencionan "plan regulador" de pasada
pero no son el texto de una ordenanza/modificacion (postergaciones de
permisos, evaluaciones ambientales, contratos de consultoria, licitaciones).

Los archivos se guardan en:  descargas/<comuna>/<fuente>/...
y se genera un indice CSV:    descargas/<comuna>/indice.csv

Uso:
    python descargar_prc.py                 # procesa comunas.txt (headless)
    python descargar_prc.py --headed        # con navegador visible
    python descargar_prc.py Peñalolén Colina # comunas por linea de comando
"""

import argparse
import csv
import hashlib
import re
import sys
import time
import unicodedata
from pathlib import Path
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

# --------------------------------------------------------------------------
# Configuracion
# --------------------------------------------------------------------------
BASE = "https://www.portaltransparencia.cl/PortalPdT"
BUSCADOR = f"{BASE}/buscador-directorio-de-organismos-regulados"
FILTRO = "plan regulador"          # palabra que se escribe en los filtros
SALIDA = Path(__file__).parent / "descargas"
REGISTRO = Path(__file__).parent / "registro_progreso.csv"
TIMEOUT = 60000                    # ms para esperas de Playwright
BATCH_SIZE_DEFECTO = 10            # comunas por lote

# Esperas base (ms). El portal es lento; damos margen generoso (min 3 s).
W_CORTA = 3000     # tras acciones simples
W_MEDIA = 4500     # tras abrir paneles / cargar tablas
W_LARGA = 6000     # tras filtros y navegaciones a sitios externos

# Etiqueta de la seccion proactiva y de la seccion Diario Oficial
LABEL_PROACTIVA = "Plan Regulador y sus Modificaciones"

# Titulos que mencionan "plan regulador" pero NO son el texto de una ordenanza
# o modificacion (son tramites administrativos/procedimentales): se descartan
# de los resultados de busqueda para no llenar la carpeta de ruido.
RECHAZAR_TITULO = re.compile(
    r"posterga\w*.{0,25}permiso|prorroga\w*.{0,25}permiso"      # postergacion/prorroga de permisos
    r"|evaluaci[oó]n ambiental"                                  # EAE, procedimiento, no el texto
    r"|\bcontrato\b|convenio"                                    # contratos de consultoria, etc.
    r"|licitaci[oó]n|concurso p[uú]blico|adjudicaci[oó]n"        # compras publicas
    r"|capacitaci[oó]n"
    r"|certificad\w*.{0,10}informe?s?\s+previ"                   # certificado de informes previos
    r"|certificad\w*.{0,10}informaci[oó]n\w*\s+previ",          # certificado de informaciones previas
    re.I,
)


def es_titulo_relevante(titulo: str) -> bool:
    return not RECHAZAR_TITULO.search(titulo or "")


# --------------------------------------------------------------------------
# Utilidades
# --------------------------------------------------------------------------
def slug(texto: str) -> str:
    """Convierte un texto a un nombre de archivo/carpeta seguro."""
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    t = re.sub(r"[^\w\s-]", "", t).strip().lower()
    t = re.sub(r"[-\s]+", "_", t)
    return t[:120] or "sin_nombre"


def log(msg: str) -> None:
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


# --------------------------------------------------------------------------
# Registro de avance (para lotes resumibles: registro_progreso.csv)
# --------------------------------------------------------------------------
CAMPOS_REGISTRO = ["slug", "comuna", "estado", "pdfs", "fecha_hora"]


def cargar_registro() -> dict:
    """Lee registro_progreso.csv -> {slug_comuna: fila}. Si no existe, {}."""
    if not REGISTRO.exists():
        return {}
    with REGISTRO.open("r", newline="", encoding="utf-8") as f:
        return {row["slug"]: row for row in csv.DictReader(f)}


def guardar_registro(reg: dict) -> None:
    """Reescribe registro_progreso.csv completo (son a lo sumo unos cientos
    de filas, así que reescribir siempre es simple y evita corrupcion)."""
    with REGISTRO.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS_REGISTRO)
        w.writeheader()
        for row in reg.values():
            w.writerow(row)


def marcar_comuna(reg: dict, comuna: str, estado: str, pdfs: int) -> None:
    """Actualiza el estado de una comuna en el registro y lo persiste
    de inmediato (asi Ctrl+C o un cierre a mitad de lote no pierde avance)."""
    s = slug(comuna)
    reg[s] = {
        "slug": s,
        "comuna": comuna,
        "estado": estado,
        "pdfs": pdfs,
        "fecha_hora": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    guardar_registro(reg)


MIN_BYTES = 1500  # descarta respuestas casi vacias (redirecciones, errores)


class Descargador:
    """Guarda todo PDF que reciba el navegador, ya sea como respuesta inline
    (content-type application/pdf) o como descarga (event 'download').
    Deduplica por contenido (hash md5).
    """

    def __init__(self):
        self.carpeta_actual: Path | None = None
        self.prefijo = ""
        self.hashes: set[str] = set()
        self.registro: list[dict] = []
        self.pendientes: list[tuple] = []   # (url, carpeta, prefijo) por descargar
        self.urls_ok: set[str] = set()       # urls ya descargadas

    def destino(self, carpeta: Path, prefijo: str = "") -> None:
        self.carpeta_actual = carpeta
        self.prefijo = prefijo

    # -- guardado comun ---------------------------------------------------
    def _guardar(self, body: bytes, url: str, sugerido: str = "") -> None:
        if self.carpeta_actual is None or not body or len(body) < MIN_BYTES:
            return
        h = hashlib.md5(body).hexdigest()
        if h in self.hashes:
            return
        self.hashes.add(h)

        base = sugerido or Path(urlparse(url).path).name or "documento"
        if not base.lower().endswith(".pdf"):
            base += ".pdf"
        nombre = f"{self.prefijo}{base}" if self.prefijo else base
        self.carpeta_actual.mkdir(parents=True, exist_ok=True)
        destino = self.carpeta_actual / nombre
        i = 1
        while destino.exists():
            destino = self.carpeta_actual / f"{destino.stem}_{i}{destino.suffix}"
            i += 1
        destino.write_bytes(body)
        kb = len(body) // 1024
        log(f"    PDF guardado: {destino.name} ({kb} KB)")
        self.registro.append({"archivo": str(destino), "url": url, "kb": kb})

    # -- handlers ---------------------------------------------------------
    def manejar_respuesta(self, response) -> None:
        # No se usa response.body() porque falla para los PDF que el navegador
        # entrega a su visor interno. Solo encolamos la URL para descargarla
        # despues con context.request.get() (comparte cookies de sesion).
        try:
            ct = (response.headers or {}).get("content-type", "")
            url = response.url
            if "application/pdf" in ct.lower() and url.startswith("http"):
                self.pendientes.append((url, self.carpeta_actual, self.prefijo))
        except Exception:
            pass

    def manejar_descarga(self, download) -> None:
        try:
            tmp = Path(download.path()) if download.path() else None
            if tmp is None:
                return
            body = tmp.read_bytes()
        except Exception:
            return
        self._guardar(body, download.url, sugerido=download.suggested_filename)

    def flush(self, context) -> None:
        """Descarga (via request API con cookies) las URLs PDF encoladas."""
        pend, self.pendientes = self.pendientes, []
        for url, carpeta, prefijo in pend:
            if url in self.urls_ok or carpeta is None:
                continue
            self.urls_ok.add(url)
            try:
                r = context.request.get(url, timeout=TIMEOUT)
                if not r.ok:
                    continue
                body = r.body()
            except Exception:
                continue
            self.carpeta_actual, self.prefijo = carpeta, prefijo
            self._guardar(body, url)

    def enganchar(self, page) -> None:
        """Conecta los handlers de respuesta y descarga a una pagina."""
        page.on("response", self.manejar_respuesta)
        page.on("download", self.manejar_descarga)


# --------------------------------------------------------------------------
# Pasos de navegacion en el portal (SPA con enlaces href="#")
# --------------------------------------------------------------------------
def buscar_organismo(page, comuna: str) -> str | None:
    """Busca la comuna y devuelve la URL de su ficha (?org=MU###).

    El buscador es un autocompletado PrimeFaces por AJAX: hay que escribir con
    eventos de teclado reales (press_sequentially) para que dispare la consulta.
    Se prefiere la coincidencia EXACTA "Municipalidad de <comuna>".
    """
    page.goto(BUSCADOR, wait_until="networkidle")
    caja = page.locator("input[type=search], input[placeholder*='organismo']").first
    caja.wait_for(state="visible", timeout=TIMEOUT)
    caja.click()
    caja.fill("")
    caja.press_sequentially(f"Municipalidad de {comuna}", delay=120)

    objetivo = f"Municipalidad de {comuna}"
    # Espera a que aparezca la sugerencia exacta y hace clic
    opcion = page.get_by_text(objetivo, exact=True).first
    try:
        opcion.wait_for(state="visible", timeout=15000)
    except PWTimeout:
        # Reintento: a veces el AJAX tarda; forzamos un caracter mas
        caja.press(" ")
        caja.press("Backspace")
        try:
            opcion.wait_for(state="visible", timeout=15000)
        except PWTimeout:
            return None
    opcion.click()
    try:
        page.wait_for_url("**/*org=*", timeout=TIMEOUT)
    except PWTimeout:
        return None
    page.wait_for_load_state("domcontentloaded")
    return page.url


def clic_por_texto(page, patron: str, exacto: bool = False, espera_ms: int = 8000):
    """Hace clic (via JS) en el primer <a> cuyo texto matchea, esperando hasta
    'espera_ms' a que el elemento aparezca (los paneles cargan por AJAX)."""
    intentos = max(1, espera_ms // 300)
    for _ in range(intentos):
        ok = page.evaluate(
            """([patron, exacto]) => {
                const re = new RegExp(patron, 'i');
                const a = Array.from(document.querySelectorAll('a')).find(x => {
                    const t = (x.textContent || '').trim();
                    return exacto ? t.toLowerCase() === patron.toLowerCase() : re.test(t);
                });
                if (a) { a.click(); return true; }
                return false;
            }""",
            [patron, exacto],
        )
        if ok:
            return True
        page.wait_for_timeout(300)
    return False


def esperar_panel(page, timeout=15000) -> bool:
    """Espera a que aparezca un panel de resultados (breadcrumb o tabla)."""
    try:
        page.wait_for_function(
            """() => /mostrando \\d+ de \\d+ resultados/.test(document.body.innerText)
                     || document.querySelector('table tbody tr td')""",
            timeout=timeout,
        )
        return True
    except PWTimeout:
        return False


# --------------------------------------------------------------------------
# FUENTE A: Transparencia proactiva -> Plan Regulador y sus Modificaciones
# --------------------------------------------------------------------------
def procesar_proactiva(page, context, dl: Descargador, carpeta: Path, org_url: str) -> None:
    log("  FUENTE A: Transparencia proactiva -> Plan Regulador")
    page.goto(org_url, wait_until="domcontentloaded")
    page.wait_for_timeout(W_MEDIA)

    # Caso 1: submenu interno "Plan Regulador y sus Modificaciones" (abre PDFs
    # alojados en el propio portal/municipio). Caso 2: enlace externo simple
    # "Plan Regulador" (target=_blank a un sitio del municipio).
    tiene_submenu = clic_por_texto(page, re.escape(LABEL_PROACTIVA), espera_ms=5000)
    if not tiene_submenu:
        log("    (sin submenu interno; probando enlace externo 'Plan Regulador')")
        _proactiva_externa(page, context, dl, carpeta, org_url)
        return
    page.wait_for_timeout(W_MEDIA)

    # Lista de subsecciones dentro del panel proactivo
    subsecciones = page.evaluate(
        """() => Array.from(document.querySelectorAll('a'))
                 .map(a => (a.textContent||'').trim())
                 .filter(t => /plan regulador|memoria|modificaci|plano|ordenanza/i.test(t)
                              && t.length < 80
                              && !/proactiva:/i.test(t))""",
    )
    # dedup preservando orden
    vistas, subs = set(), []
    for s in subsecciones:
        if s.lower() not in vistas:
            vistas.add(s.lower())
            subs.append(s)
    log(f"    subsecciones: {subs}")

    for sub in subs:
        carpeta_sub = carpeta / "proactiva" / slug(sub)
        dl.destino(carpeta_sub, prefijo="")
        # Reabrir proactiva desde cero para tener estado limpio
        page.goto(org_url, wait_until="domcontentloaded")
        page.wait_for_timeout(W_MEDIA)
        if not clic_por_texto(page, re.escape(LABEL_PROACTIVA)):
            continue
        page.wait_for_timeout(W_MEDIA)
        log(f"    -> {sub}")
        if not clic_por_texto(page, sub, exacto=True):
            continue
        page.wait_for_timeout(W_LARGA)  # da tiempo a PDF directo o carga de tabla

        # Si abrio una tabla con enlaces, seguir cada enlace/boton de descarga
        try:
            filas = page.evaluate(
                """() => Array.from(document.querySelectorAll('table tbody tr'))
                         .map(tr => { const a = tr.querySelector('a[href]');
                                      return a ? a.getAttribute('href') : null; })
                         .filter(Boolean).length""",
            )
        except Exception:
            filas = 0
        if filas:
            _descargar_enlaces_tabla(page, dl)
            page.wait_for_timeout(W_MEDIA)

        dl.flush(context)
        _cerrar_popups(context, page)


def _proactiva_externa(page, context, dl: Descargador, carpeta: Path, org_url: str) -> None:
    """Abre el enlace externo 'Plan Regulador' (sitio del municipio) y recorre
    sus sub-paginas .html descargando los .pdf de TEXTO (se omiten los que
    contienen 'Lamina', que son planos). BFS acotado sobre el mismo directorio.
    """
    destino = carpeta / "proactiva_externa"
    dl.destino(destino, prefijo="")
    href = page.evaluate(
        """() => {
            const a = Array.from(document.querySelectorAll('a'))
                .find(x => /^plan regulador\\b/i.test((x.textContent||'').trim())
                           && x.getAttribute('href') && x.getAttribute('href') !== '#');
            return a ? a.href : null;
        }"""
    )
    if not href:
        log("    (no hay enlace 'Plan Regulador' en proactiva)")
        return
    log(f"    enlace externo: {href}")

    ext = context.new_page()
    visitadas: set[str] = set()
    cola = [href]
    pdfs_total = 0
    try:
        while cola and len(visitadas) < 15:
            url = cola.pop(0)
            if url in visitadas:
                continue
            visitadas.add(url)
            try:
                ext.goto(url, wait_until="domcontentloaded", timeout=TIMEOUT)
            except Exception:
                pass  # si la url era un PDF directo, el handler ya lo capto
            ext.wait_for_timeout(W_CORTA)
            dl.flush(context)

            # Enlaces de la pagina: separar PDFs (texto) de sub-paginas .html
            try:
                data = ext.evaluate(
                    """() => Array.from(document.querySelectorAll('a[href]'))
                         .map(a => ({href: a.href, txt: (a.textContent||'').trim()}))"""
                )
            except Exception:
                data = []
            # Directorio actual sin esquema (el sitio redirige http->https, por
            # eso comparamos host+directorio ignorando el protocolo).
            def dir_sin_esquema(u):
                pu = urlparse(u)
                return pu.netloc + pu.path.rsplit("/", 1)[0]
            base_dir = dir_sin_esquema(ext.url or url)
            for it in data:
                u, txt = it["href"], it["txt"]
                if re.search(r"lamina", txt, re.I):
                    continue  # planos: se omiten
                if re.search(r"\.pdf(\?|$)", u, re.I):
                    dl.pendientes.append((u, destino, ""))
                    pdfs_total += 1
                elif (u.lower().split("?")[0].endswith(".html")
                      and dir_sin_esquema(u) == base_dir
                      and u not in visitadas and u not in cola
                      and re.search(r"plan|regulador|modific|ordenanza", u + txt, re.I)):
                    cola.append(u)
            dl.flush(context)
        log(f"    PDFs de texto encolados desde el sitio externo: {pdfs_total}")
    finally:
        try:
            ext.close()
        except Exception:
            pass
    _cerrar_popups(context, page)


def _cerrar_popups(context, principal) -> None:
    """Cierra pestañas emergentes (visores de PDF) dejando solo la principal."""
    for p in list(context.pages):
        if p is not principal:
            try:
                p.close()
            except Exception:
                pass


def _descargar_enlaces_tabla(page, dl: Descargador) -> None:
    """Hace clic en cada enlace de una tabla; los PDF los captura el handler."""
    n = page.evaluate(
        "() => document.querySelectorAll('table tbody tr a[href]').length"
    )
    for i in range(n):
        try:
            page.evaluate(
                """(i) => {
                    const a = document.querySelectorAll('table tbody tr a[href]')[i];
                    if (a) a.click();
                }""",
                i,
            )
            page.wait_for_timeout(W_CORTA)
        except Exception:
            continue


# --------------------------------------------------------------------------
# Helper: filtrar una tabla de resultados y descargar cada "Enlace"
# --------------------------------------------------------------------------
def _filtrar_y_descargar(page, context, dl: Descargador, carpeta_dest: Path,
                         col_num: int = 3, col_denom: int = 4) -> int:
    """Asume que hay una tabla con caja de filtro visible. Filtra por FILTRO y
    descarga el PDF de cada fila (via su columna 'Enlace'). Devuelve cuantas
    filas con enlace encontro. Los indices de columna varian entre tablas.
    """
    if not esperar_panel(page):
        log("    (el panel no cargo)")
        return 0
    page.evaluate(
        """(f) => {
            const inp = document.querySelector('input[type=text]');
            const btns = Array.from(document.querySelectorAll('button, input[type=submit]'));
            const filtrar = btns.find(b => /filtrar/i.test(b.textContent || b.value || ''));
            if (inp) { inp.value = f;
                       inp.dispatchEvent(new Event('input', {bubbles:true})); }
            if (filtrar) filtrar.click();
        }""",
        FILTRO,
    )
    page.wait_for_timeout(W_LARGA)

    resultados = page.evaluate(
        """([cn, cd]) => Array.from(document.querySelectorAll('table tbody tr'))
             .map(tr => {
                 const tds = Array.from(tr.querySelectorAll('td')).map(td => td.innerText.trim());
                 const a = tr.querySelector('a[href]');
                 // La denominacion suele ser la celda mas larga; usamos el
                 // indice sugerido pero caemos a la celda mas larga si falta.
                 let denom = tds[cd] || '';
                 // Si la celda elegida es vacia o muy corta (ej. "Ordenanza
                 // Municipal"), usamos la celda de texto mas larga (la breve
                 // descripcion del acto), que describe mejor el documento.
                 if (denom.length < 15)
                     denom = tds.slice().sort((x,y)=>y.length-x.length)[0] || denom;
                 return { num: tds[cn]||'', denom: denom,
                          href: a ? a.href : null };
             })
             .filter(r => r.href);""",
        [col_num, col_denom],
    )
    total = len(resultados)
    resultados = [r for r in resultados if es_titulo_relevante(r["denom"])]
    log(f"    {total} resultado(s) con enlace, {len(resultados)} relevante(s) "
        f"tras descartar tramites administrativos (permisos, EAE, contratos, etc.)")

    for r in resultados:
        nombre = slug(f"{r['num']}_{r['denom']}")[:80]
        dl.destino(carpeta_dest, prefijo=f"{nombre}__")
        _descargar_pdf_bcn(context, dl, carpeta_dest, nombre, r["href"])
        dl.flush(context)
        _cerrar_popups(context, page)
    return len(resultados)


# --------------------------------------------------------------------------
# FUENTE B: Seccion 01 Diario Oficial -> BCN / LeyChile
# --------------------------------------------------------------------------
def procesar_diario_oficial(page, context, dl: Descargador,
                            carpeta: Path, org_url: str) -> None:
    log("  FUENTE B: 01. Diario Oficial (filtro 'plan regulador')")
    page.goto(org_url, wait_until="domcontentloaded")
    page.wait_for_timeout(W_MEDIA)
    # La etiqueta del enlace varia por comuna: "...publicados en el Diario
    # Oficial" (Peñalolen) / "...objeto de publicacion en el Diario Oficial"
    # (Colina). Matcheamos el enlace de documentos que menciona Diario Oficial.
    if not clic_por_texto(page, "documentos.*Diario Oficial"):
        log("    (no se encontro la seccion Diario Oficial)")
        return
    _filtrar_y_descargar(page, context, dl, carpeta / "diario_oficial",
                         col_num=3, col_denom=4)


# --------------------------------------------------------------------------
# FUENTE C: Seccion 07 -> Ordenanzas [-> Ordenanzas Vigentes]
# --------------------------------------------------------------------------
def procesar_ordenanzas_vigentes(page, context, dl: Descargador,
                                 carpeta: Path, org_url: str) -> None:
    log("  FUENTE C: 07. Ordenanzas [Vigentes] (filtro 'plan regulador')")
    page.goto(org_url, wait_until="domcontentloaded")
    page.wait_for_timeout(W_MEDIA)
    # Abrir seccion 07
    if not clic_por_texto(page, "resoluciones con efectos sobre terceros"):
        log("    (no se encontro la seccion 07)")
        return
    page.wait_for_timeout(W_MEDIA)
    # Click en 'Ordenanzas' / 'Ordenanzas Municipales'
    if not clic_por_texto(page, r"^Ordenanzas( Municipales)?$"):
        log("    (no se encontro 'Ordenanzas' en seccion 07)")
        return
    page.wait_for_timeout(W_MEDIA)
    # Si aparece el submenu 'Ordenanzas Vigentes', entrar en el
    if clic_por_texto(page, r"^Ordenanzas Vigentes$", espera_ms=4000):
        page.wait_for_timeout(W_MEDIA)
    _filtrar_y_descargar(page, context, dl, carpeta / "ordenanzas_vigentes",
                         col_num=3, col_denom=2)


# --------------------------------------------------------------------------
# FUENTE D: Buscador global del sitio (cruza TODAS las secciones/subcarpetas)
# --------------------------------------------------------------------------
# Esta busqueda de texto completo del portal no depende de como cada
# municipio organice su seccion 07 (algunos la anidan por año/mes, otros la
# dejan plana). Por eso encuentra documentos que las Fuentes B/C no alcanzan
# a navegar. A cambio, mezcla resultados de secciones no relacionadas (multas,
# permisos, contratos) que hay que filtrar por titulo.
MAX_PAGINAS_BUSQUEDA = 8   # tope de paginas de resultados a recorrer
MAX_DOCUMENTOS_BUSQUEDA = 40  # tope de documentos relevantes a descargar


def _extraer_org_code(org_url: str) -> str | None:
    m = re.search(r"org=([^&]+)", org_url)
    return m.group(1) if m else None


def _leer_tarjetas_busqueda(page) -> list:
    """Lee las tarjetas de resultados visibles en la pagina actual del
    buscador global: [{denom, seccion}, ...]."""
    return page.evaluate(
        """() => Array.from(document.querySelectorAll('.search-results__entry'))
             .map(entry => {
                 const em = entry.querySelector('em');
                 const heads = Array.from(entry.querySelectorAll('h3, h4, strong, b'))
                     .map(h => h.textContent.trim()).join(' ');
                 return { denom: em ? em.textContent.trim() : '',
                          seccion: heads || entry.textContent.trim().slice(0, 80) };
             })
             .filter(c => c.denom);"""
    )


def _siguiente_pagina_busqueda(page) -> bool:
    """Clic en '»' (pagina siguiente) del paginador de resultados. Devuelve
    False si no hay mas paginas."""
    return page.evaluate(
        """() => {
            const links = Array.from(document.querySelectorAll('a.page-link'));
            const next = links.find(a => a.textContent.trim() === '»');
            if (!next || next.closest('.ui-state-disabled')) return false;
            next.click();
            return true;
        }"""
    )


def _click_tarjeta_y_extraer(page, denom: str) -> list:
    """Hace clic en la tarjeta cuyo titulo es exactamente `denom` (debe estar
    visible en la pagina actual) y devuelve los href de sus columnas 'Enlace'.
    Lista vacia si no se pudo hacer clic."""
    clic_ok = page.evaluate(
        """(denom) => {
            const entries = Array.from(document.querySelectorAll('.search-results__entry'));
            const entry = entries.find(e => {
                const em = e.querySelector('em');
                return em && em.textContent.trim() === denom;
            });
            if (!entry) return false;
            let n = entry;
            while (n && n.tagName !== 'A') n = n.parentElement;
            if (!n) return false;
            n.click();
            return true;
        }""",
        denom,
    )
    if not clic_ok:
        return []
    page.wait_for_timeout(W_MEDIA)
    return page.evaluate(
        """() => {
            const ths = Array.from(document.querySelectorAll('table th'));
            const idxs = ths.map((th, i) => /enlace/i.test(th.textContent) ? i : -1)
                            .filter(i => i >= 0);
            const out = [];
            document.querySelectorAll('table tbody tr').forEach(tr => {
                const tds = tr.querySelectorAll('td');
                idxs.forEach(i => {
                    const a = tds[i] && tds[i].querySelector('a[href]');
                    if (a) out.push(a.href);
                });
            });
            return out;
        }"""
    )


def procesar_busqueda_global(page, context, dl: Descargador,
                             carpeta: Path, org_url: str) -> None:
    """Busca 'plan regulador' en el buscador global del sitio (cruza todas
    las secciones/subcarpetas del organismo) y descarga los documentos
    relevantes.

    El orden de resultados no es 100% estable entre cargas (títulos casi
    idénticos, p.ej. varios "Decreto Exento N Actualización Plan Regulador
    Comunal", empatan en relevancia), así que NO confiamos en "ir a la
    página N" para reubicar una tarjeta ya vista. En su lugar, cada ronda
    recarga la búsqueda desde cero y recorre páginas hasta encontrar la
    PRIMERA tarjeta relevante que aún no se haya procesado (por título);
    la descarga y vuelve a empezar. Termina cuando una ronda completa no
    encuentra nada nuevo.
    """
    log("  FUENTE D: busqueda global del sitio (filtro 'plan regulador')")
    org_code = _extraer_org_code(org_url)
    if not org_code:
        log("    (no se pudo determinar el codigo de organismo)")
        return
    url_busqueda = f"{BASE}/buscador-es?search_org={org_code}&search_usr={FILTRO.replace(' ', '+')}"

    destino = carpeta / "busqueda_global"
    dl.destino(destino, prefijo="")
    procesados: set[str] = set()
    descargados = 0

    for ronda in range(1, MAX_DOCUMENTOS_BUSQUEDA + 6):
        page.goto(url_busqueda, wait_until="domcontentloaded")
        page.wait_for_timeout(W_LARGA if ronda == 1 else W_MEDIA)
        objetivo = None
        for pagina in range(1, MAX_PAGINAS_BUSQUEDA + 1):
            tarjetas = _leer_tarjetas_busqueda(page)
            if not tarjetas and pagina > 1:
                break
            nuevas = [t["denom"] for t in tarjetas if t["denom"] not in procesados]
            objetivo = next((d for d in nuevas if es_titulo_relevante(d)), None)
            # las no relevantes de esta pagina no se volveran a evaluar
            for d in nuevas:
                if not es_titulo_relevante(d):
                    procesados.add(d)
            if objetivo:
                break
            if not _siguiente_pagina_busqueda(page):
                break
            page.wait_for_timeout(W_MEDIA)

        if not objetivo:
            break  # una ronda completa sin nada nuevo relevante -> terminado

        procesados.add(objetivo)
        hrefs = _click_tarjeta_y_extraer(page, objetivo)
        if not hrefs:
            log(f"    (sin enlace descargable: {objetivo[:60]})")
            continue
        nombre = slug(objetivo)[:80]
        for h in hrefs:
            dl.pendientes.append((h, destino, f"{nombre}__"))
        dl.flush(context)
        _cerrar_popups(context, page)
        descargados += 1
        if descargados >= MAX_DOCUMENTOS_BUSQUEDA:
            log(f"    limite de {MAX_DOCUMENTOS_BUSQUEDA} documentos alcanzado")
            break

    log(f"    {len(procesados)} titulo(s) distinto(s) vistos en el buscador, "
        f"{descargados} documento(s) relevante(s) descargado(s)")


def _descargar_pdf_bcn(context, dl: Descargador, carpeta: Path,
                       nombre: str, href: str) -> None:
    """Abre la norma en BCN/LeyChile, obtiene el href del boton 'Descargar PDF
    de esta norma' y lo descarga via context.request.get() (comparte cookies).
    Si el enlace del portal ya ERA un PDF directo, el handler de respuesta lo
    captura al navegar.
    """
    p = context.new_page()  # queda enganchada por context.on('page')
    try:
        try:
            p.goto(href, wait_until="domcontentloaded", timeout=TIMEOUT)
        except Exception:
            pass  # si el enlace es descarga directa, el handler ya lo capto
        p.wait_for_timeout(W_CORTA)
        dl.flush(context)  # captura PDF directo (avisos alojados en el portal)

        # href real del boton de descarga PDF en la ficha BCN/LeyChile
        pdf_href = p.evaluate(
            """() => {
                const a = Array.from(document.querySelectorAll('a'))
                    .find(x => /Descargar PDF de esta norma/i.test(x.title||'')
                               || /descargar pdf/i.test(x.textContent||''));
                return a ? a.href : null;
            }"""
        )
        if pdf_href:
            dl.pendientes.append((pdf_href, carpeta, f"{nombre}__"))
            dl.flush(context)
        else:
            log(f"      (sin boton PDF BCN en {href})")
    except Exception as e:
        log(f"      error en {href}: {e}")
    finally:
        try:
            p.close()
        except Exception:
            pass


# --------------------------------------------------------------------------
# Orquestacion
# --------------------------------------------------------------------------
def procesar_comuna(context, comuna: str) -> int:
    """Procesa una comuna y devuelve la cantidad de PDFs descargados."""
    log(f"=== COMUNA: {comuna} ===")
    carpeta = SALIDA / slug(comuna)
    carpeta.mkdir(parents=True, exist_ok=True)

    # Descargador nuevo por comuna; se publica en el contexto para que el
    # wiring de paginas nuevas (context.on 'page') use el actual.
    dl = Descargador()
    context._dl = dl
    page = context.new_page()  # dispara context.on('page') -> engancha dl

    org_url = buscar_organismo(page, comuna)
    if not org_url:
        log(f"  !! No se encontro la Municipalidad de {comuna}")
        page.close()
        return 0
    log(f"  ficha: {org_url}")

    try:
        procesar_proactiva(page, context, dl, carpeta, org_url)
    except Exception as e:
        log(f"  error en proactiva: {e}")
    try:
        procesar_diario_oficial(page, context, dl, carpeta, org_url)
    except Exception as e:
        log(f"  error en diario oficial: {e}")
    try:
        procesar_ordenanzas_vigentes(page, context, dl, carpeta, org_url)
    except Exception as e:
        log(f"  error en ordenanzas vigentes: {e}")
    try:
        procesar_busqueda_global(page, context, dl, carpeta, org_url)
    except Exception as e:
        log(f"  error en busqueda global: {e}")

    page.close()

    # Indice CSV por comuna
    if dl.registro:
        with (carpeta / "indice.csv").open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["archivo", "url", "kb"])
            w.writeheader()
            w.writerows(dl.registro)
    log(f"  total PDFs guardados: {len(dl.registro)}")
    return len(dl.registro)


def _nuevo_browser(pw, headed: bool):
    """Crea browser+context nuevos (se recicla por lote para evitar que el
    navegador acumule memoria en corridas largas de muchas horas)."""
    browser = pw.chromium.launch(headless=not headed)
    context = browser.new_context(
        accept_downloads=True,
        locale="es-CL",
        viewport={"width": 1440, "height": 900},
        user_agent=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/124.0.0.0 Safari/537.36"),
    )
    context.set_default_timeout(TIMEOUT)
    context._dl = None
    # Toda pagina nueva (incluidas pestañas emergentes y PDFs) queda
    # enganchada al Descargador vigente de la comuna en curso.
    context.on("page", lambda p: context._dl and context._dl.enganchar(p))
    return browser, context


def main() -> int:
    ap = argparse.ArgumentParser(description="Descarga ordenanzas de PRC del Portal de Transparencia")
    ap.add_argument("comunas", nargs="*", help="Nombres de comuna (si se omite, usa --lista)")
    ap.add_argument("--headed", action="store_true", help="Mostrar el navegador")
    ap.add_argument("--lista", default="comunas.txt", help="Archivo con comunas (una por linea)")
    ap.add_argument("--batch-size", type=int, default=BATCH_SIZE_DEFECTO,
                     help=f"Comunas por lote (defecto {BATCH_SIZE_DEFECTO})")
    ap.add_argument("--lotes", type=int, default=None,
                     help="Cuantos lotes procesar en esta corrida (defecto: todos los pendientes)")
    ap.add_argument("--registro", default=None,
                     help="Archivo CSV de avance a usar (defecto registro_progreso.csv). "
                          "Para correr varios bots en paralelo, dale a cada uno el suyo.")
    args = ap.parse_args()

    # Permite que cada bot en paralelo lleve su propio registro de avance.
    if args.registro:
        global REGISTRO
        REGISTRO = Path(__file__).parent / args.registro

    if args.comunas:
        comunas = args.comunas
    else:
        ruta = Path(__file__).parent / args.lista
        if not ruta.exists():
            log(f"No existe {ruta}. Crea comunas.txt o pasa comunas por linea de comando.")
            return 1
        comunas = [l.strip() for l in ruta.read_text(encoding="utf-8").splitlines()
                   if l.strip() and not l.strip().startswith("#")]

    if not comunas:
        log("No hay comunas para procesar.")
        return 1

    SALIDA.mkdir(exist_ok=True)

    # -- registro de avance: filtra las que ya estan 'hecho' -----------------
    registro = cargar_registro()
    ya_hechas = {s for s, row in registro.items() if row.get("estado") == "hecho"}
    pendientes = [c for c in comunas if slug(c) not in ya_hechas]
    log(f"Total comunas en lista: {len(comunas)} | ya hechas (registro): {len(ya_hechas)} "
        f"| pendientes: {len(pendientes)}")

    if not pendientes:
        log("No quedan comunas pendientes segun el registro. Nada que hacer.")
        return 0

    batch_size = max(1, args.batch_size)
    max_lotes = args.lotes if args.lotes and args.lotes > 0 else None
    lote_num = 0

    with sync_playwright() as pw:
        while pendientes:
            if max_lotes is not None and lote_num >= max_lotes:
                log(f"Limite de {max_lotes} lote(s) alcanzado en esta corrida. "
                    f"Quedan {len(pendientes)} comuna(s) pendiente(s); vuelve a "
                    f"ejecutar para continuar (se salta lo ya hecho segun el registro).")
                break

            lote_num += 1
            chunk, pendientes = pendientes[:batch_size], pendientes[batch_size:]
            log(f"########## LOTE {lote_num}: {len(chunk)} comuna(s) "
                f"({len(chunk) + len(pendientes)} restantes contando este lote) ##########")

            browser, context = _nuevo_browser(pw, args.headed)
            for comuna in chunk:
                try:
                    n = procesar_comuna(context, comuna)
                    marcar_comuna(registro, comuna, "hecho", n)
                except Exception as e:
                    log(f"!! Error procesando {comuna}: {e}")
                    marcar_comuna(registro, comuna, "error", 0)
            browser.close()

            hechas_total = sum(1 for r in registro.values() if r.get("estado") == "hecho")
            log(f"Fin de lote {lote_num}. Hechas hasta ahora: {hechas_total}/{len(comunas)}. "
                f"Pendientes: {len(pendientes)}.")

    if pendientes:
        log(f"Corrida terminada con {len(pendientes)} comuna(s) aun pendiente(s). "
            f"Vuelve a ejecutar el script (o el .bat) para continuar donde quedo.")
    else:
        log("Todas las comunas de la lista fueron procesadas. Listo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
