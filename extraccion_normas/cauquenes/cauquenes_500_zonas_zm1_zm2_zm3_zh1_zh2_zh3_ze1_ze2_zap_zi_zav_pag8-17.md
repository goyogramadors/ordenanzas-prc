# Ordenanza Local PRC Cauquenes (Decreto 500, 04-SEP-2009) — Art. 14 (Grupos G1-G5) y Art. 24 Normativa Específica, 11 Zonas de Área Urbana (ZM1, ZM2, ZM3, ZH1, ZH2, ZH3, ZE1, ZE2, ZAP, ZI, ZAV)

**Fuente:** Decreto 500 (2009), Ordenanza Local del Plan Regulador Comunal de Cauquenes, según texto publicado en Biblioteca del Congreso Nacional de Chile — www.leychile.cl (documento generado 22-Ene-2024).

**Rango de páginas de este documento:** páginas 8 a 17 de 24 (numeración impresa en pie de página, "página X de 24"). Cubre el cierre de un cuadro de estacionamientos (Art. 12, sin su encabezado, que está en la página 7 fuera de rango), el Art. 13, el Art. 14 completo (tabla clave de Grupos de Actividades G1-G5), los Art. 15 a 21 (condiciones especiales por uso, en prosa), el Art. 22 (Macro Áreas), el Art. 23 completo (cuadro índice de zonificación) y el Art. 24 (Normativa Específica por Zona) para las 11 zonas del literal a) Área Urbana. No cubre el literal b) Zonas No Edificables/Riesgo/Patrimonio (ZNE, ZRI1, ZRI2, ZCH, ICH), cuyo desarrollo en prosa comienza justo al final de la página 17 y continúa en páginas 18-19, fuera de este rango.

**Material usado:** imágenes PNG a 250 dpi (`cauquenes500_p8-17-08.png` … `cauquenes500_p8-17-17.png`, 2125×2750 px cada una) y texto plano de apoyo (`cauquenes500_p8-17.txt`). Cada página se leyó primero completa y luego se hicieron **más de 25 recortes con zoom (1,4×-4×, con `PIL`, varios con `autocontrast`)** sobre cada tabla y cada celda donde el primer vistazo dejaba duda, en particular las filas "Científico/Salud/Seguridad/Educación/Actividades Productivas" de cada zona (para no confundir a qué zona pertenece un valor) y las descripciones textuales del cuadro G1-G5.

**Documento previo — hallazgo relevante:** la carpeta `extraccion_normas/cauquenes/` ya contenía dos fichas de **enmiendas posteriores** al Decreto 500 (no de la ordenanza original, que es la fuente de este documento):

- `cauquenes_3519_enmienda_n1.md` (Decreto 3519, 2017): sube la Altura Máxima de **ZM3** a **18 metros**.
- `cauquenes_decreto_exento_1033_enmienda_02.md` (Decreto Exento 1033): sube la Altura Máxima de **ZM2** a **14,40 metros**, explicitando que equivale a "un incremento del 20% respecto de la altura anterior".

Estos dos documentos **no se editaron ni se usaron como fuente de valores** para este trabajo (que transcribe exclusivamente el Decreto 500/2009 original, páginas 8-17). Se usaron solo como **control aritmético externo**: 14,40 m ÷ 1,20 = **12,00 m**, que coincide exactamente con el valor de Altura Máxima que se transcribió aquí para ZM2 a partir de la imagen (ver §8 y §19). Esto es una confirmación cruzada independiente de que la lectura de ZM2 es correcta. Para ZM3, el valor aquí transcrito (15 metros, del texto original de 2009) **ya no es el vigente** — fue reemplazado por 18 metros en 2017; se deja la nota correspondiente en §10 y en §19 para que una fase posterior no interprete 15 m como la norma actualmente vigente.

---

## 0. Confirmación de estructura de la fuente ("trampa de imagen") y hallazgos generales de formato

- **El `.txt` (pdftotext) confirma exactamente lo anticipado por Fase 3:** para las páginas 12 a 17, el `.txt` entrega únicamente los títulos de zona y el texto corrido de los artículos en prosa — **cero contenido de las tablas** (cuadro de estacionamiento, cuadro G1-G5, índice de zonificación, cuadro de usos de suelo y cuadro de subdivisión/edificación de cada zona). Todas estas tablas son imagen pura y se transcribieron **exclusivamente a partir del PNG**.
- **Las tablas SÍ son perfectamente legibles a 250 dpi con zoom**, incluidos números pequeños (coeficientes con coma decimal, "G1 – G2*"), sin necesidad de volver a renderizar el PDF a mayor resolución.
- **Estructura real de las tablas de zona (Art. 24) — dos cuadros por zona, salvo dos excepciones (ver más abajo):**
  1. **"NORMAS DE USOS DE SUELO"**, con columnas TIPO / CLASE / ACTIVIDADES PERMITIDAS / ACTIVIDADES PROHIBIDAS. La fila "RESIDENCIAL" y la fila "ACTIVIDADES PRODUCTIVAS" son TIPO sin CLASE (van directo a valores); el TIPO "EQUIPAMIENTO" sí se abre en hasta 10 CLASE distintas (Científico, Comercio, Culto y Cultura, Deporte, Educación, Esparcimiento, Salud, Seguridad, Servicios, Social) — **el número real de CLASE presentes varía por zona** (ver §6-§16, algunas zonas omiten Esparcimiento, Seguridad o Salud). Cierra con una fila fija "USOS DE SUELO PROHIBIDOS: TODOS LOS NO MENCIONADOS COMO PERMITIDOS".
  2. **"NORMAS DE SUBDIVISIÓN Y EDIFICACIÓN"**, con una fila por parámetro y una sola columna de valor (a diferencia de otros PRC del corpus como Angol, aquí **no hay columnas separadas por tipo de uso** — un único valor por parámetro para toda la zona). El conjunto de parámetros presentes **varía por zona**: no todas traen Antejardín, Densidad Máxima o Distancia a Medianeros (ver cuadro comparativo, §18).
  - **Excepción 1 — ZE2 (Cementerio):** no tiene ninguno de los dos cuadros. Se regula enteramente en prosa, remitiendo al Código Sanitario y al artículo 2.6.3 de la OGUC, más una exigencia textual de 30% mínimo de área verde. Ver §13.
  - **Excepción 2 — ZAV (Área Verde):** tampoco tiene los dos cuadros. Es un único párrafo que remite al artículo 2.1.31 de la OGUC. Ver §16.
  - Este hallazgo (2 de las 11 zonas sin cuadros numéricos propios) **no estaba anticipado por la nota de Fase 3**, que da a entender que las 11 zonas traen "DOS cuadros por zona" de forma uniforme. Ver §20.
- **Convención propia de la fuente para celdas sin valor:** dentro de las tablas de usos de suelo, la columna "Prohibidas" usa mayoritariamente un guion corto ("-") cuando no hay actividad prohibida específica (más allá de la cláusula general de cierre). En la tabla G1-G5 (página 9) las celdas sin actividad asignada muestran igualmente un punto/guion corto tipográfico; en un caso (RESIDENCIAL, columnas G4-G5) la celda está completamente en blanco, sin ni siquiera ese marcador — diferencia visual menor, documentada en §4, sin que se le atribuya un significado distinto.
- **Un cuadro adicional no listado explícitamente por Fase 3 dentro del cuadro de estacionamiento:** además del cuadro principal por USO/TIPO/CLASE (Residencial, Equipamiento, Actividades Productivas), la página 8 trae una **subtabla separada "INFRAESTRUCTURA"** (Terminales de radio taxis y colectivos, Estaciones de transporte terrestre/buses, Centrales de distribución de energía) con su propio estándar de estacionamiento. Ver §3.

---

## 1. Convenciones usadas en este documento

