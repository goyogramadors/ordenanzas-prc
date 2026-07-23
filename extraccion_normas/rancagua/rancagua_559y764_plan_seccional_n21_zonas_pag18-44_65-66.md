# Normas Urbanísticas — Modificación al Plan Regulador Comunal de Rancagua, Plan Seccional N°21 (Decretos Exentos N°559 y N°764)

**Fuente:** Municipalidad de Rancagua, "Modificación al Plan Regulador Comunal de Rancagua, Plan Seccional N°21" (Decretos Exentos N°559 y N°764) — Diario Oficial N°43.647, jueves 7 de septiembre de 2023, CVE 2372308.
**Documento:** `Ordenanzas Descargadas/1200 x/rancagua_559_y_764_modificacion_al_planregulador_comunal_de_rancagua_plan_seccional_n21_y__2372308.pdf` (67 páginas totales).
**Extracción:** dos tramos discontinuos — **páginas 18-44** (numeral 1.30 "Modifíquese y compleméntese los usos y normas en el Artículo N° 29, según la zona que se indican", más Temas N°1/N°2/N°3 de creación de nuevas zonas) y **páginas 65-66** (Tema N°7, creación de zona EQ-EDS). El rango 46-64 (tabla de renombre de calles/parques/ciclovías) y el rango 1-17 (vistos/articulado sin tablas de zona) quedaron fuera por instrucción explícita.
**Método:** VISUAL — lectura directa de 29 imágenes PNG renderizadas a 250 dpi con `pdftoppm`. Confirmado: todas las tablas "Normas de uso de suelo" y "Normas de subdivisión predial y edificación" están insertadas como **imagen** dentro del PDF nativo del Diario Oficial (coincide con nota_fase3); ningún valor numérico proviene de `pdftotext`. Se usaron recortes con zoom 2x (PIL + autocontraste) para verificar celdas dudosas; el detalle de cada verificación puntual se indica en la zona correspondiente.

---

## Nota de alcance (léase antes que las tablas)

**Naturaleza del documento — "de modificación", no ordenanza completa.** Este decreto **modifica y compleméntese** el Art. 29 de la Ordenanza Local vigente del PRC de Rancagua, zona por zona. Esto significa que **cada ficha de zona muestra únicamente lo que este decreto efectivamente reemplaza o agrega**, no necesariamente el cuadro normativo completo de la zona. Varias zonas (R6, SM4, BR-M1 a BR-M4, BR-SM1, BR-SM2, IT-1, EQ-CB, PE, PU1-AV, EX5, EX6, EX7, EX8, Z11B-2, ZCH-1) muestran **solo la tabla de "Normas de subdivisión predial y edificación"**, sin tabla de "Usos de suelo" (porque este decreto no modificó los usos de esa zona, que siguen vigentes según el instrumento anterior no incluido en este rango). Los campos que un cuadro no trae se transcriben como "No especificado en este documento" — no se completaron con datos de otros decretos.

**Verificación de la lista de nota_fase3 — resultado: TODOS los códigos fueron ubicados**, pero el documento real es sustancialmente **más grande** que el listado de ~25 zonas de nota_fase3: contiene **60 fichas/entradas de zona** (zonas con cuadro normativo propio, zonas derogadas sin cuadro, y dos zonas de restricción aeroportuaria sin cuadro numérico). Los códigos de nota_fase3 se verificaron todos — algunos como **vigentes con cuadro**, otros como **derogados con zona sucesora identificada en el mismo documento**. Además se encontraron **~24 códigos adicionales no anticipados** por nota_fase3 (ver índice de cobertura). La razón: nota_fase3 fue un muestreo de 20+ páginas, y este documento —al ser una modificación con creación de zonas nuevas repartida en varios "Temas" (N°1 a N°3 y N°7 dentro del rango solicitado)— tiene bastante más densidad de zonas de lo que un muestreo parcial podía anticipar.

**Trampa de nomenclatura — ex zona "Parque Urbano" (EQ-PU-1 / EQPU1).** El documento usa **dos grafías distintas** para lo que parece ser la misma familia de zonas de parque urbano, en dos secciones distintas, con resultados distintos:
- En la sección del Art. 29 (numeral 1.30, p.27): **"ZONA EQ-PU-1" y "ZONA EQ-PU-2"** (con guiones) aparecen declaradas **DEROGADAS**, y a continuación se define una zona **"ZEQPU-1, Equipamiento Parque Urbano Especial del Tipo 1"** con cuadro normativo propio (nuevo código, con "Z" antepuesta).
- En la sección del Art. 27 "Áreas Consolidadas" (numeral 3.2, p.44): **"EQPU1" y "EQPU2"** (sin guion) se **renombran** a **"PU1-AV, Zona de Parques privados"** y **"PU2-EP, Zona de Parques Bien Nacional de uso público"** respectivamente (con cuadro normativo propio para cada una, ya transcrito en p.28), y luego (3.2.1) se derogan los códigos antiguos "EQPU1"/"EQPU2".
- Resultado: **hay tres fichas distintas de "zona de parque urbano" en este documento — ZEQPU-1, PU1-AV y PU2-EP —**, cada una con su propio cuadro de normas, todas ellas sucesoras (en distintas secciones del mismo decreto) de la extinta zona "EQ-PU-1/EQPU1". Se transcriben las tres por separado, tal como aparecen, sin fusionarlas ni intentar resolver cuál es la sucesora "correcta" — eso corresponde a una lectura jurídica integral del decreto que excede el alcance de esta transcripción visual.

**Hallazgo — la familia EX no es EX1-3, es EX1 a EX8.** nota_fase3 preveía "EX1-3"; el documento real numera zonas de extensión urbana **EX1, EX2, EX3, EX4 (derogada), EX5, EX6, EX7 y EX8** (Barrio Norte). Las ocho se transcriben. La zona **EX6** de este documento (2023, Decreto 559/764) **no debe confundirse** con la zona "EX 6" ya transcrita en `rancagua_fe_erratas_tramitacion16_zona_ex6_pag1-2.md` de esta misma carpeta, que corresponde a un decreto de 2009/2010 completamente distinto (Tramitación N°16) — son documentos y (probablemente) delimitaciones distintas aunque compartan sigla; no se cruzó información entre ambos.

**Zonas ya cubiertas por otros documentos de esta carpeta — no se tocaron.** La zona **ZCH-1** aparece en este documento (p.33) pero **solo con una fila** ("Estacionamientos: Según Artículo 35"); su cuadro completo de COS/coeficiente de constructibilidad pertenece al Decreto 3.326/2020 (ya cubierto por `rancagua_2236_fe_erratas_zch1_za1_pag2.md` en esta carpeta, con CC=3,0 corregido). Aquí se transcribe **únicamente la fila que trae este decreto 559/764**, sin mezclar valores de otro decreto.

**Erratas/anomalías del original preservadas, no corregidas:**
- **Zona BRO** (p.32): el cuadro trae **"Coeficiente de Constructibilidad: 10"** (verificado con zoom 2x — se lee literalmente "10", sin coma decimal), un valor atípicamente alto frente al resto del documento (CC entre 0,2 y 5 en las demás zonas, salvo casos "Según rasante"). Podría ser un error de imprenta del original por "1,0", pero se transcribe tal cual con `[sic]` y confianza MEDIA en esa celda puntual.
- **Zona BR-M3** (p.22): el "Sistema de Agrupamiento" permite Aislado, Pareado y Continuo, pero la fila "Altura Máxima de Edificación" **solo trae valor para Pareado (7 m)** — verificado con zoom, no es un salto de lectura; Aislado y Continuo quedan sin altura explícita en el propio cuadro fuente.
- **Zona EX1** (p.29): el cuadro de subdivisión termina en la fila "Altura Máxima de Edificación — Pareado: 17,5" (verificado con zoom); no trae fila "Continuo" ni "Antejardín", a diferencia de EX2 y EX3 que sí las traen (o las dejan en "-").
- Cifras "eliminadas" del cuadro de la zona **BRO** (áreas verdes mínimo 20%, arborización mínima) se muestran en el documento dentro de un recuadro "Elimínese del cuadro de normas de subdivisión predial y edificación" — es decir, **ya NO son norma vigente**; se documentan aparte como referencia histórica, no como norma actual de BRO.
- Zona **RAM** y otras: uso reiterado de la fórmula "Según lo dispuesto en O.G.U.C." para Adosamientos/Distanciamientos/Rasantes/Ochavos en las zonas de creación más reciente (Temas N°2 y N°3) — se transcribe literal, sin resolver el valor numérico real de la OGUC (está fuera del alcance del documento fuente).

**Tablas de "incentivo" (IPAEP/IIS, Art. 9) — no confundir con la norma base.** Varias zonas (EX3, EQ-CBM1, PU-M, PU-R1, R2-A) traen, además de su cuadro de norma base, una tabla adicional de condiciones **condicionadas** a incentivos (proyectos que enfrenten parques lineales específicos, o con % de vivienda subsidiada SERVIU). Se transcriben en subsección aparte dentro de cada zona, rotuladas "Normas con incentivo", para no mezclarlas con la norma base de aplicación general.

**Tablas de "corrección de plano" / rezonificación — no son fichas de norma.** El documento trae, intercaladas entre las zonas, varias tablas "Áreas / Ubicación — Zona Vigente — Zona Propuesta" que reasignan sectores específicos de la comuna de una sigla de zona a otra (p.ej. "La Compañía con Los Talaveras: EQS → R2"). No tienen columnas de COS/CC — no son cuadros de norma urbanística, sino de rezonificación cartográfica. Se recopilan en el Anexo al final de este documento, como referencia, y no se repiten como "ficha de zona".

**Confianza:** ALTA para la gran mayoría de zonas (texto e imagen nítidos a 250 dpi, sin ambigüedad). MEDIA puntual en dos celdas específicas (BRO/CC y BR-M3/Altura Aislado y Continuo faltantes), ya señaladas arriba y repetidas en la ficha respectiva.

---

## Índice de cobertura

Cobertura de los ~25-30 códigos anticipados por nota_fase3 (todos verificados) más las zonas adicionales encontradas en el documento real, en orden de aparición:

| Código | Denominación | Estado | Página(s) | Tipo de cuadro |
|---|---|---|---|---|
| R1 | Zona Residencial 1 | Vigente | 18 | Usos + subdivisión completos |
| R2 | Zona Residencial 2 | Vigente | 18 | Usos + subdivisión completos |
| R3 | Zona Residencial 3 | Vigente | 19 | Usos + subdivisión completos |
| R4 | Zona Residencial 4 | Vigente | 19 | Usos + subdivisión (parcial) |
| R5 | Zona Residencial 5 | Vigente | 20 | Usos + subdivisión (parcial) |
| R6 | Zona Residencial 6 | Vigente | 20 | Solo subdivisión |
| SM1 | Zona Mixta 1 | Vigente | 20-21 | Usos + subdivisión (parcial) |
| SM1-A | Zona Mixta 1-A | **DEROGADA** | 21 | Sin cuadro |
| SM2 | Zona Mixta 2 | **DEROGADA** | 21 | Sin cuadro |
| SM3 | Zona Mixta 3 | Vigente | 21 | Usos + subdivisión completos |
| SM4 | Zona Mixta 4 | Vigente | 21 | Solo subdivisión |
| BR-M1 | Zona Mixta Borde Ruta 1 (Subcentro de Equipamiento) | Vigente | 21 | Solo subdivisión |
| BR-M2 | Zona Mixta Borde Ruta 2 (Reconversión Centro Norte) | Vigente | 22 | Solo subdivisión |
| BR-M3 | Zona Mixta Borde Ruta 3 (Reconversión Centro Sur) | Vigente | 22 | Solo subdivisión + incentivo |
| BR-M4 | Zona Mixta Borde Ruta 4 (Equip. e Infraestructura Sanitaria) | Vigente | 23 | Solo subdivisión |
| BR-SM1 | Zona Mixta de Servicios Borde Ruta 1 (Barrio Empresarial) | Vigente | 23 | Solo subdivisión |
| BR-SM2 | Zona Mixta de Servicios Borde Ruta 2 (Barrio Empresarial Sur) | Vigente | 23 | Solo subdivisión |
| ZM | Zona Militar | Vigente (extra, no en nota_fase3) | 23-24 | Usos + subdivisión completos |
| IA | Zona Industrial | Vigente | 24 | Usos + subdivisión |
| IE | Zona Industrial Especial | Vigente | 24-25 | Usos + subdivisión |
| IT-1 | Zona de Infraestructura de Transporte (Terminales de Buses) | Vigente | 25 | Solo subdivisión |
| EQS | Equipamiento de Salud | Vigente | 25 | Usos + subdivisión |
| EQ-SC | Equipamiento de Salud - Cementerios | Vigente | 25-26 | Usos + subdivisión |
| EQ-CB | Equipamiento Centro de Barrio | Vigente | 26 | Usos + subdivisión (1 fila) |
| EQ-CB1 | Equipamiento Centro de Barrio del Tipo 1 | Vigente | 26-27 | Usos + subdivisión |
| EQ-PU-1 | Equipamiento Parque Urbano Especial Tipo 1 | **DEROGADA** (ver ZEQPU-1/PU1-AV) | 27 | Sin cuadro |
| EQ-PU-2 | Equipamiento Parque Urbano Especial Tipo 2 | **DEROGADA** (ver PU2-EP) | 27 | Sin cuadro |
| EQ-E | Equipamiento Especial | **DEROGADA** | 27 | Sin cuadro |
| ZEQPU-1 | Equipamiento Parque Urbano Especial del Tipo 1 | Vigente (extra, sucesora de EQ-PU-1 en Art.29) | 27 | Usos + subdivisión completos |
| C1 | Zona Corredor Comercial 1 | Vigente | 27-28 | Usos + subdivisión (parcial) |
| PE | Zona Portal Estación | Vigente (extra, no en nota_fase3) | 28 | Solo subdivisión |
| PU1-AV | Zona de Parques privados | Vigente (extra; sucesora de EQPU1 en Art.27) | 28 | Solo subdivisión |
| PU2-EP | Zona de Parques Bien Nacional de uso público | Vigente (extra; sucesora de EQPU2 en Art.27) | 28 | Usos + subdivisión completos |
| EX1 | Zona Extensión urbana 1 | Vigente | 29 | Usos + subdivisión (parcial) |
| EX2 | Zona Extensión urbana 2 | Vigente | 29-30 | Usos + subdivisión completos |
| EX3 | Zona Extensión urbana 3 | Vigente | 30-31 | Usos + subdivisión + incentivo |
| EX4 | Zona Extensión urbana 4 | **DEROGADA** | 31 | Sin cuadro |
| EX5 | Zona Extensión urbana 5 | Vigente (extra) | 31 | Solo estacionamientos |
| EX6 | Zona Extensión urbana 6 | Vigente (extra; **decreto distinto** del EX6 ya en la carpeta) | 31 | Solo subdivisión |
| EX7 | Zona Extensión urbana 7 | Vigente (extra) | 31 | Solo subdivisión |
| EX8 | Zona Extensión urbana 8 (Barrio Norte) | Vigente (extra) | 31 | Solo subdivisión |
| BRO | Zona Borde Ruta Oriente | Vigente (extra, no en nota_fase3) | 32 | Solo subdivisión |
| EQ-CBSO | Zona Equipamiento Centro de Barrio Sur Oriente | Vigente | 32 | Solo subdivisión |
| RAM | Zona Residencial Altura Media | Vigente | 32 | Solo subdivisión |
| Z11A | Zona Restricción cabezales Puerto Aéreo | Vigente (extra; remite a Cono aeródromo, sin tabla) | 32 | Sin cuadro numérico |
| Z11B-1 | Zona Restricción por aproximación al Puerto Aéreo B-1 | Vigente | 32-33 | Usos + subdivisión |
| Z11B-2 | Zona Restricción por aproximación al Puerto Aéreo B-2 | Vigente (extra, no en nota_fase3) | 33 | Solo subdivisión |
| Z12 | Zona Restricción trazado alta tensión y subestaciones | Vigente (extra; solo texto, sin tabla) | 33 | Sin cuadro numérico |
| Z20 | Zona Áreas uso potencial Paraderos Buses Carretera 5 Sur | **DEROGADO** | 33 | Sin cuadro |
| ZCH-1 | Zona de Conservación Histórica N°1 - Eje Estado | Vigente (solo 1 fila en este decreto; cuadro completo en otro decreto ya cubierto en esta carpeta) | 33 | Solo estacionamientos (1 fila) |
| EQ-CBM1 | Equipamiento Centro de Barrio Mixto 1 | Vigente — **zona nueva creada por este decreto** (Tema N°2) | 35-36 | Usos + subdivisión + incentivo |
| CU | Zona Corredor Urbano | Vigente — zona nueva (Tema N°2) | 36-37 | Usos + subdivisión completos |
| PU-M | Parque Urbano Mixto | Vigente — zona nueva ("Reconocimiento de zona ya consolidada...") | 38 | Usos + subdivisión + incentivo |
| PU-R1 | Parque Urbano Residencial 1 | Vigente — zona nueva | 38-39 | Usos + subdivisión + incentivo |
| R1-A | Zona Preferentemente Residencial 1-A | Vigente — zona nueva | 39-40 | Usos + subdivisión completos |
| R2-A | Zona Preferentemente Residencial 2-A | Vigente — zona nueva | 40-41 | Usos + subdivisión + incentivo IIS |
| R3-A | Zona Preferentemente Residencial 3-A | Vigente — zona nueva | 41 | Usos + subdivisión completos |
| BR-M5 | Zona Mixta 5 Borde Ruta | Vigente — zona nueva ("Nuevas zonificaciones...") | 42-43 | Usos + subdivisión completos |
| EQ-D | Zonas de equipamiento deportivo | Vigente — zona nueva (Tema N°3) | 43-44 | Usos + subdivisión completos |
| EQ-EDS | Zonas de equipamiento Educación Superior | Vigente — zona nueva (Tema N°7) | 65-66 | Usos + subdivisión completos |

