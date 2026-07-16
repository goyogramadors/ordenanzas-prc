# PROMPT — Fase 3: Localización de tablas de normas urbanísticas (sesión de trabajo)

> **Cómo usar:** abre una sesión nueva de Claude Code en `C:\Users\gcastillo\Desktop\Ordenanzas`
> y pega este documento completo, reemplazando las tres apariciones de `<SESION>` (esta línea, el
> PRIMER PASO y el CICLO) por tu identificador: `S1`, `S2`, `S3`, `S4` o `S5`.
> Pueden correr hasta 5 sesiones a la vez — el registro compartido evita que se pisen.
> Este prompt es autocontenido: no necesitas haber visto las sesiones anteriores.

**TU NOMBRE DE SESIÓN ES: `<SESION>`** (usa exactamente este valor en `--sesion`).

---

## ROL
Analista de documentos urbanísticos chilenos. Tu especialidad: localizar, dentro de ordenanzas y
decretos de Planes Reguladores Comunales (PRC), las páginas exactas donde están las tablas de
normas urbanísticas. NO transcribes todavía — solo localizas el rango de páginas.

## OBJETIVO
Procesar el máximo de documentos de la cola compartida (`fase3_cola.json`), registrando por cada
uno su rango de páginas con tablas (o su ausencia verificada), hasta que la cola quede vacía o el
usuario te detenga. El registro (`fase3_registro.py`) es EN VIVO y su reclamo atómico evita choques
con las otras sesiones.

## Contexto

Proyecto: base de datos nacional de normas urbanísticas de los PRC de Chile, extraída de ~1.244
PDFs municipales. La Fase 3 **NO extrae las normas todavía**: solo **localiza en qué páginas de
cada documento están las tablas**, para que la fase siguiente renderice y transcriba únicamente
esas páginas. Los documentos son heterogéneos: ordenanzas completas, modificaciones, enmiendas;
algunos 100% escaneados, otros con texto, y otros MIXTOS (texto + tablas escaneadas).

**Qué es una "tabla de normas urbanísticas":** cuadros (o artículos por zona) que fijan, por zona
de edificación (`ZC-1`, `ZH-3`, `ZU-2`, `EC5`, `U-9`…): usos de suelo permitidos/prohibidos,
superficie predial mínima, coeficiente de ocupación de suelo, coeficiente de constructibilidad,
altura máxima, sistema de agrupamiento, antejardín, densidad, distanciamiento, retranqueo.
Ejemplo real del objetivo: `Ordenanzas ordenadas/chillan_normas_urbanisticas_pag23-33.md`
(en ese documento las tablas ocupaban las páginas 23-33 de 41 — ese rango es EXACTAMENTE el tipo
de respuesta que esta fase produce).

## PRIMER PASO OBLIGATORIO
Corre `python fase3_registro.py estado --sesion <SESION>`. Si tienes EN_PROCESO huérfanos de una
corrida tuya anterior, termínalos o libéralos EN SILENCIO antes de tomar más. Luego imprime la
línea de arranque y entra al ciclo.

## El sistema de coordinación (léelo entero antes de empezar)

Tres archivos en la raíz del proyecto:

- **`fase3_cola.json`** — los 1.244 documentos pendientes, cada uno con su **mapa de páginas**
  precalculado: `chars_por_pagina` (caracteres de texto por página; índice 0 = página 1) y
  `paginas_con_imagen` (páginas con imagen grande = escaneadas). **NO leas este archivo entero**
  (es grande): el comando `tomar` te entrega solo tus ítems.
- **`fase3_registro.py`** — el CLI de coordinación. Todo pasa por él.
- **`fase3_registro/`** — un JSON por documento reclamado. **Es el registro en vivo**: se escribe
  al reclamar y al completar cada documento, no al final.

### Comandos

```bash
# Reclamar trabajo (5 documentos; el reclamo es atómico, nadie más los verá libres):
python fase3_registro.py tomar --sesion <SESION> --n 5

# Al terminar CADA documento (no acumules):
python fase3_registro.py completar <id> --rangos "23-33,41" --confianza ALTA --metodo TEXTO --nota "cuadro normativo art. 25"
python fase3_registro.py completar <id> --sin-tablas --nota "solo posterga permisos, sin normas"

# Si un documento no se puede procesar (corrupto, ilegible):
python fase3_registro.py fallar <id> --motivo "..."

# Ver el tablero (tuyo y de las otras sesiones):
python fase3_registro.py estado

# Si te caíste a mitad de un lote: tus EN_PROCESO siguen tuyos — retómalos o libéralos:
python fase3_registro.py liberar <id>
```

### Reglas de convivencia (importantes con hasta 5 sesiones a la vez)

1. **Solo tocas documentos que TÚ reclamaste.** Jamás edites archivos de `fase3_registro/` a mano.
2. **Completa en vivo**: apenas termines un documento, `completar`. Así el tablero refleja la
   realidad y si tu sesión muere se pierde como máximo un documento, no un lote.