- **"Sin valor específico en la fuente":** para parámetros que una zona genuinamente no fija (fila ausente del cuadro de subdivisión/edificación, verificado visualmente que la tabla cierra sin esa fila) o para ZE2/ZAV, que no tienen cuadro numérico alguno.
- **"Dato no determinable":** reservado para texto o cifras presentes pero ilegibles incluso tras zoom. **No se usó ni una sola vez en este documento** — todas las celdas revisadas resultaron legibles con zoom de hasta 4×. Se deja constancia explícita de esto en §21.
- **`[sic]`:** marca erratas o redacciones atípicas de la fuente, preservadas tal cual, sin corregir. Ver lista consolidada en §20.
- **Separador de listas de grupos:** la fuente imprime los códigos de grupo separados por guion medio, p. ej. "G1 – G2 – G3". Se transcribe aquí de forma uniforme como "G1-G2-G3" (sin espacios), sin que esto altere el contenido.
- **Coma decimal:** se preserva tal como aparece en la fuente ("0,5", "2,5"), a diferencia de otros documentos del corpus que usan punto decimal.
- **"m2" / "m²":** la fuente de Cauquenes imprime consistentemente "m2" en línea (sin superíndice) en las tablas de zona; se preserva así, sin agregar el superíndice.
- **Celdas con doble valor condicional** (p. ej. superficie predial mínima distinta según uso, o antejardín distinto según localidad): no son un desglose que deba sumar a un total — son dos valores alternativos según condición. Se transcriben ambos, con la condición asociada, sin operar aritmética entre ellos (no corresponde).

---

## 2. Correspondencia de páginas — dónde vive cada zona

Al igual que en otros PRC del corpus, **el título de cada zona aparece al final de una página, y su(s) cuadro(s) numérico(s) aparece(n) al inicio de la página siguiente** (nunca a mitad de una tabla partida por una cifra). Detalle verificado imagen por imagen:

| Archivo | Página impresa | Contenido |
|---|---|---|
| `cauquenes500_p8-17-08.png` | página 8 de 24 | Cierre de un cuadro de estándares de estacionamiento (Art. 12, sin su encabezado — está en la página 7, fuera de rango) clasificado por G1-G5; Art. 13 (remisión al Art. 23); Art. 14 (título + párrafo introductorio del cuadro de grupos G1-G5, cuyo cuerpo aparece en la página siguiente) |
| `cauquenes500_p8-17-09.png` | página 9 de 24 | Cuadro completo de **Grupos de Actividades G1-G5** (Art. 14); Art. 15 y 16 completos; Art. 17 (inicio; la tabla de condiciones especiales para supermercados se corta a mitad) |
| `cauquenes500_p8-17-10.png` | página 10 de 24 | Art. 17 cont. (cierre tabla condiciones supermercados); Art. 18 completo (terminales de locomoción colectiva); Art. 19 (inicio) |
| `cauquenes500_p8-17-11.png` | página 11 de 24 | Art. 19 cont.; Art. 20 completo; Art. 21 completo (uso de suelo infraestructura); Capítulo V; Art. 22 (inicio, macro áreas) |
| `cauquenes500_p8-17-12.png` | página 12 de 24 | Art. 22 cont. (a) Área Urbana / b) Zonas no edificables); Art. 23 (Zonificación) con el **cuadro índice completo de las 11 zonas** de área urbana + 4 categorías de zonas no edificables/riesgo/patrimonio; Art. 24 (inicio) con el título "ZM1 ZONA MIXTA COMERCIO Y SERVICIOS" (solo el título — sus tablas están en la página siguiente) |
| `cauquenes500_p8-17-13.png` | página 13 de 24 | **ZM1** (2 tablas completas) + **ZM2** (2 tablas completas + nota de "Condiciones especiales") + título "ZM3" |
| `cauquenes500_p8-17-14.png` | página 14 de 24 | **ZM3** (2 tablas completas) + **ZH1** (2 tablas completas) + título "ZH2" |
| `cauquenes500_p8-17-15.png` | página 15 de 24 | **ZH2** (2 tablas completas) + **ZH3** (2 tablas completas) + título "ZE1" |
| `cauquenes500_p8-17-16.png` | página 16 de 24 | **ZE1** (2 tablas completas) + **ZE2** (prosa completa, sin cuadro numérico) + título "ZAP" |
| `cauquenes500_p8-17-17.png` | página 17 de 24 | **ZAP** (2 tablas completas) + **ZI** (2 tablas completas) + **ZAV** (prosa completa, sin cuadro numérico) + inicio de "b) ZONAS NO EDIFICABLES..." con título "ZNE ZONA NO EDIFICABLE" (**fuera del alcance de este encargo**) |

**Verificación de cortes de página:** en ningún caso una tabla se corta a mitad de una cifra o de una fila — el corte siempre cae en el borde de una fila completa o (más frecuentemente) justo entre el título de una zona y el inicio de su primer cuadro.

---

## 3. Página 8 — cuadro de estándares de estacionamiento (Art. 12, contexto — no es norma de zona)

**Nota de alcance:** este cuadro no es uno de los 11 cuadros de zona pedidos por el encargo (esos están en el Art. 24, §6-§16). Se documenta aquí su estructura, tal como pide el punto 7 del encargo, para confirmar o corregir la nota de Fase 3 — no se transcribe celda por celda.

Encabezado de la propia tabla (texto de la fuente): *"Los estándares de estacionamiento son los que se establecen en el cuadro siguiente, por uso, clase y actividad, según la clasificación que se establece en el Artículo 14 de la presente OL. Las cifras con decimales resultantes se aproximarán al entero superior. Cuando el resultado sea inferior a 1, se exigirá un estacionamiento."* Este párrafo, y la tabla que le sigue, aparecen **antes** del propio Art. 13/14 en el flujo de la página — es decir, son la cola de un artículo anterior (probablemente Art. 12 "Estacionamientos", cuyo encabezado estaría en la página 7, fuera de este rango).

**Estructura confirmada (coincide con, y amplía, la nota de Fase 3 "cuadro estandares de estacionamiento por uso/clase"):**
- Tabla principal, columnas G1 a G5 (cada una subdividida en "Automóviles" / "Módulos de Bicicletas"), organizada por:
  - USO=RESIDENCIAL, filas por "Destino" (Vivienda hasta 140 m2, Vivienda más de 140 m2, Edificio Deptos. de más de 140 m2, Edificio Deptos. de más de 100 m2, Edificio Deptos. de Viv. Social).
  - USO=EQUIPAMIENTO, filas por "Clase" (Científico, Comercio, Culto y Cultura, Deporte, Educación, Esparcimiento, Salud, Seguridad, Servicios, Social) — el mismo listado de 10 clases que trae el cuadro G1-G5 del Art. 14.
  - TIPO=ACTIVIDADES PRODUCTIVAS, una fila.
- **Hallazgo — subtabla separada no anticipada explícitamente por Fase 3:** debajo de la tabla principal hay un segundo cuadro independiente, "INFRAESTRUCTURA", con 3 filas (Terminales de Radio taxis y colectivos; Estaciones de transporte terrestre/buses; Centrales de distribución de energía) y sus propios estándares (p. ej. Terminales: "1 c/200 m2 construidos, Mínimo 4" automóviles / "1 c/500 m2 terreno" bicicletas).
- **Conclusión sobre la nota de Fase 3:** la descripción "cuadro estandares de estacionamiento por uso/clase" es correcta pero incompleta — falta mencionar la subtabla de Infraestructura y el hecho de que la tabla no arranca con el Art. 12/13, sino que es la cola de contenido previo a la página 8.

---

## 4. Tabla clave — Grupos de Actividades G1-G5 (Artículo 14, página 9)

Cuadro completo, transcrito y verificado con zoom en cada celda. Esta es la tabla que referencian todas las zonas del Art. 24 mediante los códigos "G1"… "G5".

**RESIDENCIAL** *(fila TIPO sin CLASE)*