**Total: 60 entradas.** De ellas, 47 tienen cuadro numérico propio, 7 están explícitamente derogadas sin cuadro (SM1-A, SM2, EQ-PU-1, EQ-PU-2, EQ-E, EX4, Z20), y 2 son zonas de restricción sin cuadro de COS/CC porque remiten a normativa aeronáutica/sectorial externa (Z11A, Z12), y ZCH-1 muestra solo una fila puntual (resto del cuadro pertenece a otro decreto ya cubierto en esta carpeta). Todos los códigos de la lista de nota_fase3 (R1-R6, SM1-SM4, BR-M1-M5, BR-SM1-2, IA, IE, IT-1, EQS, EQ-SC, EQ-CB, EQ-CB1, EQ-PU-1, C1, CU, EX1-3, BRO, EQ-CBSO, RAM, Z11B-1, EQ-D, EQ-EDS) quedan cubiertos.

---

## TEMA — Modificaciones por zona al Artículo N°29 (numeral 1.30)

### R1 (Zona Residencial 1) — p.18

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Residencial | Vivienda, Hogares de Acogida: Todos y Hospedaje: Excepto los señalados como prohibidos |
| Equipamiento | Comercio: Todos, excepto los señalados como prohibidos; Culto y Cultura: Todos, excepto los señalados como prohibidos; Deporte: Todos, excepto los señalados como prohibidos; Educación: Todos; Esparcimiento: Todos, excepto los señalados como prohibidos; Salud: Todos, excepto los señalados como prohibidos; Seguridad: Todos; Servicios: Todos; Social: Todos |
| Actividades productivas | Establecimientos de Impacto Similar al Industrial: inofensivo |
| Infraestructura | Transporte: Todos, excepto los señalados como prohibidos |
| Espacios públicos / Áreas verdes | Permitidos (sin detalle adicional) |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Residencial | En Hospedaje: Motel |
| Equipamiento | Científico: Todos; Comercio: Discotecas, Cabaret; Culto y Cultura: Salas de Espectáculo; Deporte: Hipódromos; Esparcimiento: Zoológicos; Salud: Cementerio, crematorios |
| Actividades productivas | Industria, Almacenamiento; Establecimientos de Impacto Similar al Industrial: Molestos |
| Infraestructura | Transporte de: Estaciones y Terminales Ferroviarios, Terminal Rodoviario, terminales de distribución; Sanitaria y Energía, en conformidad al artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 120 m² |
| Coeficiente de ocupación de suelo (COS) | 0,8 |
| Coeficiente de constructibilidad | 2 |
| Antejardín | 3 m |
| Densidad máxima, altura máxima, sistema de agrupamiento, distanciamientos, rasantes, ochavos | No especificado en este documento |

**Nota:** el texto agrega: "Elimínese último párrafo y el cuadro de condiciones de subdivisión predial y edificación, de los predios que colinden con los terrenos de la zona PE (Portal Estación) de la presente zona" — es decir, existía una sub-norma especial para predios colindantes con la zona PE que este decreto deroga.

---

### R2 (Zona Residencial 2) — p.18

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Residencial | Vivienda, Hogares de Acogida: todos y Hospedaje: Todos, excepto los señalados como prohibidos |
| Equipamiento | Comercio: Todos, excepto los señalados como prohibidos; Culto y Cultura: Todos; Deporte: Todos, excepto los señalados como prohibidos; Educación: Todos; Esparcimiento: Todos, excepto los señalados como prohibidos; Salud: Todos, excepto los señalados como prohibidos; Seguridad: Todos, excepto los señalados como prohibidos; Servicios: Todos; Social: Todos |
| Actividades productivas | Actividad Similar al Industrial inofensivas |
| Infraestructura | Transporte: terminales de transporte terrestre (rodoviarios, terminales de buses, taxis buses, taxis, taxis colectivos), depósito de buses o camiones (hasta dos buses o camiones) |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Residencial | Hospedaje: Motel |
| Equipamiento | Científico: Todos; Comercio: Discotecas, Cabaret, Quintas de Recreo, Restaurante de Turismo, Motel Turístico; Deporte: Hipódromos; Esparcimiento: Zoológicos; Salud: Cementerio, Crematorio; Seguridad: cárceles, centros de reclusión nocturna |
| Actividades productivas | Industria; Almacenamiento; Establecimientos de Impacto Similar al Industrial |
| Infraestructura | Transporte: Todos, con excepción de los permitidos; Sanitaria y Energía, en conformidad al artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 160 m² |
| Coeficiente de ocupación de suelo (COS) | 0,8 |
| Coeficiente de constructibilidad | 1,2 |
| Antejardín | 3 m |
| Densidad máxima, altura máxima, sistema de agrupamiento, distanciamientos, rasantes, ochavos | No especificado en este documento |

**Nota:** el texto agrega incentivos de densidad para R2: en vías de 18 m, 520 hab/Há; en vías de 25 m, 600 hab/Há, sujeto a incentivos IPAEP/IIS del Art. 9 y no aplicable a agrupamiento continuo.

---

### R3 (Zona Residencial 3) — p.19

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Residencial | Vivienda, Hogares de Acogida y Hospedaje: Excepto los señalados como prohibidos |
| Equipamiento | Comercio: Todos, excepto los señalados como prohibidos; Culto y Cultura: Todos; Deporte: Todos, excepto los señalados como prohibidos; Educación: Todos; Esparcimiento: Todos, excepto los señalados como prohibidos; Salud: Todos, excepto los señalados como prohibidos; Seguridad: Todos, excepto los señalados como prohibidos; Servicios: Todos, excepto los señalados; Social: Todos |
| Actividades productivas | Actividad Similar al Industrial inofensivas |
| Infraestructura | Transporte: terminales de transporte terrestre (rodoviarios, terminales de buses, taxis buses, taxis, taxis colectivos), depósito de buses o camiones (hasta dos buses o camiones) |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Residencial | En Hospedaje: Hostería, Motel |
| Equipamiento | Científico; Comercio: Discotecas, similares, Cabaret, Quintas de Recreo, Restaurant de Turismo, hoteles turísticos, moteles turísticos, Bombas de Bencina, Expendio de Combustibles, Centros de Servicio Automotriz o Servicentros; Deporte: Hipódromos; Esparcimiento: Zoológicos, Salas de Espectáculo, Juegos electrónicos o mecánicos; Salud: Cementerio, Crematorio; Servicios: Servicio de Estacionamientos; Seguridad: Cárceles, centros de reclusión nocturna |
| Actividades productivas | Industria; Almacenamiento y Actividad Similar al Industrial molesta |
| Infraestructura | Transporte: Todos excepto los señalados como permitidas; Sanitaria y Energía, en conformidad al artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 250 m² |
| Coeficiente de ocupación de suelo (COS) | 0,6 |
| Coeficiente de constructibilidad | 1,2 |
| Antejardín | 3 m |
| Densidad máxima, altura máxima, sistema de agrupamiento, distanciamientos, rasantes, ochavos | No especificado en este documento |

**Nota:** incentivos de densidad: vías de 18 m → 480 hab/Há; vías de 25 m → 600 hab/Há (mismo esquema condicionado que R2).

---

### R4 (Zona Residencial 4) — p.19

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Residencial | Vivienda, Hogares de Acogida; Hospedaje: Exceptos los prohibidos |
| Equipamiento | Comercio, Culto y Cultura, Deporte, Educación, Esparcimiento, Salud, Seguridad, Servicios y Social |
| Actividades productivas | Establecimientos de Impacto Similar al Industrial inofensivos |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Residencial | En Hospedaje: Moteles |
| Equipamiento | Científico; Comercio: Discotecas, similares, Cabaret, Quintas de Recreo, Restaurante de Turismo, Bombas de Bencina, Expendio de Combustibles, Centros de Servicio Automotriz o Servicentros; Deporte: Hipódromos; Esparcimiento: Zoológicos, Circos, Salas de Espectáculo, Juegos electrónicos o mecánicos; Salud: Cementerio, Crematorio; Servicios: Servicio de Estacionamientos con excepción de los asociados a proyectos de edificación; Seguridad: cárceles, centros de reclusión nocturna |
| Actividades productivas | Industria, Almacenamiento; Establecimientos de Impacto Similar al Industrial: del tipo Molesto y Talleres Industriales, tornería, carpintería metálica |
| Infraestructura | Transporte; Sanitaria y Energía, en conformidad al artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 500 m² |
| Coeficiente de ocupación de suelo (COS) | 0,4 |
| Coeficiente de constructibilidad | 1,6 |
| Densidad bruta máxima | 520 hab/Há |
| Antejardín, altura máxima, sistema de agrupamiento, distanciamientos, rasantes, ochavos | No especificado en este documento |

**Nota:** "Elimínese la frase 'los balcones, terrazas y elementos sobresalientes podrán materializarse hasta un máximo de 1.0 mts. sobre la línea de antejardín mínimo'" y "Elimínese anexo R4 y su tabla de normas" — el decreto deroga un anexo específico previo de R4 no reproducido aquí.

---

### R5 (Zona Residencial 5) — p.20

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Residencial | Vivienda |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Residencial | Hogares de acogida: todos; Hospedaje: todos |
| Equipamiento | Científico; Comercio; Culto y Cultura; Deporte; Educación; Esparcimiento; Salud; Seguridad; Servicios y Social — todos prohibidos |
| Actividades productivas | Industria, Almacenamiento y Establecimientos de Impacto Similar al Industrial: Inofensivo y Molesto |
| Infraestructura | Transporte; Sanitaria; Energía, en conformidad al artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Coeficiente de ocupación de suelo (COS) | 0,5 |
| Estacionamientos | Según Artículo 35 de la presente Ordenanza |
| Superficie predial mínima, coeficiente de constructibilidad, densidad, altura máxima, sistema de agrupamiento, antejardín, distanciamientos, rasantes, ochavos | No especificado en este documento |

---

### R6 (Zona Residencial 6) — p.20

#### Usos de suelo

No especificado en este documento — este decreto no modifica los usos de suelo de R6 (solo trae la tabla de subdivisión, más abajo, y deroga condiciones adicionales del texto vigente).

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 200 m² |
| Coeficiente de ocupación de suelo (COS) | 0,5 |
| Coeficiente de constructibilidad | 1,0 |
| Densidad, altura máxima, sistema de agrupamiento, antejardín, distanciamientos, rasantes, ochavos | No especificado en este documento |

**Nota:** "Elimínese 'Condiciones para la construcción existente' y su tabla de normas. Elimínese los tres últimos párrafos de la presente zona" — el decreto deroga contenido adicional previo no reproducido en este cuadro.

---

