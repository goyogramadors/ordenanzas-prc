# Cuadro Normativo por Zona — PRC Toltén, Localidades de Nueva Toltén y Villa Los Boldos (Diario Oficial Núm. 44.444)

**Fuente:** Diario Oficial de la República de Chile, Núm. 44.444, viernes 8 de mayo de 2026, páginas 12 a 16 de 20. CVE 2803330. Documento: "Promulgase el Plan Regulador Comunal de Tolten, localidades de Nueva Tolten y Villa Los Boldos" (nombre de archivo fuente; el número de decreto/resolución no es visible dentro del rango de páginas 12-16 entregado — aparecería en páginas anteriores del edicto, fuera de este material). Ordenanza Local, **Capítulo IV "Usos de Suelo, Zonificación, Áreas Restringidas al Desarrollo Urbano"**, **Artículo 7 "Normas específicas"** (más los Artículos 8 y 9, y el inicio del Capítulo V, contenidos en el mismo rango de páginas — ver "Nota de alcance").

**Archivo de origen (registro Fase 3/4):** `tolten_44444_promulgase_el_plan_regulador_comunal_de_tolten_localidades_de_nueva_tolten__download.aspx.pdf`, id `tolten_3f8d1ae78d`, rango de páginas útiles `[12, 16]`.

**Material fuente utilizado:** imágenes PNG renderizadas a 250dpi (`tolten_p12-16-12.png` a `tolten_p12-16-16.png`) como fuente primaria, con recortes ampliados (zoom 1.5x–2.5x) para cada tabla numérica y para los puntos de corte de página. El archivo de texto plano `tolten_p12-16.txt` se usó como apoyo y **se confirmó confiable**: a diferencia de otras comunas de este corpus (p. ej. Romeral, Caldera), aquí el `.txt` es texto nativo genuino — todos los valores de las tablas de "Usos de Suelo" y "Condiciones de Edificación y Subdivisión" están presentes como texto extraíble, no como imagen. Se contrastó cada valor numérico y cada celda del `.txt` contra el render visual y no se encontró ninguna discrepancia entre ambas fuentes en todo el rango. Adicionalmente, como verificación suplementaria fuera del rango formalmente asignado, se renderizaron **página 11** (para resolver con certeza la duda sobre la zona "ZM1", ver hallazgo 1 más abajo) y **página 17** (para confirmar el cierre del Capítulo IV y descartar contenido de zonas fuera de rango) directamente desde el PDF fuente (`Ordenanzas ordenadas/OCR ok/tolten_44444_...pdf`) con `pdftoppm -r 250`.

---

## Convenciones usadas en este documento

- **"Sin valor específico en la fuente"**: la celda aparece vacía en el original, o la fila/columna/tabla completa no existe para esa zona porque no aplica por diseño (p. ej. la Zona Área Verde no tiene fila de Densidad Bruta Máxima porque no admite uso residencial). Se explica el motivo en cada caso.
- **"Dato no determinable"**: reservado para valores que deberían existir pero no son legibles o no están en el corpus. **No fue necesario usarla ninguna vez en este documento** — el render a 250dpi es nítido y el texto es nativo; no se encontró ningún valor ilegible o ambiguo en las 5 páginas (ver "Notas finales de verificación").
- **Celdas combinadas (colspan) en las tablas "Condiciones de Edificación y Subdivisión"**: cuando la fuente presenta un único valor centrado que abarca dos o más columnas de uso (p. ej. "Residencial" y "Otros Usos" comparten el mismo Coeficiente de Ocupación del Suelo), este documento repite el valor en cada columna de la tabla Markdown correspondiente y lo marca explícitamente como *(valor único, celda combinada en la fuente)* la primera vez que aparece en cada tabla — Markdown no soporta colspan. Esta situación **varía de zona a zona** en este documento (ver detalle por zona) y no se homogeneizó entre zonas.
- Las columnas **"Área Verde"** y **"Espacio Público"** de las tablas de condiciones son, en la fuente, una única celda combinada verticalmente que abarca **todas** las filas de la tabla (Superficie hasta Densidad Bruta Máxima), con el mismo texto boilerplate en las cinco zonas que la tienen (ZMC, ZM2, ZM3, ZM4, ZE): *"Aplica Art. 2.1.31 de la O.G.U y C."* (Área Verde) y *"Aplica Art. 2.1.30 de la O.G.U y C."* (Espacio Público). Para no repetir un bloque de texto idéntico fila por fila, este documento lo transcribe **una sola vez como nota debajo de cada tabla** en lugar de como columnas Markdown — se documenta aquí explícitamente para que quede claro que no es una omisión.
- Se preservan literalmente las erratas, abreviaturas e inconsistencias tipográficas de la fuente (espaciado de "mts", uso de "m2" en vez de "m²", separador de miles inconsistente, comas variables), marcadas **[sic]** cuando corresponde, con nota explicativa. **Cuidado especial**: cada valor numérico de este documento fue verificado con zoom contra la imagen (no solo contra el `.txt`) para descartar errores de "auto-corrección" (comas decimales, unidades, cifras redondeadas a un valor "más común").
- Los códigos de zona se citan tal como aparecen en la fuente: `ZMC`, `ZM2`, `ZM3`, `ZM4`, `ZE`, `ZAV` (sin guion, a diferencia de otras comunas del corpus que usan `Z-1`, `ZU-1`, etc.).

---

## Nota de alcance y verificación de la lista de zonas (Artículo 6)

**¿Qué hay inmediatamente antes de ZMC en la página 12?** La página 12 **no** comienza con la zona ZMC. Comienza con la parte final de una tabla de identificación de zonas por localidad (encabezado "LOCALIDAD | ZONA URBANA") que **continúa desde la página 11** (fuera del rango entregado) sin repetir el encabezado de la tabla ni el nombre de "Nueva Toltén". Recién después de esa tabla viene el título "Artículo 7. Normas específicas" (párrafo introductorio) y luego el título "ZONA MIXTA CENTRO (ZMC)". Ver la sección siguiente para el detalle completo de esta tabla, incluida la verificación suplementaria de la página 11.

