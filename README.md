# Bot de descarga de ordenanzas del Plan Regulador Comunal (PRC)

> **Alcance de este repositorio.** Este es el material de trabajo (PDFs fuente,
> catálogos, y pipeline de Fases 0-5) para producir las fichas normativas del
> geolocalizador de Archibots. **El resultado final que consume la app son los
> JSON `NormativaPRC`**, que se guardan directamente en
> `Web/public/norma-data/` del repo `projectbook` (Archiblocks) — no viven aquí.
> Este repo es respaldo/proceso: útil para retomar Fase 4/5, resolver dudas
> sobre una comuna puntual, o auditar de dónde salió un dato, pero no es la
> fuente de verdad de la app.
>
> Los PDF aquí son el subconjunto **deduplicado y curado** (ver
> `corpus_unico.csv` / `lista_blanca.csv` / `escalados.csv`) de un corpus
> original de ~10.7 GB con mucha copia repetida entre carpetas de descarga.
> Ese material crudo sin curar quedó solo en el equipo local, no se subió.
>
> **Cómo continuar Fase 5:** abre `PROMPT_FASE5_SESION.md` y sigue las
> instrucciones — coordina con `fase5_registro.py` / `fase5_cola.json` para no
> pisar el trabajo de otras sesiones.
>
> **Requisito de workspace:** Fase 5 escribe el JSON final y valida contra el
> GeoJSON en el repo `projectbook` (Archiblocks), NO en este repo. `fase5_registro.py`
> y `fase5_cola.py` esperan encontrar ese repo como carpeta **hermana** de esta,
> llamada `projectbook/` (mismo padre que `ordenanzas-prc-chile/`). Si tu clon se
> llama distinto o vive en otra ruta, exporta `ARCHIBLOCKS_WEB_PUBLIC` apuntando a
> su carpeta `Web/public` antes de correr los scripts de Fase 5:
> ```bash
> export ARCHIBLOCKS_WEB_PUBLIC=/ruta/a/projectbook/Web/public
> ```

Descarga automáticamente los PDF del Plan Regulador de comunas de Chile desde el
**Portal de Transparencia** (`portaltransparencia.cl`), usando Python + Playwright.

## Qué hace

Para cada comuna del listado, entra a su ficha de organismo y busca el PRC en
**cuatro fuentes complementarias** (corre todas; los duplicados se descartan
por contenido):

1. **Transparencia proactiva → "Plan Regulador"**
   - Submenú interno *"Plan Regulador y sus Modificaciones"* (ej. Colina):
     descarga cada subsección — **Ordenanza, Memoria, Modificaciones, Planos**.
   - Enlace externo *"Plan Regulador"* al sitio del municipio (ej. Peñalolén):
     **recorre las sub-páginas** y baja los `.pdf` de **texto** (ordenanza base,
     modificaciones, ordenanzas por zona). **Omite los que dicen "Lamina"**
     (son planos), según lo pedido.

2. **Sección "01. Actos y documentos publicados en Diario Oficial"**
   - Filtra por `plan regulador` y descarga el PDF de cada norma (decretos que
     aprueban/modifican el PRC), sea PDF directo del portal o vía **BCN/LeyChile**.

3. **Sección "07 → Ordenanzas [→ Ordenanzas Vigentes]"**
   - Si la comuna separa *"Ordenanzas Vigentes"* (ej. Lo Barnechea), entra ahí,
     filtra por `plan regulador` y descarga el **texto refundido/vigente** de la
     ordenanza del PRC (a menudo el documento más completo).

4. **Buscador global del sitio** (`buscador-es?search_org=...`)
   - Busca "plan regulador" en **todas** las secciones/subcarpetas del
     organismo, sin depender de cómo esté organizada la sección 07 (algunas
     comunas la anidan por año/mes en vez de tenerla plana — ahí es donde esta
     fuente rinde más). Es la fuente más productiva en la práctica: para
     Cerrillos encontró 21 documentos que las otras 3 fuentes no alcanzaban.

Las fuentes 2, 3 y 4 aplican un **filtro de relevancia por título** (función
`es_titulo_relevante`) para descartar trámites administrativos que mencionan
"plan regulador" de pasada pero no son el texto de una ordenanza/modificación:
postergaciones de permisos de subdivisión/loteo, evaluaciones ambientales
estratégicas, contratos de consultoría, licitaciones, convenios, y
**certificados de informes/informaciones previas** (CIP — certificados por
propiedad, no la norma).

### Limpiar certificados ya descargados

