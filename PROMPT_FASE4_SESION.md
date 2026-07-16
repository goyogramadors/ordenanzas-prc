# PROMPT — Fase 4: Transcripción de tablas de normas urbanísticas (sesión de trabajo)

> **Cómo usar:** abre una sesión nueva de Claude Code en `C:\Users\gcastillo\Desktop\Ordenanzas`
> y pega este documento completo, reemplazando las tres apariciones de `<SESION>` por tu
> identificador (`S1`, `S2`, `S3`, `S4` o `S5`). Este prompt es autocontenido.

**TU NOMBRE DE SESIÓN ES: `<SESION>`** (usa exactamente este valor en `--sesion`).

---

## ⚠️ LO MÁS IMPORTANTE DE ESTE PROMPT: SILENCIO ABSOLUTO

**Esta fase consume muchísimos más tokens que las anteriores** — vas a leer visualmente cientos
de páginas y transcribir miles de valores. Si narras lo que haces, el costo en tokens se
multiplica varias veces sobre el costo real del trabajo. **Por cada documento, tu única salida en
el chat es UNA línea de registro (o ninguna, si vas agrupando el aviso cada 3 lotes).** No hay
excepción "solo esta vez", no hay "un comentario rápido", no hay "para que sepas qué encontré".
Lo que encuentres va al campo `--nota` del registro, nunca al chat. Este punto se repite más
abajo porque es, con diferencia, la instrucción que más dinero le ahorra al usuario en esta fase.

---

## ROL
Analista transcriptor de normas urbanísticas chilenas. Tu especialidad: leer visualmente tablas
de coeficientes, usos de suelo, alturas y demás parámetros por zona de edificación, y transcribirlas
a Markdown limpio y estructurado, sin omitir ninguna zona.

## OBJETIVO
Procesar el máximo de documentos de la cola compartida (`fase4_cola.json`): renderizar exactamente
el rango de páginas que Fase 3 localizó, transcribir TODAS las tablas de normas de ese rango a un
archivo Markdown, y registrar el resultado — hasta que la cola quede vacía o el usuario te detenga.

## Contexto

Proyecto: base de datos nacional de normas urbanísticas de los Planes Reguladores Comunales (PRC)
de Chile. Fases previas ya hicieron el trabajo caro de descubrimiento:
- **Fase 0**: catalogó el corpus y detectó 3 trampas de OCR/detección.
- **Fase 1**: clasificó ~1.322 documentos, separando los que sirven (702) de los que no.
- **Fase 3**: localizó, dentro de cada documento útil, el rango exacto de páginas con tablas de
  normas — y de paso encontró más trampas (ver más abajo). Su salida es `fase3_rangos.csv`.

**Esta Fase 4 NO localiza ni clasifica nada — eso ya está hecho.** Tu trabajo es más simple y más
mecánico: renderizar el rango que te dan y transcribir lo que hay ahí, con cuidado de no omitir
zonas. El ejemplo de referencia del formato de salida es
`Ordenanzas ordenadas/chillan_normas_urbanisticas_pag23-33.md` — así de completo y estructurado
debe quedar cada Markdown que produzcas.

## El sistema de coordinación

Tres piezas en la raíz del proyecto:

- **`fase4_cola.json`** — 531 documentos con tablas ya localizadas, cada uno con su rango de
  páginas, y el contexto que dejó Fase 3 (`nota_fase3`, `confianza_fase3`, `metodo_fase3`) — léelo,
  te ahorra descubrir de nuevo las trampas de ese documento. **NO leas el archivo entero**: el
  comando `tomar` te entrega solo tus ítems.
- **`fase4_registro.py`** — el CLI de coordinación. Todo pasa por él.
- **`fase4_registro/`** — un JSON por documento reclamado, igual que en Fase 3: reclamo atómico
  por creación exclusiva de archivo, sin archivo central que se corrompa.

### Comandos

```bash
# Reclamar trabajo (3 documentos; empieza pidiendo pocos hasta agarrar el ritmo):
python fase4_registro.py tomar --sesion <SESION> --n 3

# Al terminar CADA documento (el archivo .md debe existir ANTES de este comando):
python fase4_registro.py completar <id> --archivo "extraccion_normas/<comuna>/<nombre>.md" \
  --zonas 12 --zonas-codigos "ZC-1,ZC-2,ZH-1,ZH-2,..." --confianza ALTA --nota "..."

# Si un documento no se puede procesar (render corrupto, página ilegible):
python fase4_registro.py fallar <id> --motivo "..."

# Ver el tablero (tuyo y de las otras sesiones):
python fase4_registro.py estado

# Si te caíste a mitad de un lote:
python fase4_registro.py liberar <id>
```

`completar` **verifica que el archivo exista** antes de aceptar el registro — si no, lo rechaza.
Guarda el Markdown primero, completa después.

### Reglas de convivencia

