# Actualización PRC Angol (Diario Oficial 14-10-2022) — Art. 5 (cuadro estacionamientos) y Art. 7 Normas Urbanísticas, Zonas Z-1 a Z-5 y Z-AV

**Fuente:** Diario Oficial de la República de Chile, Núm. 43.376, viernes 14 de octubre de 2022 — "Actualización Plan Regulador Comunal de Angol" (CVE 2200514).

**Rango de páginas de este documento:** páginas 7 a 13 de 20 (numeración impresa en cabecera de cada página, "Página X de 20"). Cubre el final del Artículo 5 (cuadro de estándares mínimos de estacionamiento, página 7) y el Artículo 7 "Normas Urbanísticas y Condiciones Específicas" completo para las 6 zonas urbanas (páginas 8 a 13). No cubre el Artículo 6 "Zonificación" en su forma completa (aparece parcialmente, como contexto, al inicio de la página 8) ni las páginas 14 en adelante (Artículo 8-9, cuadros de vialidad, fuera de rango — ver §9 y §13 sobre la tabla de Z-AV, que queda incompleta por este límite de rango).

**Material usado:** imágenes PNG a 250 dpi (`angol_p7-13-07.png` … `angol_p7-13-13.png`, 2125×3250 px cada una) y texto plano de apoyo (`angol_p7-13.txt`). Cada página fue leída primero a resolución completa y luego se hicieron **recortes con zoom (2×-8×, con `PIL`)** sobre cada tabla numérica y sobre cada celda ambigua, para confirmar cifras y detectar diferencias reales entre zonas que a primera lectura parecían copiadas de una zona a otra (ver §0 y §12 — varias NO lo eran).

**Documento previo de Angol:** no existe. Se verificó `extraccion_normas/angol/` antes de escribir — la carpeta no existía (se creó junto con este archivo). Este es el primer documento de extracción de Angol en el repo; no hay nada previo con qué reconciliar.

---

## 0. Formato de la fuente — confirmación de la "trampa mixto" y estructura real de las tablas

Confirmación exacta de la advertencia de Fase 3, con dos matices importantes descubiertos al leer las imágenes:

- **El `.txt` (pdftotext) es aún más pobre de lo que Fase 3 describe.** Para las páginas 8-13, el `.txt` efectivamente devuelve solo el título de cada zona (`ZONA Z-1 CENTRO HISTÓRICO`, `ZONA Z-2 EJE BERNARDO O'HIGGINS`, etc.), cero contenido de tabla — igual que en Graneros. Pero **para la página 7, el `.txt` no devuelve ni siquiera un título**: el rango de texto extraído salta directamente del pie de página 7 al artículo 6 en la página 8, sin una sola línea del cuadro de estacionamientos. Es decir, la página 7 depende **100%** de la imagen, en un grado más extremo que las páginas 8-13 (que al menos entregan el título de zona como ancla).
- **Las tablas SÍ son perfectamente legibles a 250 dpi con zoom**, confirmando lo anticipado por el encargo: se leyeron y verificaron con recortes ampliados todas las cifras numéricas y casi todo el texto de usos de suelo, con muy pocas excepciones (ver §13, hallazgo sobre Z-AV).
- **Estructura real de las tablas — distinta de otros documentos del proyecto (p. ej. Caldera):** aquí **sí son tablas con bordes reales** (rejilla de celdas dibujada), no texto corrido simulando columnas. Cada zona (Art. 7) trae dos tablas propias:
  1. **"USOS DE SUELO PERMITIDOS / USOS PROHIBIDOS"**, con columnas TIPO / CLASE / DESTINO O ACTIVIDAD (permitido) / USOS PROHIBIDOS.
  2. **"NORMAS DE SUBDIVISIÓN Y EDIFICACIÓN ZONA Z-X..."**, con una fila por parámetro (Densidad Bruta, Superficie de Subdivisión Predial Mínima, COS, Coeficiente de Constructibilidad, Altura Máxima, Sistema de Agrupamiento, Antejardín Obligatorio, Rasantes, Distanciamientos, Adosamientos) y una columna por categoría de uso (Residencial / Equipamiento / a veces Actividades Productivas / a veces Infraestructura / Áreas Verdes — el número de columnas **varía por zona**, ver §2).
- **Convención propia de la fuente para celdas sin valor:** la fuente usa una línea punteada (`----------------`) para marcar "no aplica" tanto en usos prohibidos como en parámetros de edificación que una columna no define. Se transcribe esto como **"Sin valor específico en la fuente"**, indicando en cada caso que el original ya trae su propio marcador de vacío (no es una omisión de esta transcripción).
- **Hallazgo no anticipado por Fase 3 — las tablas NO son copia-pega uniforme entre zonas.** Una primera lectura rápida sugiere que las 6 zonas comparten plantilla y texto idéntico en "Equipamiento". Al verificar celda por celda con zoom (tal como pide el encargo, "no confundir a qué zona pertenece un valor"), se encontraron **diferencias sustantivas reales** entre zonas en ítems como Salud, Seguridad, Deporte, Esparcimiento, Transporte y Sanitaria — no solo diferencias de cifras, sino de qué actividades están permitidas o prohibidas. Ver detalle en cada sección de zona y consolidado en §12.

---

## 1. Convenciones usadas

- **"Sin valor específico en la fuente":** para (a) celdas donde la fuente misma imprime la línea punteada `----------------` (equivalente al original a "no aplica"/vacío), y (b) parámetros que una zona no define porque no corresponde a su naturaleza (p. ej., densidad poblacional para una columna de Equipamiento o Infraestructura).
- **"Dato no determinable":** reservado para valores que deberían existir pero no están disponibles en el corpus entregado. Se usó **únicamente** en la Zona Z-AV, para 4 filas de su tabla de normas de edificación que quedan fuera del rango de páginas entregado (la tabla se corta en la página 13 y continúa en una página 14 que no fue parte del material de este encargo) — no por ilegibilidad, sino por límite de rango. Se explica el motivo exacto en cada caso (§9).
- **`[sic]`:** marca erratas de la fuente, preservadas tal cual. Encontradas en este documento: "GASEODUCTO" (Z-3, debería ser "GASODUCTO"), "1CADA" sin espacio (página 7, ítem Academias), el título de la tabla de normas de Z-5 que dice "...DENSIDAD MEDIA" en vez de "...PRODUCTIVA" (ver §8), y un tachado explícito sobre "TODOS" en Z-AV/Esparcimiento sin que la columna de prohibidos se completara (ver §9).
- **Símbolo M²:** la fuente usa un superíndice "²" en casi toda la tabla, pero en dos puntos concretos de la página 7 imprime "M2" en línea (Estadio) sin superíndice — se preserva la variación tal como aparece, marcada [sic] donde corresponde.
- **Puntuación de valores numéricos:** se preserva tal como aparece, incluida la coma decimal ("0,9", "1,4") que usa esta fuente (a diferencia de Caldera, que usaba punto decimal) y el punto como separador de miles ("2.000 M²").
- **Líneas punteadas del original:** se representan en las tablas de este documento como `----------------` (largo aproximado, no se contaron los puntos exactos del original — no es una cifra, es un marcador visual de vacío).

---

## 2. Correspondencia de páginas y continuidad de tablas entre páginas — corrección importante a la nota de Fase 3

**Hallazgo central de este documento:** la nota heredada de Fase 3 (*"p8 Z-1, p9 Z-2, p10 Z-3, p11 Z-4, p12 Z-5, p13 Z-AV"*) sugiere una correspondencia de **una página por zona**. Verificado directamente contra las imágenes, **esto no es así**: cada zona trae dos tablas (usos de suelo + normas de edificación) que en conjunto ocupan aproximadamente **1.5 páginas**, y las 6 zonas quedan **escalonadas/desfasadas** a lo largo de las páginas 8-13, no alineadas 1 a 1. El *contenido* que identifica Fase 3 (existencia de las 6 zonas Z-1 a Z-AV) es correcto; la *asignación de página única* no lo es. Detalle exacto:

| Archivo | Página impresa | Contenido |
|---|---|---|
| `angol_p7-13-07.png` | página 7 de 20 | Cuadro de estándares mínimos de estacionamiento (continuación del Art. 5; el encabezado del artículo está en la página 6, fuera de este rango). Tabla autocontenida, completa dentro de la página, sin continuar a la página 8. |
| `angol_p7-13-08.png` | página 8 de 20 | Cierre del Art. 6 "Zonificación" (lista de las 6 zonas urbanas + zonas restringidas AR-1/AR-2 + áreas de protección, sin cuadro numérico); apertura del Art. 7; **ZONA Z-1**: tabla de usos de suelo completa hasta "COMERCIO" inclusive, se corta a mitad de la fila "CULTO Y CULTURA" |
| `angol_p7-13-09.png` | página 9 de 20 | Z-1 continuación: resto de usos de suelo (Culto y Cultura → Áreas Verdes) + tabla completa de **NORMAS DE SUBDIVISIÓN Y EDIFICACIÓN ZONA Z-1**; **ZONA Z-2**: tabla de usos de suelo desde Residencial hasta Esparcimiento inclusive (cierra limpio, sin corte a media celda) |
| `angol_p7-13-10.png` | página 10 de 20 | Z-2 continuación: resto de usos de suelo (Salud → Áreas Verdes, incluye Infraestructura) + tabla completa de **NORMAS DE SUBDIVISIÓN Y EDIFICACIÓN ZONA Z-2**; **ZONA Z-3**: tabla de usos de suelo desde Residencial hasta Social inclusive |
| `angol_p7-13-11.png` | página 11 de 20 | Z-3 continuación: Actividades Productivas, Infraestructura (incluye fila extra "Energética", exclusiva de esta zona) → Áreas Verdes + tabla completa de **NORMAS DE SUBDIVISIÓN Y EDIFICACIÓN ZONA Z-3**; **ZONA Z-4**: tabla de usos de suelo desde Residencial hasta Social inclusive (cierra limpio) |
| `angol_p7-13-12.png` | página 12 de 20 | Z-4 continuación: Infraestructura (sin fila Energética) → Áreas Verdes + tabla completa de **NORMAS DE SUBDIVISIÓN Y EDIFICACIÓN ZONA Z-4**; **ZONA Z-5**: tabla de usos de suelo desde Residencial hasta Actividades Productivas/Industria (se corta ahí) |
| `angol_p7-13-13.png` | página 13 de 20 | Z-5 continuación: Infraestructura → Áreas Verdes + tabla completa de **NORMAS DE SUBDIVISIÓN Y EDIFICACIÓN ZONA Z-5** (título con errata, ver §8); **ZONA Z-AV**: tabla de usos de suelo completa + tabla de normas **incompleta** (6 de 10 filas — se corta al final de la página, ver §9) |

**¿Hay tablas partidas entre páginas?** Sí, en casi todos los casos, pero **siempre entre filas completas** (nunca a mitad de una cifra o palabra) — el corte de página cae justo en el borde de una celda, nunca dentro de un número. La única excepción real a "sin pérdida de datos" es la tabla de normas de Z-AV, que se corta por **fin del material entregado** (fin de página 13 = fin del rango del encargo), no por un salto de página dentro del PDF que yo pueda seguir — ver §9.

---

## 3. Página 7 — Artículo 5, cuadro de estándares mínimos de estacionamiento

Página autocontenida, sin encabezado de artículo visible en el rango entregado (el título "Artículo 5" está en la página 6, no incluida). Empieza directo en la tabla, con encabezado de columnas "USO DE SUELO" / "ESTÁNDAR MÍNIMO". Se documenta completa aunque no es una norma de zona, tal como pide el encargo.

| Categoría (TIPO / CLASE) | Uso | Estándar mínimo |
|---|---|---|
| RESIDENCIAL | Vivienda | 1 por vivienda |
| RESIDENCIAL | Hogares de acogida, edificaciones o locales destinados al hospedaje | 1 cada 100 M² de la superficie total edificada |
| EQUIPAMIENTO — Científico | Centros científicos, centros tecnológicos | 1 cada 60 M² de la superficie total edificada |
| EQUIPAMIENTO — Comercio | Centros y locales comerciales, grandes tiendas, supermercados, mercados, estaciones o centros de servicio automotor, restaurantes, fuentes de soda, bares | 1 cada 20 M² de la superficie total edificada |
| EQUIPAMIENTO — Comercio | Discotecas | 1 cada 25 M² de la superficie total edificada |
| EQUIPAMIENTO — Culto y Cultura | Templos, parroquias, santuarios, sinagogas, mezquitas, centros culturales, museos, bibliotecas, galerías de arte | 1 cada 50 M² de la superficie total edificada |
| EQUIPAMIENTO — Culto y Cultura | Salas de concierto o espectáculos, cines, teatros, auditorios, centros de eventos, centros de convenciones | 1 cada 20 M² de la superficie total edificada |
| EQUIPAMIENTO — Deporte | Estadio | 1 cada 20 M2 de la superficie total edificada `[sic: "M2" impreso sin formato de superíndice, único caso de este tipo en la tabla — el resto de la tabla usa "M²"]` |
| EQUIPAMIENTO — Deporte | Centros deportivos y gimnasios | 1 cada 60 M² de la superficie total edificada |
| EQUIPAMIENTO — Deporte | Piscinas | 1 cada 80 M² de la superficie total del predio |
| EQUIPAMIENTO — Deporte | Multicancha | 1 cada 150 M² de la superficie total del predio |
| EQUIPAMIENTO — Educación | Liceos, colegios, escuelas básicas, jardines infantiles, salas cuna, parvularios | 1 cada 100 M² de la superficie total edificada |
| EQUIPAMIENTO — Educación | Academias, institutos, universidades | 1 cada 50 M² de la superficie total edificada `[sic: la fuente imprime "1CADA" sin espacio entre "1" y "CADA"]` |
| EQUIPAMIENTO — Esparcimiento | Parques de entretenciones, zoológicos | 1 cada 200 M² de la superficie total del predio |
| EQUIPAMIENTO — Salud | Hospitales, clínicas, hospitalización | 1 cada 120 M² de la superficie total edificada |
| EQUIPAMIENTO — Salud | Policlínicos, consultorios, postas | 1 cada 100 M² de la superficie total edificada |
| EQUIPAMIENTO — Salud | Cementerios, crematorios | 1 cada 250 M² de la superficie total del predio |
| EQUIPAMIENTO — Seguridad | Unidades policiales, cuarteles de bomberos, cárceles, centros de detención, centros de internación provisoria, centros de privación de libertad | 1 cada 50 M² de la superficie total edificada |
| EQUIPAMIENTO — Servicio | Oficinas, centros médicos, centros dentales | 1 cada 80 M² de la superficie total edificada |
| EQUIPAMIENTO — Servicio | Servicios públicos en general | 1 cada 50 M² de la superficie total edificada |
| EQUIPAMIENTO — Servicio | Centros de pago, bancos | 1 cada 100 M² de la superficie total edificada `[sic: la fuente imprime "100M²" sin espacio]` |
| EQUIPAMIENTO — Social | Clubes sociales | 1 cada 50 M² de la superficie total edificada |
| ACTIVIDADES PRODUCTIVAS — Industria | Hasta 500 M² de la superficie total edificada | 1 cada 150 M² de la superficie total edificada |
| ACTIVIDADES PRODUCTIVAS — Industria | Desde 501 M² de la superficie total edificada | 1 cada 180 M² de la superficie total edificada |
| ACTIVIDADES PRODUCTIVAS — Talleres | (sin distinción por tramo) | 1 cada 100 M² de la superficie total edificada |
| ACTIVIDADES PRODUCTIVAS — Grandes depósitos, bodegas industriales | Hasta 500 M² de la superficie total edificada | 1 cada 200 M² de la superficie total edificada |
| ACTIVIDADES PRODUCTIVAS — Grandes depósitos, bodegas industriales | Desde 501 M² hasta 1.500 M² de la superficie total edificada | 1 cada 250 M² de la superficie total edificada |
| ACTIVIDADES PRODUCTIVAS — Grandes depósitos, bodegas industriales | Desde 1.501 M² de la superficie total edificada | 1 cada 300 M² de la superficie total edificada |
| INFRAESTRUCTURA — Transporte | Terminal de transporte terrestre | 2 cada 100 M² de la superficie total del predio |
| INFRAESTRUCTURA — Sanitaria | Plantas de captación, distribución o tratamiento de agua potable, de aguas servidas o de aguas lluvia | 1 cada 50 M² de la superficie total edificada |