**¿Qué hay inmediatamente después de ZAV, y termina el Capítulo IV en la página 16?** Después de completarse la tabla de "NORMA URBANÍSTICA" de ZAV (última de las 6 zonas), la página 16 continúa **dentro del mismo rango entregado** con: el párrafo estándar de áreas de riesgo para ZAV; el **Artículo 8** completo ("Áreas restringidas al desarrollo urbano: Áreas de Riesgo", definiciones AR-1 a AR-4); el **Artículo 9** completo ("Áreas de protección de recursos de valor patrimonial cultural", un inmueble: Parroquia San Antonio); y el **inicio del Capítulo V "VIALIDAD"** (título del capítulo + título del Artículo 10 "De la Red Vial Pública" + un párrafo introductorio), que se corta a media oración ("...según se detalla en los siguientes cuadros de vialidad.") justo al terminar la página 16. Es decir: el Capítulo IV (zonas + áreas de riesgo + patrimonio) **sí termina completo dentro de la página 16**; lo que continúa en la página 17 (fuera de rango, verificado como comprobación suplementaria) son exclusivamente los cuadros de vialidad del Artículo 10.1 (Red Vial Existente y Red Vial Colectora de Nueva Toltén) — **no hay zonas adicionales ni normas de edificación fuera del rango 12-16.**

**Verificación de "trampa comuna ajena":** no se detectó ningún contenido ajeno a Toltén en el rango 12-16 ni en las páginas 11 y 17 usadas como verificación suplementaria. El encabezado de Diario Oficial (Núm. 44.444, viernes 8 de mayo de 2026), el CVE 2803330 y el pie de página (Director Giovanni Calderón Bassi) son idénticos y consistentes en las 7 páginas revisadas (11 a 17); todo el contenido sustantivo se refiere a Nueva Toltén y Villa Los Boldos.

---

## Artículo 6 (verificación suplementaria, página 11) + continuación en página 12 — Identificación de zonas por localidad

**Nota metodológica:** esta tabla pertenece formalmente al Artículo 6 (no al Artículo 7, que es el asignado a esta tarea), y su inicio está en la página 11, fuera del rango 12-16 entregado. Se incluye aquí completa porque es la única forma de **verificar con certeza directa** (no solo por inferencia) si existe o no una zona "ZM1" — la duda explícita planteada para esta tarea. Se renderizó la página 11 del PDF fuente como paso adicional de verificación.

Página 11 — Artículo 6. Zonificación (texto introductorio): *"Para el área urbana de las localidades de Nueva Toltén y Villa Los Boldos se definen las siguientes zonas, graficadas en los planos, Nueva Toltén PRC-09118-1 y Villa Los Boldos PRC-09118-2:"*

| Localidad | Zona urbana | Código |
|---|---|---|
| Nueva Toltén | Zona Mixta Centro | **ZMC** |
| Nueva Toltén | Zona Mixta 2 Alta Densidad | **ZM2** |
| *(cont. p.12, sin repetir "Nueva Toltén")* | Zona Mixta 3 Media Densidad | **ZM3** |
| *(íd.)* | Zona Mixta 4 Baja Densidad | **ZM4** |
| *(íd.)* | Zona Equipamiento | **ZE** |
| *(íd.)* | Zona Área Verde | **ZAV** |
| Villa Los Boldos | Zona Mixta 2 Alta Densidad | **ZM2** |
| Villa Los Boldos | Zona Mixta 3 Media Densidad | **ZM3** |
| Villa Los Boldos | Zona Mixta 4 Baja Densidad | **ZM4** |
| Villa Los Boldos | Zona Área Verde | **ZAV** |

**Hallazgo 1 — resuelto con certeza: no existe zona "ZM1".** La tabla, vista completa (p.11+p.12), confirma que para Nueva Toltén la secuencia es **ZMC → ZM2 → ZM3 → ZM4 → ZE → ZAV**, sin ningún salto de página perdido entre ZMC y ZM2 (ambas están en la misma página 11, filas consecutivas). No se trata de una zona faltante ni de un error de Fase 3: **este PRC específico (Nueva Toltén / Villa Los Boldos) simplemente no tiene una zona llamada "ZM1"** — la numeración de las zonas mixtas por densidad empieza en "ZM2" (Alta Densidad), y la zona central de mayor intensidad se llama "ZMC" (Zona Mixta Centro) en vez de "ZM1". Esto se confirma también por exclusión: las 6 zonas mencionadas por Fase 3 (ZMC, ZM2, ZM3, ZM4, ZE, ZAV) son exactamente las 6 que trae el Artículo 7, ni más ni menos, y ninguna sección del documento (páginas 11-17 revisadas) menciona "ZM1". **Aclaración importante para no confundir con otro documento de este mismo corpus:** existe un PRC *distinto* de Toltén — para las localidades de **Queule y Villa O'Higgins** (Decreto MINVU N°7/2012, ya transcrito en `tolten_7_prc_queule_villa_ohiggins.md` de esta misma carpeta) — cuyo esquema de zonificación **sí incluye una "ZM-1"** (junto con Z-1, Z-2, Z-3, ZE-1, ZE-2, ZAV). Son dos instrumentos de planificación distintos, para localidades distintas de la misma comuna, con esquemas de nomenclatura de zonas independientes entre sí; no es una inconsistencia sino dos PRC parciales distintos.

**Villa Los Boldos** tiene 4 zonas (ZM2, ZM3, ZM4, ZAV) — no tiene ZMC ni ZE. Esto es consistente con el texto de cada zona en el Artículo 7 (ver más abajo), **con una excepción**: ver "Hallazgo 2" en la sección de discrepancias, sobre la zona ZAV.

---

## ZMC — Zona Mixta Centro
*(página 12 — cuadro completo: Usos de Suelo + Condiciones de Edificación y Subdivisión, ambos en la misma página, sin partición)*

Zona presente en la localidad de Nueva Toltén.

### Usos de suelo