| G1 | G2 | G3 | G4 | G5 |
|---|---|---|---|---|
| Viviendas en propiedad individual o copropiedad. | Edificaciones destinadas al hospedaje remunerado o gratuito (sin salones, bares y restoranes `[sic: grafía informal; forma estándar "restaurantes"]`). | Hogares de acogida de niños, estudiantes, ancianos y similares. | *(celda en blanco en la fuente, sin marcador — ver nota en §0)* | *(celda en blanco en la fuente, sin marcador — ver nota en §0)* |

**EQUIPAMIENTO** *(TIPO / CLASE)*

| Clase | G1 | G2 | G3 | G4 | G5 |
|---|---|---|---|---|---|
| **Científico** *(sin frase descriptiva propia en la fuente, a diferencia de las demás clases)* | Establecimientos destinados a la investigación y divulgación científica, al desarrollo y transferencia tecnológico y o la innovación técnica `[sic: redacción de la fuente; se esperaría "tecnológica y/o a la"]`. | - | - | - | - |
| **Comercio** — *"Locales o centros comerciales destinados a la compraventa de:"* | Mercaderías manufacturados diversos, artículos para el hogar u oficina y sus repuestos, tales como perfumerías, ferreterías, paqueterías, librerías, tiendas de vestuario y similares. | Alimentos, bebidas y medicamentos para consumo fuera del recinto, tales como minimarket, almacenes, farmacias, botillerías, mercados, supermercados y similares. | Alimentos y bebidas con y sin contenido alcohólico con consumo en el mismo recinto, tales como cafeterías, salones de té, fuentes de soda, restaurantes, bares, pubs y similares. | Combustibles sólidos y líquidos (leña, carbón, gas licuado, bencina, parafina, etc.) y estaciones o centros de servicio automotor. Automóviles y maquinarias. | Materiales de construcción. |
| **Culto y Cultura** — *"Establecimientos destinados a actividades de desarrollo espiritual, religioso o cultural, tales como:"* | Capillas, salones, oratorios, iglesias, mezquitas, sinagogas, templos, parroquias, santuarios y similares. | Bibliotecas, galerías de arte, centros culturales, salas de concierto, teatros, cines, espectáculos, medios de comunicaciones (radio o TV). | Centros de convenciones, auditorios, museos. | - | - |
| **Deporte** — *"Establecimientos destinados a actividades de práctico o enseñanza de cultura física, tales como:"* `[sic: "práctico" — se esperaría "práctica"]` | Centros y clubes deportivos, gimnasios, multicanchas, sauna, baños turcos, piscinas, en recintos cerrados y abiertos. | Estadios, canchas de patinaje, grandes complejos deportivos. | - | - | - |
| **Educación** — *"Establecimientos destinados a la formación en educación pública y privado, tales como:"* `[sic: "privado" — se esperaría "privada"]` | Jardines infantiles, salas cuna, parvularios. | Colegios básicos o diferenciales. | Liceos humanistas científicos o técnico profesionales. | Centros de Capacitación, Academias de arte y oficios, preuniversitarios, sedes o campus universitarios, centros de formación tecnológica o científica. | - |
| **Esparcimiento** — *"Establecimientos destinados a actividades recreativas en recintos cerrados o al aire libre."* | Juegos no mecánicos (billar, ping pong, video juegos) | Parques zoológicos y de entretenciones. | - | - | - |
| **Salud** — *"Establecimientos destinados a la prevención, tratamiento y recuperación de la salud."* | Servicios de medicina general ambulatoria tales como consultorios y policlínicos médicos, dentales y veterinarios. | Centros de Diagnóstico, tratamientos, exploración, rehabilitación y laboratorios. | Centros de Urgencia y primeros auxilios como postas. | Hospitales, Maternidades, Clínicas, Morgue. | Cementerios y Crematorios. |
| **Seguridad** — *"Establecimientos destinados a unidades encargadas de seguridad público y privado."* `[sic: se esperaría "pública y privada"]` | Unidades policiales, retenes, comisarías, subcomisarías, cuarteles de bomberos. | Centros de detención, centro penitenciario, y centros de rehabilitación delictual. | - | - | - |
| **Servicios** — *"Establecimientos destinados a actividades de servicios, artesanales y profesionales públicos y privados."* | Oficinas, notarías, centros de pago, correos, centros de llamado e internet, Bancos, Administradoras de de Fondos de Pensiones `[sic: "de de" duplicado]`, Compañías de Seguros, oficinas Municipales, Juzgados, Instituciones Previsionales de Salud. | Servicios artesanales de reparación y oficios: peluquería, servicio técnico de artículos electrónicos electrodomésticos, bicicletas, relojerías, grabados y joyas, pequeños jardines de plantas, servicios de gasfitería, lavanderías, talleres de fotografía, fotocopias, reparadora de calzado, talabarterías, ropa, sastrería, costuras, modas, Panaderías, tintorerías, servicios artesanales de reparación de objetos diversos. | - | - | - |
| **Social** — *"Establecimientos destinados a actividades comunitarias tales como:"* | Sedes sociales, juntas de vecinos, centros de madres, centros para el adulto mayor. | Clubes sociales, sedes de organizaciones e instituciones deportivas, culturales y juveniles. | - | - | - |

**ACTIVIDADES PRODUCTIVAS** *(fila TIPO sin CLASE)* — *"Este uso se rige por lo dispuesto en el Artículo 2.1.28 de la OGUC; las actividades productivas pueden ser industriales o de impacto similar al industrial:"*

| G1 | G2 | G3 | G4 | G5 |
|---|---|---|---|---|
| Actividades productivas industriales, tales como industrias, talleres y talleres artesanales, clasificadas como inofensivas. | Actividades de impacto similar al industrial, tales como almacenamiento o bodegaje, frigoríficos, depósitos de vehículos o maquinarias, venta de materiales de construcción, centros de reparación automotor, entre otras, clasificadas como inofensivas. | Actividades productivas industriales, tales como industrias, talleres y talleres artesanales, clasificadas como molestas. | Actividades de impacto similar al industrial, tales como almacenamiento o bodegaje, frigoríficos, depósitos de vehículos o maquinarias, venta de materiales de construcción, centros de reparación automotor, entre otras, clasificadas como molestas. | *(en blanco)* |

**Patrón verificado con zoom (columna alineada bajo el encabezado G1-G5 de la fila superior de la misma tabla):** G1/G3 agrupan el mismo texto ("industriales... talleres artesanales") distinguidos solo por "inofensivas" (G1) vs. "molestas" (G3); G2/G4 agrupan el mismo texto ("impacto similar al industrial... bodegaje") distinguidos por "inofensivas" (G2) vs. "molestas" (G4). Esta simetría es la que después permite entender, por ejemplo, que ZI (Zona Industrial) autorice "Todas" las actividades productivas (G1-G4 sin excepción, ver §15) mientras otras zonas solo autorizan G1-G2 (las calificadas inofensivas).

---

## 5. Cuadro índice de zonificación (Artículo 23, página 12)

Transcrito completo. **Confirma exactamente las 11 zonas listadas en el encargo, sin faltantes ni sobrantes.**

**a) ÁREA URBANA**

| Código | Nombre |
|---|---|
| ZM1 | Zona Mixta Comercio y Servicios |
| ZM2 | Zona Mixta Residencial, Comercio y Servicios |
| ZM3 | Zona Mixta Residencial y Equipamiento Educacional |
| ZH1 | Zona Habitacional 1 |
| ZH2 | Zona Habitacional 2 |
| ZH3 | Zona Habitacional 3 |
| ZE1 | Zona de Equipamiento Público y Privado |
| ZE2 | Cementerio |
| ZAP | Zona de Actividades Productivas |
| ZI | Zona Industrial |
| ZAV | Zona Área Verde |