**Verificación de cierre:** confirmado con zoom que la tabla termina exactamente después de la fila "Sanitaria" — no hay más categorías (ninguna fila "Energética" aquí, a diferencia de la tabla de Infraestructura de la Zona Z-3), y el pie de página estándar aparece inmediatamente después, sin contenido cortado.

**Hallazgo sobre el valor "1.500 M²" (tramo de Grandes depósitos/bodegas):** este número se verificó con especial cuidado por ser visualmente ambiguo entre "1500" y "1600" a resolución normal. Con zoom ×6-8 se confirmó "1500", y es además el valor lógicamente consistente con el tramo siguiente ("desde 1.501 M²" — los tramos empalman sin salto ni superposición).

---

## 4. ZONA Z-1 CENTRO HISTÓRICO (páginas 8→9)

### Usos de suelo permitidos / prohibidos

| Tipo | Clase | Permitido | Prohibido |
|---|---|---|---|
| RESIDENCIAL | — | Vivienda Hogares de acogida, edificaciones y locales destinados a hospedaje. `[sic: sin coma ni punto entre "Vivienda" y "Hogares de acogida" — se lee como dos usos distintos concatenados, tal como aparece en la fuente]` | Sin valor específico en la fuente |
| EQUIPAMIENTO | Científico | Todos | Sin valor específico en la fuente |
| EQUIPAMIENTO | Comercio | Locales comerciales, supermercados, mercados, estaciones o centros de servicio automotor, restaurantes, fuentes de soda, bares, ferias | Centros comerciales, grandes tiendas y discotecas |
| EQUIPAMIENTO | Culto y Cultura | Culto: Todos / Cultura: Todos | Sin valor específico en la fuente (ambas sub-filas) |
| EQUIPAMIENTO | Deporte | Centros deportivos, clubes deportivos, gimnasios, multicanchas, piscinas y recintos destinados al deporte o actividad física en general | Estadios, autódromos, saunas y baños turcos |
| EQUIPAMIENTO | Educación | Todos | Sin valor específico en la fuente |
| EQUIPAMIENTO | Esparcimiento | Juegos electrónicos o mecánicos | Parques de entretenciones, parques zoológicos y casinos |
| EQUIPAMIENTO | Salud | Hospitales, clínicas, policlínicos, consultorios, postas, centros de rehabilitación | Cementerios y crematorios |
| EQUIPAMIENTO | Seguridad | Unidades policiales, cuarteles de bomberos, centros de internación provisoria | Cárceles, centros de detención y centros de privación de libertad |
| EQUIPAMIENTO | Servicios | Todos | Sin valor específico en la fuente |
| EQUIPAMIENTO | Social | Todos | Sin valor específico en la fuente |
| ÁREAS VERDES | — | Todos | Sin valor específico en la fuente |

**Nota estructural:** Z-1 es la única zona (junto con la propia Z-AV, que es de otra naturaleza) que **no tiene** columnas/filas de "Actividades Productivas" ni "Infraestructura" en su tabla de usos de suelo — coherente con ser el centro histórico, sin industria ni infraestructura de transporte/sanitaria contemplada.

**Nota — Salud y Seguridad más permisivos que en otras zonas:** verificado con zoom y comparado directamente célula por célula: Z-1 es la **única** zona de las 6 donde "postas, centros de rehabilitación" están del lado permitido de Salud y "centros de internación provisoria" está del lado permitido de Seguridad. En Z-2 y Z-3 ambos ítems pasan al lado prohibido (ver §12 para la comparación completa); Z-4 coincide con Z-1 en Salud pero no en Seguridad. No es un error de esta transcripción — se releyó dos veces contra la imagen por lo inesperado del patrón.

### Normas de subdivisión y edificación — Zona Z-1 Centro Histórico

*(3 columnas: Residencial / Equipamiento / Áreas Verdes)*

| Norma urbanística | Residencial | Equipamiento | Áreas Verdes |
|---|---|---|---|
| Densidad Bruta Máxima Hab/Ha | 400 HAB/HA | Sin valor específico en la fuente (línea punteada) | Sin valor específico en la fuente (celda vacía en la fuente, sin línea punteada — a diferencia de la celda de Equipamiento de la misma fila; se documenta la diferencia visual sin interpretarle un significado distinto) |
| Superficie de Subdivisión Predial Mínima (M²) | 250 M² *(celda única fusionada, aplica a las 3 columnas)* | | |
| Coeficiente de Ocupación de Suelo | 0,9 | 0,9 | 0,1 |
| Coeficiente de Constructibilidad | 1,4 | 1,2 | 2 |
| Altura Máxima de la Edificación | 14,00 M (máximo de 4 pisos) | 14,00 M (máximo de 4 pisos) | 7,00 M (máximo de 2 pisos) |
| Sistema de Agrupamiento | Aislado, pareado, continuo | Aislado, pareado, continuo | Aislado |
| Antejardín Obligatorio (M) | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente |
| Rasantes | OGUC | OGUC | OGUC |
| Distanciamientos | OGUC | OGUC | OGUC |
| Adosamientos | OGUC | OGUC | OGUC |

---

## 5. ZONA Z-2 EJE BERNARDO O'HIGGINS (páginas 9→10)

### Usos de suelo permitidos / prohibidos

| Tipo | Clase | Permitido | Prohibido |
|---|---|---|---|
| RESIDENCIAL | — | Vivienda Hogares de acogida, edificaciones y locales destinados a hospedaje. | Sin valor específico en la fuente |
| EQUIPAMIENTO | Científico | Todos | Sin valor específico en la fuente |
| EQUIPAMIENTO | Comercio | Locales comerciales, centros comerciales, grandes tiendas, supermercados, mercados, estaciones o centros de servicio automotor, restaurantes, fuentes de soda, ferias | Discotecas |
| EQUIPAMIENTO | Culto y Cultura | Culto: Todos / Cultura: Todos | Sin valor específico en la fuente (ambas sub-filas) |
| EQUIPAMIENTO | Deporte | Centros deportivos, clubes deportivos, gimnasios, multicanchas, piscinas y recintos destinados al deporte o actividad física en general | Estadios, autódromos, saunas y baños turcos |
| EQUIPAMIENTO | Educación | Todos | Sin valor específico en la fuente |
| EQUIPAMIENTO | Esparcimiento | Juegos electrónicos o mecánicos | Parques de entretenciones, parques zoológicos y casinos |
| EQUIPAMIENTO | Salud | Hospitales, clínicas, policlínicos, consultorios | Postas, centros de rehabilitación, cementerios y crematorios |
| EQUIPAMIENTO | Seguridad | Unidades policiales, cuarteles de bomberos | Centros de internación provisoria, cárceles, centros de detención y centros de privación de libertad |
| EQUIPAMIENTO | Servicios | Todos | Sin valor específico en la fuente |
| EQUIPAMIENTO | Social | Todos | Sin valor específico en la fuente |
| INFRAESTRUCTURA | Transporte | Estaciones ferroviarias, terminales de transporte terrestre | Recintos marítimos o portuarios, instalaciones o recintos aeroportuarios |
| INFRAESTRUCTURA | Sanitaria | Plantas de captación, distribución y tratamiento de agua potable, de aguas servidas y/o de aguas lluvia | Rellenos sanitarios, estaciones exclusivas de transferencia de residuos, etc. |
| ÁREAS VERDES | — | Todos | Sin valor específico en la fuente |