| Categoría | Ítem | Permitido / Prohibido |
|---|---|---|
| RESIDENCIAL | Vivienda | Permitido |
| RESIDENCIAL | Hospedaje | Permitido |
| EQUIPAMIENTO | Científico | Permitido |
| EQUIPAMIENTO | Comercio | Permitido, excepto estaciones o centros de servicio automotor y discotecas |
| EQUIPAMIENTO | Culto y Cultura | Permitido |
| EQUIPAMIENTO | Deporte | Permitido, excepto estadios, medialuna y autódromos. |
| EQUIPAMIENTO | Educación | Permitido |
| EQUIPAMIENTO | Salud | Permitido excepto hospital, centros de rehabilitación, cementerio y crematorio. |
| EQUIPAMIENTO | Seguridad | Permitido, excepto cárceles, centros de detención, centros de internación provisoria, centros de privación de libertad y recintos militares. |
| EQUIPAMIENTO | Servicios | Permitido |
| EQUIPAMIENTO | Social | Permitido |
| INFRAESTRUCTURA | Transporte | Permitido |
| ACTIVIDADES PRODUCTIVAS | *(sin ítem específico)* | Todo prohibido |
| ESPACIO PÚBLICO | *(sin ítem específico)* | Permitido solo lo indicado en el artículo 2.1.30 de la O.G.U y C. |
| ÁREAS VERDES | *(sin ítem específico)* | Permitido solo lo indicado en el artículo 2.1.31 de la O.G.U y C. |
| USOS DE SUELO PROHIBIDOS | *(sin ítem específico)* | Todos los no señalados como permitidos. |

*Nota: "Salud" es la única fila de ZMC sin coma después de "Permitido" ("Permitido excepto..." en vez de "Permitido, excepto..."); se verificó con zoom 2.3x contra el original — no es un error de transcripción, así aparece literalmente en la fuente.*

### Condiciones de edificación y subdivisión

| Norma | Residencial | Otros usos |
|---|---|---|
| Superficie de subdivisión predial mínima (m2) | 200 *(valor único, celda combinada en la fuente)* | 200 |
| Coeficiente de ocupación del suelo | 0,6 | 0,8 |
| Coeficiente de constructibilidad | 2,4 | 3,2 |
| Altura máxima de edificación (m) | 12 | 12 |
| Sistema agrupamiento | Continuo, Aislado y Pareado *(valor único, celda combinada)* | Continuo, Aislado y Pareado |
| Antejardín (m) | 0 *(valor único, celda combinada)* | 0 |
| Densidad Bruta Máxima (hab/Há) | 1000 | No aplica |

Área Verde: Aplica Art. 2.1.31 de la O.G.U y C. — Espacio Público: Aplica Art. 2.1.30 de la O.G.U y C. *(columnas combinadas verticalmente en toda la tabla, ver Convenciones)*

**Nota:** ZMC es la única de las 6 zonas **sin** párrafo de "áreas de riesgo AR-" a continuación de su tabla — la página 12 termina inmediatamente después de esta tabla y la página 13 comienza directamente con el título de ZM2. Se verificó que no falta contenido en el corte: el pie de página de Diario Oficial aparece completo después de la tabla en la página 12. Ver "Hallazgo 5" en la sección de Discrepancias y hallazgos, más abajo.

---

## ZM2 — Zona Mixta 2 Alta Densidad
*(página 13 — cuadro completo: Usos de Suelo + Condiciones de Edificación y Subdivisión, ambos en la misma página, sin partición)*

Zona presente en las localidades de Nueva Toltén y Villa Los Boldos.

### Usos de suelo

| Categoría | Ítem | Permitido / Prohibido |
|---|---|---|
| RESIDENCIAL | Vivienda | Permitido |
| RESIDENCIAL | Hospedaje | Permitido |
| EQUIPAMIENTO | Científico | Permitido |
| EQUIPAMIENTO | Comercio | Permitido, excepto discotecas |
| EQUIPAMIENTO | Culto y Cultura | Permitido |
| EQUIPAMIENTO | Deporte | Permitido, excepto estadios, autódromos y medialuna |
| EQUIPAMIENTO | Educación | Permitido |
| EQUIPAMIENTO | Salud | Permitido excepto cementerio y crematorio |
| EQUIPAMIENTO | Seguridad | Permitido, excepto cárceles, centros de detención, centros de internación provisoria, centros de privación de libertad y recintos militares |
| EQUIPAMIENTO | Servicios | Permitido |
| EQUIPAMIENTO | Social | Permitido |
| INFRAESTRUCTURA | Transporte | Permitido |
| ACTIVIDADES PRODUCTIVAS | *(sin ítem específico)* | Todo prohibido |
| ESPACIO PÚBLICO | *(sin ítem específico)* | Permitido solo lo indicado en el artículo 2.1.30 de la O.G.U y C. |
| ÁREAS VERDES | *(sin ítem específico)* | Permitido solo lo indicado en el artículo 2.1.31 de la O.G.U y C. |
| USOS DE SUELO PROHIBIDOS | *(sin ítem específico)* | Todos los no señalados como permitidos. |

*Nota comparativa con ZMC: el orden de la excepción de Deporte se invierte ("autódromos y medialuna" vs. "medialuna y autódromos" en ZMC) y ninguna fila de ZM2 lleva punto final, a diferencia de varias filas de ZMC — inconsistencia tipográfica de la fuente, transcrita literalmente.*

### Condiciones de edificación y subdivisión

**Nota de estructura — distinta de ZMC:** en esta tabla las columnas de la fuente no son "Residencial" y "Otros Usos" separadas; son **"Residencial / Otros Usos" fusionada como una sola columna**, y **"Equipamiento - Salud"** como la otra (es decir, aquí lo que se diferencia no es "vivienda vs. otros usos" sino "todo uso general vs. equipamiento de salud específicamente", que tiene parámetros más permisivos). Se verificó con zoom 1.9x contra el original.

| Norma | Residencial / Otros usos | Equipamiento - Salud |
|---|---|---|
| Superficie de subdivisión predial mínima (m2) | 200 *(valor único, celda combinada)* | 200 |
| Coeficiente de ocupación del suelo | 0,6 | 0,8 |
| Coeficiente de constructibilidad | 1,8 | 3,2 |
| Altura máxima de edificación (m) | 9 | 12 |
| Sistema agrupamiento | Continuo, Aislado y Pareado *(valor único, celda combinada)* | Continuo, Aislado y Pareado |
| Antejardín (m) | 3 mts *(valor único, celda combinada; sin punto final — distinto de ZM3/ZM4/ZE, ver Notas finales)* | 3 mts |
| Densidad Bruta Máxima (hab/Há) | 800 | No aplica |

Área Verde: Aplica Art. 2.1.31 de la O.G.U y C. — Espacio Público: Aplica Art. 2.1.30 de la O.G.U y C. *(columnas combinadas verticalmente)*