Si en descargas anteriores (antes de agregar ese filtro) se colaron CIP, corre
el limpiador para borrarlos:

```bash
python limpiar_certificados.py --dry-run   # muestra qué borraría, sin borrar
python limpiar_certificados.py             # los elimina
```

O doble clic en **`limpiar_certificados.bat`** (muestra la vista previa y pide
confirmar "SI" antes de borrar). Solo borra archivos cuyo nombre contiene
"informes previos" / "informaciones previas"; respeta ordenanzas y otros
certificados legítimos (ej. certificado de exposición del plan regulador).

Los PDF se deduplican por contenido y se guardan en:

```
descargas/<comuna>/
├── proactiva/<subseccion>/*.pdf         (submenú interno proactiva)
├── proactiva_externa/*.pdf              (sitio externo del municipio, solo textos)
├── diario_oficial/*.pdf                 (normas del Diario Oficial / BCN)
├── ordenanzas_vigentes/*.pdf            (ordenanza vigente del PRC)
├── busqueda_global/*.pdf                (hallazgos del buscador global del sitio)
└── indice.csv                           (archivo, url, tamaño KB)
```

> Los tiempos de espera son generosos (mínimo 3 s por acción) porque el portal es
> lento; una comuna sin resultados tarda ~1–2 min, una con muchos resultados en
> el buscador global (fuente 4) puede tardar 6–10 min, porque cada documento
> relevante requiere recargar la búsqueda desde cero (el orden de resultados
> con títulos casi idénticos no es 100% estable, así que no se puede confiar en
> "ir a la página N" para reubicar uno ya visto — cada uno se busca de nuevo).
> Ajustables en las constantes `W_CORTA/W_MEDIA/W_LARGA`.

## Instalación

```bash
pip install -r requirements.txt
python -m playwright install chromium
```

## Uso rápido (Windows, doble clic)

- **`ejecutar_bot.bat`** → procesa **todas** las comunas pendientes de
  `comunas_chile.txt` (343 comunas de Chile, orden: Región Metropolitana →
  Valparaíso → resto del país), en lotes internos de 10. Se puede cerrar la
  ventana en cualquier momento e interrumpirlo sin perder avance: al volver a
  hacer doble clic, retoma donde quedó (lee `registro_progreso.csv` y se salta
  lo ya hecho).
- **`ejecutar_un_lote.bat`** → procesa un solo lote de 10 y se detiene. Útil si
  prefieres avanzar de a poco y revisar entre lotes.

## Uso por línea de comandos

```bash
# Procesa TODAS las comunas pendientes de una lista, en lotes de 10 (por defecto)
python descargar_prc.py --lista comunas_chile.txt

# Solo el siguiente lote (10 comunas) y se detiene
python descargar_prc.py --lista comunas_chile.txt --lotes 1

# Tamaño de lote distinto
python descargar_prc.py --lista comunas_chile.txt --batch-size 5

# Comunas puntuales por línea de comando (ignora el registro igual)
python descargar_prc.py Peñalolén Colina

# Ver el navegador mientras trabaja (útil para depurar)
python descargar_prc.py Colina --headed
```

> **Nota:** en Windows conviene ejecutar con `PYTHONIOENCODING=utf-8` para que los
> nombres con tildes (Peñalolén) se muestren bien en consola (los `.bat` ya lo
> configuran solos).

## Lotes y registro de avance (resumible)

El bot procesa la lista en **lotes de 10 comunas** (configurable con
`--batch-size`), reciclando el navegador entre lotes para no acumular memoria
en corridas de muchas horas. Después de cada comuna, actualiza
**`registro_progreso.csv`** (columnas: `slug, comuna, estado, pdfs, fecha_hora`).

Al iniciar, el bot **lee ese registro** y salta las comunas ya marcadas
`hecho` — así puedes interrumpir la corrida (cerrar la ventana, apagar el
equipo) y **retomarla después ejecutando lo mismo otra vez**: no vuelve a
descargar lo que ya tiene. Las comunas con error quedan marcadas `error` y se
reintentan automáticamente en la siguiente corrida.

Para forzar que una comuna se vuelva a procesar, borra su fila de
`registro_progreso.csv` (o el archivo completo para reprocesar todo).

## Correr varios bots en PARALELO (más rápido)

Para acelerar, se puede repartir el trabajo pendiente entre varios bots que
corren a la vez, cada uno con **su propia lista y su propio registro** (así no
se pisan). Como las listas son disjuntas, cada comuna la procesa un solo bot y
todos escriben en la misma carpeta `descargas/` sin chocar.