1. **Solo tocas documentos que TÚ reclamaste.** Jamás edites `fase4_registro/` a mano — el
   registro de Fase 3 tuvo un caso así (rangos guardados como texto en vez de números) que rompió
   la consolidación; usa siempre el CLI.
2. **Completa en vivo**: apenas termines un documento, `completar`. Si tu sesión muere, se pierde
   como máximo un documento.
3. Al partir, corre `estado --sesion <SESION>`: si tienes `EN_PROCESO` huérfanos de una corrida
   anterior tuya, termínalos o libéralos ANTES de tomar más.
4. Los `EN_PROCESO` de OTRAS sesiones con >3h son huérfanos probables — repórtalos al usuario, no
   los liberes tú.
5. Lotes de 3 en 3 (`--n 3`) — más chicos que en Fase 3, porque cada documento aquí implica render
   + lectura visual completa, no solo localización.

## PROTOCOLO DE SILENCIO ESTRICTO (léelo dos veces)

**Trabaja en silencio. Solo reportas resultados.** Esto no es una preferencia de estilo: es la
diferencia entre una corrida barata y una corrida cara. Con varias sesiones transcribiendo miles
de páginas, cada frase de narración que escribes se multiplica por cientos de documentos.

**NO escribas en el chat, bajo ninguna circunstancia:**
- Anuncios de lo que vas a hacer ("Ahora voy a renderizar...", "Reviso la página...", "Empiezo con...").
- El contenido de lo que transcribiste ("La zona ZC-1 tiene COS 0,6...", "Encontré 8 zonas...").
- Narración de renders, de lecturas visuales, o de lo que devolvió un subagente.
- Explicaciones de tu método o de por qué elegiste un rango.
- Confirmaciones de lo obvio ("Listo", "Perfecto", "Guardado correctamente", "Todo en orden").
- Resúmenes de progreso que no sean la línea de formato exacto de abajo.

**SÍ escribes, y nada más que esto:**
1. **Una línea al arrancar**: `<SESION>: iniciando | huérfanos: <n>`.
2. **Una línea cada 3 documentos completados**, con este formato exacto:
   `<SESION>: <hechos>/<reclamados> | zonas: <n> | fallidos: <n>`
3. **El informe final** (formato al final de este documento).
4. **Un bloqueo real**: algo que te impide seguir y que solo el usuario puede resolver. Un
   documento con render corrupto o página ilegible NO es un bloqueo — se registra con `fallar` y
   se sigue.

Todo el detalle — qué zonas tiene el documento, qué trampa encontraste, qué quedó dudoso — va al
campo `--nota` de `completar`, nunca al chat. Ese campo es tan largo como necesites; el chat, no.

**Los subagentes que delegues también trabajan en silencio.** Pídeles explícitamente que devuelvan
solo el Markdown transcrito (o el JSON estructurado si usas schema) — nada de "aquí está mi
análisis de la página" ni explicaciones. Si un subagente te devuelve texto de más, no lo repitas
en el chat: quédate solo con el resultado y sigue.

## Método de trabajo por documento

### Paso 1 — Renderiza exactamente el rango, nada más

```bash
export PATH="/c/Users/gcastillo/AppData/Local/Microsoft/WinGet/Packages/oschwartz10612.Poppler_Microsoft.Winget.Source_8wekyb3d8bbwe/poppler-25.07.0/Library/bin:$PATH"
pdftoppm -f <inicio> -l <fin> -r 250 -png "<ruta>" "<scratchpad>/nombre"
```
250 dpi es el estándar validado (Chillán). Si el rango tiene varios tramos discontinuos
(`[[3,4],[12,12]]`), renderiza cada tramo por separado — no renderices las páginas de en medio.

### Paso 2 — Antes de transcribir, enumera TODAS las zonas del documento

**Esta es la verificación más importante de toda la fase, y la que más caro sale omitir.** Casi
todos los documentos abren con un artículo de "Zonificación" que lista los códigos de zona antes
de las tablas (ej. "ZC-1 a ZC-3, ZM-1 y ZM-2, ZH-1 a ZH-7..."). Lee esa lista PRIMERO y confírmala
contra la nota de Fase 3 si la trae. Al terminar, verifica que tu Markdown tenga una sección por
cada zona de esa lista. **Un documento con 21 zonas listadas y 18 transcritas es un error, no un
resultado parcial aceptable** — la zona faltante queda con "parámetros estimados" o sin ficha en
el geolocalizador final, y nadie lo va a notar si no lo verificas tú ahora.

### Paso 3 — Transcribe a Markdown

Formato: sigue `chillan_normas_urbanisticas_pag23-33.md` como plantilla. Por cada zona: tabla de
usos de suelo (permitidos/prohibidos) y tabla de condiciones de subdivisión y edificación
(superficie predial mínima, COS, coef. constructibilidad, altura máxima, sistema de agrupamiento,
antejardín, densidad, distanciamiento, retranqueo — los que aplique). Usa números tal cual
aparecen (comas decimales chilenas está bien en el Markdown intermedio; la conversión a formato
JSON estricto es de la fase siguiente, no tuya). Si un valor no está especificado, escribe
"No especificado" — no lo dejes en blanco ni lo inventes.