**Áreas de riesgo:** *"Para autorizar proyectos en terrenos que estén bajo las áreas de riesgo AR-2, a que se refiere el artículo 8 de esta Ordenanza Local, se requerirá dar cumplimiento a lo señalado en la Ordenanza General de Urbanismo y Construcciones. Las normas urbanísticas aplicables a dichos proyectos, serán las establecidas para la presente zona una vez que cumplan con los requisitos establecidos en la normativa vigente."* (solo AR-2; párrafo completo dentro de la página 13, sin partición)

---

## ZM3 — Zona Mixta 3 Media Densidad
*(usos de suelo: comienza en página 13, **continúa en página 14 sin repetir el título de zona ni el encabezado de tabla**; condiciones de edificación y subdivisión: completa en página 14)*

Zona presente en las localidades de Nueva Toltén y Villa Los Boldos.

### Usos de suelo

**Patrón de partición de tabla (según lo anticipado por la instrucción de la tarea):** la tabla "USOS DE SUELO" de ZM3 se corta entre las páginas 13 y 14. La página 13 termina en la fila "Educación | Permitido"; la página 14 continúa directamente con la fila "Salud" — sin repetir "ZONA MIXTA 3 MEDIA DENSIDAD (ZM3)", sin repetir el encabezado "USOS DE SUELO / TIPO DE USO", y sin repetir el subtítulo "EQUIPAMIENTO". Se verificó con zoom que no se perdió ninguna fila en el corte.

| Categoría | Ítem | Permitido / Prohibido | Página |
|---|---|---|---|
| RESIDENCIAL | Vivienda | Permitido | 13 |
| RESIDENCIAL | Hospedaje | Permitido | 13 |
| EQUIPAMIENTO | Científico | Permitido | 13 |
| EQUIPAMIENTO | Comercio | Permitido, excepto estaciones o centros de servicio automotor y discotecas | 13 |
| EQUIPAMIENTO | Culto y Cultura | Permitido | 13 |
| EQUIPAMIENTO | Deporte | Permitido | 13 |
| EQUIPAMIENTO | Educación | Permitido | 13 *(← corte de página aquí)* |
| EQUIPAMIENTO | Salud | Permitido excepto cementerio y crematorio. | 14 |
| EQUIPAMIENTO | Seguridad | Permitido, excepto cárceles, centros de detención, centros de internación provisoria, centros de privación de libertad y recintos militares. | 14 |
| EQUIPAMIENTO | Servicios | Permitido | 14 |
| EQUIPAMIENTO | Social | Permitido | 14 |
| INFRAESTRUCTURA | Transporte | Permitido | 14 |
| ACTIVIDADES PRODUCTIVAS | Industrias inofensivas | Permitido | 14 |
| ESPACIO PÚBLICO | *(sin ítem específico)* | Permitido solo lo indicado en el artículo 2.1.30 de la O.G.U y C. | 14 |
| ÁREAS VERDES | *(sin ítem específico)* | Permitido solo lo indicado en el artículo 2.1.31 de la O.G.U y C. | 14 |
| USOS DE SUELO PROHIBIDOS | *(sin ítem específico)* | Todos los no señalados como permitidos. | 14 |

*Nota: a diferencia de ZMC y ZM2, "Deporte" en ZM3 no tiene ninguna excepción listada (solo "Permitido"); y "Actividades Productivas" pasa de "Todo prohibido" (ZMC/ZM2) a permitir "Industrias inofensivas" — primera zona de las 6 que admite actividad productiva.*

### Condiciones de edificación y subdivisión
*(completa en página 14, sin partición)*

| Norma | Residencial | Otros usos | Actividad productiva |
|---|---|---|---|
| Superficie de subdivisión predial mínima (m2) | 150 *(valor único, celda combinada en las 3 columnas)* | 150 | 150 |
| Coeficiente de ocupación del suelo | 0,6 | 0,4 | 0,4 |
| Coeficiente de constructibilidad | 1,8 | 1,2 | 1,2 |
| Altura máxima de edificación (m) | 9 | 9 | 9 |
| Sistema agrupamiento | Aislado y Pareado *(valor único, celda combinada en las 3 columnas)* | Aislado y Pareado | Aislado y Pareado |
| Antejardín (m) | 3 mts. *(valor único, celda combinada en las 3 columnas; con punto final)* | 3 mts. | 3 mts. |
| Densidad Bruta Máxima (hab/Há) | 500 | No aplica *(celda combinada Otros Usos + Actividad Productiva)* | No aplica |

Área Verde: Aplica Art. 2.1.31 de la O.G.U y C. — Espacio Público: Aplica Art. 2.1.30 de la O.G.U y C. *(columnas combinadas verticalmente)*

**Áreas de riesgo:** *"Para autorizar proyectos en terrenos que estén bajo las áreas de riesgo AR-2..."* (idéntico patrón de texto que ZM2, solo AR-2; párrafo completo dentro de la página 14, sin partición)

---

## ZM4 — Zona Mixta 4 Baja Densidad
*(usos de suelo: comienza en página 14, **continúa en página 15 sin repetir el título de zona ni el encabezado de tabla**; condiciones de edificación y subdivisión: completa en página 15)*

Zona presente en las localidades de Nueva Toltén y Villa Los Boldos.

### Usos de suelo

**Patrón de partición de tabla:** igual fenómeno que ZM3, en el corte entre páginas 14 y 15. La página 14 termina en la fila "ESPACIO PÚBLICO"; la página 15 continúa directamente con "ÁREAS VERDES" y "USOS DE SUELO PROHIBIDOS" — sin repetir título de zona ni encabezados de tabla.

