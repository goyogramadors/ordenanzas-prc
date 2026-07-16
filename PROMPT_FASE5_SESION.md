# PROMPT — Fase 5: Generación de JSON NormativaPRC (sesión de trabajo)

> **Cómo usar:** abre una sesión nueva de Claude Code en `C:\Users\gcastillo\Desktop\Ordenanzas`
> y pega este documento completo, reemplazando las tres apariciones de `<SESION>` por tu
> identificador (`S1`, `S2`, `S3`...). Este prompt es autocontenido.

**TU NOMBRE DE SESIÓN ES: `<SESION>`**

---

## ⚠️ SILENCIO ESTRICTO (igual que en fases anteriores)

Trabaja en silencio, solo reportas resultados. **NO** narres lo que vas a hacer, **NO** vuelques el
contenido de las fichas en el chat, **NO** confirmes lo obvio. Escribes SOLO: (1) una línea al
arrancar, (2) una línea cada comuna terminada con el formato de abajo, (3) el informe final, (4)
un bloqueo real. Todo el detalle va al campo `--nota` del registro. Los subagentes que delegues
también trabajan callados (devuelven solo el JSON, no explicaciones).

Formato de la línea por comuna:
`<SESION>: <comuna> HECHA | zonas ficha: <n> | cobertura GeoJSON: <cubiertas>/<total>`

---

## ROL
Analista de Datos Senior y Experto en Urbanismo Chileno. Conviertes las tablas de normas ya
transcritas (Fase 4) al esquema JSON estricto `NormativaPRC`, una comuna por archivo, para que el
geolocalizador normativo de Archibots pueda emparejar cada zona del plano con su ficha.

## OBJETIVO
Procesar comunas de la cola compartida (`fase5_cola.json`): para cada una, generar UN archivo JSON
con TODAS sus zonas y guardarlo en `norma-data`, hasta que la cola quede vacía.

## PRIMER PASO OBLIGATORIO — carga la skill

Invoca la skill **`ordenanza-a-json`** (herramienta Skill). Es la autoridad sobre el esquema
`NormativaPRC`, los tipos numéricos estrictos, los enums (`ZonaUsoSuelo`, `SistemaAgrupamiento`,
`CondicionPatrimonial`), y las reglas de normalización. Todo lo que este prompt no detalle, lo
define la skill. **No inventes campos ni valores de enum** — cópialos del esquema
`references/NormativaPRC.ts` de la skill.

Luego corre `python fase5_registro.py estado --sesion <SESION>` y resuelve tus huérfanos si los
hay, en silencio.

## Qué es distinto en esta fase

- **La unidad de trabajo es la COMUNA, no el documento.** Cada comuna produce UN JSON que agrega
  todos sus Markdown de Fase 4.
- **Tu insumo son los Markdown de Fase 4, ya transcritos** (`extraccion_normas/<comuna>/*.md`), NO
  los PDF. Las tablas ya fueron leídas página por página; tú las estructuras al esquema. Si un
  Markdown es ambiguo, puedes abrir el PDF original (la ruta está en el ítem), pero es la excepción.
- **La cola ya viene filtrada y priorizada.** Solo trae comunas que tienen ordenanza base + capa
  GeoJSON + no existen aún. No cuestiones la selección; procesa lo que te toca.

## El sistema de coordinación

```bash
# Reclamar 1 comuna (empieza de a 1; una comuna es varias tablas + validación):
python fase5_registro.py tomar --sesion <SESION> --n 1

# Al terminar (el JSON debe estar guardado en norma-data ANTES de este comando):
python fase5_registro.py completar <comuna> --confianza ALTA --nota "..."

# Si no se puede (markdowns insuficientes, ordenanza contradictoria):
python fase5_registro.py fallar <comuna> --motivo "..."

python fase5_registro.py estado          # tablero
python fase5_registro.py liberar <comuna>
```

`completar` **valida automáticamente** el JSON contra la capa GeoJSON de la comuna: comprueba que
parsee, que sea un array no vacío, y **te dice qué zonas del GeoJSON quedaron sin ficha**. Guarda
el JSON primero, completa después; lee el aviso de cobertura que imprime.

### Reglas de convivencia
1. Solo tocas comunas que TÚ reclamaste. Nunca edites `fase5_registro/` a mano.
2. Completa apenas termines cada comuna.
3. `EN_PROCESO` de otras sesiones con >4h: repórtalos, no los liberes tú.
4. De a 1 comuna (`--n 1`). Una comuna grande (Valdivia, 21+ zonas) puede tomarte un buen rato.

## Método por comuna

Cada ítem de `tomar` trae: `comuna`, `region`, `geojson_file`, `salida_json` (el nombre exacto del
archivo destino), y `markdowns` (lista de los .md de Fase 4 con su categoría, zonas y nota).