### SM1 (Zona Mixta 1) — p.20-21

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Residencial | Vivienda; Hogares de acogida y Hospedaje |
| Equipamiento | Comercio, Culto y Cultura, Deporte (Multicanchas, Gimnasios, Piscinas, Sauna, Baños Turcos), Educación, Esparcimiento, Salud, Seguridad, Servicios y Social |
| Actividades productivas | Industria: inofensiva; Almacenamiento: inofensivo; Talleres de Impacto Similar al Industrial: inofensivo |
| Infraestructura | Transporte: terminales de buses, camiones, taxibuses y taxis colectivos, depósito de hasta 2 buses o camiones |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Equipamiento | Científico: Todos; Deporte: Hipódromos, Estadios, Centros Deportivos, Medialunas, Coliseos; Esparcimiento: Zoológicos; Salud: Cementerio, Crematorio; Seguridad: cárceles, centros de reclusión nocturna |
| Actividades productivas | Industria molesta, Almacenamiento molesto, Act. de Impacto Similar al Industrial: Molesta como Talleres Industriales, tornería, carpintería metálica, Talleres de Reparación Automotriz o Garajes, Vulcanizaciones, Imprentas y Litografías, Carpintería de Madera, Mueblerías, Amasanderías y Panaderías molestos |
| Infraestructura | Transporte: Estaciones y Terminales Ferroviarios, Terminal Rodoviario, Depósito de 3 o más buses o camiones; Sanitaria y Energía, en conformidad al artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 120 m² |
| Coeficiente de constructibilidad | 2 |
| Antejardín | 3 m |
| (*) Profundidad Mínima de Edificación Continua | 30% del deslinde común |
| Coeficiente de ocupación de suelo, densidad, altura máxima, sistema de agrupamiento, distanciamientos, rasantes, ochavos | No especificado en este documento |

**Nota:** se elimina la tabla previa de "Condiciones de subdivisión predial y edificación zona SM1 emplazado en zona de renovación urbana para obras nuevas de equipamiento y densificación", los incentivos en vías de 18 y 25 m, y una restricción sobre bombas de bencina/locales de expendio de combustibles.

---

### SM1-A (Zona Mixta 1-A) — p.21 — **DEROGADA**

El documento declara textualmente: **"ZONA SM1-A, Zona Mixta 1-A, DEROGADA"**. No trae cuadro de usos de suelo ni de subdivisión y edificación. Zona adicional no anticipada por nota_fase3.

---

### SM2 (Zona Mixta 2) — p.21 — **DEROGADA**

El documento declara textualmente: **"ZONA SM2, Zona Mixta 2 DEROGADA"**. No trae cuadro de usos de suelo ni de subdivisión y edificación.

---

### SM3 (Zona Mixta 3) — p.21

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Residencial | Todos |
| Equipamiento | Comercio, Culto y Cultura, Deporte, Educación, Esparcimiento, Salud, Seguridad, Servicios y Social, con excepción de lo indicado como prohibido |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Equipamiento | Científico; Comercio: Ferias Libres, Centros de Servicio Automotor o Servicentros, Bombas Bencineras (salvo la existente en el Rol de Avalúo N° 12042-5), Locales de Expendio de Combustibles, Quintas de Recreo; Cabarets y Similares; Deporte: Medialunas y Estadios; Esparcimiento: Zoológicos; Salud: Hospitales, Cementerio, Crematorio; Seguridad: Cuarteles, Cárceles, Centros de Detención y Otros |
| Actividades productivas | Salvo lo existente, Talleres Mecánicos de Reparación Automotriz, Tornerías, Carpintería Metálica, Mueblería y Carpintería |
| Infraestructura | de Transporte salvo la existente; Sanitaria y Energía, en conformidad al artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 200 m² |
| Coeficiente de ocupación de suelo (COS) | 0,8 |
| Coeficiente de constructibilidad | 2 |
| Densidad máxima | 300 hab/Há |
| Altura máxima de edificación — Aislado | 14,5 m |
| Altura máxima de edificación — Pareado | 14,5 m |
| Altura máxima de edificación — Continuo | — (no aplica / sin dato) |
| Antejardín | 5 m |

**Nota:** incentivos de densidad (480 hab/Há en vías de 18 m; 600 hab/Há en vías de 25 m) y eliminación de "Condiciones de expresión de la imagen urbana del barrio".

---

### SM4 (Zona Mixta 4) — p.21

#### Usos de suelo

No especificado en este documento — solo se transcribe la tabla de subdivisión (este decreto no modifica los usos de suelo de SM4).

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 150 m² |
| Coeficiente de ocupación de suelo (COS) | 0,8 |
| Coeficiente de constructibilidad | 2 |
| Antejardín | 3 m |
| Densidad, altura máxima, sistema de agrupamiento, distanciamientos, rasantes, ochavos | No especificado en este documento |

**Nota:** "Reemplácese en vías de 25 metros 'no habrá exigencias de densidad' por 'excepto el sistema de agrupamiento continuo y una densidad de 600 hab/Há'". Elimínense los tres últimos párrafos.

---

### BR-M1 (Zona Mixta Borde Ruta 1, Subcentro de Equipamiento) — p.21

#### Usos de suelo

No especificado en este documento — solo tabla de subdivisión.

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 500 m² |
| Coeficiente de ocupación de suelo (COS) | 0,6 |
| Coeficiente de constructibilidad | 2,0 |
| Antejardín | 5 m |
| Densidad, altura máxima, sistema de agrupamiento, distanciamientos, rasantes, ochavos | No especificado en este documento |

**Nota:** incentivos para proyectos que enfrenten Ruta Travesía (Ex-Ruta 5 Sur): hasta 20% incremento de densidad bruta máxima, hasta 25% incremento de coeficiente de constructibilidad, y 15% adicional de constructibilidad si además enfrenta vías ≥20 m de ancho — todos sujetos a incentivos IPAEP (Art. 9).

---

### BR-M2 (Zona Mixta Borde Ruta 2, Zona de Reconversión Sector Centro Norte) — p.22

#### Usos de suelo

No especificado en este documento — solo tabla de subdivisión.

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Coeficiente de ocupación de suelo (COS) | 0,8 |
| Coeficiente de constructibilidad | 1,2 |
| Antejardín | 5 m |
| Superficie predial mínima, densidad, altura máxima, sistema de agrupamiento, distanciamientos, rasantes, ochavos | No especificado en este documento |

**Nota:** incentivos similares a BR-M1 (25% densidad, 20% constructibilidad, +15% adicional en vías ≥20 m), sujeto a Art. 9.

---

### BR-M3 (Zona Mixta Borde Ruta 3, Zona de Reconversión Sector Centro Sur) — p.22

#### Usos de suelo

No especificado en este documento — solo tabla de subdivisión.

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 300 m² |
| Coeficiente de ocupación de suelo (COS) | 0,6 |
| Coeficiente de constructibilidad | 1,2 |
| Sistema de agrupamiento de las edificaciones | Aislado, Pareado, Continuo |
| Altura máxima de edificación — Pareado | 7 m |
| Altura máxima de edificación — Aislado / Continuo | No especificado en la tabla fuente (verificado con zoom: el cuadro solo trae valor para "Pareado", pese a permitir los 3 sistemas de agrupamiento — posible omisión del documento original, no de esta transcripción) |
| Antejardín | 5 m |
| Alturas de cierros | Según Artículo 14 de la presente Ordenanza |

**Normas con incentivo** (cuando esté ejecutada o garantizada la urbanización de las vías Enrique Molina y Claudio Matte — incentivo IV, Art. 9):

| Norma | Valor |
|---|---|
| Coeficiente de constructibilidad | 1,5 |
| Densidad máxima | 540 hab/Há |
| Altura máxima de edificación — Aislado | 24 m |
| Altura máxima de edificación — Pareado | — |
| Altura máxima de edificación — Continuo | 7 m |

---

### BR-M4 (Zona Mixta Borde Ruta 4, Zona de Equipamiento e Infraestructura Sanitaria) — p.23

#### Usos de suelo

No especificado en este documento — solo tabla de subdivisión.

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Coeficiente de ocupación de suelo (COS) | 0,8 |
| Coeficiente de constructibilidad | 2 |
| Superficie predial mínima, densidad, altura máxima, sistema de agrupamiento, antejardín, distanciamientos, rasantes, ochavos | No especificado en este documento |

**Nota:** incentivo para proyectos frente a Travesía (Ex-Ruta 5 Sur): +25% coeficiente de constructibilidad y +20% altura máxima, sujeto a Art. 9.

---

### BR-SM1 (Zona Mixta de Servicios Borde Ruta 1, Barrio Empresarial) — p.23

#### Usos de suelo

No especificado en este documento — solo tabla de subdivisión.

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Coeficiente de ocupación de suelo (COS) | 0,6 |
| Coeficiente de constructibilidad | 1,5 |
| Antejardín | 10 m |
| Superficie predial mínima, densidad, altura máxima, sistema de agrupamiento, distanciamientos, rasantes, ochavos | No especificado en este documento |

**Nota:** incentivo de +25% coeficiente de constructibilidad para proyectos frente a Ruta Travesía y vías ≥20 m, sujeto a Art. 9.

---

### BR-SM2 (Zona Mixta de Servicios Borde Ruta 2, Barrio Empresarial Sur) — p.23

#### Usos de suelo

No especificado en este documento — solo tabla de subdivisión.

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Coeficiente de ocupación de suelo (COS) | 0,8 |
| Coeficiente de constructibilidad | 2,0 |
| Antejardín | 10 m |
| Superficie predial mínima, densidad, altura máxima, sistema de agrupamiento, distanciamientos, rasantes, ochavos | No especificado en este documento |

**Nota:** incentivo de +15% coeficiente de constructibilidad en las mismas condiciones que BR-SM1.

---

### ZM (Zona Militar) — p.23-24 — *zona adicional, no en nota_fase3*

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Infraestructura | de Transporte: Instalaciones o recintos aeroportuarios y actividades de equipamiento complementarias al uso |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Residencial | Todos |
| Equipamiento | Todos |
| Actividades productivas | Todos |
| Infraestructura | de Transporte: Todos excepto los permitidos; Sanitaria y Energía, en conformidad al artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 2.500 m² |
| Coeficiente de ocupación de suelo (COS) | 0,3 |
| Coeficiente de constructibilidad | 0,2 |
| Densidad bruta máxima | — (no aplica / sin dato) |
| Sistema de agrupamiento — Residencial | — |
| Sistema de agrupamiento — Equipamiento | Aislado |
| Sistema de agrupamiento — Otros usos | Aislado |
| Adosamientos | Según lo dispuesto en O.G.U.C |
| Distanciamientos mínimos de adosamiento | Según lo dispuesto en O.G.U.C |
| Distanciamientos mínimos a los medianeros | Según lo dispuesto en O.G.U.C |
| Rasantes | Según lo dispuesto en O.G.U.C |
| Ochavos | Según lo dispuesto en O.G.U.C |
| Altura máxima de edificación — Aislado | 14 m |
| Altura máxima de edificación — Pareado | — |
| Altura máxima de edificación — Continuo | — |
| Antejardín | 10 m |
| Estacionamientos | Según Artículo 35 de la presente Ordenanza |
| Alturas de cierros | Según Artículo 14 de la presente Ordenanza |

---

### IA (Zona Industrial) — p.24

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Equipamiento | Científico, Comercio, Repartimiento, Seguridad y Servicios |
| Actividades productivas | Industria: inofensiva; Almacenamiento y Talleres de Impacto Similar al Industrial: inofensivos y molestos |
| Infraestructura | de Transporte: Todos |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Residencial | Todos |
| Equipamiento | Culto y Cultura: Todos; Deporte: Hipódromo; Educación: Todos; Esparcimiento: Zoológicos; Salud: Todos; Seguridad: Todos; Social: Todos |
| Actividades productivas | Industria: molesta |
| Infraestructura | Sanitaria: Todos y Energía: Todos, en conformidad al artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 600 m² |
| Coeficiente de ocupación de suelo (COS) | 0,8 |
| Coeficiente de constructibilidad | 1,5 |
| Alturas de cierros | 2,5 m |
| Densidad, altura máxima, sistema de agrupamiento, antejardín, distanciamientos, rasantes, ochavos | No especificado en este documento |

**Nota:** "Elimínese los cuatro últimos párrafos del texto vigente."

---

### IE (Zona Industrial Especial) — p.24-25

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Equipamiento | Científico, Comercio, Educación: referida exclusivamente a Educación Superior e Institutos Profesionales, y Servicios |
| Actividades productivas | Industria, Almacenamiento y Talleres de Impacto Similar al Industrial: inofensivas y molestas |
| Infraestructura | de Transporte: Todos |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Residencial | Todos |
| Equipamiento | Culto y Cultura, Deporte, Educación: Liceos, Academias, Establecimientos de Educación Básica y Media; Esparcimiento; Salud: Hospitales, clínicas; Seguridad: cárceles; Social |
| Infraestructura | Sanitaria: Todos y Energía: Todos, en conformidad al artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 800 m² |
| Coeficiente de ocupación de suelo (COS) | 0,8 |
| Coeficiente de constructibilidad | 1,5 |
| Antejardín | 10 m |
| Alturas de cierros | 2,5 m |
| Densidad, altura máxima, sistema de agrupamiento, distanciamientos, rasantes, ochavos | No especificado en este documento |

---

### IT-1 (Zona de Infraestructura de Transporte — Terminales de Buses) — p.25

#### Usos de suelo

No especificado en este documento — solo tabla de subdivisión.

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Coeficiente de ocupación de suelo (COS) | 0,5 |
| Coeficiente de constructibilidad | 1,5 |
| Estacionamientos | Según Artículo 35 de la presente Ordenanza |
| Superficie predial mínima, densidad, altura máxima, sistema de agrupamiento, antejardín, distanciamientos, rasantes, ochavos | No especificado en este documento |

---

### EQS (Equipamiento de Salud) — p.25

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Equipamiento | Comercio: locales comerciales (Librería, farmacia, ópticas, venta de insumos médicos, fuentes de soda, cafetería); Deporte: orientado exclusivamente a centros de rehabilitación física y tratamiento terapéutico, gimnasios; Salud: Todos excepto los prohibidos; Servicios: instituciones de salud, previsional, administradoras de fondos de pensiones, compañías de seguros, bancos, centros de belleza (centros de estética, peluquerías, spa), servicios de estacionamiento |
| Espacios públicos / Áreas verdes | Todos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Residencial | Viviendas; Hogares de acogida y Hospedaje |
| Equipamiento | Científico: todos; Comercio: Todos, excepto los señalados como permitidos; Culto y Cultura: Todos; Deporte: Todos, excepto los señalados como permitidos; Salud: Cementerios y crematorios; Educación: Todos; Esparcimiento: Todos; Seguridad: Todos; Servicios: Todos, excepto los señalados como permitidos; Social: Todos |
| Actividades productivas | Todos |
| Infraestructura | Todos, en conformidad al artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 2.500 m² |
| Coeficiente de ocupación de suelo (COS) | 0,6 |
| Coeficiente de constructibilidad | 1,5 |
| Estacionamientos | Según Artículo 35 de la presente Ordenanza |
| Densidad, altura máxima, sistema de agrupamiento, antejardín, distanciamientos, rasantes, ochavos | No especificado en este documento |

---