**b) ZONAS NO EDIFICABLES, ÁREAS DE RIESGO Y PROTECCIÓN PATRIMONIAL CULTURAL** *(fuera del alcance de este encargo — su desarrollo en prosa está en páginas 18-19; se deja listado aquí solo porque el índice mismo cae dentro del rango 8-17)*

| Categoría | Código | Nombre |
|---|---|---|
| Zonas no Edificables | ZNE | Zona No Edificable |
| Áreas de Riesgo | ZRI1 | Zona de Riesgo por Inundación 1 |
| Áreas de Riesgo | ZRI2 | Zona d e Riesgo por Inundación 2 `[sic: espacio suelto entre "d" y "e" en la fuente]` |
| Áreas Protección Patrimonial Cultural | ZCH | Zona de Conservación Histórica |
| Áreas Protección Patrimonial Cultural | ICH | Inmueble de Conservación Histórica |

**Verificación de conteo (punto explícito pedido por el encargo):** se contaron personalmente 11 zonas en el literal a), ni una más ni una menos, y las 11 coinciden en código y orden con las que pide el encargo (ZM1, ZM2, ZM3, ZH1, ZH2, ZH3, ZE1, ZE2, ZAP, ZI, ZAV). El índice, por tanto, **sí coincide exactamente** con la lista del encargo — no hay discrepancia aquí, a diferencia de lo que insinúa el punto 7 del encargo como posibilidad a chequear.

**Erratum de referencia cruzada interna (Art. 23):** el propio texto del Art. 23 dice *"Las macro áreas descritas en el Artículo 21 se dividen en las zonas que se señalan a continuación..."* — pero las macro áreas (a) Área Urbana, b) Zonas no edificables...) están descritas en el **Artículo 22** ("MACRO ÁREAS", página 11), no en el Artículo 21 (que es "USO DE SUELO INFRAESTRUCTURA"). Se preserva el error de numeración `[sic]` tal como aparece.

---

## 6. ZM1 — ZONA MIXTA COMERCIO Y SERVICIOS (página 13)

### Normas de usos de suelo

| Tipo | Clase | Actividades permitidas | Actividades prohibidas |
|---|---|---|---|
| RESIDENCIAL | — | G1-G2-G3 | Motel |
| EQUIPAMIENTO | Científico | G1-G2-G3-G4-G5 | - |
| EQUIPAMIENTO | Comercio | G1-G2-G3 | Supermercado más de 1.000 m2 construidos. |
| EQUIPAMIENTO | Culto y Cultura | G1-G2-G3 | - |
| EQUIPAMIENTO | Deporte | G1 | - |
| EQUIPAMIENTO | Educación | G1-G2-G3-G4 | - |
| EQUIPAMIENTO | Esparcimiento | G1-G2 | - |
| EQUIPAMIENTO | Salud | G1-G2-G3-G4-G5 | - |
| EQUIPAMIENTO | Seguridad | G1-G2 `(*)` | - |
| EQUIPAMIENTO | Servicios | G1-G2 | - |
| EQUIPAMIENTO | Social | G1-G2 | - |
| ACTIVIDADES PRODUCTIVAS | — | G1-G2 | Talleres y fábricas de confección, talleres mecánicos de mantención, editoriales e imprentas. Frigoríficos, laboratorios médicos, distribuidoras por mayor, químicos y sólidos inofensivos. Talleres o bodegas industriales. |
| **USOS DE SUELO PROHIBIDOS** | | TODOS LOS NO MENCIONADOS COMO PERMITIDOS | |

`(*)` Nota al pie de la fuente: *"Sólo se permite en la Localidad de Santa Sofía."* (Santa Sofía es una localidad rural de la comuna de Cauquenes — confirma que el documento es de Cauquenes, ver §17).

**Nota estructural:** ZM1 es la única de las 11 zonas donde Científico y Salud permiten los 5 grupos (G1-G5) completos — es, en ese sentido, la zona con el uso de suelo de equipamiento más amplio del PRC.

### Normas de subdivisión y edificación

| Parámetro (rótulo exacto de la fuente) | Valor |
|---|---|
| SUPERFICIE PREDIAL MÍNIMA: | 300 m2 |
| COEFICIENTE DE OCUPACIÓN DE SUELO | 1 |
| COEFICIENTE DE CONSTRUCTIBILIDAD | 2,5 |
| ALTURA MÁXIMA | 30 metros |
| SISTEMA DE AGRUPAMIENTO | Continuo - Pareado |
| ANTEJARDÍN | Sin valor específico en la fuente (fila ausente del cuadro) |
| DENSIDAD MÁXIMA | Sin valor específico en la fuente (fila ausente del cuadro) |

---

## 7. ZM2 — ZONA MIXTA RESIDENCIAL, COMERCIO Y SERVICIOS (página 13)

### Normas de usos de suelo

| Tipo | Clase | Actividades permitidas | Actividades prohibidas |
|---|---|---|---|
| RESIDENCIAL | — | G1-G2-G3 | Sin valor específico en la fuente |
| EQUIPAMIENTO | Científico | G1 | - |
| EQUIPAMIENTO | Comercio | G1-G2-G3-G4 | Venta de automóviles y maquinarias. |
| EQUIPAMIENTO | Culto y Cultura | G1-G2-G3 | - |
| EQUIPAMIENTO | Deporte | G1 | - |
| EQUIPAMIENTO | Educación | G1-G2-G3-G4 | - |
| EQUIPAMIENTO | Esparcimiento | G1 | - |
| EQUIPAMIENTO | Salud | G1-G2-G3-G4 | - |
| EQUIPAMIENTO | Seguridad | G1 | - |
| EQUIPAMIENTO | Servicios | G1-G2 | - |
| EQUIPAMIENTO | Social | G1-G2 | - |
| ACTIVIDADES PRODUCTIVAS | — | G1-G2 | Frigoríficos, laboratorios médicos, distribuidoras por mayor, químicos y sólidos inofensivos. Talleres o bodegas industriales. |
| **USOS DE SUELO PROHIBIDOS** | | TODOS LOS NO MENCIONADOS COMO PERMITIDOS | |

### Normas de subdivisión y edificación

| Parámetro (rótulo exacto de la fuente) | Valor |
|---|---|
| SUPERFICIE PREDIAL MÍNIMA: | 200 m2 |
| COEFICIENTE DE OCUPACIÓN DE SUELO | 0,7 |
| COEFICIENTE DE CONSTRUCTIBILIDAD | 1,5 |
| ALTURA MÁXIMA | 12 metros — **superada por la Enmienda N°2 (Decreto Exento 1033), que la fija en 14,40 metros (+20%); ver §1 y §19** |
| SISTEMA DE AGRUPAMIENTO | Continuo - Pareado - Aislado |
| ANTEJARDÍN | 3 metros |
| DENSIDAD MÁXIMA | Sin valor específico en la fuente (fila ausente del cuadro) |

**Condiciones especiales (nota textual adicional de la fuente, fuera de la estructura estándar de las dos tablas):** *"los predios que enfrenten la zona ZM1 podrán incrementar en un 30% el coeficiente de ocupación de suelo, el coeficiente de constructibilidad y la altura, siempre que el uso de suelo predominante en el primer piso sea el de equipamiento."* Esta nota es exclusiva de ZM2 dentro de las 11 zonas revisadas — ninguna otra trae una cláusula de incremento condicional equivalente.

---

## 8. ZM3 — ZONA MIXTA RESIDENCIAL Y EQUIPAMIENTO EDUCACIONAL (página 14)

### Normas de usos de suelo