| Categoría | Ítem | Permitido / Prohibido | Página |
|---|---|---|---|
| RESIDENCIAL | Vivienda | Permitido | 14 |
| RESIDENCIAL | Hospedaje | Permitido | 14 |
| EQUIPAMIENTO | Científico | Permitido | 14 |
| EQUIPAMIENTO | Comercio | Permitido | 14 |
| EQUIPAMIENTO | Culto y Cultura | Permitido | 14 |
| EQUIPAMIENTO | Deporte | Permitido | 14 |
| EQUIPAMIENTO | Educación | Permitido | 14 |
| EQUIPAMIENTO | Salud | Permitido, excepto cementerio y crematorio. | 14 |
| EQUIPAMIENTO | Seguridad | Permitido, excepto cárceles, centros de detención, centros de internación provisoria, centros de privación de libertad y recintos militares. | 14 |
| EQUIPAMIENTO | Servicios | Permitido | 14 |
| EQUIPAMIENTO | Social | Permitido | 14 |
| INFRAESTRUCTURA | Transporte | Permitido | 14 |
| INFRAESTRUCTURA | Sanitaria | Permitido | 14 |
| INFRAESTRUCTURA | Energía | Permitido | 14 |
| ACTIVIDADES PRODUCTIVAS | Industrias inofensivas | Permitido | 14 |
| ESPACIO PÚBLICO | *(sin ítem específico)* | Permitido solo lo indicado en el artículo 2.1.30 de la O.G.U y C. | 14 *(← corte de página aquí)* |
| ÁREAS VERDES | *(sin ítem específico)* | Permitido solo lo indicado en el artículo 2.1.31 de la O.G.U y C. | 15 |
| USOS DE SUELO PROHIBIDOS | *(sin ítem específico)* | Todos los no señalados como permitidos. | 15 |

*Nota: "Salud" en ZM4 sí lleva coma ("Permitido, excepto...") — a diferencia de ZMC, ZM2 y ZM3, que no la llevan. Verificado con zoom 2.3x; no es un error de transcripción, es una inconsistencia real de puntuación de la fuente. ZM4 es también la única de las 6 zonas con dos ítems de INFRAESTRUCTURA adicionales (Sanitaria, Energía) más allá de Transporte.*

### Condiciones de edificación y subdivisión
*(completa en página 15, sin partición)*

**Nota de estructura — distinta de ZMC/ZM2/ZM3:** en ZM4, el Coeficiente de Ocupación del Suelo, el Coeficiente de Constructibilidad y la Altura Máxima son **valores únicos** (celda combinada Residencial + Otros Usos), no valores distintos por columna como en las tres zonas anteriores. Solo la Densidad Bruta Máxima distingue Residencial de Otros Usos. Verificado con zoom 1.8x.

| Norma | Residencial | Otros usos |
|---|---|---|
| Superficie de subdivisión predial mínima (m2) | 200 *(valor único, celda combinada)* | 200 |
| Coeficiente de ocupación del suelo | 0,4 *(valor único, celda combinada)* | 0,4 |
| Coeficiente de constructibilidad | 0,8 *(valor único, celda combinada)* | 0,8 |
| Altura máxima de edificación (m) | 6 *(valor único, celda combinada)* | 6 |
| Sistema agrupamiento | Aislado y Pareado *(valor único, celda combinada)* | Aislado y Pareado |
| Antejardín (m) | 3mts. *(valor único, celda combinada; sin espacio entre "3" y "mts.", con punto final — [sic], distinto de "3 mts" de ZM2 y "3 mts." de ZM3)* | 3mts. |
| Densidad Bruta Máxima (hab/Há) | 250 | No aplica |

Área Verde: Aplica Art. 2.1.31 de la O.G.U y C. — Espacio Público: Aplica Art. 2.1.30 de la O.G.U y C. *(columnas combinadas verticalmente)*

**Áreas de riesgo:** *"Para autorizar proyectos en terrenos que estén bajo las áreas de riesgo AR-1 y AR-2..."* (AR-1 y AR-2; párrafo completo dentro de la página 15, sin partición)

---

## ZE — Zona Equipamiento
*(página 15 — cuadro completo: Usos de Suelo + Condiciones de Edificación y Subdivisión, ambos en la misma página, sin partición; solo el párrafo de áreas de riesgo que sigue se corta hacia la página 16, ver más abajo)*

Zona presente en la localidad de Nueva Toltén.

### Usos de suelo

**Nota de estructura — distinta de las 4 zonas mixtas anteriores:** ZE es la única zona con uso residencial permitido (Vivienda, Hospedaje) que **no** tiene fila "Científico", ni "Educación", ni "Salud", ni "Seguridad", ni "Servicios" bajo EQUIPAMIENTO — y en cambio agrega "Esparcimiento", que no aparece en ninguna de las 4 zonas mixtas. Se verificó con zoom que la tabla efectivamente no tiene esas filas (no es un corte de página perdido: el resto de la tabla en la misma página está completo, con los subtítulos INFRAESTRUCTURA/ACTIVIDADES PRODUCTIVAS/ESPACIO PÚBLICO/ÁREAS VERDES/USOS DE SUELO PROHIBIDOS todos presentes y completos).

| Categoría | Ítem | Permitido / Prohibido |
|---|---|---|
| RESIDENCIAL | Vivienda | Permitido |
| RESIDENCIAL | Hospedaje | Permitido |
| EQUIPAMIENTO | Comercio | Permitido, excepto term. de distribución, grandes tiendas. |
| EQUIPAMIENTO | Culto y Cultura | Permitido |
| EQUIPAMIENTO | Deporte | Permitido, excepto estadios, centros deportivos, medialunas y gimnasios. |
| EQUIPAMIENTO | Esparcimiento | Permitido |
| EQUIPAMIENTO | Social | Permitido |
| INFRAESTRUCTURA | *(sin ítem específico)* | Todo Prohibido |
| ACTIVIDADES PRODUCTIVAS | *(sin ítem específico)* | Todo Prohibido |
| ESPACIO PÚBLICO | *(sin ítem específico)* | Permitido solo lo indicado en el artículo 2.1.30 de la O.G.U y C. |
| ÁREAS VERDES | *(sin ítem específico)* | Permitido solo lo indicado en el artículo 2.1.31 de la O.G.U y C. |
| USOS DE SUELO PROHIBIDOS | *(sin ítem específico)* | Todos los no señalados como permitidos. |

*Nota sobre "term.": abreviatura literal de la fuente en la fila Comercio ("term. de distribución"), probablemente por "terminales de distribución"; se transcribe tal cual, sin expandir, porque no hay forma de confirmar la expansión exacta dentro del rango de páginas entregado. Verificado con zoom 2.15x — la abreviatura con punto es real, no es un artefacto de renderizado.*

### Condiciones de edificación y subdivisión

**Nota de estructura:** igual que ZM4, el COS, el CC y la Altura Máxima son valores únicos (celda combinada Residencial + Equipamiento), no valores distintos por columna.