### EQ-SC (Equipamiento de Salud - Cementerios) — p.25-26

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Equipamiento | Comercio: fuentes de sodas, Cafeterías, Florería; Servicios: servicio de Estacionamientos; Salud: Cementerio, Crematorios |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Residencial | Viviendas; Hogares de acogida y Hospedaje |
| Equipamiento | Todos, excepto los señalados como permitidos |
| Actividades productivas | Todos |
| Infraestructura | Todos, en conformidad al artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Predial mínima | 2.500 m² |
| Coeficiente de ocupación de suelo (COS) | 0,2 |
| Coeficiente de constructibilidad | 0,2 |
| Altura máxima de edificación | 7 m |
| Antejardín | — (no aplica / sin dato) |
| Estacionamientos | Según Artículo 35 de la presente Ordenanza |
| Alturas de cierros | Según Artículo 14 de la presente Ordenanza |
| Densidad, sistema de agrupamiento, distanciamientos, rasantes, ochavos | No especificado en este documento |

---

### EQ-CB (Equipamiento Centro de Barrio) — p.26

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Equipamiento | Comercio: Todos, excepto los señalados como prohibidos; Culto y Cultura: Todos, excepto los señalados como prohibidos; Deporte: Todos, excepto los señalados como prohibidos; Educación: Universidades, Institutos Profesionales o Centro de Formación Técnica; Salud: Todos, excepto los señalados como prohibidos; Seguridad: Unidades policiales; Servicios: Todos |
| Actividades productivas | Talleres de Impacto Similar al Industrial: inofensivos excepto los prohibidos |
| Infraestructura | Transporte: Todos |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Residencial | Viviendas; Hogares de acogida y Hospedaje |
| Equipamiento | Científico: Todos; Comercio: Quintas de Recreo, restaurante de turismo, Cabaret (espectáculo y show en vivo), discotecas o salón de bailes similares, peña folclórica, hotel de turismo, motel de turismo; Culto y Cultura: Catedrales, Templos, Santuarios, Sinagogas, Mezquitas, Capillas, Parroquias; Deporte: Estadios, Hipódromos, Medialunas, cancha; Educación: Todos, excepto los señalados como permitidos; Esparcimiento: Todos; Salud: Hospitales, Centro de rehabilitación, Cementerios, Crematorios; Seguridad: Todos, excepto los señalados como permitidos; Social: Todos |
| Actividades productivas | Industria y Almacenamiento: inofensivos y molestos; Talleres de Impacto Similar al Industrial de Tornería, Carpintería Metálica, Mueblería, Carpintería y Vulcanización y los Talleres molestos |
| Infraestructura | Sanitaria: Todos y Energía: Todos, en conformidad al artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Coeficiente de constructibilidad | 2,5 |
| Superficie predial mínima, COS, densidad, altura máxima, sistema de agrupamiento, antejardín, distanciamientos, rasantes, ochavos | No especificado en este documento (el cuadro fuente solo trae esta fila) |

---

### EQ-CB1 (Equipamiento Centro de Barrio del Tipo 1) — p.26-27

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Residencial | Hospedaje: Hoteles |
| Equipamiento | Comercio; Culto y Cultura; Deporte: Centros Deportivos, Gimnasios; Educación: Jardines Infantiles y Salas Cuna, Establecimientos de Educación Básica y Media, OTEC; Esparcimiento: Parque de Entretenciones, Casino de Juegos; Salud; Servicios |
| Actividades productivas | Talleres de Impacto Similar al Industrial: inofensivos excepto los prohibidos |
| Infraestructura | Transporte: de Taxibuses, Taxis y Taxis Colectivos de Servicio Urbano Comunal |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Residencial | Vivienda, Hogares de acogida y Hospedaje: todos, excepto lo permitido |
| Equipamiento | Científico; Comercio: Quintas de Recreo, Ferias libres, Centro de Servicio Automotor o Servicentros, Bombas de Bencina, Locales de Expendio de Combustibles; Culto y Cultura: Templos, Santuarios; Deporte: Estadios, Multicanchas, Piscinas, Sauna, Baños Turcos; Educación: Educación Superior, Universidades, Institutos Profesionales o Centro de Formación Técnica, Centros de Capacitación, Centros de rehabilitación Conductual, Academias, Educación Básica Especial; Esparcimiento: Parques Zoológicos, Parques Juegos electrónicos o mecánicos, Circos, Zona de Picnic, Balneario; Salud: Hospitales, Clínicas, Consultorios, Policlínicos, Postas, Centros de Rehabilitación, Cementerios, Crematorios; Seguridad; Servicios: Servicio de Estacionamientos con excepción de los asociados a proyectos de edificación; Social |
| Actividades productivas | Industria, Almacenamiento y Talleres de Impacto Similar al Industrial: Talleres Mecánicos de Reparación Automotriz, Garajes, Carpintería Metálica, Mueblería, Carpintería de Madera, de tipo molestos |
| Infraestructura | Transporte: Estación o terminal Ferroviario, Terminales de Transporte Terrestre, Rodoviarios, Depósito de 3 o más buses o camiones; Sanitaria y Energía, en conformidad al artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 1.000 m² |
| Coeficiente de ocupación de suelo (COS) | 0,7 |
| Coeficiente de constructibilidad | 4,0 |
| Antejardín | 5 m |
| Estacionamientos | Según Artículo 35 de la presente Ordenanza |
| Densidad, altura máxima, sistema de agrupamiento, distanciamientos, rasantes, ochavos | No especificado en este documento |

---

### EQ-PU-1 (Equipamiento Parque Urbano Especial del Tipo 1) — p.27 — **DEROGADA**

El documento declara textualmente: **"ZONA EQ-PU-1, Equipamiento Parque Urbano Especial del Tipo 1 DEROGADA"**. Ver zona sucesora **ZEQPU-1** (misma sección, con cuadro completo) y, en la sección del Art. 27 "Áreas Consolidadas", la sucesora alternativa **PU1-AV** (p.28) — ambas derivadas de esta zona derogada, en dos partes distintas del decreto (ver "Nota de alcance").

---

### EQ-PU-2 (Equipamiento Parque Urbano Especial del Tipo 2) — p.27 — **DEROGADA**

El documento declara textualmente: **"ZONA EQ-PU-2, Equipamiento Parque Urbano Especial del Tipo 2 DEROGADA"**. Ver zona sucesora **PU2-EP** (p.28, sección Art. 27).

---

### EQ-E (Equipamiento Especial) — p.27 — **DEROGADA**

El documento declara textualmente: **"ZONA EQ-E, Equipamiento Especial DEROGADA"**. No se identificó zona sucesora explícita dentro del rango de páginas transcrito.

---

### ZEQPU-1 (Equipamiento Parque Urbano Especial del Tipo 1) — p.27 — *sucesora de EQ-PU-1 en esta sección*

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Equipamiento | Comercio: Cafetería, Casino de Alimentos; Culto y Cultura: centros culturales, salas de cultura, museos, bibliotecas, salas de concierto, galerías de arte, salas de exposición, auditorios, centro de eventos, centros de convenciones, exposiciones o centros de difusión de toda especie (medios de comunicación: canales de televisión, radio, prensa escrita); Deporte: Todos |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Residencial | Viviendas, Hogares de Acogida, Hospedaje |
| Equipamiento | Científico: Todos; Comercio: Supermercado, Centros Comerciales, Grandes Tiendas, Mercados, Centros de Servicio Automotor o Servicentros, Bombas de Bencina, Locales de Expendio de Combustible, Bares, Cantinas, Quintas de Recreo, Cabaret, Discotecas, Salones de Baile, Depósitos de Alcoholes; Culto y Cultura: Todos excepto los permitidos, Jardines Botánicos; Educación: Educación Superior, Universidades, Institutos Profesionales o Centro de Formación Técnica, Educación Técnica, Establecimientos de Educación Básica y Media, Educación Básica Especial, Jardín Infantil, Sala Cuna, Centros de Capacitación OTEC, Centros de Orientación, Centros de Rehabilitación Conductual, Academias; Esparcimiento: Todos; Salud: Todos; Seguridad: Todos; Servicios: Todos; Social: Todos |
| Actividades productivas | Industria, Almacenamiento y Talleres de Impacto Similar al Industrial: inofensivas y molestas |
| Infraestructura | De Transporte; Sanitaria y Energía, en conformidad al artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 2.500 m² |
| Coeficiente de ocupación de suelo (COS) | 0,2 |
| Coeficiente de constructibilidad | 0,5 |
| Densidad bruta máxima | No se exige |
| Sistema de agrupamiento — Residencial | — |
| Sistema de agrupamiento — Equipamiento | Aislado |
| Sistema de agrupamiento — Otros usos | Aislado |
| Adosamientos | Según lo dispuesto en O.G.U.C |
| Distanciamientos mínimos de adosamiento | Según lo dispuesto en O.G.U.C |
| Distanciamientos mínimos a los medianeros | Según lo dispuesto en O.G.U.C |
| Rasantes | Según lo dispuesto en O.G.U.C |
| Ochavos | Según lo dispuesto en O.G.U.C |
| Altura máxima de edificación — Aislado | Según rasante |
| Altura máxima de edificación — Pareado | — |
| Altura máxima de edificación — Continuo | — |
| Antejardín | 10 m |
| Estacionamientos | Según Artículo 35 de la presente Ordenanza |
| Alturas de cierros | 5,5 m |

---

### C1 (Zona Corredor Comercial 1) — p.27-28

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Residencial | Vivienda, Hogares de Acogida y Hospedaje: Hotel |
| Equipamiento | Científico; Comercio; Culto y Cultura; Deporte; Educación; Esparcimiento; Salud: Todos, exceptos los prohibidos; Seguridad: Todos, exceptos los prohibidos; Servicios; Social |
| Actividades productivas | Almacenamiento: del tipo Inofensivos y Talleres de Impacto Similar al Industrial: del tipo inofensivo excepto los prohibidos |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Residencial | Hospedaje: Excepto los permitidos |
| Equipamiento | Deporte: Hipódromos; Esparcimiento: Zoológicos; Salud: Cementerios, Crematorios; Seguridad: Cárceles |
| Actividades productivas | Industria, Almacenamiento del tipo molestos; Talleres de Impacto Similar al Industrial del tipo Molestos y Tornería, Carpintería Metálica, Carpintería de Madera |
| Infraestructura | De transporte; Sanitaria y Energía, conforme lo señala el artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Coeficiente de constructibilidad | 4,0 |
| Antejardín | 3 m |
| Alturas de cierros | Según Artículo 14 de la presente Ordenanza |
| Superficie predial mínima, COS, densidad, altura máxima, sistema de agrupamiento, distanciamientos, rasantes, ochavos | No especificado en este documento |

**Nota:** se eliminan incentivos en vías de 18 y 25 m, 7 párrafos referidos a bombas de bencina/talleres de garajes, y condiciones de expresión de la imagen urbana del barrio.

---

### PE (Zona Portal Estación) — p.28 — *zona adicional, no en nota_fase3*

#### Usos de suelo

No especificado en este documento — solo tabla de subdivisión.

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Coeficiente de ocupación de suelo (COS) | 0,9 |
| Coeficiente de constructibilidad | 5 |
| Antejardín | 5 m |
| Superficie predial mínima, densidad, altura máxima, sistema de agrupamiento, distanciamientos, rasantes, ochavos | No especificado en este documento |

**Nota:** se elimina, a continuación del cuadro, el bloque de "áreas verdes y arborización" y "condiciones de expresión de la imagen urbana del barrio".

---

### PU1-AV (Zona de Parques privados) — p.28 — *sucesora de EQPU1 (Art. 27)*

#### Usos de suelo

No especificado en este documento — solo tabla de subdivisión. El texto agrega, posterior al cuadro: "Se considerarán siempre permitidos puntos limpios y verdes en áreas verdes privadas".

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 2.500 m² |
| Alturas de cierros | 5,5 m |
| COS, coeficiente de constructibilidad, densidad, altura máxima, sistema de agrupamiento, antejardín, distanciamientos, rasantes, ochavos | No especificado en este documento |

---

### PU2-EP (Zona de Parques Bien Nacional de uso público) — p.28 — *sucesora de EQPU2 (Art. 27)*

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Equipamiento | Científico; Comercio: locales comerciales, ferias itinerantes (complementario al uso del Parque); Culto y Cultura: Todos; Deporte: Todos; Esparcimiento: Todo excepto lo prohibido |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Residencial | Todos |
| Equipamiento | Comercio: Todos los no permitidos; Educación: Todos; Esparcimiento: juegos electrónicos o mecánicos (máquinas destreza); Salud: Todos; Seguridad: Todos; Servicios: servicios públicos, servicios profesionales, servicios artesanales; Social: Todo |
| Actividades productivas | Todos |
| Infraestructura | De Transporte, Sanitaria y Energía, conforme lo señala el artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 2.500 m² |
| Coeficiente de ocupación de suelo (COS) | 0,2 |
| Coeficiente de constructibilidad | 0,3 |
| Densidad bruta máxima | — |
| Sistema de agrupamiento — Residencial | — |
| Sistema de agrupamiento — Equipamiento | Aislado |
| Sistema de agrupamiento — Otros usos | Aislado |
| Adosamientos | Según lo dispuesto en O.G.U.C |
| Distanciamientos mínimos de adosamiento | Según lo dispuesto en O.G.U.C |
| Distanciamientos mínimos a los medianeros | Según lo dispuesto en O.G.U.C |
| Rasantes | Según lo dispuesto en O.G.U.C |
| Ochavos | Según lo dispuesto en O.G.U.C |
| Altura máxima de edificación — Aislado | Según rasante |
| Altura máxima de edificación — Pareado | — |
| Altura máxima de edificación — Continuo | — |
| Antejardín | 5 m |
| Estacionamientos | Según Artículo 35 de la presente Ordenanza |
| Alturas de cierros | 5,5 m |

---