| Tipo | Clase | Actividades permitidas | Actividades prohibidas |
|---|---|---|---|
| RESIDENCIAL | — | G1-G2-G3 | Moteles |
| EQUIPAMIENTO | Científico | G1 | - |
| EQUIPAMIENTO | Comercio | "Solo en un 15% de la superficie edificada y siempre que el destino principal sea educación" *(texto condicional, no códigos G — ver nota)* | - |
| EQUIPAMIENTO | Culto y Cultura | G1-G2-G3 | - |
| EQUIPAMIENTO | Deporte | G1-G2 | - |
| EQUIPAMIENTO | Educación | G1-G2-G3-G4 | - |
| EQUIPAMIENTO | Salud | G1-G2-G3-G4-G5 | - |
| EQUIPAMIENTO | Social | G1-G2 | - |
| **USOS DE SUELO PROHIBIDOS** | | TODOS LOS NO MENCIONADOS COMO PERMITIDOS | |

**Nota estructural — verificada con zoom:** ZM3 **no tiene** filas de Esparcimiento ni Seguridad en Equipamiento, y **no tiene** fila de TIPO "ACTIVIDADES PRODUCTIVAS" (a diferencia de ZM1 y ZM2). Coherente con ser una zona mixta residencial + educacional, sin vocación industrial. La celda de "Comercio" usa una condición en prosa en vez de códigos G1-G5, igual que ZE1 (§11) — mismo patrón textual, distinta condición ("educación" aquí, "deportivo" en ZE1).

### Normas de subdivisión y edificación

| Parámetro (rótulo exacto de la fuente) | Valor |
|---|---|
| SUPERFICIE PREDIAL MÍNIMA: | 2.000 m2 Equipamiento Educación / 300 m2 Otros Usos *(dos valores condicionales, no un desglose que sume — se transcriben ambos)* |
| COEFICIENTE DE OCUPACIÓN DE SUELO | 0,5 |
| COEFICIENTE DE CONSTRUCTIBILIDAD | 2,5 |
| ALTURA MÁXIMA | 15 metros — **superada por la Enmienda N°1 (Decreto 3519, 2017), que la fija en 18 metros; ver §1 y §19. El valor aquí transcrito es el original de 2009, ya no vigente.** |
| SISTEMA DE AGRUPAMIENTO | Aislado |
| ANTEJARDÍN | 12 metros |
| DENSIDAD MÁXIMA | Sin valor específico en la fuente (fila ausente del cuadro) |

---

## 9. ZH1 — ZONA HABITACIONAL 1 (página 14)

### Normas de usos de suelo

| Tipo | Clase | Actividades permitidas | Actividades prohibidas |
|---|---|---|---|
| RESIDENCIAL | — | G1-G2-G3 | Moteles |
| EQUIPAMIENTO | Científico | G1 | - |
| EQUIPAMIENTO | Comercio | G1-G2-G3-G4 | Compra y Venta de automóviles y maquinarias. |
| EQUIPAMIENTO | Culto y Cultura | G1-G2-G3 | - |
| EQUIPAMIENTO | Deporte | G1 | - |
| EQUIPAMIENTO | Educación | G1-G2-G3-G4 | - |
| EQUIPAMIENTO | Esparcimiento | G1 | - |
| EQUIPAMIENTO | Salud | G1-G2-G3-G4 | - |
| EQUIPAMIENTO | Seguridad | G1 | - |
| EQUIPAMIENTO | Servicios | G1-G2 | - |
| EQUIPAMIENTO | Social | G1-G2 | - |
| **USOS DE SUELO PROHIBIDOS** | | TODOS LOS NO MENCIONADOS COMO PERMITIDOS | |

**Nota:** sin fila de "ACTIVIDADES PRODUCTIVAS" (coherente con ser zona puramente habitacional).

### Normas de subdivisión y edificación

| Parámetro (rótulo exacto de la fuente) | Valor |
|---|---|
| SUPERFICIE PREDIAL MÍNIMA: | 130 m2 |
| COEFICIENTE DE OCUPACIÓN DE SUELO | 0,8 |
| COEFICIENTE DE CONSTRUCTIBILIDAD | 1 |
| ALTURA MÁXIMA | 12 metros |
| SISTEMA DE AGRUPAMIENTO | Aislado y Pareado |
| ANTEJARDÍN | 3 metros |
| DENSIDAD MÁXIMA | 200 hab/há |

---

## 10. ZH2 — ZONA HABITACIONAL 2 (página 15)

### Normas de usos de suelo

| Tipo | Clase | Actividades permitidas | Actividades prohibidas |
|---|---|---|---|
| RESIDENCIAL | — | G1-G2-G3 | Moteles |
| EQUIPAMIENTO | Científico | G1 | - |
| EQUIPAMIENTO | Comercio | G1-G2-G3-G4 | Fuentes de soda, bares, pubs y similares. Compra y Venta de automóviles y maquinarias. |
| EQUIPAMIENTO | Culto y Cultura | G1-G2-G3 | - |
| EQUIPAMIENTO | Deporte | G1 | - |
| EQUIPAMIENTO | Educación | G1-G2-G3-G4 | - |
| EQUIPAMIENTO | Esparcimiento | G1 | - |
| EQUIPAMIENTO | Salud | G1-G2-G3-G4 | - |
| EQUIPAMIENTO | Seguridad | G1 | - |
| EQUIPAMIENTO | Servicios | G1-G2 | - |
| EQUIPAMIENTO | Social | G1-G2 | - |
| **USOS DE SUELO PROHIBIDOS** | | TODOS LOS NO MENCIONADOS COMO PERMITIDOS | |

### Normas de subdivisión y edificación

| Parámetro (rótulo exacto de la fuente) | Valor |
|---|---|
| SUPERFICIE PREDIAL MÍNIMA: | 300 m2 |
| COEFICIENTE DE OCUPACIÓN DE SUELO | 0,8 |
| COEFICIENTE DE CONSTRUCTIBILIDAD | 1 |
| ALTURA MÁXIMA | 6 metros |
| SISTEMA DE AGRUPAMIENTO | Aislado |
| ANTEJARDÍN | 3 metros |
| DENSIDAD MÁXIMA | 120 hab/há |

---

## 11. ZH3 — ZONA HABITACIONAL 3 (página 15)

### Normas de usos de suelo

**Hallazgo verificado con zoom, carácter por carácter:** la tabla de usos de suelo de ZH3 es **idéntica** a la de ZH2 (mismas 11 filas, mismo texto exacto en permitidas y prohibidas). No es un error de esta transcripción — se comparó dos veces contra la imagen por lo inesperado de la coincidencia total. Se reproduce completa para que cada zona quede autocontenida:

| Tipo | Clase | Actividades permitidas | Actividades prohibidas |
|---|---|---|---|
| RESIDENCIAL | — | G1-G2-G3 | Moteles |
| EQUIPAMIENTO | Científico | G1 | - |
| EQUIPAMIENTO | Comercio | G1-G2-G3-G4 | Fuentes de soda, bares, pubs y similares. Compra y Venta de automóviles y maquinarias. |
| EQUIPAMIENTO | Culto y Cultura | G1-G2-G3 | - |
| EQUIPAMIENTO | Deporte | G1 | - |
| EQUIPAMIENTO | Educación | G1-G2-G3-G4 | - |
| EQUIPAMIENTO | Esparcimiento | G1 | - |
| EQUIPAMIENTO | Salud | G1-G2-G3-G4 | - |
| EQUIPAMIENTO | Seguridad | G1 | - |
| EQUIPAMIENTO | Servicios | G1-G2 | - |
| EQUIPAMIENTO | Social | G1-G2 | - |
| **USOS DE SUELO PROHIBIDOS** | | TODOS LOS NO MENCIONADOS COMO PERMITIDOS | |

### Normas de subdivisión y edificación

**A diferencia de los usos de suelo, este cuadro SÍ es distinto del de ZH2** (menor densidad/mayor predio mínimo, coherente con "Habitacional 3" siendo la más extensiva de las tres):

| Parámetro (rótulo exacto de la fuente) | Valor |
|---|---|
| SUPERFICIE PREDIAL MÍNIMA: | 1.000 m2 |
| COEFICIENTE DE OCUPACIÓN DE SUELO | 0,3 |
| COEFICIENTE DE CONSTRUCTIBILIDAD | 0,4 |
| ALTURA MÁXIMA | 6 metros |
| SISTEMA DE AGRUPAMIENTO | Aislado |
| ANTEJARDÍN | 5 metros |
| DENSIDAD MÁXIMA | 120 hab/há |