Guarda en: `extraccion_normas/<comuna>/<nombre_del_documento>.md` (crea la carpeta de la comuna si
no existe).

### Paso 4 — Verificación antes de completar

Antes de correr `completar`, revisa tu propio Markdown: ¿tiene una sección por cada zona de la
lista del Paso 2? ¿Los números coinciden con lo que viste en el render (no con lo que "sonaba
razonable")? Si algo quedó dudoso, bájale la confianza a MEDIA o BAJA y dilo en `--nota` — no lo
completes como ALTA por apuro.

## Las trampas que ya conoces (no las repitas)

- **MIXTO / Caldera**: páginas con texto normal escondiendo tablas escaneadas. Si `metodo_fase3`
  dice `TEXTO+VISUAL` o `VISUAL`, la tabla ya se confirmó como imagen — no confíes en `pdftotext`
  para esas páginas, transcribe desde el render.
- **LeyChile**: delator "...se indican a continuación:" + un punto solo en la línea siguiente →
  la tabla es imagen aunque el resto del documento sea texto perfecto.
- **Diario Oficial nativo con tablas en imagen** (hallazgo de la revisión de Fase 3): documentos
  2017+ con veredicto TEXTO donde los encabezados de zona son texto pero los valores de la tabla
  son imagen. Si ves nombres de zona sin ningún número cerca en el texto extraído, es esto.
- **Decreto pegado**: un acto que "deja sin efecto X" puede promulgar OTRA modificación real en
  el mismo documento. Ya viene resuelto en `fase3_rangos.csv` (el rango ya apunta a lo correcto),
  pero si algo no cuadra, revisa si hay dos actos mezclados.
- Si la `nota_fase3` de tu ítem menciona una trampa específica de ESE documento, tómala como
  verdad — no la reinvestigues, solo transcribe lo que ya te dice dónde mirar.

## Delegación en agentes Sonnet (con las mismas reglas de silencio)

Lanza subagentes con la herramienta **Agent** (`model: "sonnet"`) para paralelizar:
- **Documentos de 1-2 páginas**: un agente puede resolver 3-4 de estos por sí solo.
- **Documentos largos (7+ páginas)**: un agente por documento, o divide por zona si son muchas.
Pide SIEMPRE que el subagente devuelva el Markdown ya formateado (o JSON con schema si prefieres
estructurar zona por zona) — nunca una explicación de lo que hizo. **Verifica tú** el Paso 4
(cobertura de zonas) antes de aceptar el resultado de un subagente y completar el registro — la
responsabilidad de lo que se registra es tuya, no del subagente.

## Criterios de calidad

- **Cobertura de zonas por encima de todo**: mejor una zona con valores en "No especificado" que
  una zona ausente del Markdown. Ver Paso 2.
- **No inventes valores.** Si un número es ilegible en el render, dilo en la tabla ("ilegible en
  el escaneo") y bájale la confianza — no interpoles ni asumas.
- **Un documento, un Markdown.** No fusiones varios documentos de la misma comuna en un solo
  archivo — eso es trabajo de una fase posterior que compara la ordenanza base con sus
  modificaciones.
- Usa `--nota` para dejar cualquier discrepancia entre lo que dice `nota_fase3` y lo que realmente
  viste — es la miga que evita que la próxima fase repita tu verificación.

## Ciclo de trabajo

```
estado --sesion <SESION>       (¿huérfanos míos? -> resolverlos EN SILENCIO)
-> imprime la línea de arranque
LOOP:
  tomar --sesion <SESION> --n 3
  si reclamados == 0: FIN -> informe final
  por cada documento: render -> enumerar zonas -> transcribir -> verificar -> completar/fallar
  cada 3 documentos: imprime la línea de avance (una sola línea)
```

## Informe final (lo único extenso que escribes)

```
<SESION> — FINALIZADA
Documentos procesados : <n>   (zonas transcritas: <n> | fallidos: <n>)
Fallidos: <id> — <motivo>            (uno por línea; omite si no hay)
Hallazgos: <patrones que afectan a la fase siguiente, trampas nuevas, comunas problemáticas>
```

Si no hay hallazgos, escribe `ninguno`. No resumas tu trabajo ni expliques tu método — el registro
ya lo tiene. **No corras `consolidar`** salvo que el tablero muestre 0 `EN_PROCESO` en TODAS las
sesiones — la consolidación es el cierre global de la fase.

---

## Para lanzar una sesión

1. Abre una sesión nueva de Claude Code en `C:\Users\gcastillo\Desktop\Ordenanzas`.
2. Pega TODO este documento.
3. Reemplaza las tres apariciones de `<SESION>` por tu identificador.
4. Vigila el avance global desde cualquier terminal con `python fase4_registro.py estado`.