### EX1 (Zona Extensión urbana 1) — p.29

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Residencial | Viviendas, Hogares de acogida |
| Equipamiento | Comercio, Culto y Cultura, Deporte, Educación, Esparcimiento; Salud; Seguridad, Servicios y Social |
| Actividades productivas | Industria: del tipo Inofensivo; Almacenamiento: del tipo Inofensivo y Talleres de Impacto Similar al Industrial: del tipo Inofensivo |
| Infraestructura | Transporte: Terminales de Buses, Taxibuses, Taxis, Taxis Colectivos, Depósitos de Buses o Camiones de hasta 2 vehículos |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Residencial | Hospedaje |
| Equipamiento | Científico; Esparcimiento: Parques Zoológicos; Seguridad: Centros de Detención (Cárceles, etc.), Centros de Reclusión Nocturno |
| Actividades productivas | Industria Molesta, Almacenamiento Molesto: Centros de distribución de todo tipo, Almacenamiento Industrial y/o Bodegaje molestos; Establecimientos de Impacto Similar al Industrial: Talleres Industriales, Talleres Mecánicos de Reparación Automotriz, Garajes, Tornerías, Carpintería Metálica, Maestranzas; Mueblerías, Carpintería Madera, Imprentas clasificadas molestas |
| Infraestructura | Transporte: Vías Ferroviarias, Estaciones Ferroviarias, Instalaciones o Recintos Aeroportuarios, Rodoviario, Depósitos de Buses o Camiones de 3 vehículos o más; Sanitaria: Plantas de Captación, Plantas de Distribución, Plantas de Tratamiento, Rellenos Sanitarios, Estaciones de Transferencia de Residuos; Energía: Centrales de Generación o Distribución de Energía, Centrales de Generación o Distribución de Gas, Centrales de Generación o Distribución de Telecomunicaciones, Gasoductos, Etc., conforme lo señala el artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 250 m² |
| Coeficiente de ocupación de suelo (COS) | 0,5 |
| Coeficiente de constructibilidad | 1,4 |
| Altura máxima de edificación — Aislado | 17,5 m |
| Altura máxima de edificación — Pareado | 17,5 m |
| Altura máxima de edificación — Continuo, antejardín, densidad, sistema de agrupamiento, distanciamientos, rasantes, ochavos | No especificado en este documento (el cuadro fuente termina en la fila "Pareado"; verificado con zoom) |

**Nota:** incentivo IIS para proyectos con desarrollo mínimo de 2,0 Há por extensión o densificación: pueden acogerse a usos y normas de la Zona R2, Art. 9.

---

### EX2 (Zona Extensión urbana 2) — p.29-30

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Residencial | Viviendas, Hogares de acogida |
| Equipamiento | Comercio, Culto y Cultura, Deporte, Educación, Esparcimiento; Salud; Seguridad, Servicios y Social |
| Actividades productivas | Almacenamiento: Inofensivo y Talleres de Impacto Similar al Industrial: Inofensivos |
| Infraestructura | Transporte: Terminales de Buses, Taxibuses, Taxis, Taxis Colectivos, Depósitos de Buses o Camiones de hasta 2 vehículos |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Residencial | Hospedaje |
| Equipamiento | Científico; Comercio: Moteles de Turismo, Cabaret, Quintas de Recreo, Discotecas o Salones de Baile, similares; Esparcimiento: Parques Zoológicos; Seguridad: Centros de Detención, Cárceles, etc., Centros de Reclusión Nocturna |
| Actividades productivas | Industria, Almacenamiento del tipo Molesto, Centros de distribución de todo tipo, Almacenamiento Industrial y/o Bodegaje molestos, del tipo peligroso y/o contaminante; Establecimientos de Impacto Similar al Industrial: Talleres Industriales del tipo molesto, Talleres Mecánicos de Reparación Automotriz, Garajes, Tornerías, Carpintería Metálica, Maestranzas; Mueblerías, Carpintería Madera, Imprentas clasificadas molestas |
| Infraestructura | Transporte: Vías Ferroviarias, Estaciones Ferroviarias, Instalaciones o Recintos Aeroportuarios, Rodoviario, Depósitos de Buses o Camiones de 3 vehículos o más; Sanitaria: Plantas de Captación, Plantas de Distribución, Plantas de Tratamiento, Rellenos Sanitarios, Estaciones de Transferencia de Residuos; Energía: Centrales de Generación o Distribución de Energía, Gas o Telecomunicaciones, Gasoductos, Etc., conforme lo señala el artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 250 m² |
| Coeficiente de ocupación de suelo (COS) | 0,4 |
| Coeficiente de constructibilidad | 0,7 |
| Altura máxima de edificación — Aislado | 17,5 m |
| Altura máxima de edificación — Pareado | 17,5 m |
| Altura máxima de edificación — Continuo | — |
| Profundidad Máxima de Pareo | 40% del deslinde común |
| Densidad, antejardín, distanciamientos, rasantes, ochavos | No especificado en este documento |

**Nota:** mismo incentivo IIS de 2,0 Há descrito en EX1 (acogerse a normas de Zona R2).

---

### EX3 (Zona Extensión urbana 3) — p.30-31

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Residencial | Viviendas, Hogares de acogida |
| Equipamiento | Comercio, Culto y Cultura, Deporte, Educación, Esparcimiento, Salud; Servicios y Social |
| Actividades productivas | Talleres de Impacto Similar al Industrial: Inofensivos |
| Infraestructura | Transporte: Terminales de Buses, Taxibuses, Taxis, Taxis Colectivos, Depósitos de Buses o Camiones de hasta 2 vehículos |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Residencial | Hospedaje |
| Equipamiento | Científico; Comercio: Centros Comerciales, Grandes Tiendas, Supermercados, Estaciones o centros de Servicio Automotor, Discotecas o Salones de Baile, Bombas de bencina, Locales de Expendio de Combustibles, Servicios de Estacionamiento, Cabarets, Quintas de Recreo; Culto y Cultura: Templos, Santuarios, Centros Culturales, Salas de Cultura, Museos, Salas de Concierto o Espectáculos, Cines, Teatros, Galerías de Arte, Salas de Exposición, Auditorios, Centros de Convenciones, Exposiciones o centros de Difusión de toda especie, Jardines Botánicos; Deporte: Autódromos, Hipódromos, Saunas, Baños Turcos, Medialunas, Coliseos; Educación: Educación Básica (Liceos, Colegios, Escuelas Básicas), Educación Básica Especial, Educación Parvularia, Jardín Infantil, Salas Cuna, Academias (Danza, Música, Idiomas); Esparcimiento: Parques de Entretenciones, Parques Zoológicos, Circos, Zonas de Picnic, Balnearios, Camping, Casinos de Juegos; Salud: Hospitales, Clínicas, Postas, Centros de Rehabilitación Física o Terapéutico, Cementerios, Crematorios, Laboratorios Clínicos, Laboratorios dentales; Seguridad; Servicios: Centros de Oficinas en General, Centros Médicos, Centros Dentales, Notarías, Instituciones Financieras (Bancos, Financieras), Servicios Públicos en General (Ministerios, Intendencias, Gobernaciones, Defensorías, Ministerios Públicos, Cortes de Justicia, Servicios de Utilidad Pública, Servicios de la Administración Pública, Departamentos o Unidades Municipales, Juzgados, etc.) |
| Actividades productivas | Industria, Almacenamiento, Establecimientos de Impacto Similar al Industrial: Talleres Industriales del tipo molesto, Talleres Mecánicos de Reparación Automotriz, Garajes, Tornerías, Carpintería Metálica, Maestranzas; Mueblerías, Carpintería Madera, Imprentas clasificadas molestas |
| Infraestructura | De Transporte: Vías Ferroviarias, Estaciones Ferroviarias, Instalaciones o Recintos Aeroportuarios, Rodoviario, Depósitos de Buses o Camiones de 3 vehículos o más; Sanitaria: Plantas de Captación, Plantas de Distribución, Plantas de Tratamiento, Rellenos Sanitarios, Estaciones de Transferencia de Residuos; Energía: Centrales de Generación o Distribución de Energía, Gas o Telecomunicaciones, Gasoductos, Etc., en conformidad con el artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 600 m² |
| Coeficiente de ocupación de suelo (COS) | 0,3 |
| Coeficiente de constructibilidad | 0,5 |
| Altura máxima de edificación — Aislado | 17,5 m |
| Altura máxima de edificación — Pareado | — |
| Altura máxima de edificación — Continuo | — |
| Densidad, antejardín, sistema de agrupamiento, distanciamientos, rasantes, ochavos | No especificado en este documento |

**Normas con incentivo** (proyectos que enfrenten/formen parte de Parque Lineal Vía Verde Parque Norte, Parque Las Torres, Parque Lineal Las Torres, Parque Lineal Santa Blanca, Parque Lineal Nemesio Antúnez, Parque Rabanal Norte, Parque Lineal El Rabanal Sur, Parque Diagonal Doñihue, consolidación infraestructura verde eje Río Loco — Art. 9):

| Norma | Valor |
|---|---|
| Densidad Bruta Máxima | 480 hab/Há |
| Coeficiente de ocupación de suelo | 0,4 |
| Coeficiente de constructibilidad | 0,8 |
| Altura máxima de edificación | 28 m |

---

### EX4 (Zona Extensión urbana 4) — p.31 — **DEROGADA**

El documento declara textualmente: **"ZONA EX4, Zona Extensión urbana 4/ DEROGADA"**. No trae cuadro de usos de suelo ni de subdivisión y edificación.

---

### EX5 (Zona Extensión urbana 5) — p.31 — *zona adicional, no en nota_fase3*

#### Usos de suelo

No especificado en este documento.

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Estacionamientos | Según Artículo 35 de la presente Ordenanza |
| Todos los demás campos (predial mínima, COS, CC, densidad, altura, agrupamiento, antejardín, distanciamientos, rasantes, ochavos) | No especificado en este documento (el cuadro fuente solo trae esta fila) |

**Nota:** "Elimínese todos los párrafos después del cuadro de normas de subdivisión predial y edificación."

---

### EX6 (Zona Extensión urbana 6) — p.31 — *zona adicional, no en nota_fase3; decreto distinto del "EX 6" ya cubierto en esta carpeta*

**Advertencia:** esta zona EX6 pertenece al Decreto 559/764 de 2023 (Plan Seccional N°21). **No debe confundirse** con la zona "EX 6" del archivo `rancagua_fe_erratas_tramitacion16_zona_ex6_pag1-2.md` de esta misma carpeta, que corresponde a la Fe de Erratas de la Tramitación N°16 (2009/2010) — documento y probablemente delimitación distintos, aunque compartan sigla. No se cruzó ni mezcló información entre ambos.

#### Usos de suelo

No especificado en este documento — solo tabla de subdivisión.

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 400 m² |
| Coeficiente de ocupación de suelo (COS) | 0,8 |
| Coeficiente de constructibilidad | 1,2 |
| Antejardín | 2 m |
| Estacionamientos | Según Artículo 35 de la presente Ordenanza |
| Densidad, altura máxima, sistema de agrupamiento, distanciamientos, rasantes, ochavos | No especificado en este documento |

---

### EX7 (Zona Extensión urbana 7) — p.31 — *zona adicional, no en nota_fase3*

#### Usos de suelo

No especificado en este documento — solo tabla de subdivisión.

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 600 m² |
| Coeficiente de ocupación de suelo (COS) | 0,3 |
| Coeficiente de constructibilidad | 0,5 |
| Altura máxima de edificación — Aislado | 17,5 m |
| Altura máxima de edificación — Pareado / Continuo | No especificado en este documento (el cuadro fuente solo trae "Aislado") |
| Densidad, antejardín, sistema de agrupamiento, distanciamientos, rasantes, ochavos | No especificado en este documento |

**Nota:** "Elimínese: 'Todo equipamiento deberá regirse para los efectos de su emplazamiento, al Artículo 37 de la presente Ordenanza'".

---

### EX8 (Zona Extensión urbana 8, Barrio Norte) — p.31 — *zona adicional, no en nota_fase3*

#### Usos de suelo

No especificado en este documento — solo tabla de subdivisión.

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 300 m² |
| Coeficiente de ocupación de suelo (COS) | 0,8 |
| Coeficiente de constructibilidad | 2 |
| Antejardín | 3 m |
| Estacionamientos | Según Artículo 35 de la presente Ordenanza |
| Densidad, altura máxima, sistema de agrupamiento, distanciamientos, rasantes, ochavos | No especificado en este documento |

---

### BRO (Zona Borde Ruta Oriente) — p.32 — *zona adicional, no en nota_fase3*

#### Usos de suelo

No especificado en este documento — solo tabla de subdivisión.

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 1.500 m² |
| Coeficiente de ocupación de suelo (COS) | 0,6 |
| Coeficiente de constructibilidad | 10 [sic] — verificado con zoom 2x, se lee literalmente "10" sin coma decimal; valor atípicamente alto frente al resto de las zonas del documento (posible errata del original por "1,0"; confianza MEDIA en esta celda puntual, se transcribe tal cual sin corregir) |
| Densidad, altura máxima, sistema de agrupamiento, antejardín, distanciamientos, rasantes, ochavos | No especificado en este documento |

**Nota — valores ELIMINADOS por este decreto (ya NO vigentes, no confundir con norma actual):** el documento muestra un recuadro "Elimínese del cuadro de normas de subdivisión predial y edificación" con los siguientes valores que dejan de aplicar: Áreas verdes mínimo 20%; Arborización Mínima al interior del terreno de edificios colectivos: 1 árbol por c/piso dentro del terreno del proyecto; Arborización Mínima al interior del terreno de otros usos residencial y otros usos: 1 árbol por c/150 m² del terreno del proyecto. Se documentan aquí solo como referencia histórica.

---

### EQ-CBSO (Zona Equipamiento Centro de Barrio Sur Oriente) — p.32

#### Usos de suelo

No especificado en este documento — solo tabla de subdivisión.

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 1.500 m² |
| Coeficiente de ocupación de suelo (COS) | 0,6 |
| Coeficiente de constructibilidad | 8 |
| Altura máxima de edificación — Aislado | 17,5 m |
| Altura máxima de edificación — Pareado / Continuo, densidad, antejardín, sistema de agrupamiento, distanciamientos, rasantes, ochavos | No especificado en este documento |

---

### RAM (Zona Residencial Altura Media) — p.32

#### Usos de suelo

No especificado en este documento — solo tabla de subdivisión.

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Densidad bruta máxima | 750 hab/Há |
| Altura máxima de edificación — Aislado | 17,5 m |
| Altura máxima de edificación — Pareado | — |
| Altura máxima de edificación — Continuo | — |
| Estacionamientos | Según Artículo 35 de la presente Ordenanza |
| Superficie predial mínima, COS, coeficiente de constructibilidad, sistema de agrupamiento, antejardín, distanciamientos, rasantes, ochavos | No especificado en este documento |

---

### Z11A (Zona Restricción de los cabezales del Puerto Aéreo) — p.32 — *zona adicional, no en nota_fase3*

#### Usos de suelo y normas de subdivisión

No trae cuadro numérico. El texto reemplaza íntegramente la norma anterior por: **"En esta zona se aplican las restricciones establecidas en el Cono de Proyección Protección del Aeródromo 'La Independencia', Rancagua, VI Región, elaborado por la Dirección General de Aeronáutica Civil, reglamentada por la Ley 16.752"**. Todos los campos de COS/CC/altura/etc. quedan, por tanto, **No especificado en este documento** (remiten a normativa aeronáutica sectorial externa al PRC).

---