---

## 12. ZE1 — ZONA DE EQUIPAMIENTO PÚBLICO Y PRIVADO (página 15→16)

### Normas de usos de suelo

| Tipo | Clase | Actividades permitidas | Actividades prohibidas |
|---|---|---|---|
| RESIDENCIAL | — | "Sólo la vivienda del cuidador." *(texto condicional, no código G)* | - |
| EQUIPAMIENTO | Científico | G1 | - |
| EQUIPAMIENTO | Comercio | "Solo en un 15% de la superficie edificada y siempre que el destino principal sea deportivo." *(texto condicional, no código G)* | - |
| EQUIPAMIENTO | Culto y Cultura | G1-G2-G3 | - |
| EQUIPAMIENTO | Deporte | G1-G2 | - |
| EQUIPAMIENTO | Educación | G1-G2-G3-G4 | - |
| EQUIPAMIENTO | Salud | G1-G2-G3-G4 | - |
| EQUIPAMIENTO | Seguridad | G1 | - |
| EQUIPAMIENTO | Servicios | G1-G2 | - |
| EQUIPAMIENTO | Social | G1-G2 | - |
| **USOS DE SUELO PROHIBIDOS** | | TODOS LOS NO MENCIONADOS COMO PERMITIDOS | |

**Nota estructural:** sin fila de Esparcimiento ni de "ACTIVIDADES PRODUCTIVAS". La fila RESIDENCIAL usa el mismo patrón textual "Sólo la vivienda del cuidador" que reaparece en ZAP y ZI (§14, §15) — común a las zonas no propiamente habitacionales.

### Normas de subdivisión y edificación

| Parámetro (rótulo exacto de la fuente) | Valor |
|---|---|
| SUPERFICIE PREDIAL MÍNIMA: | 2.000 m2 |
| COEFICIENTE DE OCUPACIÓN DE SUELO | 0,5 |
| COEFICIENTE DE CONSTRUCTIBILIDAD | 1 |
| ALTURA MÁXIMA | 12 metros |
| SISTEMA DE AGRUPAMIENTO | Aislado y Pareado |
| ANTEJARDÍN | 10 metros |
| DISTANCIA A MEDIANEROS | 6 metros *(parámetro exclusivo de ZE1 dentro de las 11 zonas — ninguna otra zona de este documento trae esta fila)* |
| DENSIDAD MÁXIMA | Sin valor específico en la fuente (fila ausente del cuadro) |

---

## 13. ZE2 — CEMENTERIO (página 16) — sin cuadros numéricos

**Hallazgo estructural (ver §0 y §20):** ZE2 es una de las dos zonas (junto con ZAV, §16) que **no** traen los dos cuadros estándar. Se regula enteramente en prosa. Transcripción completa del texto:

> *"Corresponden a los predios destinados a un uso exclusivo de Cementerio, los cuales se regirán según la normativa contenida en el Reglamento general sobre cementerios que establece el Código Sanitario, sin perjuicio de observar las disposiciones sobre rasantes y distanciamiento a que se refiere al artículo 2.6.3 de la OGUC, para todas las edificaciones emplazadas en el perímetro.*
> *En estas zonas se debe asegurar la conservación de los árboles valiosos existentes según lo establecido en la Ordenanza Municipal de Aseo y Ornato y destinar al menos un 30% de la superficie a área verde.*
> *No se permitirá la subdivisión predial ni las ampliaciones a estas zonas, sólo aquellas indicadas en el presente plan."*

| Parámetro | Valor |
|---|---|
| Superficie predial mínima | Sin valor específico en la fuente (remite al Reglamento general sobre cementerios / Código Sanitario) |
| Coeficiente de ocupación de suelo | Sin valor específico en la fuente |
| Coeficiente de constructibilidad | Sin valor específico en la fuente |
| Altura máxima | Sin valor específico en la fuente (remite a rasantes y distanciamiento del art. 2.6.3 OGUC) |
| Sistema de agrupamiento | Sin valor específico en la fuente |
| Antejardín | Sin valor específico en la fuente |
| Densidad máxima | Sin valor específico en la fuente |
| Área verde mínima *(único valor numérico que sí fija esta zona, fuera de la estructura estándar)* | 30% de la superficie del predio |
| Subdivisión predial | Expresamente prohibida ("No se permitirá la subdivisión predial ni las ampliaciones a estas zonas, sólo aquellas indicadas en el presente plan.") |

---

## 14. ZAP — ZONA DE ACTIVIDADES PRODUCTIVAS (página 16→17)

### Normas de usos de suelo

| Tipo | Clase | Actividades permitidas | Actividades prohibidas |
|---|---|---|---|
| RESIDENCIAL | — | "Sólo la vivienda del cuidador." | - |
| EQUIPAMIENTO | Científico | G1 | - |
| EQUIPAMIENTO | Comercio | G1-G2-G3-G4-G5 | - |
| EQUIPAMIENTO | Culto y Cultura | G1-G2-G3 | - |
| EQUIPAMIENTO | Deporte | G1 | - |
| EQUIPAMIENTO | Educación | G3-G4 | - |
| EQUIPAMIENTO | Esparcimiento | G1-G2 | Parques Zoológicos |
| EQUIPAMIENTO | Seguridad | G1 | - |
| EQUIPAMIENTO | Servicios | G1-G2 | - |
| EQUIPAMIENTO | Social | G1-G2 | - |
| ACTIVIDADES PRODUCTIVAS | — | G1-G2 | - |
| **USOS DE SUELO PROHIBIDOS** | | TODOS LOS NO MENCIONADOS COMO PERMITIDOS | |

**Notas estructurales verificadas con zoom (comparación directa con ZI, §15):**
- **Sin fila de "Salud"** en Equipamiento — igual que ZI, y a diferencia de las 7 zonas anteriores (ZM1-ZE1), que sí la traen.
- **Educación restringida a G3-G4** (liceos/técnica y educación superior/capacitación), **sin G1-G2** (jardines infantiles/salas cuna ni colegios básicos) — a diferencia de ZI, que sí permite el rango completo G1-G2-G3-G4 (ver §15). Verificado dos veces por lo contraintuitivo del hallazgo (cabría esperar que la zona industrial fuera más restrictiva que la de "actividades productivas", y aquí es al revés en este ítem puntual).
- **Actividades Productivas limitado a G1-G2** (solo las calificadas inofensivas), a diferencia de ZI que autoriza "Todas".

### Normas de subdivisión y edificación

| Parámetro (rótulo exacto de la fuente) | Valor |
|---|---|
| SUPERFICIE PREDIAL MÍNIMA: | 1.000 m2 |
| COEFICIENTE DE OCUPACIÓN DE SUELO | 0,6 |
| COEFICIENTE DE CONSTRUCTIBILIDAD | 1 |
| ALTURA MÁXIMA | 12 metros |
| SISTEMA DE AGRUPAMIENTO | Aislado y Pareado |
| ANTEJARDÍN | 5 metros |
| DENSIDAD MÁXIMA | Sin valor específico en la fuente (fila ausente del cuadro) |

---

## 15. ZI — ZONA INDUSTRIAL (página 17)

### Normas de usos de suelo