**Diferencia respecto de Z-1 (verificada, no es copia-pega):** en Z-2, "postas" y "centros de rehabilitación" (Salud) y "centros de internación provisoria" (Seguridad) pasan al lado **prohibido** — en Z-1 estaban del lado permitido. Comercio en Z-2 sí permite "centros comerciales, grandes tiendas" (en Z-1 estaban prohibidos), coherente con ser el eje comercial principal de la comuna.

**Nota estructural:** Z-2 es la primera zona con columna/filas de "Infraestructura" (Transporte, Sanitaria) en su tabla de usos de suelo; no tiene "Actividades Productivas".

### Normas de subdivisión y edificación — Zona Z-2 Eje Bernardo O'Higgins

*(4 columnas: Residencial / Equipamiento / Infraestructura / Áreas Verdes)*

| Norma urbanística | Residencial | Equipamiento | Infraestructura | Áreas Verdes |
|---|---|---|---|---|
| Densidad Bruta Máxima Hab/Ha | 400 HAB/HA | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente |
| Superficie de Subdivisión Predial Mínima (M²) | 250 M² *(celda fusionada, 4 columnas)* | | | |
| Coeficiente de Ocupación de Suelo | 0,8 | 0,8 | 0,7 | 0,1 |
| Coeficiente de Constructibilidad | 2 | 2 | 2 | 2 |
| Altura Máxima de la Edificación | 16,00 M (máximo de 4 pisos) | 16,00 M (máximo de 4 pisos) | 16,00 M (máximo de 4 pisos) | 7,00 M (máximo de 2 pisos) |
| Sistema de Agrupamiento | Aislado, pareado, continuo | Aislado, pareado, continuo | Aislado | Aislado |
| Antejardín Obligatorio (M) | 3,00 M | 3,00 M | 3,00 M | 3,00 M |
| Rasantes | OGUC | OGUC | OGUC | OGUC |
| Distanciamientos | OGUC | OGUC | OGUC | OGUC |
| Adosamientos | OGUC | OGUC | OGUC | OGUC |

**Verificación de cifra crítica — Altura Máxima:** este valor se leyó primero como posible "14,00 M" (por similitud con Z-1) y se descartó tras comparar ambos dígitos lado a lado con zoom ×8: la forma del segundo carácter en Z-2 (curva cerrada inferior) es inequívocamente un "6", no un "4" (trazo angular recto, como el confirmado en Z-1). **Z-2 usa 16,00 M, distinto de Z-1 (14,00 M).**

---

## 6. ZONA Z-3 RESIDENCIAL MIXTA DENSIDAD MEDIA (páginas 10→11)

### Usos de suelo permitidos / prohibidos

| Tipo | Clase | Permitido | Prohibido |
|---|---|---|---|
| RESIDENCIAL | — | Vivienda Hogares de acogida, edificaciones y locales destinados a hospedaje. | Sin valor específico en la fuente |
| EQUIPAMIENTO | Científico | Todos | Sin valor específico en la fuente |
| EQUIPAMIENTO | Comercio | Locales comerciales, supermercados, mercados, estaciones o centros de servicio automotor, restaurantes, fuentes de soda, bares, ferias | Centros comerciales, grandes tiendas y discotecas |
| EQUIPAMIENTO | Culto y Cultura | Culto: Todos / Cultura: Todos | Sin valor específico en la fuente (ambas sub-filas) |
| EQUIPAMIENTO | Deporte | Centros deportivos, clubes deportivos, gimnasios, multicanchas, piscinas y recintos destinados al deporte o actividad física en general | Estadios, autódromos, saunas y baños turcos |
| EQUIPAMIENTO | Educación | Todos | Sin valor específico en la fuente |
| EQUIPAMIENTO | Esparcimiento | Juegos electrónicos o mecánicos | Parques de entretenciones, parques zoológicos y casinos |
| EQUIPAMIENTO | Salud | Hospitales, clínicas, policlínicos, consultorios, postas, centros de rehabilitación | Cementerios y crematorios |
| EQUIPAMIENTO | Seguridad | Unidades policiales, cuarteles de bomberos | Centros de internación provisoria, cárceles, centros de detención y centros de privación de libertad |
| EQUIPAMIENTO | Servicios | Todos | Sin valor específico en la fuente |
| EQUIPAMIENTO | Social | Todos | Sin valor específico en la fuente |
| ACTIVIDADES PRODUCTIVAS | Industria | Actividades productivas calificadas como inofensivas | Actividades productivas molestas, insalubres, contaminantes o peligrosas |
| INFRAESTRUCTURA | Transporte | Estaciones ferroviarias, terminales de transporte terrestre | Recintos marítimos o portuarios, instalaciones o recintos aeroportuarios |
| INFRAESTRUCTURA | Sanitaria | Plantas de captación, distribución y tratamiento de agua potable o servidas de aguas lluvias, rellenos sanitarios, estaciones exclusivas de transferencia de residuos, etc. | Sin valor específico en la fuente |
| INFRAESTRUCTURA | Energética `[sic: la fuente imprime "ENERGETICA", sin tilde — consistente con el estilo general en mayúsculas de esta tabla, que omite tildes en varias palabras]` | Gaseoducto `[sic: la fuente imprime "GASEODUCTO"; la forma correcta en español es "gasoducto"]` | Centrales de generación de energía, de gas y de telecomunicaciones, etc. |
| ÁREAS VERDES | — | Todos | Sin valor específico en la fuente |

**Diferencia respecto de Z-1 y Z-2 (verificada):** Salud en Z-3 coincide con Z-1 (postas/rehabilitación permitidos), pero Seguridad en Z-3 coincide con Z-2 (centros de internación provisoria prohibidos) — es decir, Z-3 no replica completamente ni a Z-1 ni a Z-2, tiene su propia combinación. **Sanitaria es la diferencia más notable:** Z-3 es la única zona de las 5 con columna Infraestructura donde "rellenos sanitarios, estaciones exclusivas de transferencia de residuos" están del lado **permitido** (en Z-2, Z-4 y Z-5 están prohibidos) — verificado dos veces por lo inesperado del hallazgo. Z-3 es también la única zona con fila "Energética" en Infraestructura.

### Normas de subdivisión y edificación — Zona Z-3 Residencial Mixta Densidad Media

*(5 columnas: Residencial / Equipamiento / Actividades Productivas / Infraestructura / Áreas Verdes)*