### Z11B-1 (Zona Restricción por aproximación al Puerto Aéreo B-1) — p.32-33

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Equipamiento | Comercio: Locales comerciales, Estaciones o centros de Servicio Automotor, Restaurantes, Restaurantes de Turismo, Fuentes de Soda, Bares, Bombas de bencina, Locales de Expendio de Combustibles, Botillerías, Depósitos de Alcoholes, Cocinerías, Locales de Comida al Paso, Almacenes; Culto y Cultura: Centros Culturales, Salas de Cultura, Museos, Bibliotecas; Deporte: Centros y Clubes Deportivos, Multicanchas, Piscinas, Saunas, Baños Turcos; Esparcimiento: Jardines Botánicos; Seguridad: Todos excepto los señalados como prohibido; Servicios: Servicios de Estacionamiento y Social |
| Actividades productivas | Almacenamiento: del tipo inofensiva y Talleres de Impacto Similar al Industrial: del tipo inofensivo |
| Infraestructura | Transporte: Todos excepto los señalados como prohibido |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Residencial | Vivienda; Hogares de acogida, Hospedaje |
| Equipamiento | Científico; Comercio: Todos excepto los señalados como permitidos; Culto y Cultura: Todos excepto los señalados como permitidos; Deporte: Todos excepto los señalados como permitidos; Educación: Todos; Seguridad: cárceles; Servicios: Todos excepto los señalados como permitidos; Social |
| Actividades productivas | Industria: inofensivos y molestas; Almacenamiento: Todos excepto los señalados como permitidos; Establecimientos de Impacto Similar al Industrial: Todos excepto los señalados como permitidos |
| Infraestructura | Transporte: Rodoviario; Sanitaria, Energía, conforme lo señala el artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Coeficiente de ocupación de suelo (COS) | 0,3 |
| Coeficiente de constructibilidad | 0,3 |
| Alturas de cierros | Según Artículo 14 de la presente Ordenanza |
| Superficie predial mínima, densidad, altura máxima, sistema de agrupamiento, antejardín, distanciamientos, rasantes, ochavos | No especificado en este documento |

**Nota:** se agrega también la referencia al Cono de Proyección Protección del Aeródromo "La Independencia" (Ley 16.752/DGAC).

---

### Z11B-2 (Zona Restricción por aproximación al Puerto Aéreo B-2) — p.33 — *zona adicional, no en nota_fase3*

#### Usos de suelo

No especificado en este documento — solo tabla de subdivisión.

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Coeficiente de ocupación de suelo (COS) | 0,4 |
| Distanciamientos mínimos de adosamiento | Según lo dispuesto en O.G.U.C |
| Rasantes | Según lo dispuesto en O.G.U.C |
| Ochavos | Según lo dispuesto en O.G.U.C |
| Alturas de cierros | Según Artículo 14 de la presente Ordenanza |
| Superficie predial mínima, coeficiente de constructibilidad, densidad, altura máxima, sistema de agrupamiento, antejardín, distanciamientos a medianeros | No especificado en este documento |

**Nota:** también remite al Cono de Proyección Protección del Aeródromo "La Independencia" (Ley 16.752/DGAC).

---

### Z12 (Zona Restricción de trazado de alta tensión y subestaciones eléctricas) — p.33 — *zona adicional, no en nota_fase3*

No trae cuadro numérico ni de usos de suelo. El decreto **elimina** la disposición anterior: "Los proyectos que se emplacen en interior de la zona Z12 cuyos terrenos sean afectados por redes de alta tensión, deberán respetar las disposiciones sectoriales que regulan las fajas de protección asociadas a dichas redes establecidas por el organismo competente, bajo las cuales sólo se podrán desarrollar usos de suelo de área verde, espacio público y los usos fijados por dicha normativa sectorial." Todos los campos quedan **No especificado en este documento**.

---

### Z20 (Zona Áreas de uso potencial Paraderos de Buses Carretera 5 Sur) — p.33 — **DEROGADO**

El documento declara textualmente: **"ZONA Z20, Zona Áreas de uso potencial Paraderos de Buses Carretera 5 Sur, DEROGADO"**. No trae cuadro de usos de suelo ni de subdivisión y edificación.

---

### ZCH-1 (Zona de Conservación Histórica N°1 - Eje Estado) — p.33 — *ver nota importante*

**Advertencia:** el cuadro completo de normas de ZCH-1 (con COS y Coeficiente de Constructibilidad = 3,0 corregido) pertenece al **Decreto 3.326/2020**, ya transcrito en `rancagua_2236_fe_erratas_zch1_za1_pag2.md` de esta misma carpeta. Este documento (Decreto 559/764, 2023) es un **decreto distinto** y **solo modifica una fila puntual** de la norma de ZCH-1:

#### Normas de subdivisión y edificación (según este decreto, 2023)

| Norma | Valor |
|---|---|
| Estacionamientos | Según Artículo 35 de la presente Ordenanza |
| Resto de las normas (superficie predial mínima, COS, coeficiente de constructibilidad, densidad, altura, agrupamiento, antejardín, distanciamientos, rasantes, ochavos) | No especificado en este documento — ver Decreto 3.326/2020 (archivo `rancagua_2236_fe_erratas_zch1_za1_pag2.md` de esta carpeta) para el cuadro completo vigente a esa fecha |

---

## TEMA N°2 — Creación y fortalecimiento de subcentros urbanos / corredores comerciales

### EQ-CBM1 (Equipamiento Centro de Barrio Mixto 1) — p.35-36 — *zona nueva creada por este decreto*

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Residencial | Vivienda: Todos |
| Equipamiento | Comercio: Todos, excepto los señalados como prohibidos; Culto y Cultura: Todos, excepto los señalados como prohibidos; Deporte: Todos, excepto los señalados como prohibidos; Educación: Universidades, Institutos Profesionales o Centro de Formación Técnica; Salud: Todos, excepto los señalados como prohibidos; Seguridad: Unidades policiales; Servicios: Todos |
| Infraestructura | Transporte: Todos |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Residencial | Hogares de acogida: todos y Hospedaje: todos |
| Equipamiento | Científico: Todos; Comercio: Quintas de Recreo, restaurante de turismo, Cabaret (espectáculo y show en vivo), discotecas o salón de bailes similares, peña folclórica, hotel de turismo, motel de turismo; Culto y Cultura: Catedrales, Templos, Santuarios, Sinagogas, Mezquitas, Capillas, Parroquias; Deporte: Estadios, Hipódromos, Medialunas; Educación: Todos, excepto los señalados como permitidos; Esparcimiento: Todos; Salud: Hospitales, Centro de rehabilitación, Cementerios, Crematorios; Seguridad: Todos, excepto los señalados como permitidos; Social |
| Actividades productivas | Industria, Almacenamiento y Talleres de Impacto Similar al Industrial: inofensivas y molestas |
| Infraestructura | De Transporte; Sanitaria y Energía, en conformidad al artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 1.000 m² |
| Coeficiente de ocupación de suelo (COS) | 0,6 |
| Coeficiente de constructibilidad | 2,5 |
| Densidad bruta máxima | 60 hab/Há |
| Sistema de agrupamiento — Residencial | Aislado, Pareado y Continuo |
| Sistema de agrupamiento — Equipamiento | Aislado, Pareado y Continuo |
| Sistema de agrupamiento — Otros usos | Aislado, Pareado y Continuo |
| Adosamientos | Según lo dispuesto en O.G.U.C |
| Distanciamientos mínimos de adosamiento | Según lo dispuesto en O.G.U.C |
| Distanciamientos mínimos a los medianeros | Según lo dispuesto en O.G.U.C |
| Rasantes | Según lo dispuesto en O.G.U.C |
| Ochavos | Según lo dispuesto en O.G.U.C |
| Altura máxima de edificación — Aislado | 14 m |
| Altura máxima de edificación — Pareado | 14 m |
| Altura máxima de edificación — Continuo | 14 m |
| Antejardín | 5 m |
| Estacionamientos | Según Artículo 35 de la presente Ordenanza |
| Alturas de cierros | Según Artículo 14 de la presente Ordenanza |

**Normas con incentivo** (proyectos que enfrenten/formen parte de Parque Proyección Poniente de Parque Cordillera, Parque Lineal Arturo Matte Larraín, Parque Lineal San Pedro — Art. 9; también generación o recuperación de áreas verdes y espacios públicos):

| Norma | Valor |
|---|---|
| Densidad máxima | 120 hab/Há |
| Altura máxima de edificación — Aislado | 21 m |
| Altura máxima de edificación — Pareado | 21 m |
| Altura máxima de edificación — Continuo | 14 m |

---

### CU (Zona Corredor Urbano / "corredor comercial y urbano") — p.36-37 — *zona nueva creada por este decreto*

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Residencial | Residencial, Hogares de acogida y Hospedaje: Hoteles |
| Equipamiento | Científico: Todos; Comercio: Todos, exceptos los prohibidos; Culto y Cultura: Todos; Deporte: Todos, exceptos los prohibidos; Educación: Todos; Esparcimiento: parque botánico; Salud: Hospitales, clínicas, policlínicos, consultorios, postas, centros de rehabilitación, Laboratorios clínicos, laboratorios dentales, dispensarios, centros de rehabilitación física y tratamiento terapéutico, clínicas dentales, centros de larga estadía para adultos mayores con tratamiento médico; Seguridad: Unidades policiales (comisarías, tenencias, retenes), cuarteles de bomberos; Servicios: Todos y Social: Todos |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Residencial | Hospedaje: Todos exceptos los permitidos |
| Equipamiento | Comercio: cocinas oscuras, restaurante de turismo (cabarets), fuentes de soda, bares, discotecas o salón de baile similares (espectáculos y shows en vivo), peñas folclóricas, pubs/tabernas, quintas de recreo, centro o salón de eventos, hoteles de turismo, motel de turismo, botillerías y depósito licores; Deporte: Estadios, autódromos, hipódromos, medialunas, airsoft, Paintball; Esparcimiento: Todos, exceptos los permitidos; Salud: Todos, exceptos los permitidos; Seguridad: Todos, exceptos los permitidos |
| Actividades productivas | Industria, Almacenamiento; Establecimientos de Impacto Similar al Industrial: inofensivas y molestos |
| Infraestructura | De transporte; Sanitaria y Energía, conforme lo señala el artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 2.000 m² |
| Coeficiente de ocupación de suelo (COS) | 0,3 |
| Coeficiente de constructibilidad | 1,8 |
| Densidad bruta máxima | 500 hab/Há |
| Sistema de agrupamiento — Residencial | Aislado, Pareado y Continuo |
| Sistema de agrupamiento — Equipamiento | Aislado, Pareado y Continuo |
| Sistema de agrupamiento — Otros usos | Aislado |
| Adosamientos | Según lo dispuesto en O.G.U.C |
| Distanciamientos mínimos de adosamiento | Según lo dispuesto en O.G.U.C |
| Distanciamientos mínimos a los medianeros | Según lo dispuesto en O.G.U.C |
| Rasantes | Según lo dispuesto en O.G.U.C |
| Ochavos | Según lo dispuesto en O.G.U.C |
| Altura máxima de edificación — Aislado | 21 m |
| Altura máxima de edificación — Pareado | 14 m |
| Altura máxima de edificación — Continuo | 14 m |
| Antejardín | 10 m |
| Estacionamientos | Según Artículo 35 de la presente Ordenanza |
| Alturas de cierros | Según Artículo 14 de la presente Ordenanza |

---

## Reconocimiento de zona ya consolidada dentro del área de extensión urbana

### PU-M (Parque Urbano Mixto) — p.38 — *zona nueva creada por este decreto*

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Residencial | Vivienda, Hogares de Acogida |
| Equipamiento | Comercio: locales comerciales (Librería, farmacia, ópticas, venta de insumos médicos, ferretería), restaurantes, salón de té o cafetería; Culto y Cultura: centros culturales, salas de cultura, museos, bibliotecas, teatros, galerías de arte, salas de exposición; Deporte: centros y clubes deportivos, gimnasios, canchas (tenis, bowling, padel, ráquetbol u otros tipos), multicanchas, piscinas, Saunas, circuitos deportivos, Skatepark, bikepark, dirt jump park; Educación: Todos; Esparcimiento: Todos, excepto los señalados como prohibidos; Salud: Todos, excepto los señalados como prohibidos; Seguridad: Todos, excepto los señalados como prohibidos; Servicios: Todos y Social: Todos |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Residencial | Hospedaje: Todos |
| Equipamiento | Científico: Todos; Comercio: Todos, excepto los señalados como permitidos; Culto y Cultura: Todos, excepto los señalados como permitidos; Deporte: todo excepto lo prohibido; Esparcimiento: Parques de entretenciones, parques zoológicos, casinos de juegos, juegos electrónicos o mecánicos (máquinas destreza); Salud: Cementerio, crematorios; Seguridad: cárceles, centros de detención, centros de reclusión nocturna |
| Actividades productivas | Industria, Almacenamiento y Establecimientos de Impacto Similar al Industrial: inofensivo y/o molesto |
| Infraestructura | de Transporte, Sanitaria y Energía, conforme lo señala artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 600 m² |
| Coeficiente de ocupación de suelo (COS) | 0,2 |
| Coeficiente de constructibilidad | 0,6 |
| Densidad bruta máxima | 350 hab/Há |
| Sistema de agrupamiento — Residencial | Aislado |
| Sistema de agrupamiento — Equipamiento | Aislado |
| Sistema de agrupamiento — Otros usos | Aislado |
| Adosamientos | Según lo dispuesto en O.G.U.C |
| Distanciamientos mínimos de adosamiento | Según lo dispuesto en O.G.U.C |
| Distanciamientos mínimos a los medianeros | Según lo dispuesto en O.G.U.C |
| Rasantes | Según lo dispuesto en O.G.U.C |
| Ochavos | Según lo dispuesto en O.G.U.C |
| Altura máxima de edificación — Aislado | 17,5 m |
| Altura máxima de edificación — Pareado | — |
| Altura máxima de edificación — Continuo | — |
| Antejardín | 5 m |
| Estacionamientos | Según Artículo 35 de la presente Ordenanza |
| Alturas de cierros | Según Artículo 14 de la presente Ordenanza |

**Normas con incentivo** (proyectos que enfrenten/formen parte de parque avenida José Miguel Carrera, Parque Lineal Camino del Alba, Parque Lineal Av. La Victoria, Parque Lineal Viña del Mar Poniente, área verde adyacente a calle La Fragua — Art. 9):

| Norma | Valor |
|---|---|
| Densidad Bruta Máxima | 650 hab/Há |
| Coeficiente de constructibilidad | 0,8 |
| Altura máxima de edificación | 28 m |

---