| Tipo | Clase | Actividades permitidas | Actividades prohibidas |
|---|---|---|---|
| RESIDENCIAL | — | "Sólo la vivienda del cuidador." | - |
| EQUIPAMIENTO | Científico | G1 | - |
| EQUIPAMIENTO | Comercio | G1-G2-G3-G4-G5 | - |
| EQUIPAMIENTO | Culto y Cultura | G1-G2-G3 | - |
| EQUIPAMIENTO | Deporte | G1 | - |
| EQUIPAMIENTO | Educación | G1-G2-G3-G4 | - |
| EQUIPAMIENTO | Esparcimiento | G1-G2 | Parques Zoológicos |
| EQUIPAMIENTO | Seguridad | G1 | - |
| EQUIPAMIENTO | Servicios | G1-G2 | - |
| EQUIPAMIENTO | Social | G1-G2 | - |
| ACTIVIDADES PRODUCTIVAS | — | Todas | - |
| **USOS DE SUELO PROHIBIDOS** | | TODOS LOS NO MENCIONADOS COMO PERMITIDOS | |

**Nota:** ver comparación con ZAP en §14 — mismo patrón general, pero Educación más amplia (G1-G2-G3-G4 completo) y Actividades Productivas sin restricción ("Todas", incluidas las calificadas molestas, coherente con ser la zona propiamente industrial).

### Normas de subdivisión y edificación

| Parámetro (rótulo exacto de la fuente) | Valor |
|---|---|
| SUPERFICIE PREDIAL MÍNIMA: | 1.000 m2 |
| COEFICIENTE DE OCUPACIÓN DE SUELO | 0,6 |
| COEFICIENTE DE CONSTRUCTIBILIDAD | 1 |
| ALTURA MÁXIMA | 12 metros |
| SISTEMA DE AGRUPAMIENTO | Aislado y Pareado |
| ANTEJARDÍN | 5 metros / 12 metros en Localidad de Cauquenes *(dos valores condicionales según localidad dentro de la comuna — no es un desglose que sume, se transcriben ambos)* |
| DENSIDAD MÁXIMA | Sin valor específico en la fuente (fila ausente del cuadro) |

---

## 16. ZAV — ZONA ÁREA VERDE (página 17) — sin cuadros numéricos

**Hallazgo estructural (ver §0 y §20):** igual que ZE2, ZAV **no** trae los dos cuadros estándar. Es un único párrafo:

> *"Las zonas de área verde se sujetarán a las normas contenidas en el Artículo 2.1.31 de la OGUC."*

| Parámetro | Valor |
|---|---|
| Todos los parámetros de usos de suelo y de subdivisión/edificación | Sin valor específico en la fuente — remite íntegramente al artículo 2.1.31 de la OGUC, sin fijar cifras propias en la Ordenanza Local |

---

## 17. Verificación de "trampa comuna ajena"

Se revisó explícitamente, como pide el encargo, si hay contenido de otra comuna mezclado en las 10 páginas. **No se encontró ninguno.** Elementos verificados:

- Encabezado idéntico en las 10 páginas: **"Decreto 500, CAUQUENES (2009)"**.
- Texto explícito en el Art. 22 (página 11): *"El Plan Regulador de Cauquenes comprende las siguientes macro áreas."*
- Acrónimo **"PRCC"** (Plan Regulador Comunal de Cauquenes) usado consistentemente en los artículos 13 a 21.
- Nota al pie de ZM1 (página 13): *"Sólo se permite en la Localidad de Santa Sofía."* — Santa Sofía es efectivamente un distrito/localidad rural real de la comuna de Cauquenes (Región del Maule), no de otra comuna.
- Nota de ZI (página 17): *"12 metros en Localidad de Cauquenes"* — referencia interna a la localidad cabecera de la propia comuna, consistente.
- No se detectó ningún nombre de calle, alcalde, u otro topónimo que corresponda a una comuna distinta de Cauquenes en ninguna de las 10 páginas.

**Conclusión:** no hay trampa de comuna ajena en este rango de páginas — el material es exclusivamente de Cauquenes.

---

## 18. Cuadro comparativo resumen — Normas de subdivisión y edificación de las 11 zonas

| Zona | Predial mín. | COS | CC | Altura máx. | Agrupamiento | Antejardín | Densidad máx. | Otro |
|---|---|---|---|---|---|---|---|---|
| ZM1 | 300 m2 | 1 | 2,5 | 30 m | Continuo-Pareado | Sin valor específico | Sin valor específico | — |
| ZM2 | 200 m2 | 0,7 | 1,5 | 12 m *(14,40 m según Enmienda 2)* | Continuo-Pareado-Aislado | 3 m | Sin valor específico | Condición de incremento +30% si linda con ZM1 |
| ZM3 | 2.000 m2 (Educ.) / 300 m2 (otros) | 0,5 | 2,5 | 15 m *(18 m según Enmienda 1)* | Aislado | 12 m | Sin valor específico | — |
| ZH1 | 130 m2 | 0,8 | 1 | 12 m | Aislado y Pareado | 3 m | 200 hab/há | — |
| ZH2 | 300 m2 | 0,8 | 1 | 6 m | Aislado | 3 m | 120 hab/há | — |
| ZH3 | 1.000 m2 | 0,3 | 0,4 | 6 m | Aislado | 5 m | 120 hab/há | Usos de suelo idénticos a ZH2 |
| ZE1 | 2.000 m2 | 0,5 | 1 | 12 m | Aislado y Pareado | 10 m | Sin valor específico | Distancia a medianeros: 6 m |
| ZE2 | Sin valor específico | Sin valor específico | Sin valor específico | Sin valor específico | Sin valor específico | Sin valor específico | Sin valor específico | Sin cuadro — remite a Código Sanitario/OGUC 2.6.3; 30% mínimo área verde |
| ZAP | 1.000 m2 | 0,6 | 1 | 12 m | Aislado y Pareado | 5 m | Sin valor específico | — |
| ZI | 1.000 m2 | 0,6 | 1 | 12 m | Aislado y Pareado | 5 m / 12 m (Localidad de Cauquenes) | Sin valor específico | — |
| ZAV | Sin valor específico | Sin valor específico | Sin valor específico | Sin valor específico | Sin valor específico | Sin valor específico | Sin valor específico | Sin cuadro — remite a OGUC art. 2.1.31 |

**Patrón de intensidad:** ZM1 (zona mixta comercio/servicios, centro) concentra la mayor altura y constructibilidad (30 m, CC 2,5) de las 11 zonas, coherente con ser el núcleo comercial. Las tres zonas habitacionales (ZH1>ZH2>ZH3) siguen un orden decreciente lógico de intensidad según su numeración (predio mínimo creciente, COS/CC/altura decrecientes), igual que ZAP/ZI son casi idénticas entre sí en subdivisión/edificación (difieren solo en el desglose por localidad del antejardín de ZI y en usos de suelo).

---

## 19. Control aritmético — cruce con enmiendas posteriores (Decreto 3519 y Decreto Exento 1033)

Tal como pide el punto 8 del encargo, se buscaron filas con desglose que debieran sumar a un total dentro de los propios cuadros de las 11 zonas — **no se encontró ningún caso** (a diferencia de otros PRC del corpus, aquí "Altura Máxima" es siempre un valor único, sin tramos parciales por piso que deban sumarse). Los únicos valores "dobles" encontrados (predial mínima de ZM3, antejardín de ZI) son alternativas condicionales, no una suma — se documentaron ambos valores sin operar aritmética entre ellos, por no corresponder.

Sí fue posible, en cambio, un control aritmético **externo**, cruzando este documento contra las dos enmiendas ya guardadas en `extraccion_normas/cauquenes/`:

- **ZM2:** Enmienda 02 (Decreto Exento 1033) fija la nueva altura máxima en **14,40 metros**, indicando explícitamente que es "un incremento del 20% respecto de la altura anterior". Operando en reversa: 14,40 ÷ 1,20 = **12,00 metros exactos**. Esto coincide dígito por dígito con el valor leído aquí para ZM2 (ALTURA MÁXIMA = 12 metros, §7). **Verificación aritmética exitosa — confirma independientemente que la lectura de esta cifra es correcta.**
- **ZM3:** Enmienda N°1 (Decreto 3519) fija la nueva altura máxima en 18 metros, sin indicar el porcentaje de incremento respecto del valor anterior. Con el valor aquí transcrito (15 metros, §8), el incremento implícito sería 18/15 = 1,20, es decir, también un +20% — **consistente con el mismo criterio de incremento usado en la Enmienda 02 para ZM2**, aunque la Enmienda 1 no lo declare explícitamently. Esto es una segunda corroboración indirecta, no tan concluyente como la de ZM2 (no está declarada en el propio texto de la enmienda), pero refuerza la confianza en el valor de 15 metros leído para ZM3.