| Norma urbanística | Residencial | Equipamiento | Actividades Productivas | Infraestructura | Áreas Verdes |
|---|---|---|---|---|---|
| Densidad Bruta Máxima Hab/Ha | 250 HAB/HA | Sin valor específico | Sin valor específico | Sin valor específico | Sin valor específico |
| Superficie de Subdivisión Predial Mínima (M²) | 200 M² *(celda fusionada, 5 columnas)* | | | | |
| Coeficiente de Ocupación de Suelo | 0,7 | 0,5 | 0,7 | 0,5 | 0,1 |
| Coeficiente de Constructibilidad | 1,5 | 1 | 1,5 | 1 | 2 |
| Altura Máxima de la Edificación | 10,50 M (máximo de 3 pisos) | 10,50 M (máximo de 3 pisos) | 10,50 M (máximo de 3 pisos) | 10,50 M (máximo de 3 pisos) | 7,00 M (máximo de 2 pisos) |
| Sistema de Agrupamiento | Aislado, pareado, continuo | Aislado, pareado | Aislado | Aislado | Aislado |
| Antejardín Obligatorio (M) | 3,00 M | 3,00 M | 7,00 M | 7,00 M | 3,00 M |
| Rasantes | OGUC | OGUC | OGUC | OGUC | OGUC |
| Distanciamientos | OGUC | OGUC | OGUC | OGUC | OGUC |
| Adosamientos | OGUC | OGUC | OGUC | OGUC | OGUC |

---

## 7. ZONA Z-4 RESIDENCIAL MIXTA DENSIDAD BAJA (páginas 11→12)

### Usos de suelo permitidos / prohibidos

| Tipo | Clase | Permitido | Prohibido |
|---|---|---|---|
| RESIDENCIAL | — | Vivienda Hogares de acogida, edificaciones y locales destinados a hospedaje. | Sin valor específico en la fuente |
| EQUIPAMIENTO | Científico | Todos | Sin valor específico en la fuente |
| EQUIPAMIENTO | Comercio | Locales comerciales, supermercados, mercados, estaciones o centros de servicio automotor, restaurantes, fuentes de soda, bares, ferias | Centros comerciales, grandes tiendas y discotecas |
| EQUIPAMIENTO | Culto y Cultura | Culto: Todos / Cultura: Todos | Sin valor específico en la fuente (ambas sub-filas) |
| EQUIPAMIENTO | Deporte | Centros deportivos, clubes deportivos, gimnasios, multicanchas, piscinas y recintos destinados al deporte o actividad física en general | Estadios, autódromos, saunas y baños turcos |
| EQUIPAMIENTO | Educación | Todos | Sin valor específico en la fuente |
| EQUIPAMIENTO | Esparcimiento | Juegos electrónicos o mecánicos | Parques de entretenciones, parques zoológicos y casinos |
| EQUIPAMIENTO | Salud | Hospitales, clínicas, policlínicos, consultorios, postas, centros de rehabilitación | Cementerios y crematorios |
| EQUIPAMIENTO | Seguridad | Unidades policiales, cuarteles de bomberos | Centros de internación provisoria, cárceles, centros de detención y centros de privación de libertad |
| EQUIPAMIENTO | Servicios | Todos | Sin valor específico en la fuente |
| EQUIPAMIENTO | Social | Todos | Sin valor específico en la fuente |
| INFRAESTRUCTURA | Transporte | Estaciones ferroviarias, terminales de transporte terrestre | Recintos marítimos o portuarios, instalaciones o recintos aeroportuarios |
| INFRAESTRUCTURA | Sanitaria | Plantas de captación, distribución y tratamiento de agua potable, de aguas servidas o de aguas lluvia | Rellenos sanitarios, estaciones exclusivas de transferencia de residuos, etc. |
| ÁREAS VERDES | — | Todos | Sin valor específico en la fuente |

**Nota estructural:** Z-4 no tiene fila de "Actividades Productivas" (ni de "Energética" dentro de Infraestructura) — se verificó explícitamente el borde de cierre de la tabla de Equipamiento en el límite de página 11→12 para descartar que una fila se hubiera perdido en el corte: el cuadro cierra limpio en "Social" y la Infraestructura retoma directo con "Transporte" en la página 12, sin hueco. **Salud coincide con Z-1 (permisivo); Seguridad coincide con Z-2/Z-3 (restrictivo)** — combinación propia, ni calco de una ni de otra.

### Normas de subdivisión y edificación — Zona Z-4 Residencial Mixta Densidad Baja

*(4 columnas: Residencial / Equipamiento / Infraestructura / Áreas Verdes)*

| Norma urbanística | Residencial | Equipamiento | Infraestructura | Áreas Verdes |
|---|---|---|---|---|
| Densidad Bruta Máxima Hab/Ha | 50 HAB/HA | Sin valor específico | Sin valor específico | Sin valor específico |
| Superficie de Subdivisión Predial Mínima (M²) | 800 M² *(celda fusionada, 4 columnas)* | | | |
| Coeficiente de Ocupación de Suelo | 0,5 | 0,4 | 0,4 | 0,1 |
| Coeficiente de Constructibilidad | 0,6 | 0,7 | 0,8 | 2 |
| Altura Máxima de la Edificación | 7,00 M (máximo de 2 pisos) | 7,00 M (máximo de 2 pisos) | 7,00 M (máximo de 2 pisos) | 7,00 M (máximo de 2 pisos) |
| Sistema de Agrupamiento | Aislado, pareado, continuo | Aislado, pareado | Aislado | Aislado |
| Antejardín Obligatorio (M) | 5,00 M | 5,00 M | 7,00 M | 3,00 M |
| Rasantes | OGUC | OGUC | OGUC | OGUC |
| Distanciamientos | OGUC | OGUC | OGUC | OGUC |
| Adosamientos | OGUC | OGUC | OGUC | OGUC |

**Nota:** Z-4 es la única de las 6 zonas donde las 4 columnas comparten la misma Altura Máxima (7,00 M / 2 pisos) — coherente con el nombre de la zona, "Densidad Baja". También tiene la mayor Superficie de Subdivisión Predial Mínima de las zonas residenciales-mixtas (800 M², solo superada por Z-AV con 2.000 M²).

---

## 8. ZONA Z-5 RESIDENCIAL MIXTA PRODUCTIVA (páginas 12→13)

### Usos de suelo permitidos / prohibidos

| Tipo | Clase | Permitido | Prohibido |
|---|---|---|---|
| RESIDENCIAL | — | Vivienda Hogares de acogida, edificaciones y locales destinados a hospedaje. | Sin valor específico en la fuente |
| EQUIPAMIENTO | Científico | Todos | Sin valor específico en la fuente |
| EQUIPAMIENTO | Comercio | Locales comerciales, centros comerciales, grandes tiendas, supermercados, estaciones o centros de servicio automotor, restaurantes, fuentes de soda, bares, discotecas, ferias | **Mercados** |
| EQUIPAMIENTO | Culto y Cultura | Culto: Todos / Cultura: Todos | Sin valor específico en la fuente (ambas sub-filas) |
| EQUIPAMIENTO | Deporte | Todos | Sin valor específico en la fuente |
| EQUIPAMIENTO | Educación | Todos | Sin valor específico en la fuente |
| EQUIPAMIENTO | Esparcimiento | Todos | Sin valor específico en la fuente |
| EQUIPAMIENTO | Salud | Todos | Sin valor específico en la fuente |
| EQUIPAMIENTO | Seguridad | Todos | Sin valor específico en la fuente |
| EQUIPAMIENTO | Servicios | Todos | Sin valor específico en la fuente |
| EQUIPAMIENTO | Social | Todos | Sin valor específico en la fuente |
| ACTIVIDADES PRODUCTIVAS | Industria | Actividades productivas calificadas como inofensivas | Actividades productivas molestas, insalubres, contaminantes o peligrosas |
| INFRAESTRUCTURA | Transporte | Estaciones ferroviarias, terminales de transporte terrestre, instalaciones o recintos aeroportuarios | **Recintos marítimos o portuarios** |
| INFRAESTRUCTURA | Sanitaria | Plantas de captación, distribución y tratamiento de agua potable o servidas y de aguas lluvias | Rellenos sanitarios, estaciones exclusivas de transferencia de residuos, etc. |
| ÁREAS VERDES | — | Todos | Sin valor específico en la fuente |

