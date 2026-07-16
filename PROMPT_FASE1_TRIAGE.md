# PROMPT DELEGABLE — Fase 1: Triage y clasificación del corpus de ordenanzas

> Pega este contenido completo como primer mensaje de una sesión nueva de Claude Code,
> abierta en `C:\Users\gcastillo\Desktop\Ordenanzas`.
> Esta fase es autocontenida: no necesitas haber visto las sesiones anteriores.

---

## Contexto del proyecto

Estoy construyendo una base de datos nacional de **normas urbanísticas** (coeficientes de
constructibilidad y ocupación de suelo, alturas máximas, superficie predial mínima, densidad,
sistema de agrupamiento, antejardín, usos de suelo permitidos/prohibidos) para las **343 comunas
de Chile**. La fuente son las ordenanzas locales de los Planes Reguladores Comunales (PRC),
descargadas como PDF desde el Portal de Transparencia por un bot propio.

El destino final es un JSON por comuna conforme al esquema `NormativaPRC`, que alimenta un
geolocalizador normativo. **Esa conversión NO es parte de esta fase** — la hace después una skill
llamada `ordenanza-a-json`. Tu trabajo es anterior: decidir **qué documentos sirven**.

## Estado actual (Fase 0, ya completada — NO la repitas)

Ya existe un catálogo maestro del corpus. Estos archivos están en la raíz del proyecto y son tu
punto de partida:

| Archivo | Qué contiene |
|---|---|
| `corpus_unico.csv` | **~1.322 documentos únicos** (deduplicados de 3 copias). Es TU archivo de entrada. |
| `catalogo_maestro.csv` | Las ~3.564 filas crudas, una por archivo en disco, antes de deduplicar. |
| `catalogo_paginas.json` | Detalle **página a página** de cada PDF: caracteres y si tiene imagen grande. Clave para la Fase 3. |
| `cobertura_comunas.csv` | Estado de las 343 comunas. |

Columnas relevantes de `corpus_unico.csv`:
`comuna`, `familia`, `ruta`, `nombre`, `paginas`, `paginas_texto`, `paginas_escaneadas`,
`veredicto`, `rutas_copias`.

El campo **`veredicto`** ya te dice el estado de la capa de texto de cada documento:
- `TEXTO` (~636) — legible con `pdftotext`.
- `ESCANEADO` (~559) — todo imagen, requiere lectura visual.
- `MIXTO` (~106) — **tiene texto PERO sus tablas son imágenes**. Ver la trampa 2 más abajo.
- `VACIO` / `ILEGIBLE` (~21) — descartables.

## TU TAREA (Fase 1)

Clasificar los ~1.322 documentos de `corpus_unico.csv` y producir una **lista blanca** de los que
efectivamente contienen normas urbanísticas, más una lista de descartados **auditable** (yo la voy
a revisar antes de que sigas).

### Taxonomía (usa exactamente estas etiquetas)

| Categoría | Definición | ¿Sirve? |
|---|---|---|
| `ORDENANZA_PRC` | Ordenanza local completa o texto refundido del PRC. **Máximo valor.** | SÍ |
| `MODIFICACION_PRC` | Decreto/resolución que aprueba o promulga una modificación del PRC. Suele traer normas nuevas para algunas zonas. | SÍ |
| `ENMIENDA_PRC` | Enmienda al PRC (cambio acotado, p. ej. solo antejardines). | SÍ |
| `PRI_INTERCOMUNAL` | Plan Regulador **Intercomunal** o Metropolitano (PRI/PRM). Afecta a varias comunas. | SÍ (marcar aparte) |
| `TRAMITE_ADMINISTRATIVO` | Inicio de proceso, consulta pública, postergación de permisos, "deja sin efecto", exposición, adjudicación de estudio, fe de erratas sin normas, audiencias. **Sin normas urbanísticas.** | NO |
| `OTRO_TEMA_MUNICIPAL` | Nada que ver con el PRC: "atribuciones esenciales", ordenanza de derechos municipales, medio ambiente, becas, tránsito. | NO |
| `PLANO_LAMINA` | Plano o lámina gráfica, sin cuadro normativo. | NO |
| `INDETERMINADO` | No se puede decidir con nombre + texto disponible. **Requiere mirada visual.** | Escalar |

### Método — cascada de lo barato a lo caro