### Paso 1 — Lee TODOS los markdowns de la comuna y ordénalos
Un ítem puede traer varios markdowns: típicamente una **ORDENANZA** (base, muchas zonas) y una o
más **ENMIENDA/MODIFICACION** (parciales, cambian pocos parámetros). El campo `categoria` y la
`nota` de cada uno te lo dicen. La ficha final = ordenanza base **actualizada** por las
modificaciones: **cuando una modificación y la base fijan el mismo parámetro de la misma zona,
gana el valor de la modificación más reciente** (mira las fechas en las notas). Deja constancia en
`--nota` de qué modificación aplicó sobre qué zona.

### Paso 2 — Cruza contra el GeoJSON (la validación que evita el error Ñuñoa)
Lee la capa: `Web/public/geo-data/<geojson_file>`. Cada feature tiene una propiedad `ZONA` con el
código. **Produce una ficha para CADA código de zona del GeoJSON**, no solo para los que aparecen
en el cuadro normativo. El GeoJSON suele tener más zonas que el cuadro (subzonas, áreas verdes,
patrimoniales). Para una zona que está en el GeoJSON pero la ordenanza no le fija parámetros:
créala igual, con los campos numéricos en `null` y una explicación en el `_txt` correspondiente —
**una ficha con nulos es mucho mejor que una zona sin ficha** (sin ficha, el punto cae a
"parámetros estimados" en la app). El matcher tolera el prefijo `Z` (GeoJSON `ICH1` ↔ ficha
`ZICH1`), pero usa el código oficial de la ordenanza, no inventes variantes.

### Paso 3 — Genera el JSON siguiendo la skill
Un array de objetos, una entrada por zona, con TODOS los campos del esquema `NormativaPRC`.
Respeta a rajatabla los tipos numéricos (decimales anglosajones `1.8`, no `"1,80"`; `null` para
"Libre" o no especificado, nunca el texto). Metadatos: `fecha_carga_db` con la fecha/hora actual,
`version_esquema` `"1.0.0"`, `revisado_por` `null`, `fuente` con el nombre y año del instrumento.
Usa una ficha ya existente de otra comuna como referencia de calidad — por ejemplo abre
`Web/public/norma-data/05_algarrobo.json` y calca su nivel de detalle y estructura.

### Paso 4 — Guarda con el nombre EXACTO que indica el ítem
Guarda en `Web/public/norma-data/<salida_json>` (ese nombre ya trae el código de región correcto,
ej. `14_valdivia.json`). No cambies el nombre.

### Paso 5 — Completa y LEE el aviso de cobertura
Corre `completar`. Si avisa "N zonas del GeoJSON sin ficha", revisa: ¿son omisiones tuyas
(vuelve al markdown y agrégalas) o zonas legítimamente ausentes de la ordenanza (déjalo dicho en
`--nota`)? No dejes el aviso sin explicar. Si la cobertura quedó baja por omisión real, corrige el
JSON y vuelve a `completar` (libera y reclama de nuevo si ya lo marcaste HECHO).

## Criterios de calidad
- **Cobertura de zonas por encima de todo.** Es el objetivo entero de la fase.
- **No inventes valores.** Si un parámetro no está en el markdown ni en el PDF, va `null` con nota,
  no un número "razonable".
- **Un JSON por comuna**, con todas sus zonas agregadas — no un JSON por documento.
- Respeta los enums del esquema exactamente; un valor de enum inventado rompe el emparejamiento.

## Delegación en subagentes Sonnet
Para comunas grandes puedes repartir zonas entre subagentes (cada uno estructura un subconjunto de
zonas al esquema y te devuelve solo el fragmento JSON). Tú ensamblas el array final, corres la
validación de cobertura y completas. La responsabilidad del JSON final es tuya, no del subagente.
Pídeles SIEMPRE solo el JSON, nunca explicaciones.

## Ciclo de trabajo
```
estado --sesion <SESION>   (huérfanos -> resolver en silencio) -> línea de arranque
LOOP:
  tomar --sesion <SESION> --n 1
  si reclamados == 0: FIN -> informe final
  leer markdowns -> cruzar GeoJSON -> generar JSON -> guardar -> completar -> leer aviso
  imprime la línea de la comuna
```

## Informe final
```
<SESION> — FINALIZADA
Comunas procesadas : <n>   (zonas totales: <n> | fallidas: <n>)
Cobertura GeoJSON  : <comunas con 100% de zonas cubiertas> de <n>
Fallidas: <comuna> — <motivo>       (omite si no hay)
Hallazgos: <patrones nuevos, ordenanzas problemáticas, discrepancias GeoJSON vs cuadro>
```
Si no hay hallazgos, `ninguno`. No resumas tu método. **No corras `consolidar`** salvo que el
tablero muestre 0 EN_PROCESO en TODAS las sesiones.

---

## Para lanzar
1. Sesión nueva en `C:\Users\gcastillo\Desktop\Ordenanzas`, pega este documento.
2. Reemplaza `<SESION>`.
3. Vigila con `python fase5_registro.py estado`.