### PU-R1 (Parque Urbano Residencial 1) — p.38-39 — *zona nueva creada por este decreto*

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Residencial | Vivienda, Hogares de Acogida; Hospedaje: Hoteles |
| Equipamiento | Comercio: locales comerciales (Librería, farmacia, ópticas, venta de insumos médicos, ferretería); Culto y Cultura: centros culturales, salas de cultura; Deporte: multicanchas, piscinas, Saunas, circuitos deportivos, Skatepark, bikepark, dirt jump park; Esparcimiento: Todos, excepto los señalados como prohibidos; Salud: Todos, excepto los señalados como prohibidos; Social: Todos |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Residencial | Hospedaje: Todos, excepto los señalados como permitidos |
| Equipamiento | Científico: Todos; Comercio: Todos, excepto los señalados como permitidos; Culto y Cultura: Todos, excepto los señalados como permitidos; Deporte: centros y clubes deportivos, gimnasios, canchas (tenis, bowling, padel, ráquetbol u otros tipos), multicanchas, piscinas, Saunas, circuitos deportivos, Skatepark, bikepark, dirt jump park [nota: listados en ambos lados del cuadro, ver reserva de confianza más abajo]; Esparcimiento: Parques de entretenciones, parques zoológicos, casinos de juegos, juegos electrónicos o mecánicos (máquinas destreza); Salud: Cementerio, crematorios |
| Actividades productivas | Industria, Almacenamiento y Establecimientos de Impacto Similar al Industrial: Inofensivos y/o molestos |
| Infraestructura | de Transporte, Sanitaria y Energía |

**Nota de confianza MEDIA sobre "Prohibidos — Equipamiento — Deporte":** el bloque de prohibidos de PU-R1 repite, en la columna Deporte, una lista muy similar a la de "Permitidos" de PU-M/PU-R1 (multicanchas, piscinas, Saunas, etc.) junto con ítems adicionales (centros y clubes deportivos, gimnasios, canchas). Esto podría reflejar que el cuadro fuente diferencia sub-tipos específicos de instalación deportiva entre permitido y prohibido (p.ej. "multicanchas sí, canchas de otro tipo no"), o podría ser una imprecisión del original. Se transcribe literal tal como aparece en el render, sin resolver la aparente redundancia.

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 600 m² |
| Coeficiente de ocupación de suelo (COS) | 0,2 |
| Coeficiente de constructibilidad | 0,6 |
| Densidad bruta máxima | 480 hab/Há |
| Sistema de agrupamiento — Residencial | Aislado |
| Sistema de agrupamiento — Equipamiento | — |
| Sistema de agrupamiento — Otros usos | — |
| Adosamientos | Según lo dispuesto en O.G.U.C |
| Distanciamientos mínimos de adosamiento | Según lo dispuesto en O.G.U.C |
| Distanciamientos mínimos a los medianeros | Según lo dispuesto en O.G.U.C |
| Rasantes | Según lo dispuesto en O.G.U.C |
| Ochavos | Según lo dispuesto en O.G.U.C |
| Altura máxima de edificación — Aislado | 17,5 m |
| Altura máxima de edificación — Pareado | — |
| Altura máxima de edificación — Continuo | — |
| Antejardín | 5 m |
| Estacionamientos | Según Artículo 35 de la presente Ordenanza |
| Alturas de cierros | Según Artículo 14 de la presente Ordenanza |

**Normas con incentivo** (proyectos que enfrenten/formen parte de Parque Sustentable, proyección poniente de parque Cordillera, Parque Sandro Botticelli, Parque Puerto Bertrand, Parque Centro Español — Art. 9):

| Norma | Valor |
|---|---|
| Densidad Bruta Máxima | 650 hab/Há |
| Coeficiente de constructibilidad | 0,8 |
| Altura máxima de edificación | 28 m |

---

### R1-A (Zona Preferentemente Residencial 1-A) — p.39-40 — *zona nueva creada por este decreto*

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Residencial | Vivienda, Hogares de Acogida: Todos y Hospedaje: Todos, excepto los señalados como prohibidos |
| Equipamiento | Comercio: Todos, excepto los señalados como prohibidos; Culto y Cultura: Todos; Deporte: Todos, excepto los señalados como prohibidos; Educación: Todos; Esparcimiento: Todos, excepto los señalados como prohibidos; Salud: Todos, excepto los señalados como prohibidos; Seguridad: Todos, excepto los señalados como prohibidos; Servicios: Todos y Social: Todos |
| Infraestructura | Transporte: terminales de transporte terrestre (rodoviarios, terminales de buses, taxis buses, taxis, taxis colectivos, depósito de buses o camiones hasta dos buses o camiones) |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Residencial | Hospedaje: Motel |
| Equipamiento | Científico: Todos; Comercio: Discotecas, Cabaret; Deporte: Hipódromos; Esparcimiento: Zoológicos; Salud: Cementerio, Crematorio; Seguridad: cárceles, centros de reclusión nocturna |
| Actividades productivas | Industria; Almacenamiento; Establecimientos de Impacto Similar al Industrial: Todos, excepto los señalados como permitidos |
| Infraestructura | Transporte de: Estaciones y Terminales Ferroviarios, Terminal Rodoviario, terminales de distribución; Sanitaria y Energía, conforme lo señala el artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 120 m² |
| Coeficiente de ocupación de suelo (COS) | 0,8 |
| Coeficiente de constructibilidad | 2 |
| Densidad bruta máxima | 480 hab/Há |
| Sistema de agrupamiento — Residencial | Aislado, Pareado y Continuo |
| Sistema de agrupamiento — Equipamiento | Aislado, Pareado y Continuo |
| Sistema de agrupamiento — Otros usos | Aislado, Pareado y Continuo |
| Adosamientos | Según lo dispuesto en O.G.U.C |
| Distanciamientos mínimos de adosamiento | Según lo dispuesto en O.G.U.C |
| Distanciamientos mínimos a los medianeros | Según lo dispuesto en O.G.U.C |
| Rasantes | Según lo dispuesto en O.G.U.C |
| Ochavos | Según lo dispuesto en O.G.U.C |
| Altura máxima de edificación — Aislado | 17,5 m |
| Altura máxima de edificación — Pareado | 17,5 m |
| Altura máxima de edificación — Continuo | 10,5 m |
| Antejardín | 3 m |
| Estacionamientos (ART. 35) | Según Artículo 35 de la presente Ordenanza |
| Alturas de cierros (ART. 14) | Según Artículo 14 de la presente Ordenanza |

---

### R2-A (Zona Preferentemente Residencial 2-A) — p.40-41 — *zona nueva creada por este decreto*

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Residencial | Vivienda, Hogares de Acogida: todos y Hospedaje: Todos, excepto los señalados como prohibidos |
| Equipamiento | Comercio: Todos, excepto los señalados como prohibidos; Culto y Cultura: Todos; Deporte: Todos, excepto los señalados como prohibidos; Educación: Todos; Esparcimiento: Todos, excepto los señalados como prohibidos; Salud: Todos, excepto los señalados como prohibidos; Seguridad: Todos, excepto los señalados como prohibidos; Servicios: Todos y Social: Todos |
| Infraestructura | Transporte: terminales de transporte terrestre (rodoviarios, terminales de buses, taxis buses, taxis, taxis colectivos, depósito de buses o camiones hasta dos buses o camiones) |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Residencial | Hospedaje: Motel |
| Equipamiento | Científico: Todos; Comercio: Discotecas, Cabaret, Quintas de Recreo, Restaurante de Turismo, Motel Turístico; Deporte: Hipódromos; Esparcimiento: Zoológicos; Salud: Cementerio, Crematorio; Seguridad: cárceles, centros de reclusión nocturna |
| Actividades productivas | Industria; Almacenamiento; Establecimientos de Impacto Similar al Industrial: inofensivo y molesto |
| Infraestructura | Transporte: Todos, con excepción de los permitidos; Sanitaria y Energía, conforme lo señala el artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 160 m² |
| Coeficiente de ocupación de suelo (COS) | 0,8 |
| Coeficiente de constructibilidad | 1,2 |
| Densidad bruta máxima | 480 hab/Há |
| Sistema de agrupamiento — Residencial | Aislado, Pareado y Continuo |
| Sistema de agrupamiento — Equipamiento | Aislado, Pareado y Continuo |
| Sistema de agrupamiento — Otros usos | Aislado, Pareado y Continuo |
| Adosamientos | Según lo dispuesto en O.G.U.C |
| Distanciamientos mínimos de adosamiento | Según lo dispuesto en O.G.U.C |
| Distanciamientos mínimos a los medianeros | Según lo dispuesto en O.G.U.C |
| Rasantes | Según lo dispuesto en O.G.U.C |
| Ochavos | Según lo dispuesto en O.G.U.C |
| Altura máxima de edificación — Aislado | 17,5 m |
| Altura máxima de edificación — Pareado | 17,5 m |
| Altura máxima de edificación — Continuo | 10,5 m |
| Antejardín | 3 m |
| Estacionamientos | Según Artículo 35 de la presente Ordenanza |
| Alturas de cierros | Según Artículo 14 de la presente Ordenanza |

**Normas con incentivo IIS** (proyectos de vivienda con al menos 30% de unidades adquiridas u ocupadas con subsidio del Estado, mandatados por SERVIU, sujetas a escritura pública de prohibición de transferencia sin pago del subsidio — Art. 9):

| Norma | Valor |
|---|---|
| Coeficiente de constructibilidad | 1,5 |
| Densidad máxima | 640 hab/Há |
| Altura máxima de edificación — Aislado | 22 m |
| Altura máxima de edificación — Pareado | 22 m |
| Altura máxima de edificación — Continuo | 10,5 m |

---

### R3-A (Zona Preferentemente Residencial 3-A) — p.41 — *zona nueva creada por este decreto*

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Residencial | Vivienda, Hogares de Acogida: Todos y Hospedaje: Todos, excepto los señalados como prohibidos |
| Equipamiento | Comercio: Todos, excepto los señalados como prohibidos; Culto y Cultura: Todos; Deporte: Todos, excepto los señalados como prohibidos; Educación: Todos; Esparcimiento: Todos, excepto los señalados como prohibidos; Salud: Todos, excepto los señalados como prohibidos; Seguridad: Todos, excepto los señalados como prohibidos; Servicios: Todos, excepto los señalados como prohibidos y Social: Todos |
| Actividades productivas | Actividad Similar al Industrial: inofensiva |
| Infraestructura | de Transporte: terminales de transporte terrestre (rodoviarios, terminales de buses, taxis buses, taxis, taxis colectivos, depósito de buses o camiones hasta dos buses o camiones) |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Residencial | Hospedaje: Hostería, Motel |
| Equipamiento | Científico, Comercio: Discotecas, similares, Cabaret, Quintas de Recreo, Restaurant de Turismo, hoteles turísticos, moteles turísticos, Bombas de Bencina, Expendio de Combustibles, Centros de Servicio Automotriz o Servicentros; Deporte: Hipódromos; Esparcimiento: Zoológicos, Salas de Espectáculo, Juegos electrónicos o mecánicos; Salud: Cementerio, Crematorio; Servicios: Servicio de Estacionamientos; Seguridad: Cárceles, centros de reclusión nocturna |
| Actividades productivas | Industria y Almacenamiento: inofensivas y molestas; Actividad Similar al Industrial: molestas |
| Infraestructura | de Transporte: Todos excepto los señalados como permitidas; Sanitaria y Energía, conforme lo señala artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 250 m² |
| Coeficiente de ocupación de suelo (COS) | 0,2 |
| Coeficiente de constructibilidad | 1,2 |
| Densidad bruta máxima | 600 hab/Há |
| Sistema de agrupamiento — Residencial | Aislado |
| Sistema de agrupamiento — Equipamiento | Aislado |
| Sistema de agrupamiento — Otros usos | Aislado |
| Adosamientos | Según lo dispuesto en O.G.U.C |
| Distanciamientos mínimos de adosamiento | Según lo dispuesto en O.G.U.C |
| Distanciamientos mínimos a los medianeros | Según lo dispuesto en O.G.U.C |
| Rasantes | Según lo dispuesto en O.G.U.C |
| Ochavos | Según lo dispuesto en O.G.U.C |
| Altura máxima de edificación — Aislado | 17,5 m |
| Altura máxima de edificación — Pareado | 17,5 m |
| Altura máxima de edificación — Continuo | 10,5 m |
| Antejardín | 3 m |
| Estacionamientos | Según Artículo 35 de la presente Ordenanza |
| Alturas de cierros | Según Artículo 14 de la presente Ordenanza |

**Nota — diferencia con R1-A/R2-A:** el "Sistema de Agrupamiento" de R3-A es únicamente **Aislado** en las tres categorías (Residencial/Equipamiento/Otros usos), a diferencia de R1-A y R2-A que permiten "Aislado, Pareado y Continuo" — verificado, no es omisión de esta transcripción.

---

## Nuevas zonificaciones dentro del área de extensión urbana

### BR-M5 (Zona Mixta 5 Borde Ruta) — p.42-43 — *zona nueva creada por este decreto*

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Residencial | Vivienda, Hogares y Hospedaje |
| Equipamiento | Científico, Comercio, Culto y Cultura, Deporte, Educación, Salud, Seguridad, Servicios y Social |
| Infraestructura | De Transporte: Todas; Sanitaria: Todos excepto los prohibidos; Energía: Todos excepto los prohibidos |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Equipamiento | Comercio: discotecas, bares, cabaret; Deporte: estadios, medialunas, autódromos; Educación: centros de rehabilitación conductual; Esparcimiento: hipódromos, circos, parques de entretención; Salud: cementerios, crematorios; Seguridad: cárceles y cuarteles |
| Actividades productivas | Industria, Almacenamiento, Instalaciones de Impacto Similar al Industrial: inofensivos y molestos |
| Infraestructura | Sanitaria: edificaciones e instalaciones — rellenos sanitarios, estaciones exclusivas de transferencia de residuos; Energética: edificaciones e instalaciones — plantas y centrales de generación eléctrica, en conformidad al artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 1.000 m² |
| Coeficiente de ocupación de suelo (COS) | 0,4 |
| Coeficiente de constructibilidad | 1,2 |
| Densidad bruta máxima | 450 hab/Há |
| Sistema de agrupamiento — Residencial | Aislado, Pareado |
| Sistema de agrupamiento — Equipamiento | Aislado, Pareado |
| Sistema de agrupamiento — Otros usos | Aislado, Pareado |
| Adosamientos | Según lo dispuesto en O.G.U.C |
| Distanciamientos mínimos de adosamiento | Según lo dispuesto en O.G.U.C |
| Distanciamientos mínimos a los medianeros | Según lo dispuesto en O.G.U.C |
| Rasantes | Según lo dispuesto en O.G.U.C |
| Ochavos | Según lo dispuesto en O.G.U.C |
| Altura máxima de edificación — Aislado | 17,5 m |
| Altura máxima de edificación — Pareado | 17,5 m |
| Altura máxima de edificación — Continuo | — (no aplica; el sistema de agrupamiento de esta zona no incluye Continuo) |
| Antejardín | 5 m |
| Estacionamientos | Según Artículo 35 de la presente Ordenanza |
| Alturas de cierros | Según Artículo 14 de la presente Ordenanza |