**Hallazgo estructural importante (no anticipado por Fase 3):** Z-5 es la única zona donde Deporte, Esparcimiento, Salud y Seguridad **se simplifican a "Todos / sin valor"**, en vez de la lista diferenciada permitido/prohibido que traen las otras 5 zonas para estos mismos ítems. Verificado con zoom fila por fila (§ en imágenes `angol_p12_z5_culto_deporte.png`, `angol_p12_z5_salud_seg_v3.png`, `angol_p12_z5_social.png`) — no es un error de lectura, la fuente efectivamente imprime "TODOS" seguido de la línea punteada en las 4 filas, distinto del patrón detallado de Z-1 a Z-4.

**Otras dos diferencias verificadas y no triviales:**
- **Comercio:** Z-5 es la única zona que permite "discotecas" (prohibidas en Z-1, Z-3, Z-4; ausentes de la lista de Z-2) y, a la inversa, es la única que prohíbe específicamente "Mercados" (que las demás zonas permiten) — una sola palabra en la columna de prohibidos, verificada con zoom para excluir que fuera un fragmento cortado de una lista más larga.
- **Transporte:** Z-5 es la única zona que permite "instalaciones o recintos aeroportuarios" (prohibidos en Z-2, Z-3 y Z-4) y, a la inversa, prohíbe únicamente "recintos marítimos o portuarios" (sin agrupar ambos ítems del lado prohibido, como sí hacen las otras 3 zonas con columna de Infraestructura).

### Normas de subdivisión y edificación — Zona Z-5 [ver nota sobre el título]

*(5 columnas: Residencial / Equipamiento / Actividades Productivas / Infraestructura / Áreas Verdes)*

> **Hallazgo `[sic]` — errata de copia-pega en el título de esta tabla:** el título impreso en la fuente es **"NORMAS DE SUBDIVISIÓN Y EDIFICACIÓN ZONA Z-5 RESIDENCIAL MIXTA DENSIDAD MEDIA"**, verificado con zoom ×3 letra por letra. Esto es incorrecto: "Residencial Mixta Densidad Media" es el nombre de la **Zona Z-3** (confirmado en el Artículo 6, página 8, y en el título de la propia tabla de usos de suelo de Z-5 dos filas más arriba en la misma página 13, que sí dice correctamente "ZONA Z-5 / RESIDENCIAL MIXTA PRODUCTIVA"). Es, con alta probabilidad, un error de copia-pega del redactor del Diario Oficial al generar la tabla de normas de Z-5 a partir de la de Z-3. Se preserva el texto erróneo tal como aparece en la fuente, marcado `[sic]`, y se usa el nombre correcto ("Zona Z-5 Residencial Mixta Productiva") en el resto de este documento para evitar confusión.

| Norma urbanística | Residencial | Equipamiento | Actividades Productivas | Infraestructura | Áreas Verdes |
|---|---|---|---|---|---|
| Densidad Bruta Máxima Hab/Ha | 160 HAB/HA | Sin valor específico | Sin valor específico | Sin valor específico | Sin valor específico |
| Superficie de Subdivisión Predial Mínima (M²) | 300 M² *(celda fusionada, 5 columnas)* | | | | |
| Coeficiente de Ocupación de Suelo | 0,6 | 0,4 | 0,6 | 0,4 | 0,1 |
| Coeficiente de Constructibilidad | 1 | 0,8 | 1 | 0,8 | 2 |
| Altura Máxima de la Edificación | 7,00 M (máximo de 2 pisos) | 10,50 M (máximo de 3 pisos) | 10,50 M (máximo de 3 pisos) | 10,50 M (máximo de 3 pisos) | 7,00 M (máximo de 2 pisos) |
| Sistema de Agrupamiento | Aislado, pareado, continuo | Aislado, pareado | Aislado | Aislado | Aislado |
| Antejardín Obligatorio (M) | 5,00 M | 5,00 M | 7,00 M | 5,00 M | 3,00 M |
| Rasantes | OGUC | OGUC | OGUC | OGUC | OGUC |
| Distanciamientos | OGUC | OGUC | OGUC | OGUC | OGUC |
| Adosamientos | OGUC | OGUC | OGUC | OGUC | OGUC |

**Nota:** Z-5 es la única zona donde la columna Residencial tiene una Altura Máxima (7,00 M) **distinta y menor** que su propia columna de Equipamiento (10,50 M) — en todas las demás zonas con más de una columna, Residencial y Equipamiento comparten la misma altura máxima entre sí.

---

## 9. ZONA Z-AV ÁREA VERDE (página 13) — tabla de normas incompleta

### Usos de suelo permitidos / prohibidos

Patrón invertido respecto de las demás zonas (área verde: prohíbe casi todo uso salvo equipamiento pasivo y áreas verdes):

| Tipo | Clase | Permitido | Prohibido |
|---|---|---|---|
| RESIDENCIAL | — | Sin valor específico en la fuente | Todos |
| EQUIPAMIENTO | Científico | Todos | Sin valor específico en la fuente |
| EQUIPAMIENTO | Comercio | Sin valor específico en la fuente | Todos |
| EQUIPAMIENTO | Culto y Cultura | Culto: Todos / Cultura: Todos | Sin valor específico en la fuente (ambas sub-filas) |
| EQUIPAMIENTO | Deporte | Todos | Sin valor específico en la fuente |
| EQUIPAMIENTO | Educación | Sin valor específico en la fuente | Todos |
| EQUIPAMIENTO | Esparcimiento | **"Todos" — ver hallazgo abajo** | Sin valor específico en la fuente |
| EQUIPAMIENTO | Salud | Sin valor específico en la fuente | Todos |
| EQUIPAMIENTO | Seguridad | Sin valor específico en la fuente | Todos |
| EQUIPAMIENTO | Servicios | Sin valor específico en la fuente | Todos |
| EQUIPAMIENTO | Social | Sin valor específico en la fuente | Todos |
| ÁREAS VERDES | — | Todos | Sin valor específico en la fuente |

> **Hallazgo `[sic]` no anticipado por Fase 3 — tachado explícito sin resolver en el original:** en la fila "Esparcimiento", la palabra **"TODOS"** de la columna de permitidos aparece impresa **con una línea de tachado explícita atravesándola** (verificado con zoom ×6, imagen `angol_p13_todos_strikethrough_mega.png` — es un trazo recto y limpio sobre toda la palabra, no una mancha ni un artefacto de escaneo). La columna de prohibidos correspondiente muestra la línea punteada estándar (sin valor), no "Todos". Esto deja el estado real de "Esparcimiento" en Z-AV **ambiguo en la propia fuente**: parece una corrección editorial (¿se quiso prohibir Esparcimiento y no se completó el valor en la columna de prohibidos?) que no fue depurada antes de la publicación en el Diario Oficial. Se preserva tal cual — no se interpreta ni se completa el valor faltante. Se documenta como hallazgo porque una fase posterior no debería asumir automáticamente "Esparcimiento permitido" en Z-AV sin considerar este tachado.

### Normas de subdivisión y edificación — Zona Z-AV Área Verde

*(3 columnas: Residencial / Equipamiento / Áreas Verdes)*

> **Hallazgo importante — tabla incompleta por límite de rango, no por ilegibilidad:** de las 10 filas que traen todas las demás zonas (Densidad Bruta … Adosamientos), en la página 13 solo son visibles las **primeras 6**. La tabla llega hasta "Sistema de Agrupamiento" y ahí se acaba el espacio de la página 13 (queda un espacio en blanco antes del pie de página, consistente con que la tabla continúa en una página 14 que **no forma parte del material entregado para este encargo**, que se limita a las páginas 7-13). No se trata de una cifra borrosa: literalmente no hay imagen de esa parte de la tabla en el material recibido.