| Norma | Residencial | Equipamiento |
|---|---|---|
| Superficie de subdivisión predial mínima (m2) | 1000 *(valor único, celda combinada — [sic] sin separador de miles, a diferencia de ZAV que usa "2.000"; ver Notas finales)* | 1000 |
| Coeficiente de ocupación del suelo | 0,3 *(valor único, celda combinada)* | 0,3 |
| Coeficiente de constructibilidad | 0,9 *(valor único, celda combinada)* | 0,9 |
| Altura máxima de edificación (m) | 9 *(valor único, celda combinada)* | 9 |
| Sistema agrupamiento | Aislado *(valor único, celda combinada)* | Aislado |
| Antejardín (m) | 3mts. *(valor único, celda combinada; sin espacio, con punto — mismo patrón que ZM4)* | 3mts. |
| Densidad Bruta Máxima (hab/Há) | 250 | No aplica |

Área Verde: Aplica Art. 2.1.31 de la O.G.U y C. — Espacio Público: Aplica Art. 2.1.30 de la O.G.U y C. *(columnas combinadas verticalmente)*

**Áreas de riesgo (párrafo partido entre páginas 15 y 16):** *"Para autorizar proyectos en terrenos que estén bajo las áreas de riesgo AR-1, AR-3, a que se refiere el artículo 8 de esta Ordenanza Local, se requerirá dar cumplimiento a lo señalado en la Ordenanza General de Urbanismo y Construcciones. Las normas urbanísticas aplicables a dichos proyectos,"* [corte de página 15→16] *"serán las establecidas para la presente zona una vez que cumplan con los requisitos establecidos en la normativa vigente."* — Nota: la fuente escribe "AR-1, AR-3" con coma, no "AR-1 y AR-3" como sería consistente con la redacción "AR-1 y AR-2" usada para ZM4; inconsistencia menor de redacción, transcrita literalmente. Este es el único caso, dentro del rango 12-16, de un párrafo (no una tabla de normas) partido entre dos páginas.

---

## ZAV — Zona Área Verde
*(página 16 — cuadro completo, sin partición)*

Zona presente en la localidad de Nueva Toltén. *(Ver Hallazgo 2 — discrepancia con la tabla de identificación de zonas del Artículo 6, que también lista ZAV para Villa Los Boldos.)*

Texto introductorio propio de esta zona (no presente en las otras 5): *"En esta zona aplican las disposiciones establecidas en la Ordenanza General de Urbanismo y Construcciones, además de las siguientes normas urbanísticas."*

### Usos de suelo

**Nota de estructura — la más simple de las 6 zonas:** ZAV es la única zona sin desglose por categorías (RESIDENCIAL/EQUIPAMIENTO/INFRAESTRUCTURA/etc.). Solo tiene dos filas:

| Categoría | Permitido / Prohibido |
|---|---|
| USOS DE SUELO PERMITIDOS | Según art. 2.1.31 de la O.G.U. y C. |
| USOS DE SUELO PROHIBIDOS | Todos los no señalados como permitidos. |

### Norma urbanística
*(la fuente titula esta tabla "NORMA URBANÍSTICA", no "CONDICIONES DE EDIFICACIÓN Y SUBDIVISIÓN" como las otras 5 zonas — único caso en el documento)*

**Nota de estructura:** tabla de una sola columna de uso ("Equipamiento"), sin columnas "Área Verde" ni "Espacio Público" (no aplican — esta zona es en sí misma la referencia de área verde para las demás), y **sin fila de Densidad Bruta Máxima** (no admite uso residencial).

| Norma | Equipamiento |
|---|---|
| Superficie de subdivisión predial mínima (m2) | 2.000 |
| Coeficiente de ocupación del suelo | 0,2 |
| Coeficiente de constructibilidad | 0,1 |
| Altura máxima de edificación (m) | 7 |
| Sistema agrupamiento | Aislado |
| Antejardín (m) | 10 |
| Densidad Bruta Máxima (hab/Há) | **Sin valor específico en la fuente** (fila ausente en la tabla; no aplica — zona sin uso residencial) |

**Áreas de riesgo:** *"Para autorizar proyectos en terrenos que estén bajo las áreas de riesgo AR-1, AR-2, AR-3, AR-4, a que se refiere el artículo 8 de esta Ordenanza Local..."* — la única de las 6 zonas afectada por las 4 áreas de riesgo simultáneamente (párrafo completo dentro de la página 16, sin partición).

---

## Artículo 8. Áreas restringidas al desarrollo urbano: Áreas de Riesgo
*(página 16, transcripción completa — referenciado por todas las zonas excepto ZMC)*

> "En el presente Plan, se constituyen las siguientes áreas de riesgo:"

| Código | Descripción |
|---|---|
| AR-1 | Zona inundable por cercanía a río |
| AR-2 | Zona potencialmente inundable por napa freática |
| AR-3 | Zona potencialmente inundable por cercanía a río |
| AR-4 | Zona inundable por napa freática. |

> "Para autorizar proyectos en estas áreas, se requerirá dar cumplimiento a lo establecido en el artículo 2.1.17. de la Ordenanza General de Urbanismo y Construcciones. Las normas urbanísticas aplicables serán las establecidas en el artículo 7 de esta Ordenanza Local."

*Nota: obsérvese la similitud casi especular entre AR-1 ("inundable por cercanía a río") / AR-3 ("potencialmente inundable por cercanía a río") y AR-2 ("potencialmente inundable por napa freática") / AR-4 ("inundable por napa freática") — dos pares de causas (río / napa freática) cruzados con dos niveles de certeza (confirmado / potencial). Se transcribe literal; no es un error, es el diseño de la clasificación.*

## Artículo 9. Áreas de protección de recursos de valor patrimonial cultural
*(página 16, transcripción completa)*

Un solo inmueble de conservación histórica identificado:

| # | Inmueble | Dirección | Rol de avalúo |
|---|---|---|---|
| 1 | Parroquia San Antonio | O'Higgins #440 | 54-2 |

> "Las condiciones de edificación para los Inmuebles de Conservación Histórica, serán las establecidas en la Zona ZMC."

## Inicio del Capítulo V — fuera de alcance de esta tarea
*(página 16, últimas líneas del rango entregado)*