---

## TEMA N°3 — Implementación de un sistema de infraestructura verde

### EQ-D (Zonas de equipamiento deportivo) — p.43-44 — *zona nueva creada por este decreto*

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Equipamiento | Comercio: locales comerciales (Librería, farmacia, ópticas, venta de insumos médicos, ferretería), restaurantes, salón de té o cafetería, almacenes; Deporte: Estadios, centros y clubes deportivos, gimnasios, canchas (tenis, bowling, padel, ráquetbol u otros tipos), multicanchas, piscinas, Saunas, autódromos, hipódromos, medialunas, circuitos deportivos, parkor, airsoft, Paintball, Skatepark, bikepark, dirt jump park; Salud: centros de rehabilitación física y tratamiento terapéutico; Social: Sedes de juntas de vecinos, centros de madres, clubes sociales (clubes adulto mayor, centros juveniles, centros discapacitados, centros de funcionarios públicos, sedes asociaciones gremiales, etc.), locales comunitarios, centros sociales |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Residencial | Viviendas; Hogares de Acogida; Hospedaje |
| Equipamiento | Científico: Todos; Comercio: Todos excepto los permitidos; Educación: Todos; Esparcimiento: Todos; Salud: Todos exceptos los permitidos; Seguridad: Todos |
| Actividades productivas | Industria, Almacenamiento y Talleres de Impacto Similar al Industrial: inofensivas y molestas |
| Infraestructura | De Transporte; Sanitaria y Energía, en conformidad al artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 2.000 m² |
| Coeficiente de ocupación de suelo (COS) | 0,3 |
| Coeficiente de constructibilidad | 1,8 |
| Densidad bruta máxima | — (no aplica / sin dato) |
| Sistema de agrupamiento — Residencial | — |
| Sistema de agrupamiento — Equipamiento | Aislado, Pareado |
| Sistema de agrupamiento — Otros usos | Aislado, Pareado |
| Adosamientos | Según lo dispuesto en O.G.U.C |
| Distanciamientos mínimos de adosamiento | Según lo dispuesto en O.G.U.C |
| Distanciamientos mínimos a los medianeros | Según lo dispuesto en O.G.U.C |
| Rasantes | Según lo dispuesto en O.G.U.C |
| Ochavos | Según lo dispuesto en O.G.U.C |
| Altura máxima de edificación — Aislado | 21 m |
| Altura máxima de edificación — Pareado | 14 m |
| Altura máxima de edificación — Continuo | — |
| Antejardín | 10 m |
| Estacionamientos | Según Artículo 35 de la presente Ordenanza |
| Alturas de cierros | Según Artículo 14 de la presente Ordenanza |

---

## TEMA N°7 — Reconocimiento de centros de salud y educación

### EQ-EDS (Zonas de equipamiento Educación Superior) — p.65-66 — *zona nueva creada por este decreto*

#### Usos de suelo

**Permitidos**

| Categoría | Detalle |
|---|---|
| Equipamiento | Científico: Todos; Comercio: locales comerciales (Librería, farmacia, ópticas, venta de insumos médicos, ferretería), restaurantes, salón de té o cafetería, almacenes; Culto y Cultura: Todos exceptos los prohibidos; Deporte: centros y clubes deportivos, gimnasios, canchas (tenis, bowling, padel, ráquetbol u otros tipos), multicanchas, piscinas, circuitos deportivos, Skatepark, bikepark, dirt jump park; Educación: Educación superior, educación técnica, escuelas para adultos, centros de capacitación (OTEC), Universidades, institutos profesionales, centros de formación técnica, Academias (danza, yoga, cocina, pintura, música e idiomas); Servicios: servicios de courier o encomiendas/mensajería, centros de pago, bancos, cajas de cambio, financieras; Servicios públicos en general (ministerios, intendencias, defensorías, ministerios públicos, cortes de justicia, servicios de utilidad pública, servicios de la administración pública, Departamentos o Unidades Municipales, juzgados); Social: Sedes de juntas de vecinos, centros de madres, clubes sociales (clubes adulto mayor, centros juveniles, centros discapacitados, centros de funcionarios públicos, sedes asociaciones gremiales, etc.), locales comunitarios, centros sociales |
| Espacios públicos / Áreas verdes | Permitidos |

**Prohibidos**

| Categoría | Detalle |
|---|---|
| Residencial | Todos |
| Equipamiento | Comercio: Todos, exceptos los permitidos; Culto y Cultura: Catedrales, Templos, Santuarios, Sinagogas, Mezquitas, Capillas, Parroquias; Deporte: Todos excepto los permitidos; Educación: Todos, excepto los señalados como permitidos; Esparcimiento: Todos; Salud: Hospitales, Centro de rehabilitación, Cementerios, Crematorios; Seguridad: Todos, excepto los señalados como permitidos; Social |
| Actividades productivas | Industria, Almacenamiento y Talleres de Impacto Similar al Industrial: inofensivas y molestas |
| Infraestructura | De Transporte; Sanitaria y Energía, en conformidad al artículo 21 |

#### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 1.000 m² |
| Coeficiente de ocupación de suelo (COS) | 0,7 |
| Coeficiente de constructibilidad | 4 |
| Densidad bruta máxima | — (no aplica / sin dato) |
| Sistema de agrupamiento — Residencial | — |
| Sistema de agrupamiento — Equipamiento | Aislado, Pareado y Continuo |
| Sistema de agrupamiento — Otros usos | Aislado, Pareado y Continuo |
| Adosamientos | Según lo dispuesto en O.G.U.C |
| Distanciamientos mínimos de adosamiento | Según lo dispuesto en O.G.U.C |
| Distanciamientos mínimos a los medianeros | Según lo dispuesto en O.G.U.C |
| Rasantes | Según lo dispuesto en O.G.U.C |
| Ochavos | Según lo dispuesto en O.G.U.C |
| Altura máxima de edificación — Aislado | 28 m |
| Altura máxima de edificación — Pareado | 28 m |
| Altura máxima de edificación — Continuo | 28 m |
| Antejardín | 5 m |
| Estacionamientos | Según Artículo 35 de la presente Ordenanza |
| Alturas de cierros | Según Artículo 14 de la presente Ordenanza |

---

## Anexo — Tablas de "Corrección de Plano" (rezonificación de áreas específicas)

Estas tablas reasignan sectores puntuales de la comuna de una sigla de zona a otra. **No son cuadros de norma urbanística** (no traen COS/CC/altura) — se listan aquí solo como referencia cruzada de nomenclatura, ya que ayudan a entender el origen de varias zonas nuevas de este decreto.

**1.42 — Correcciones de Plano (BR-M1, C1, EQ-SC, R2, R5, SM1, ZM) — p.34-35**

| Ubicación | Zona Vigente | Zona Propuesta |
|---|---|---|
| La Compañía con Los Talaveras | EQS | R2 |
| La Compañía con Miguel Ramírez | EQE | C1 |
| Las Azaleas | Sin zona | R5 |
| Libertador Bernardo O'Higgins con proyección de Provincial | EQ-PU2 y C1 | EQ-SC |
| Cachapoal con Ruta Travesía | Sin zona | BR-M1 |
| Baquedano (zona de protección aeródromo) | Z11A | ZM y EQ-SC, con restricción de zona de protección aeródromo Z11A |
| Baquedano con Camino Salvador Allende Gossens | AVPU (Caducado) | SM1 |

**2.1.2 — reasignación hacia EQ-CBM1 — p.36**

| Áreas | Zona Vigente | Zona Propuesta |
|---|---|---|
| Límite urbano Norte, límite urbano oriente, Miguel Ramírez y Ruta Travesía | EQPU2 | EQ-CBM1 |
| Límite urbano norte, Ruta Travesía, Libertador Bernardo O'Higgins y límite urbano poniente | R2 | EQ-CBM1 |
| Límite Libertador Bernardo O'Higgins, Ruta Travesía, límite urbano sur y límite urbano poniente | BR-MS1, R2 | EQ-CBM1 |

**2.1.3 — reasignación hacia EQ-CB1 — p.36**

| Ubicación | Zona Vigente | Zona Propuesta |
|---|---|---|
| Av. la Victoria con Avenida Circunvalación Norte | EX1 y EX2 | EQ-CB1 |
| Libertador Bernardo O'Higgins con Nueva Alberto Einstein | R2 | EQ-CB1 |
| Presidente Eduardo Frei Montalva con Av. Alberto Einstein | EX2 | EQ-CB1 |
| Av. Nelson Pereira con Samuel Román Rojas | SM3 | EQ-CB1 |
| Diagonal Doñihue con Provincial | EX3 | EQ-CB1 |

**2.2.2 — reasignación hacia CU — p.37**

| Áreas | Zona Vigente | Zona Propuesta |
|---|---|---|
| Carretera del Cobre Presidente Arturo Frei Montalva | R2, R5, BR-M1, R3, EX5, EQPU2 | CU |

**2.2.3 — reasignación hacia C1 — p.37**

| Ubicación | Zona Vigente | Zona Propuesta |
|---|---|---|
| Corredor Comercial República de Chile | EX2, R1 y R2 | C1 |
| Libertador Bernardo O'Higgins | R2 | C1 |
| Corredor Comercial Av. Diagonal Doñihue | EX1, EX3 y EX4 | C1 |
| Libertador Bernardo O'Higgins con Av. España | R2 | C1 |
| Miguel Ramírez con San Joaquín | AV PU | C1 |

**2.3.1 — reasignación hacia PU-M / PU-R1 / R1-A / R2-A / R3-A — p.41-42**

| Áreas | Zona Vigente | Zona Propuesta |
|---|---|---|
| Límite urbano Norte, límite urbano oriente, Miguel Ramírez y Ruta Travesía | EX1, EX2, EX8, R2, EQPU2, EQ-CB | R1-A, R2-A, R3-A y PU-M |
| Límite Miguel Ramírez, límite urbano oriente, límite urbano sur y Ruta Travesía | EX2, EX5 | R2-A, R3-A y PU-M |
| Límite urbano norte, Ruta Travesía, Libertador Bernardo O'Higgins y límite urbano poniente | EX2, EX7, EQPU2, BR-M2, R2 | R2-A, PU-R1 |
| Límite Libertador Bernardo O'Higgins, Ruta Travesía, límite urbano sur y límite urbano poniente | EX1, EX3, EX4, EQPU1, EQPU2-R1-R2 | R1-A, R2-A, PU-R1, PU-M |

**2.3.2 — reasignación hacia R2 / R3 / R6 / BR-M2 — p.42**

| Ubicación | Zona Vigente | Zona Propuesta |
|---|---|---|
| Av. Diagonal Doñihue | EX3 y EX4 | R6 |
| Edmundo Cabezas con Bombero Domingo Villalobos | EX2 | R6 |
| Ruta Travesía con Burgos | EX2 | BR-M2 |
| San Pedro con Calle Nueva N°50 | BR-M1 | R2 |
| Lircay entre Parque los Tuñones y el Sol (Zona regeneración urbana de Vicuña Mackenna) | R1 | R2 |
| Javiera Carrera con Alberto Einstein | EX2 | R3 |

**2.4.2 — reasignación hacia BR-M5 — p.43**

| Áreas | Zona Vigente | Zona Propuesta |
|---|---|---|
| Salvador Allende Gossens | EX7 | BR-M5 |

**3.1.2 — reasignación hacia EQ-D (uso exclusivo a deporte) — p.44**

| Uso exclusivo a deporte | Zona Vigente | Zona Propuesta |
|---|---|---|
| Estadio el Teniente | EQPU1 | EQ-D |
| Canchas Diego de Almagro | EQPU1 | EQ-D |
| Recinto Guillermo Saavedra | EQPU1 | EQ-D |

**3.1.3 — reasignación hacia SM1 (uso seguridad) — p.44**

| Uso seguridad | Zona Vigente | Zona Propuesta |
|---|---|---|
| Bombero Domingo Villalobos (Estación de Bomberos y Carabineros) | EQPU1 | SM1 |

**6.1 (Tema N°6, "Zonas de Amortiguación del Aeródromo") — reasignación hacia ZM — p.65**

| Ubicación | Zona Vigente | Zona Propuesta |
|---|---|---|
| Estrella Azul | EQ-PU2 | ZM |
| Av. Baquedano | Z11A | ZM |
| Entre Diagonal Doñihue y Salvador Allende Gossens (H-210) | EX7-EQ-PU2 | ZM |

**7.5 (Tema N°7) — reasignación hacia EQS (centros de salud) — p.66**

| Ubicación | Zona Vigente | Zona Propuesta |
|---|---|---|
| CESFAM 6 — Av. Constanza 1790 | EX1 | EQS |
| CESFAM 5 — Martínez de Rosas | R1 | EQS |
| CESFAM 3 — Bombero Domingo Villalobos 010 | SM1 | EQS |
| Centro Rehabilitación TELETON — Av. Manuel Montt | PU1-AV | EQS |
| CESFAM propuesto mod. 21 — Sector Sur-Oriente | PU1-AV | EQS |
| CESFAM 8 — Av. N. Pereira 2411 | SM3 | EQS |
| CESFAM 4 — Av. República con Av. Recreo | EQ-CB | EQS |
| Hospital Regional — Av. Libertador Bernardo O'Higgins 3065 | EX2 | EQS |
| CESFAM 1 — Av. Baquedano 626 | R2 | EQS |
| Centro de Salud — Almarza 1061 | R2 | EQS |
| CESFAM 2 — Río Loco con San Pedro | BR-MS1 | EQS |
| CESFAM propuesto mod. 21 — Sector Sur-poniente | EX3 | EQS |

---

## Confianza global: ALTA

Confianza ALTA para la gran mayoría de las 47 fichas con cuadro numérico (render nítido a 250 dpi, sin ambigüedad de lectura). Confianza MEDIA puntual, señalada en su propia ficha, en dos celdas: (1) **BRO** — Coeficiente de Constructibilidad "10" (posible errata del original por "1,0", verificado con zoom que efectivamente dice "10"); (2) **BR-M3** — Altura Máxima de Edificación Aislado/Continuo sin dato en el cuadro fuente pese a que el Sistema de Agrupamiento permite ambos (verificado con zoom, es del original, no un salto de lectura). El resto del documento no presentó celdas ilegibles que requirieran degradar la confianza.