**Conclusión:** ambas cifras de altura máxima más sensibles de este documento (ZM2 y ZM3) quedan corroboradas por una fuente externa independiente (las enmiendas posteriores), lo que eleva la confianza de la transcripción completa.

---

## 20. Discrepancias y hallazgos respecto de la nota de Fase 3

1. **"p8: cuadro estandares de estacionamiento por uso/clase":** confirmado, con una precisión: el cuadro no es autocontenido del Art. 12/13 — es la cola de un artículo previo (probablemente Art. 12, con encabezado en la página 7, fuera de rango) y trae además una subtabla separada "INFRAESTRUCTURA" no mencionada por Fase 3. Ver §3.
2. **"p9: TABLA CLAVE art.14 = grupos de actividades G1-G5 (imprescindible...)":** confirmado sin reservas — la tabla completa está íntegramente en la página 9, no partida con la página 8 ni la 10. Transcrita completa en §4.
3. **"p10-11: condiciones por uso en texto":** confirmado — páginas 10 y 11 son prosa pura (Art. 17 cont., 18, 19, 20, 21, 22 inicio), sin tablas de zona.
4. **"p12: cuadro de zonificacion (indice de zonas)":** confirmado, con precisión adicional: el índice **sí coincide exactamente** con las 11 zonas del encargo (ZM1…ZAV), sin faltantes ni sobrantes — no se encontró la discrepancia que el punto 7 del encargo pedía chequear como posibilidad. El índice también lista, para contexto, las 4 categorías de "zonas no edificables" (ZNE, ZRI1, ZRI2, ZCH, ICH), fuera del alcance de este encargo.
5. **"p13-17: art.24 normativa especifica, DOS cuadros por zona":** **cierto para 9 de las 11 zonas, pero no para ZE2 (Cementerio) ni ZAV (Área Verde)**, que se regulan enteramente en prosa remitiendo a normativa externa (Código Sanitario/OGUC), sin cuadro de usos de suelo ni de subdivisión/edificación propio. Este es el hallazgo más importante a corregir de la nota heredada — ver §13 y §16.
6. **"Zonas: ZM1 ZM2 ZM3 ZH1 ZH2 ZH3 ZE1 ZE2 ZAP ZI ZAV":** confirmado exactamente — se encontraron las 11, ni una más ni una menos, todas dentro del rango páginas 8-17 (títulos entre p.12 y p.17, cuadros entre p.13 y p.17).
7. **Hallazgo nuevo — dos zonas con tabla de usos de suelo idéntica (ZH2 y ZH3):** no anticipado por Fase 3. Ver §11.
8. **Hallazgo nuevo — celdas de "Comercio" con condición en prosa en vez de códigos G (ZM3 y ZE1):** no anticipado por Fase 3. Ver §8 y §12.
9. **Hallazgo nuevo — asimetría contraintuitiva entre ZAP y ZI en Educación (G3-G4 vs. G1-G2-G3-G4):** no anticipado por Fase 3, verificado dos veces por lo inesperado. Ver §14 y §15.
10. **Hallazgo nuevo — erratas de redacción `[sic]` en el cuadro G1-G5 (página 9):** "restoranes", "tecnológico y o la", "práctico" (por "práctica"), "privado" (por "privada"), "público y privado" (por "pública y privada"), "de de Fondos de Pensiones" (duplicación). Ninguna estaba anticipada por Fase 3 (que no había leído el contenido de esta tabla, solo confirmó su existencia). Ver §4.
11. **Hallazgo nuevo — erratum de referencia cruzada interna en el Art. 23** ("Artículo 21" en vez de "Artículo 22" al referirse a las macro áreas). Ver §5.
12. **Hallazgo nuevo — espacio suelto "d e" en "ZRI2"** (índice del literal b, fuera del alcance directo del encargo pero visible en la página 12). Ver §5.
13. **Hallazgo no pedido explícitamente pero relevante — cruce con enmiendas posteriores ya presentes en el repo:** las alturas máximas de ZM2 y ZM3 aquí transcritas (valores originales de 2009) ya no son las vigentes; fueron modificadas por el Decreto Exento 1033 (ZM2 → 14,40 m) y el Decreto 3519 (ZM3 → 18 m) respectivamente. Este documento transcribe correctamente el texto **original** de 2009 tal como pedía el encargo, pero se deja la advertencia explícita para evitar que una fase posterior use estos valores como "vigentes" sin más contexto. Ver §1 y §19.
14. **No se usó "Dato no determinable" en ningún punto de este documento** — todas las celdas revisadas resultaron legibles con zoom.

---

## 21. Notas finales de verificación

**Método:** lectura directa de las 10 imágenes PNG a 250 dpi, complementada con más de 25 recortes ampliados (zoom 1,4×-4×, procesados con `PIL`, varios con `autocontrast` para mejorar contraste en celdas con trama de fondo) sobre cada tabla y cada celda de texto donde una primera lectura dejaba duda — en particular las filas de Científico/Salud/Seguridad/Educación/Actividades Productivas de cada una de las 11 zonas (para no atribuir un valor a la zona equivocada), el título completo del cuadro G1-G5, y las notas al pie (Santa Sofía, condiciones especiales de ZM2, distancia a medianeros de ZE1).

**Resultado de la verificación imagen-vs-texto:** el `.txt` de apoyo solo aporta títulos de artículo/zona y prosa corrida; el contenido de las 4 tablas grandes (estacionamiento, G1-G5, índice de zonificación, y las 18 tablas de zona — 9 zonas × 2 tablas) es imagen pura y se verificó **exclusivamente** contra el PNG, tal como anticipaba la nota de Fase 3.

**Confianza por sección:**

| Sección | Confianza | Motivo |
|---|---|---|
| Cuadro de estacionamiento (p.8) | Alta (estructura); no transcrito celda a celda (fuera del alcance pedido) | Estructura confirmada con lectura completa de la imagen |
| Cuadro G1-G5 (Art. 14, p.9) | Alta | Transcrito completo, cada celda verificada con zoom, incluidas las erratas |
| Índice de zonificación (Art. 23, p.12) | Alta | Coincide exactamente con las 11 zonas esperadas, verificado dos veces |
| ZM1, ZM2, ZM3 | Alta | Cuadros completos, sin cortes de página que perdieran datos; ZM2 y ZM3 con corroboración aritmética externa (enmiendas) |
| ZH1, ZH2, ZH3 | Alta | Cuadros completos; identidad ZH2=ZH3 (usos de suelo) verificada dos veces |
| ZE1 | Alta | Cuadro completo, incluida la fila exclusiva "Distancia a Medianeros" |
| ZE2, ZAV | Alta (de que NO tienen cuadro numérico) | Se revisó el espacio completo de página alrededor de cada título para descartar que una tabla hubiera quedado fuera de la imagen; son genuinamente solo prosa |
| ZAP, ZI | Alta | Cuadros completos; asimetría en Educación y en Actividades Productivas verificada dos veces cada una |
| Verificación de comuna ajena | Alta | Verificada contra encabezado de página, texto del Art. 22 y dos referencias a localidades internas de Cauquenes |

**Nivel de confianza global: Alto.** No se inventó ningún valor: todo campo sin dato en la fuente se marcó "Sin valor específico en la fuente" (con el motivo, cuando corresponde). No fue necesario usar "Dato no determinable" en ningún punto — todo el material del rango 8-17 resultó legible tras zoom.