**Flujo (Windows):**

1. Genera el reparto (por defecto 10 partes):
   ```bash
   python preparar_paralelo.py          # 10 bots  (o --n 5 para 5)
   ```
   Esto **consolida** el avance de bots previos en `registro_progreso.csv`
   (borra los `registro_NN.csv` viejos para partir limpio), toma lo que quede
   pendiente y crea:
   - `comunas_lote_01.txt` … `comunas_lote_10.txt` (las sub-listas)
   - `ejecutar_lote_01.bat` … `ejecutar_lote_10.bat` (un `.bat` por bot)
   - `ejecutar_paralelo.bat` (lanzador que abre los 10 de una vez)

   > Para **rehacer el reparto** con lo que quede pendiente (p. ej. tras una
   > tanda con errores), **detén todos los bots** y corre
   > `python preparar_paralelo.py --forzar`. Consolida lo hecho y reparte solo
   > lo que falta (las comunas con `error` o sin terminar se reintentan).

2. Doble clic en **`ejecutar_paralelo.bat`** → abre 10 ventanas, una por bot.
   (O abre solo algunos `ejecutar_lote_NN.bat` sueltos si prefieres menos.)

3. Para ver el avance combinado: doble clic en **`estado_paralelo.bat`**.

**Importante:**
- Son **10 navegadores headless a la vez** → usa bastante CPU/RAM y el portal
  (que ya es lento) puede responder más despacio bajo tanta carga simultánea.
  Si el equipo se pone lento, cierra algunas ventanas: cada bot guarda su avance
  y se reanuda solo al reabrir su `.bat`. Si prefieres menos carga, usa
  `python preparar_paralelo.py --n 5 --forzar` (tras detener los bots).
- Cada bot es **resumible** por su cuenta (su `registro_NN.csv`). Puedes cerrar
  una ventana y reabrir su `.bat` cuando quieras.
- Para **rehacer el reparto** con lo que quede pendiente (p. ej. tras avanzar un
  rato), detén todos los bots y corre `python preparar_paralelo.py --forzar`.

## Notas técnicas / limitaciones

- El portal es una SPA (PrimeFaces). El bot usa un **user-agent de escritorio**
  (necesario: en modo headless "puro" el buscador no renderiza el input).
- Los PDF se capturan re-descargándolos con `context.request.get()` (comparte las
  cookies de sesión), en vez de `response.body()`, que falla con el visor de PDF.
- **Las etiquetas y la estructura varían por comuna.** El bot ya contempla las dos
  variantes vistas, pero comunas nuevas podrían usar otra redacción; si una fuente
  sale vacía, correr con `--headed` para inspeccionar.
- El PRC "vigente" normalmente **no es un solo archivo**: es el texto/ordenanza base
  más sus modificaciones. Por eso se descarga todo lo disponible en ambas fuentes.

## Resultado de referencia (validado 2026-07-09)

| Comuna | Fuente destacada | Total PDFs |
|--------|------------------|-----------|
| Peñalolén | Proactiva externa: PRC2021 (24 MB) + 13 modificaciones + zonas | 60 |
| Colina | Proactiva: Ordenanza (1.8 MB) + Plano (9 MB) + BCN | 8 |
| Lo Barnechea | Ordenanzas Vigentes: Texto refundido PRC (15 MB) + 31 decretos | 32 |
| Cerrillos | Buscador global: 21 decretos de actualización del PRC (2018–2023) | 21 |

## Escala: correr las 343 comunas de Chile

`comunas_chile.txt` trae las 343 comunas (RM → Valparaíso → resto del país).
Corriendo esto completo es una tarea de **muchas horas** (posiblemente 1–2
días si se deja correr sin pausa):

- Una comuna sin resultados en ninguna fuente tarda ~1–2 min (tiempos de
  espera + intentos fallidos). Una con muchos resultados en el buscador
  global (fuente 4) puede tardar 6–10 min (Cerrillos, con 21 documentos
  relevantes, tardó ~6 min solo en esa fuente).
- Con 343 comunas, el rango estimado es **10 a 30+ horas** de corrida.
- Espacio en disco: comunas grandes pueden traer 50–100+ MB (PRC consolidados
  y planos en PDF pesan varios MB cada uno); la mayoría de comunas pequeñas
  traerán mucho menos o nada. Estimado grueso: **varios GB** en total.
- Por eso el diseño es **resumible por lotes**: puedes dejarlo corriendo de
  fondo, pausarlo cuando quieras (cerrando la ventana) y continuar después sin
  perder lo ya descargado.