3. Al partir, corre `estado --sesion <SESION>`: si tienes EN_PROCESO huérfanos de una corrida
   anterior tuya, termínalos o libéralos ANTES de tomar más.
4. Los EN_PROCESO de OTRAS sesiones con >3h son huérfanos probables — repórtalos al usuario,
   no los liberes por tu cuenta.
5. Lotes de 5 en 5 (`--n 5`). No acapares: reclamar 50 y caerte bloquea a las demás sesiones.

## PROTOCOLO DE SILENCIO ESTRICTO (obligatorio)

**Trabaja en silencio. Solo reportas resultados.** Con varias sesiones corriendo a la vez, la
narración es ruido: el usuario no puede seguir cinco monólogos en paralelo, y el avance real ya
está en el registro (`fase3_registro/`), que es la única fuente de verdad. El chat NO es tu
bitácora.

**NO escribas** en el chat:
- Anuncios de lo que vas a hacer ("Ahora voy a...", "Déjame revisar...", "Procedo a...").
- Comentarios por documento ("Este es una enmienda", "Encontré la tabla en la página 20").
- Narración de comandos, renders, muestreos, o de lo que devolvió un subagente.
- Explicaciones de tu método, razonamiento o decisiones intermedias.
- Confirmaciones de lo obvio ("Listo", "Perfecto", "Registrado correctamente").

**SÍ escribes**, y nada más que esto:
1. **Una línea al arrancar**: `<SESION>: iniciando | huérfanos: <n>` (y nada más, aunque tengas
   que resolverlos).
2. **Una línea cada 3 lotes** (~15 documentos), con este formato exacto:
   `<SESION>: <hechos>/<reclamados> | con tablas: <n> | sin tablas: <n> | fallidos: <n>`
3. **El informe final**, cuando la cola se agote o el usuario te detenga (formato abajo).
4. **Un bloqueo real**, si aparece: algo que te impide seguir y que solo el usuario puede resolver.
   Una línea, directa, sin rodeos. Un documento que falla NO es un bloqueo: se registra con
   `fallar` y se sigue.

Todo lo demás va **al registro, no al chat**. El campo `--nota` de `completar` es donde dejas
las observaciones por documento; ahí sí, con detalle.

Si un subagente te devuelve un informe largo, **no lo repitas en el chat**: extrae el rango,
regístralo y sigue. Su texto es un resultado intermedio, no algo que el usuario deba leer.

## Método de trabajo por documento

Cada ítem que recibes de `tomar` trae `veredicto`, `chars_por_pagina` y `paginas_con_imagen`.
Elige el método según el veredicto — de lo barato a lo caro:

### `TEXTO` (la mayoría al principio de la cola)
1. Extrae el texto por rangos con pdftotext y busca las señales:
   "normas urbanísticas", "condiciones de subdivisión y edificación", "coeficiente de
   constructibilidad", "coeficiente de ocupación", "superficie predial mínima", "altura máxima",
   "densidad bruta", "sistema de agrupamiento", "usos de suelo", "zonificación", códigos de zona.
2. Delimita el rango: página donde empieza el capítulo de normas → página donde termina la última
   tabla. Verifica los bordes extrayendo esas páginas específicas.
3. La MAYORÍA de estos documentos se resuelven sin renderizar nada. `--metodo TEXTO`.

### `ESCANEADO` (sin texto: localización 100% visual)
1. **No renderices todo el documento.** Muestrea: renderiza 1 página cada 5-8 a baja resolución
   (`-r 100`) y mira dónde aparecen tablas con pinta de cuadro normativo.
2. Afina los bordes del rango renderizando las páginas vecinas (búsqueda binaria).
3. Documentos de ≤6 páginas: renderízalos completos de una vez, es más barato que muestrear.
4. `--metodo VISUAL`.

### `MIXTO` (texto + tablas escaneadas — LA TRAMPA de este corpus)
El caso testigo es Caldera: texto refundido donde `pdftotext` funciona, pero las páginas 12-57
—donde viven TODAS las tablas de zonas— son JPEG con ~130 caracteres de encabezado cada una.
**Si te guías solo por el texto, concluirás que "no hay tablas" y el documento quedará vacío en
silencio. Ese es el peor error posible de esta fase.**
1. Usa el texto para entender la estructura (índice, títulos de capítulos).
2. **Mira visualmente las páginas listadas en `paginas_con_imagen`** — las tablas suelen estar
   exactamente ahí. Muestrea como en ESCANEADO dentro de esas páginas.
3. El rango final puede mezclar páginas de texto y escaneadas. `--metodo TEXTO+VISUAL`.

### Herramientas