**Paso 1 — Reglas sobre el nombre de archivo (gratis).**
Los nombres son muy descriptivos porque vienen del título del documento en el portal. Escribe un
script Python con regex que descarte de inmediato lo evidente. Patrones de descarte que YA sé que
funcionan (verifícalos, no los asumas):
`atribuciones_esenciales`, `potestades_competencias`, `consulta_publica`, `iniciese_el_proceso`,
`inicio_de(l)?_proceso`, `postergacion`, `posterga_por`, `deja_sin_efecto`, `audiencias_publicas`,
`adjudicase`, `autoriza_compra`, `insercion_prensa`, `llamado_a_licitacion`,
`certificado_de_inform(e|acion)es_previas`, `solicito_`, `estimados_`, `a_quien_corresponda`.
**Cuidado:** varios nombres son preguntas ciudadanas de transparencia ("solicito información
del plano regulador…") — son trámites, no normas.
Y patrones que sugieren valor: `ordenanza_local`, `texto_refundido`, `promulga`, `aprueba_modificacion`,
`enmienda`, `plan_regulador_comunal`.

**Paso 2 — Texto de las primeras páginas (barato).**
Para los que sobreviven y tienen `veredicto=TEXTO` o `MIXTO`, extrae texto y busca señales
positivas: "normas urbanísticas", "coeficiente de constructibilidad", "coeficiente de ocupación de
suelo", "superficie predial mínima", "altura máxima de edificación", "densidad bruta", "sistema de
agrupamiento", "zonificación", códigos de zona (`ZC-1`, `ZH-3`, `ZU-2`, `EC5`, `ICH`…).
Usa `pdftotext` (está en el PATH; ver "Herramientas" abajo).

**Paso 3 — Lectura visual, SOLO para los que quedan indeterminados (caro).**
Para `ESCANEADO` sin nombre concluyente, y para cualquier `INDETERMINADO`: renderiza **1 o 2
páginas a baja resolución (100 dpi)** y que un agente decida. **No renderices el documento entero
en esta fase** — eso es Fase 3 y ya hay un mapa de páginas para hacerlo dirigido.

### Paralelización

Esto es trabajo perfecto para delegar en agentes. Reparte los documentos en lotes (~25-30 por
agente) y lánzalos concurrentemente con la herramienta `Workflow` o `Agent`. Cada agente devuelve
JSON estructurado con la clasificación de su lote. **Usa `schema` para forzar salida estructurada**
y evitar parsear texto libre.

Si un agente falla, registra el fallo y continúa con el resto — no detengas la corrida global.

---

## TRES TRAMPAS QUE YA ME COSTARON BUGS — no las repitas

**1. Nunca confíes en la extensión del archivo.**
El bot guardó 822 páginas HTML con extensión `.pdf`. Ya fueron borradas, pero si aparecen más,
detecta el tipo por **bytes de cabecera** (`%PDF-` vs `<!doctype html`), jamás por el sufijo.
Hay además 30 archivos rescatados en `_recuperables_no_pdf/` (ZIP, .doc, imágenes, RAR) que **son
ordenanzas reales en el contenedor equivocado** — para algunas comunas son el único material que
existe. No los ignores: inclúyelos en tu inventario como pendientes de conversión.

**2. La carpeta "OCR ok" MIENTE, y el conteo de caracteres por documento también.**
Caso testigo: `caldera_1718…` (texto refundido, 61 MB, 57 páginas) está en la carpeta "OCR ok" y
`pdftotext` extrae texto de él — pero **sus páginas 12 a 57, donde viven TODAS las tablas de
zonas, son imágenes JPEG**. La capa de texto solo trae el encabezado de LeyChile (~130 caracteres
por página). Un documento puede "tener texto" y aun así tener sus tablas ilegibles.
Por eso el `veredicto` del catálogo se calculó **por página** y cruzando con imágenes.
**Confía en la columna `veredicto`, no en `pdftotext` a secas.** Hay 106 documentos MIXTOS así,
con ~1.094 páginas escaneadas escondidas.

**3. La comuna se infiere emparejando contra la lista oficial, no cortando el nombre.**
`comunas_chile.txt` tiene los nombres propios ("Cerro Navia", "Conchalí") — hay que slugificar
(minúsculas, sin tildes, `_` por espacio). Y para asignar comuna a un archivo, empareja por
**prefijo más largo** contra esa lista (así `san_jose_de_maipo` gana sobre `san_jose`). Cortar el
nombre en el primer número inventa comunas falsas (`las_condes_n`, `el_quisco_inform`).
Esto ya está resuelto en `corpus_unico.csv` — no lo rehagas, pero no lo rompas.

---

## Herramientas disponibles

**Poppler ya está instalado** (vía `winget install oschwartz10612.Poppler`). Los binarios están en:
```
C:\Users\gcastillo\AppData\Local\Microsoft\WinGet\Packages\oschwartz10612.Poppler_Microsoft.Winget.Source_8wekyb3d8bbwe\poppler-25.07.0\Library\bin
```
`pdftotext`, `pdfinfo`, `pdfimages` y `pdftoppm` funcionan desde ahí (agrega esa ruta al PATH en tus
scripts; puede no estar en el PATH del proceso).

Extraer texto:            `pdftotext -f 1 -l 4 "archivo.pdf" -`
Renderizar una página:    `pdftoppm -f 20 -l 20 -r 100 -png "archivo.pdf" salida`

**IMPORTANTE — rutas con espacios:** casi todas las rutas tienen espacios ("Ordenanzas ordenadas",
"OCR ok"). Cita SIEMPRE las rutas en bash y usa `while IFS= read -r` en los bucles.

**NO intentes hacer OCR local con Python** (PyMuPDF + rapidocr): ya se probó y **fracasó por
consumo de recursos**, además de leer mal las tablas. El método que funciona es renderizar la
página con `pdftoppm` a 250 dpi y que un agente con visión la transcriba. Ya se validó con la
comuna de Chillán (ver `Ordenanzas ordenadas/chillan_normas_urbanisticas_pag23-33.md` como ejemplo
del formato de salida esperado en la fase de extracción).

---

## PROTOCOLO DE SILENCIO ESTRICTO (obligatorio)

**Trabaja en silencio. Solo reportas resultados.** El avance real vive en los archivos que
produces, no en el chat.

**NO escribas** en el chat: anuncios de lo que vas a hacer, comentarios por documento, narración
de comandos o de lo que devolvió un subagente, explicaciones de tu método, ni confirmaciones de lo
obvio ("listo", "perfecto").

**SÍ escribes**, y nada más:
1. Una línea al arrancar: `Fase 1: iniciando | <n> documentos en corpus_unico.csv`.
2. Una línea de avance por cada ~200 documentos clasificados:
   `Fase 1: <n>/<total> | sirve: <n> | descarta: <n> | escalar: <n>`.
3. El informe final (formato abajo).
4. Un bloqueo real, si aparece: algo que solo el usuario puede resolver. Una línea. Un documento
   que falla no es un bloqueo — se marca `ESCALAR` y se sigue.

Las observaciones por documento van a la columna `motivo` del CSV, no al chat.
Si un subagente devuelve un informe largo, **no lo repitas**: incorpora su clasificación y sigue.

## Entregables de esta fase

1. **`fase1_triage.py`** — el script de las reglas del Paso 1 y 2, reproducible y reanudable.
2. **`corpus_clasificado.csv`** — `corpus_unico.csv` + columnas nuevas:
   `categoria` (una de las 8 de la taxonomía), `sirve` (SI/NO/ESCALAR),
   `confianza` (ALTA/MEDIA/BAJA), `motivo` (frase corta que explique la decisión — esto es lo que
   yo voy a auditar), `metodo` (NOMBRE / TEXTO / VISUAL).
3. **`lista_blanca.csv`** — solo los `sirve=SI`, ordenados por comuna. Estimo que serán ~600-700.
4. **`descartados.csv`** — los `sirve=NO`, con su motivo. **Este archivo lo reviso yo**: un falso
   descarte es el error más caro de todo el pipeline, porque el documento desaparece en silencio.
5. El **informe final en el chat**, con este formato y nada más:

```
FASE 1 — FINALIZADA
Clasificados : <n>   (sirve: <n> | descarta: <n> | escalar: <n>)
Por categoría: ORDENANZA_PRC <n> · MODIFICACION_PRC <n> · ENMIENDA_PRC <n> · PRI_INTERCOMUNAL <n>
               TRAMITE <n> · OTRO_TEMA <n> · PLANO <n> · INDETERMINADO <n>
Cobertura    : <n>/343 comunas con al menos un documento útil
Comunas sin nada: <lista>        (necesitan otra ronda de descarga — no es tu tarea, solo repórtalas)
Confianza    : qué quedó sin verificar y con qué nivel de certeza
Hallazgos    : solo lo accionable para las fases siguientes; si no hay, "ninguno"
```

No resumas tu trabajo ni expliques tu método — los CSV ya lo tienen.

## Criterio de calidad — léelo antes de empezar

**Ante la duda, NO descartes: marca `ESCALAR`.** El costo de procesar de más un documento inútil es
unos centavos de cómputo. El costo de descartar por error una ordenanza es que una comuna entera
queda sin normas y nadie se entera. **Los errores no son simétricos.** Si tu regex de descarte
tiene dudas sobre un nombre, que gane la inclusión.

Al terminar, dime explícitamente qué quedó sin verificar y con qué nivel de confianza, en vez de
presentar el resultado como si fuera completo.