Título "CAPÍTULO V VIALIDAD" y "Artículo 10. De la Red Vial Pública", con un párrafo introductorio que se corta al final de la página 16: *"La red vial estructurante del Plan está conformada por las vías existentes y proyectadas de las localidades de Nueva Toltén y Villa Los Boldos según se detalla en los siguientes cuadros de vialidad."* Los cuadros mismos (Red Vial Existente y Red Vial Colectora, Artículo 10.1 Localidad de Nueva Toltén) están en la página 17, confirmados como puramente viales (nombre de vía, tramo desde/hasta, ancho, clasificación OGUC) mediante render de verificación suplementaria — no contienen normas de zona ni contenido ajeno a Toltén. No se transcriben en detalle por estar fuera del alcance de esta tarea (zonas del Artículo 7).

---

## Discrepancias y hallazgos respecto de la nota de Fase 3

1. **Conteo y códigos de zona: confirmados exactamente, sin discrepancia — y la duda sobre "ZM1" queda resuelta con evidencia directa, no solo inferencia.** Las 6 zonas (ZMC, ZM2, ZM3, ZM4, ZE, ZAV) existen exactamente como las listó Fase 3, con los mismos códigos. Mediante verificación suplementaria de la página 11 (fuera del rango asignado, pero renderizada expresamente para resolver esta duda) se confirmó que la tabla de identificación de zonas del Artículo 6 pasa directo de ZMC a ZM2 para Nueva Toltén, sin ningún salto de página que pudiera esconder una zona "ZM1" perdida. No existe zona ZM1 en este instrumento — es una característica de diseño de la nomenclatura (zona central = "ZMC", zonas mixtas por densidad numeradas 2/3/4), no un error ni de la fuente ni de Fase 3. Se documenta además que existe otro PRC de la misma comuna de Toltén (localidades de Queule y Villa O'Higgins, ya transcrito en `tolten_7_prc_queule_villa_ohiggins.md`) que sí tiene una zona "ZM-1" — son instrumentos y esquemas de zonificación independientes, para no generar confusión al consolidar ambos archivos de la carpeta `tolten/`.

2. **Hallazgo nuevo, no mencionado por Fase 3 — inconsistencia interna de la fuente sobre el alcance geográfico de ZAV.** La tabla de identificación de zonas del Artículo 6 (página 12) lista explícitamente "Zona Área Verde | ZAV" bajo **Villa Los Boldos**. Sin embargo, el texto introductorio de la zona ZAV en el Artículo 7 (página 16) dice literalmente: *"Zona presente en la localidad de Nueva Toltén."* — en singular, sin mencionar Villa Los Boldos, a diferencia de ZM2/ZM3/ZM4 que sí dicen explícitamente "Zona presente en las localidades de Nueva Toltén y Villa Los Boldos" cuando corresponde. Es decir, **la tabla de zonificación (Art. 6) y el texto normativo de la zona (Art. 7) se contradicen entre sí sobre si ZAV aplica a Villa Los Boldos.** Se verificó ambos puntos con zoom contra la imagen: la fila "Villa Los Boldos / Zona Área Verde / ZAV" en la tabla del Art. 6 es legible sin ambigüedad, y la frase "Zona presente en la localidad de Nueva Toltén." en el Art. 7 también lo es. No se puede resolver esta contradicción con el material disponible — se documenta como hallazgo para que la fase de generación del JSON final decida cómo tratarla (posiblemente consultando el plano PRC-09118-2 de Villa Los Boldos, fuera del alcance de este documento).

3. **Hallazgo nuevo — patrón de partición de tabla presente, pero en una tabla distinta a la que anticipaba la instrucción de la tarea.** La instrucción de esta tarea advertía sobre tablas de "Normas de Subdivisión y Edificación" que continúan en la página siguiente sin repetir el encabezado de zona (patrón visto en otros documentos de este proyecto). En este documento **eso no ocurre nunca**: las 6 tablas de "Condiciones de Edificación y Subdivisión" / "Norma Urbanística" están cada una completa dentro de una sola página, sin excepción. En cambio, **sí se repite un patrón análogo, pero en las tablas de "Usos de Suelo"**: la de ZM3 se parte entre páginas 13 y 14 (corte tras la fila "Educación"), y la de ZM4 se parte entre páginas 14 y 15 (corte tras la fila "Espacio Público"). En ambos casos, la página siguiente continúa directamente con la próxima fila de la tabla, sin repetir el título de la zona ni los encabezados de columna — mismo mecanismo de corte que el anticipado, aplicado a la tabla "hermana". Adicionalmente, el párrafo (no tabla) de áreas de riesgo de ZE se parte entre las páginas 15 y 16. Se verificó con zoom en los tres cortes que no se perdió contenido.

4. **Hallazgo nuevo — heterogeneidad real (no error) en la estructura de columnas de "Condiciones de Edificación y Subdivisión" entre zonas.** No todas las zonas separan sus parámetros de Coeficiente de Ocupación del Suelo / Coeficiente de Constructibilidad / Altura Máxima por columna de uso: ZMC y ZM3 sí tienen valores distintos por columna; ZM2 los distingue pero por "Residencial/Otros Usos" fusionados vs. "Equipamiento - Salud" (no es la misma partición que ZMC); y ZM4 y ZE tienen esos tres parámetros como **valor único combinado** para todas las columnas de uso, distinguiendo solo la Densidad Bruta Máxima. Esto se verificó exhaustivamente con zoom en las 5 tablas (ZMC, ZM2, ZM3, ZM4, ZE) para no asumir que todas comparten la estructura de ZMC. ZAV, con una sola columna de uso ("Equipamiento"), no tiene esta ambigüedad.

5. **Hallazgo nuevo — ZMC es la única zona sin párrafo de áreas de riesgo.** Las otras 5 zonas (ZM2, ZM3, ZM4, ZE, ZAV) tienen, inmediatamente después de su tabla de condiciones, un párrafo que remite a una o más áreas de riesgo AR-1 a AR-4 definidas en el Artículo 8. ZMC no tiene ningún párrafo de este tipo — la página 12 termina en su tabla de condiciones y la página 13 arranca directo con el título de ZM2. Es consistente con que ZMC sea el núcleo urbano consolidado de Nueva Toltén, presumiblemente fuera de las zonas de inundación/napa freática que sí afectan a las demás zonas (que en conjunto cubren los 4 tipos de área de riesgo: ZM2 y ZM3 con AR-2; ZM4 con AR-1 y AR-2; ZE con AR-1 y AR-3; ZAV con las 4).

6. **Hallazgo nuevo — el `.txt` de esta comuna resultó ser texto nativo confiable, a diferencia del patrón dominante en este corpus.** La instrucción de la tarea pedía verificar el `.txt` igual "aunque debería ser confiable". Se confirma que sí lo es: cada valor numérico y cada celda de las 6 zonas fue cruzado entre `tolten_p12-16.txt` y el render de imagen, sin encontrar una sola discrepancia. Esto contrasta con la experiencia documentada en otros archivos de esta misma carpeta de trabajo (p. ej. Romeral, Caldera), donde el `.txt` capturaba solo encabezados y ninguna celda numérica. Aun así, todos los valores de este documento fueron verificados contra la imagen (no solo aceptados del `.txt`), conforme a la instrucción de máximo rigor.

7. **Contenido adicional en página 16 no mencionado por la nota de Fase 3.** La nota de Fase 3 dice "Capítulo IV pág12-16, zonas... con usos permitidos/prohibidos + condiciones edificación y subdivisión completas", lo que podría sugerir que las 5 páginas están dedicadas íntegramente a las 6 zonas. En realidad, después de ZAV (página 16) hay contenido adicional real: el Artículo 8 completo (áreas de riesgo AR-1 a AR-4), el Artículo 9 completo (patrimonio — Parroquia San Antonio, remitida a las condiciones de ZMC) y el inicio del Capítulo V (Vialidad). Se documenta su existencia por completitud, aunque no se transcribieron en detalle los artículos de vialidad por estar fuera del alcance de esta tarea (que pidió específicamente las 6 zonas del Artículo 7).

8. **No se detectó "trampa de comuna ajena" en este rango.** Se revisó cada página (11 a 17, incluidas las 2 de verificación suplementaria) buscando contenido de otra comuna u organismo mezclado — patrón recurrente en otras ediciones de Diario Oficial de este proyecto. No se encontró ninguno: el encabezado, el CVE, el pie de página y el contenido sustantivo son consistentes y pertenecen a Toltén en las 7 páginas revisadas.

---

## Notas finales de verificación

**Confianza global: alta.** Las 5 páginas asignadas (12-16) se leyeron completas en imagen a 250dpi y se re-verificaron con recortes ampliados (zoom 1.5x–2.5x) para cada tabla de "Usos de Suelo" y de "Condiciones de Edificación y Subdivisión" de las 6 zonas, además de los 3 puntos de corte de página detectados (ZM3 p.13→14, ZM4 p.14→15, párrafo de riesgo de ZE p.15→16) y del punto de apertura de la página 12. Se hicieron además 2 renders suplementarios (páginas 11 y 17, fuera del rango formal) específicamente para resolver con evidencia directa la duda sobre "ZM1" y para confirmar el cierre del Capítulo IV. El texto nativo (`tolten_p12-16.txt`) se cruzó valor por valor contra la imagen y coincidió en el 100% de los casos revisados.

**Confianza por página/sección:**
- Página 11 (verificación suplementaria — Art. 6 intro + tabla de zonas, filas de Nueva Toltén ZMC y ZM2): alta.
- Página 12 (cont. tabla Art. 6 + Art. 7 intro + ZMC completa): alta.
- Página 13 (ZM2 completa + ZM3 usos de suelo, parcial): alta.
- Página 14 (ZM3 usos de suelo cont. + ZM3 condiciones + ZM4 usos de suelo, parcial): alta.
- Página 15 (ZM4 usos de suelo cont. + ZM4 condiciones + ZE completa, con su párrafo de riesgo partido): alta.
- Página 16 (cont. párrafo de riesgo de ZE + ZAV completa + Art. 8 + Art. 9 + inicio Cap. V): alta.
- Página 17 (verificación suplementaria — cuadros de vialidad, confirmación de cierre de Capítulo IV): alta, transcripción no requerida (fuera de alcance).

**Sobre "Dato no determinable":** no se usó en ningún campo de este documento. El único vacío encontrado (fila "Densidad Bruta Máxima" ausente en ZAV) es un caso claro de "Sin valor específico en la fuente" por diseño (zona sin uso residencial), no un dato faltante. No hubo texto borroso, cortado a media palabra sin continuación encontrada, ni ambiguo en ninguna de las 7 páginas revisadas.

**Inconsistencias tipográficas menores de la fuente (no normativas, transcritas literalmente):** "m2" en vez de "m²" en todas las zonas (consistente, no es un error puntual); coma decimal chilena consistente (0,6 / 2,4 / etc.); "hab/Há" consistente en las 5 zonas con densidad (sin la mezcla há/ha vista en otras comunas de este corpus); formato de "Antejardín" inconsistente entre zonas ("0" en ZMC, "3 mts" en ZM2, "3 mts." en ZM3, "3mts." en ZM4 y ZE, "10" sin unidad en ZAV); separador de miles inconsistente ("1000" en ZE vs. "2.000" en ZAV, mismo orden de magnitud, solo difiere la puntuación); comas variables antes de "excepto" en la columna de usos de suelo (algunas filas "Permitido excepto...", otras "Permitido, excepto..." — incluso dentro de la misma zona, ver ZMC/Salud vs. ZM4/Salud); y "AR-1, AR-3" con coma en vez de "AR-1 y AR-3" (única zona, ZE, que no usa "y" en la lista de áreas de riesgo). Ninguna de estas variaciones afecta el valor numérico o el sentido normativo de los campos; todas se verificaron con zoom para descartar que fueran artefactos de renderizado.

**Limitación de alcance a señalar:** el número de decreto/resolución que promulga este PRC no es visible dentro de las páginas 12-17 revisadas (aparecería en las primeras páginas del edicto, no incluidas en el material entregado ni en la verificación suplementaria). Tampoco se transcribieron en detalle los Artículos 10 en adelante (Capítulo V, Vialidad) ni los cuadros de vías de la página 17, por estar fuera del alcance solicitado (las 6 zonas del Artículo 7). La discrepancia de ZAV/Villa Los Boldos (hallazgo 2) tampoco se pudo resolver con el material disponible.