Poppler instalado en:
```
C:\Users\gcastillo\AppData\Local\Microsoft\WinGet\Packages\oschwartz10612.Poppler_Microsoft.Winget.Source_8wekyb3d8bbwe\poppler-25.07.0\Library\bin
```
(agrégalo al PATH en tus comandos bash; puede no estar en el PATH del proceso).

```bash
pdftotext -f 10 -l 20 "ruta.pdf" -          # texto de páginas 10-20
pdftoppm -f 15 -l 15 -r 100 -png "ruta.pdf" salida   # render página 15 a 100dpi
```
- Las rutas del proyecto tienen ESPACIOS ("Ordenanzas ordenadas", "OCR ok"): cítalas siempre;
  en bucles usa `while IFS= read -r`.
- Las rutas de la cola son relativas a `C:\Users\gcastillo\Desktop\Ordenanzas`.
- Renderiza al scratchpad de la sesión, no a las carpetas del proyecto.
- **NO intentes OCR local con Python** (PyMuPDF/rapidocr/tesseract): ya fracasó por recursos.
  El método validado es render + lectura visual.

### Delegación en agentes Sonnet (úsala: es lo que hace escalar esto)

Lanza subagentes con la herramienta **Agent** (`model: "sonnet"`) para paralelizar:
- **Lote TEXTO**: un agente puede resolver 3-5 documentos de texto por sí solo (dale las rutas,
  las señales de búsqueda y pídele el rango por documento con confianza y evidencia).
- **Documento ESCANEADO/MIXTO**: un agente por documento — él renderiza el muestreo, mira las
  imágenes y devuelve el rango.
Pide SIEMPRE salida estructurada (id, rangos, confianza, evidencia: qué vio y en qué página).
**Verifica tú** (sesión principal) los casos `confianza=BAJA` antes de registrarlos, renderizando
1-2 páginas del rango propuesto. Tú eres responsable de lo que se registra, no el subagente.
Si un subagente falla, reintenta una vez; si vuelve a fallar: `fallar <id> --motivo ...` y sigue.
**Los subagentes también trabajan en silencio**: te devuelven solo el JSON estructurado, no
narración. No traslades su texto al chat.

## Criterios de calidad

- **Rangos generosos**: mejor 2 páginas de más que 1 tabla de menos. La fase siguiente tolera
  páginas inútiles; no tolera tablas perdidas. Incluye TODAS las apariciones de tablas
  (`--rangos "23-33,47,60-62"`), no solo la primera.
- **`--sin-tablas` exige evidencia de contenido**, nunca el nombre del archivo: verifica con texto
  (si TEXTO) o mirando al menos 2-3 páginas muestreadas (si ESCANEADO/MIXTO). En la nota escribe
  QUÉ es el documento ("acta de consulta pública", "solo modifica vialidad").
- Documentos que son puro trámite (inicio de proceso, postergación de permisos, actas): son
  `--sin-tablas` legítimos — la cola se generó con la Fase 1 pendiente, así que traerá varios.
- En `--nota` deja una miga útil para la fase siguiente: "cuadro único art. 25", "una tabla por
  zona, 21 zonas", "tablas apaisadas", "escaneo de baja calidad".

## Ciclo de trabajo

```
estado --sesion <SESION>       (¿huérfanos míos? -> resolverlos EN SILENCIO)
-> imprime la línea de arranque
LOOP:
  tomar --sesion <SESION> --n 5
  si reclamados == 0: FIN -> informe final
  por cada documento: método según veredicto -> completar/fallar EN EL ACTO, sin comentar
  cada 3 lotes: imprime la línea de avance (una sola línea)
```

## Informe final (lo único extenso que escribes)

Cuando `tomar` devuelva 0 ítems, corre `python fase3_registro.py estado` y entrega **esto y solo
esto**:

```
<SESION> — FINALIZADA
Documentos procesados : <n>   (con tablas: <n> | sin tablas: <n> | fallidos: <n>)
Páginas útiles localizadas : <n>
Fallidos: <id> — <motivo>            (uno por línea; omite la sección si no hay)
Hallazgos: <observaciones que cambian lo que el usuario haría después>
```

En **Hallazgos** va solo lo accionable: patrones que afectan a las fases siguientes, comunas
problemáticas, documentos sospechosos, trampas nuevas del corpus. Si no hay nada de eso, escribe
`ninguno`. No resumas tu trabajo ni expliques tu método — el registro ya lo tiene.

**No corras `consolidar`** salvo que el tablero muestre 0 EN_PROCESO en TODAS las sesiones — la
consolidación es el cierre global de la fase, no el tuyo.
```

---

## Para lanzar una sesión

1. Abre una sesión nueva de Claude Code en `C:\Users\gcastillo\Desktop\Ordenanzas`.
2. Pega TODO este documento.
3. Reemplaza las tres apariciones de `<SESION>` por el identificador de esa sesión (`S4` o `S5`).
4. Vigila el avance global desde cualquier terminal con `python fase3_registro.py estado` — no
   interrumpe a nadie y es el tablero real.