| Norma urbanística | Residencial | Equipamiento | Áreas Verdes |
|---|---|---|---|
| Densidad Bruta Máxima Hab/Ha | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente |
| Superficie de Subdivisión Predial Mínima (M²) | 2.000 M² *(celda fusionada, 3 columnas)* | | |
| Coeficiente de Ocupación de Suelo | Sin valor específico en la fuente | 0,1 | 0,1 |
| Coeficiente de Constructibilidad | Sin valor específico en la fuente | 2 | 2 |
| Altura Máxima de la Edificación | Sin valor específico en la fuente | 7,00 M (máximo de 2 pisos) | 7,00 M (máximo de 2 pisos) |
| Sistema de Agrupamiento | Sin valor específico en la fuente | Aislado, pareado | Aislado |
| Antejardín Obligatorio (M) | **Dato no determinable** — fila fuera del rango de páginas entregado (continúa en p.14, no incluida) | **Dato no determinable** — ídem | **Dato no determinable** — ídem |
| Rasantes | **Dato no determinable** — ídem | **Dato no determinable** — ídem | **Dato no determinable** — ídem |
| Distanciamientos | **Dato no determinable** — ídem | **Dato no determinable** — ídem | **Dato no determinable** — ídem |
| Adosamientos | **Dato no determinable** — ídem | **Dato no determinable** — ídem | **Dato no determinable** — ídem |

**Superficie de Subdivisión Predial Mínima (2.000 M²):** es, con amplio margen, la mayor de las 6 zonas (la siguiente más alta es Z-4 con 800 M²) — coherente con ser suelo de área verde, no de loteo habitacional.

---

## 10. Zonas mencionadas en el Artículo 6 sin tabla propia en este rango (fuera de alcance)

El Artículo 6 (inicio de la página 8) menciona, además de las 6 zonas urbanas con tabla en el Art. 7, dos categorías de "Zonas Restringidas al Desarrollo Urbano" y una de "Áreas de Protección": **AR-1** (con subáreas AR-1a Deslizamientos, AR-1b Flujos, AR-1c Desprendimientos), **AR-2** (con subáreas AR-2a Inundables/Potencialmente Inundables, AR-2b Anegamiento), e **Inmuebles de Conservación Histórica / Monumentos Nacionales**. Se verificó que **ninguna de estas figura con una tabla de usos de suelo o de normas de edificación dentro de las páginas 8 a 13** — el Art. 7 tal como aparece en este rango cubre exclusivamente las 6 zonas urbanas (Z-1 a Z-AV). Es esperable que estas áreas de restricción/protección se regulen en artículos posteriores (fuera del rango 7-13 de este encargo) o remitiendo a normativa sectorial (geología, OGUC patrimonio, etc.) en vez de cuadros de intensidad de uso — no se puede confirmar esto último sin ver páginas adicionales, y no se específula más allá de lo observado.

---

## 11. Verificación de "trampa comuna ajena"

Se revisó explícitamente, como pide el encargo, si hay contenido de otra comuna mezclado en las 7 páginas. **No se encontró ninguno.** Elementos verificados:

- Las 7 páginas se refieren consistentemente al **"Plan Regulador Comunal de Angol"** (texto explícito en el Art. 6, página 8: *"El Área Urbana del Plan Regulador Comunal de Angol comprende las siguientes zonas..."*).
- Los planos de zonificación se citan como **"láminas PRC 09201-1 y PRC 09201-2"**. El código **09201** corresponde efectivamente al código INE oficial de la comuna de Angol (Región de La Araucanía, Provincia de Malleco) — esto es una corroboración positiva adicional, no solo la ausencia de contradicción.
- Los nombres de las 6 zonas (Centro Histórico, Eje Bernardo O'Higgins, Residencial Mixta Densidad Media/Baja/Productiva, Área Verde) son consistentes entre sí y con la morfología típica de un plan regulador de una ciudad intermedia con avenida principal nombrada en honor a Bernardo O'Higgins — no hay topónimos, nombres de calles o referencias geográficas de otra comuna en ningún punto de las 7 páginas.
- El encabezado de cada página (Diario Oficial, Núm. 43.376, viernes 14 de octubre de 2022) es idéntico en las 7 páginas, sin discontinuidad de fecha/número de edición que sugiera contenido insertado de otro documento.

**Conclusión:** no hay trampa de comuna ajena en este rango de páginas.

---

## 12. Tabla comparativa resumen — Normas de subdivisión y edificación, columna Residencial de las 6 zonas

*(Lectura rápida; el detalle completo y autoritativo, incluidas las columnas de Equipamiento/Actividades Productivas/Infraestructura/Áreas Verdes de cada zona, está en §4-9)*

| Parámetro | Z-1 Centro Histórico | Z-2 Eje B. O'Higgins | Z-3 Res. Mixta Media | Z-4 Res. Mixta Baja | Z-5 Res. Mixta Productiva | Z-AV Área Verde |
|---|---|---|---|---|---|---|
| Densidad Bruta Máx. | 400 HAB/HA | 400 HAB/HA | 250 HAB/HA | 50 HAB/HA | 160 HAB/HA | Sin valor específico |
| Subdivisión Predial Mínima | 250 M² | 250 M² | 200 M² | 800 M² | 300 M² | 2.000 M² |
| COS (Residencial) | 0,9 | 0,8 | 0,7 | 0,5 | 0,6 | Sin valor específico |
| CC (Residencial) | 1,4 | 2 | 1,5 | 0,6 | 1 | Sin valor específico |
| Altura Máx. (Residencial) | 14,00 M / 4 pisos | 16,00 M / 4 pisos | 10,50 M / 3 pisos | 7,00 M / 2 pisos | 7,00 M / 2 pisos | Sin valor específico |
| Sistema Agrupamiento (Res.) | Aislado, pareado, continuo | Aislado, pareado, continuo | Aislado, pareado, continuo | Aislado, pareado, continuo | Aislado, pareado, continuo | Sin valor específico |
| Antejardín (Residencial) | Sin valor específico | 3,00 M | 3,00 M | 5,00 M | 5,00 M | Dato no determinable¹ |
| Rasantes / Distanc. / Adosam. | OGUC (las 3) | OGUC (las 3) | OGUC (las 3) | OGUC (las 3) | OGUC (las 3) | Dato no determinable¹ |
| N° columnas de la tabla de normas | 3 (sin Act.Prod. ni Infra.) | 4 (+Infra.) | 5 (+Act.Prod. +Infra.) | 4 (+Infra.) | 5 (+Act.Prod. +Infra.) | 3 (sin Act.Prod. ni Infra.) |

¹ Ver §9 — filas fuera del rango de páginas entregado (continúan en p.14, no incluida en este encargo).

**Patrón de densidad/altura:** las 4 zonas "Residencial Mixta" numeradas siguen un orden decreciente lógico de intensidad según su propio nombre — Z-3 "Densidad Media" (250 HAB/HA, 10,50 M) > Z-4 "Densidad Baja" (50 HAB/HA, 7,00 M) — con Z-5 "Productiva" (160 HAB/HA) como un perfil intermedio propio, no comparable en la misma escala por su naturaleza mixta con industria. Z-1 y Z-2 (centro histórico y eje comercial) concentran la mayor densidad y altura de las 6, coherente con ser el núcleo urbano consolidado de Angol.

---

## 13. Discrepancias y hallazgos respecto de la nota de Fase 3

1. **"p7 = cuadro estacionamientos mínimos (art.5)":** confirmado sin reservas. Tabla completa y legible, transcrita íntegra en §3. Hallazgo adicional: el `.txt` no aporta ni siquiera el título en esta página (peor que las páginas 8-13, que sí dan el título) — la dependencia de la imagen es total.
2. **"p8 Z-1, p9 Z-2, p10 Z-3, p11 Z-4, p12 Z-5, p13 Z-AV" (una página = una zona):** **el conteo y los nombres de zona son correctos** (6 zonas, exactamente esos 6 códigos, confirmados uno por uno — ver punto 3 abajo), pero **la asignación de página única es una simplificación que no corresponde a la realidad del documento**. Cada zona ocupa aproximadamente 1.5 páginas (tabla de usos de suelo + tabla de normas de edificación), y las 6 zonas quedan escalonadas: Z-1 realmente vive en p.8-9, Z-2 en p.9-10, Z-3 en p.10-11, Z-4 en p.11-12, Z-5 en p.12-13, y Z-AV *empieza* en p.13 pero su tabla de normas queda **incompleta** por fin de rango (ver punto 4). Se corrige esto en detalle en §2.
3. **Verificación del conteo de zonas (punto explícito pedido por el encargo):** se contaron personalmente, sin asumir el número de Fase 3. Resultado: **exactamente 6 zonas urbanas con tabla de usos de suelo + tabla de normas de edificación en el Art. 7, páginas 8-13**: Z-1 Centro Histórico, Z-2 Eje Bernardo O'Higgins, Z-3 Residencial Mixta Densidad Media, Z-4 Residencial Mixta Densidad Baja, Z-5 Residencial Mixta Productiva (nombre real, pese al error de título en su tabla de normas — ver punto 6), Z-AV Área Verde. Coincide exactamente con la lista de Fase 3, y también con la lista de "Zonas Urbanas" del Art. 6 (página 8). No se encontró una séptima zona urbana ni faltó ninguna de las 6.
4. **Hallazgo nuevo, no anticipado por Fase 3 — tabla de normas de Z-AV incompleta:** de las 10 filas esperables, solo 6 están dentro del rango de páginas entregado (7-13); las 4 restantes (Antejardín, Rasantes, Distanciamientos, Adosamientos) requerirían una página 14 que no fue parte de este encargo. Se marcaron explícitamente "Dato no determinable" con la razón exacta (fuera de rango, no ilegibilidad) — ver §9.
5. **Hallazgo nuevo — errata de copia-pega en el título de la tabla de normas de Z-5:** dice "...DENSIDAD MEDIA" (nombre de Z-3) en vez de "...PRODUCTIVA" (nombre real de Z-5). Ver §8.
6. **Hallazgo nuevo — tachado sin resolver en Z-AV/Esparcimiento:** la palabra "Todos" aparece tachada en la columna de permitidos, sin que la columna de prohibidos se completara. Ver §9.
7. **Hallazgo nuevo — "GASEODUCTO" (Z-3) en vez de "GASODUCTO":** errata ortográfica de la fuente, ver §6.
8. **Hallazgo nuevo, el más relevante para el uso posterior de estos datos — las tablas de usos de suelo NO son uniformes entre zonas pese a compartir plantilla:** Fase 3 no advirtió (ni tenía cómo saberlo, dado que solo veía títulos) que valores aparentemente repetidos entre zonas (p. ej., "Salud: Hospitales, clínicas, policlínicos, consultorios...") en realidad tienen diferencias reales y no triviales de qué queda permitido o prohibido, zona por zona — documentadas en detalle en cada sección y consolidadas en §12. Cualquier fase posterior que use estos datos para poblar el geolocalizador **no debe asumir que un valor de una zona aplica a otra similar** sin revisar la tabla específica.
9. **"Trampa comuna ajena":** verificada explícitamente, sin hallazgos — ver §11. Corroboración adicional no solicitada: el código de láminas "PRC 09201" coincide con el código INE real de Angol.
10. **No se usó "Dato no determinable" por ilegibilidad en ningún punto de este documento** — las únicas 4 instancias de "Dato no determinable" (Z-AV, filas finales de su tabla de normas) se deben a límite de rango de páginas, no a que una cifra fuera borrosa. Se marcaron así, con la razón explícita, siguiendo la convención del encargo de no usar esa etiqueta "por defecto" solo porque Fase 3 avisó de la trampa de imagen.

---

## 14. Notas finales de verificación

**Método:** lectura directa de las 7 imágenes PNG a 250 dpi, complementada con **más de 30 recortes ampliados (zoom 1.4×-8×, procesados con `PIL`)** sobre cada tabla numérica y sobre cada celda de texto donde una primera lectura dejaba duda — en particular: (a) las cifras de Altura Máxima de cada zona (para no confundir 14/16 M ni 1.500/1.600 M²); (b) las filas de Salud, Seguridad, Deporte, Esparcimiento, Transporte y Sanitaria de cada zona, cotejadas individualmente entre sí para no asumir uniformidad; (c) el título completo de la tabla de normas de Z-5, verificado letra por letra por lo inesperado del hallazgo; (d) el borde de cierre de página en cada transición Z-N→Z-N+1, para confirmar que ninguna fila quedó oculta en el corte.

**Resultado de la verificación imagen-vs-texto:** para las páginas 8-13, el `.txt` solo aporta el título de cada zona, que coincide exactamente con lo visible en la imagen (cero discrepancia en los títulos). Para la página 7, el `.txt` no aporta ningún contenido de la tabla — se dependió enteramente de la imagen, consistente con y más extremo que lo anticipado por Fase 3.

**Confianza por sección:**

| Sección | Confianza | Motivo |
|---|---|---|
| p.7 — cuadro de estacionamientos (Art. 5) | **Alta** | Tabla completa, nítida, verificada con zoom en las cifras ambiguas (1.500 M², M2 sin superíndice) |
| Zona Z-1 Centro Histórico | **Alta** | Usos de suelo y normas completos, verificados con zoom; sin cortes de página que perdieran datos |
| Zona Z-2 Eje Bernardo O'Higgins | **Alta** | Ídem; Altura Máxima (16,00 M) verificada con comparación directa de dígitos contra Z-1 |
| Zona Z-3 Residencial Mixta Densidad Media | **Alta** | Ídem; fila "Energética" y diferencia en Sanitaria verificadas dos veces por ser hallazgos inesperados |
| Zona Z-4 Residencial Mixta Densidad Baja | **Alta** | Ídem; verificado que no falta una fila de Actividades Productivas en el corte de página 11→12 |
| Zona Z-5 Residencial Mixta Productiva | **Alta** | Usos de suelo y normas completos y verificados; la errata del título se confirmó con zoom ×3, no es lectura dudosa |
| Zona Z-AV Área Verde — usos de suelo | **Alta** | Tabla completa; el tachado en Esparcimiento se verificó con zoom ×6, es un trazo real, no artefacto |
| Zona Z-AV Área Verde — normas de edificación | **Media-Alta para las 6 filas visibles; sin dato (por diseño del encargo, no por falla de lectura) para las 4 filas restantes** | Límite de rango de páginas, no de legibilidad — ver §9 |
| Verificación de conteo de zonas (6) y ausencia de comuna ajena | **Alta** | Verificado explícitamente contra el Art. 6 y contra el código INE de la lámina de plano |

**Nivel de confianza global: Alto**, con la única salvedad explícita y acotada de las 4 filas finales de la tabla de normas de Z-AV, que quedan fuera del rango de páginas de este encargo (no por ilegibilidad). No se inventó ningún valor: todo campo sin dato se marcó "Sin valor específico en la fuente" (con el motivo, cuando corresponde) o "Dato no determinable" (solo para Z-AV, con la razón exacta de rango explicada en cada celda).
