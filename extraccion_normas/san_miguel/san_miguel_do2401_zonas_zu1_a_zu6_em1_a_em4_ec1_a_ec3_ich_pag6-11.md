# Normas Urbanísticas — Decreto N° 2.401 (2005), Aprueba NUEVO Plan Regulador Comunal de San Miguel

**Fuente:** Decreto N° 2.401/2005, Municipalidad de San Miguel, "Aprueba Nuevo Plan Regulador Comuna de San Miguel". Publicado en el Diario Oficial de la República de Chile N° 38.323, lunes 28 de noviembre de 2005 (páginas propias del cuerpo del Diario: 11 a 16, numeración interna "(16035)" a "(16040)").

**Material usado para esta extracción:** imágenes PNG a 250 dpi (`sanmiguel2_p6-11-06.png` … `sanmiguel2_p6-11-11.png`, 6 páginas) y texto plano de apoyo (`sanmiguel2_p6-11.txt`). Cada una de las 6 páginas fue leída directamente en la imagen; el `.txt` se usó solo como verificación secundaria carácter por carácter, nunca como fuente primaria (ver §0 sobre el desorden de columnas del `.txt`). **No se usó la carpeta `zoom/` del mismo directorio de render** — ver advertencia explícita en §0.

**Rango de este documento:** páginas 6 a 11 del PDF de origen (numeración del nombre de archivo), correspondientes a las páginas propias del Diario Oficial 11 a 16 (offset constante +5, verificado en las 6 páginas mediante el pie de página "Página X"). No incluye las páginas 1-5 del PDF (vistos/considerandos y trámite del decreto, según nota de Fase 3, no entregadas para este encargo).

---

## 0. Formato de la fuente y advertencias metodológicas

- **Texto nativo, no escaneado.** Las 6 páginas son tipografía limpia de Diario Oficial (no hay artefactos de escaneo/OCR); el `.txt` de apoyo coincide carácter por carácter con las imágenes en todos los puntos verificados. Nivel de confianza más alto que un documento escaneado.
- **Layout a 2 columnas con orden de lectura NO lineal en el `.txt`.** Igual que en el documento hermano `san_miguel_do515_zonas_em3_em4_restriccion_d_e_pag1-2_11-13.md` (mismo fenómeno, ya advertido en ese documento), el extractor de texto plano intercala líneas de la columna izquierda y derecha cuando ambas columnas tienen distinta longitud. Ejemplo concreto encontrado aquí: el `.txt` muestra "ZONA ZU–2" (línea 101) **antes** que "ZONA ZU–1" (línea 110), en el orden equivocado. Verificado contra la imagen de la página 07: ZU-1 está en la columna izquierda completa y ZU-2 en la columna derecha, ambas empezando cerca de la parte superior de la página — el orden correcto es ZU-1 primero. **Todo el contenido de este documento se transcribió siguiendo el orden verificado en las imágenes, columna por columna, nunca el orden crudo del `.txt`.**
- **Advertencia importante — carpeta `zoom/` contaminada con recortes de OTROS documentos.** El directorio `render8/zoom/` contiene decenas de archivos con nombres como `p9_z1_densidad_row.png`, `p13_z5_cos_cc.png`, etc., que a primera vista parecen crops de páginas/zonas de este documento (el patrón `zN` sugiere "zona N", coincidiendo tentadoramente con ZU-1, ZU-5, etc.). **Se verificó abriendo dos muestras y NINGUNA corresponde a San Miguel Decreto 2401:** `p9_z1_densidad_row.png` muestra una tabla sobre "SEGURIDAD / UNIDADES POLICIALES, CUARTELES DE BOMBEROS... / CÁRCELES, CENTROS DE DETENCIÓN..." y `p13_z5_cos_cc.png` muestra un cuadro con decimales de coma ("0,6", "10,50 M", "(MÁXIMO DE 3 PISOS)") en una tipografía de escaneo distinta a la de este Diario Oficial — contenido y formato ajenos, casi con certeza de otra comuna procesada en el mismo lote de render (`render8/` contiene también angol, caldera2, paine, rengo, sancarlos, sanfernando, tolten2, villarrica47). **Se descartó por completo el uso de esa carpeta para este documento.** Toda cifra transcrita aquí proviene exclusivamente de las 6 imágenes principales `sanmiguel2_p6-11-06.png` a `-11.png`, cada una confirmada individualmente por su encabezado visible "Nº 38.323 … Lunes 28 de Noviembre de 2005". Se deja esta advertencia por escrito para que una fase posterior no reutilice esa carpeta `zoom/` asumiendo que el prefijo del nombre de archivo garantiza pertenencia a este decreto.
- **No se usó "Dato no determinable" en ningún campo de este documento.** El texto fuente es nítido y completo en las 6 páginas entregadas; todo caso de "sin dato" corresponde a un campo que la zona no define por diseño (marcado "Sin valor específico en la fuente" con motivo explicado), no a una ilegibilidad real.

---

## 1. Convenciones usadas

- **"Sin valor específico en la fuente":** para campos/filas que no aplican por diseño a una zona (se explica el motivo en cada caso).
- **"Dato no determinable":** reservado para valores que deberían existir pero no son legibles o no están en el material entregado — no fue necesario usarlo en ningún punto de este documento.
- **`[sic]`:** marca erratas o inconsistencias tipográficas/gramaticales de la fuente, preservadas tal cual, sin corregir.
- Las cifras de los cuadros de normas urbanísticas usan **punto decimal** tal como la fuente ("1.8", "0.70") — se preserva sin normalizar. El símbolo `---` que imprime el propio cuadro (columna "Adosamiento máximo %" de varias zonas de equipamiento) se transcribe literalmente: es la fuente marcando la casilla, no una omisión de esta transcripción.
- Unidad de superficie: la fuente usa `m²` (con superíndice, a diferencia de otros documentos de este proyecto con texto plano monoespaciado) — se preserva tal cual.

---

## 2. Correspondencia de páginas

| Archivo (PDF) | Página Diario Oficial | Contenido |
|---|---|---|
| `sanmiguel2_p6-11-06.png` | Página 11 (16035) | Fin Art. 23°/Art. 24° (Cap. IV, Tipología y Escalas del Equipamiento); Art. 25° completo (Cap. V — listado de las 14 zonas/áreas); inicio de reglas de límites entre zonas y remisión breve a AR-1/AR-2/AR-3/AR-4 |
| `sanmiguel2_p6-11-07.png` | Página 12 (16036) | Cierre de la remisión a AR-1 a AR-4; **ZONA ZU-1 completa**; **ZONA ZU-2 completa**; inicio de **ZONA ZU-3** (título + 1 frase) |
| `sanmiguel2_p6-11-08.png` | Página 13 (16037) | ZU-3 continuación (usos + cuadro + disposiciones, completa); **ZONA ZU-4** (usos + cuadro; disposiciones complementarias inicia, corta tras 2 ítems) |
| `sanmiguel2_p6-11-09.png` | Página 14 (16038) | ZU-4 disposiciones complementarias continuación (8 ítems más); **ZONA ZU-5 completa**; **ZONA ZU-6 completa**; inicio sección "Zonas de Equipamiento y Áreas Verdes, Nivel Metropolitano e Intercomunal"; **ZONA EM-1** (usos, corta en usos prohibidos) → cuadro + disposiciones de EM-1 al inicio de la columna derecha; **ZONA EM-2 completa**; inicio **ÁREA EM-3** (corta en disposiciones complementarias) |
| `sanmiguel2_p6-11-10.png` | Página 15 (16039) | EM-3 disposiciones complementarias continuación; **ÁREA EM-4 completa**; sección "Áreas de Equipamiento y Áreas Verdes, Nivel Comunal"; **ÁREA EC-1 completa**; inicio **ÁREA EC-2** (usos, corta antes del cuadro) → cuadro + disposiciones de EC-2 al inicio de la columna derecha; **ÁREA EC-3 completa**; **ICH completa**; inicio **Artículo 26° AR-1** (corta a media descripción) |
| `sanmiguel2_p6-11-11.png` | Página 16 (16040) | AR-1 cierre; **AR-2, AR-3 (+tabla), AR-4 completas**; **Capítulo VI completo** (Instalación de Torres y Antenas, Art. 27°-34°); **Capítulo VII inicio** (Vialidad Estructurante, Art. 35°-38°) — **se corta a media disposición del capítulo, sin tabla de vías ni artículos finales** (ver advertencia central en §21 y §25) |

Ningún cuadro numérico de "CUADRO DE NORMAS URBANÍSTICAS" quedó partido a mitad de una cifra entre dos páginas; los cortes de página caen siempre entre secciones o ítems completos.

---

## 3. Capítulo IV — Tipología y Escalas del Equipamiento (Art. 23°-24°, resumen)

Por instrucción del encargo se transcribe en forma **breve** (no es norma de zona).

**Artículo 23° — Equipamiento:** de conformidad al Art. 2.1.27. de la O.G.U.C., constituyen equipamiento los terrenos y edificios urbanos destinados a la prestación de servicios que complementan las funciones de habitar, producir y circular. Define 10 clases de equipamiento con sus actividades típicas: **Científico** (investigación y transferencia tecnológica), **Comercio** (compraventa de mercaderías: centros comerciales, supermercados, restaurantes, discotecas, etc.), **Culto y Cultura** (templos, museos, bibliotecas, canales de TV/radio/prensa), **Deporte** (estadios, gimnasios, multicanchas, piscinas), **Educación** (desde prebásica a universitaria y capacitación), **Esparcimiento** (parques de entretención, zoológicos, casinos), **Salud** (hospitales, clínicas, consultorios, cementerios, crematorios), **Seguridad** (unidades policiales, bomberos, cárceles), **Servicios** (oficinas profesionales, bancos, notarías, servicios artesanales) y **Social** (sedes vecinales, clubes sociales).

**Artículo 24° — Escalas del Equipamiento:** de acuerdo al Art. 2.1.36. de la O.G.U.C., cuatro escalas independientes de la clase, según carga de ocupación y estacionamientos requeridos, condicionando la vía que debe enfrentar el predio:

| Escala | Carga de ocupación | Estacionamientos | Vías que debe enfrentar |
|---|---|---|---|
| Mayor | sobre 4.000 personas | más de 800 | solo vías expresas |
| Mediano | hasta 4.000 personas (u hasta 3.000) | no más de 800 (u no más de 500) | troncales o expresas (o colectoras/troncales/expresas) |
| Menor | hasta 1.000 personas | no más de 250 | de servicio, colectoras, troncales o expresas |
| Básico | hasta 250 personas | no más de 50 | locales, de servicio, colectoras, troncales o expresas |

Clasificación viaria remitida al Capítulo 3, Título 2 de la O.G.U.C. (Vías Expresas, Troncales, Colectoras, de Servicio, Locales), graficada en el plano PRSM-2. Cierra con una disposición ambiental: edificios de uso público con más de 5.000 personas o más de 1.000 estacionamientos deben presentar Estudio de Impacto Ambiental (conforme al D.S. N° 131/1998 del Ministerio Secretaría General de la Presidencia).

---

## 4. Capítulo V — Definición de Zonificación, Usos del Suelo y Normas Específicas — Artículo 25°

> **Texto literal de apertura:** "Las zonas de usos de suelo establecidas y sus límites, están graficadas en el plano PRSM–1 y son las siguientes:"

### Listado completo de las 14 zonas/áreas (verificado directamente contra la imagen de la página 06)

| Categoría | Código | Denominación |
|---|---|---|
| RESIDENCIAL | Zona ZU-1 | COMERCIAL PREFERENTE Y RESIDENCIAL |
| | Zona ZU-2 | RESIDENCIAL DE RENOVACIÓN |
| INDUSTRIAL | Zona ZU-3 | INDUSTRIAL EXCLUSIVA |
| | Zona ZU-4 | INDUSTRIAL–MIXTA |
| SALUD | Zona ZU-5 | EQUIPAMIENTO REGIONAL DE SALUD |
| FERROVIARIO | Zona ZU-6 | FERROVIARIA |
| EQUIPAMIENTO Y ÁREAS VERDES, NIVEL METROPOLITANO E INTERCOMUNAL | Zona EM-1 | EQUIPAMIENTO INTERCOMUNAL |
| | Area EM-2 | EQUIPAMIENTO RECREACIONAL Y DEPORTIVO |
| | Area EM-3 | ÁREAS VERDES EXISTENTES INTERCOMUNALES |
| | Area EM-4 | ÁREAS VERDES PROYECTADAS INTERCOMUNALES |
| EQUIPAMIENTO Y ÁREAS VERDES, NIVEL COMUNAL | Area EC-1 | EQUIPAMIENTO RECREACIONAL Y DEPORTIVO |
| | Area EC-2 | ÁREAS VERDES COMUNALES |
| | Area EC-3 | ÁREAS VERDES PROYECTADAS COMUNALES |
| *(sin categoría de nivel)* | ICH | INMUEBLES DE CONSERVACIÓN HISTÓRICA |

**Total: 14 códigos de zona/área**, no 8. Ver §25 (Discrepancias) para el contraste explícito con la nota de Fase 3, que solo anticipaba "ZU-1 a ZU-5, EC-1 a EC-3".

### Reglas de límites entre zonas (texto literal, 3 ítems)

- Cuando el límite corresponda a una calle, se entenderá ubicado en el eje de la misma.
- Cuando el límite entre dos zonas cruce por el interior de un predio, o el predio se encuentre afectado por dos o más zonas con diferentes usos de suelo y exigencias, se aplicará lo dispuesto en el Art. 2.1.21. de la O.G.U.C.
- La fusión de terrenos no autoriza extender una zona más allá del límite de ésta graficado en el plano PRSM–1, y rige para estos casos el párrafo precedente.

### Remisión a las áreas de restricción (Art. 26°, desarrollado en §19)

> "El cumplimiento de las respectivas normas para las zonas antes mencionadas, debe entenderse complementado con las normas de restricción que corresponden a las siguientes áreas": AR-1 (protección de canales de riego, Zanjón de la Aguada y Canal San Joaquín), AR-2 (resguardo de Aeródromos El Bosque y Los Cerrillos), AR-3 (resguardo de líneas de alta tensión 110 Kw) y AR-4 (resguardo de vía férrea, Ferrocarril de Circunvalación y línea de Metro subterránea Línea 2). También se aclara: "El tipo de uso 'Espacio Público' se entenderá como permitido en todas las zonas."

---

## 5. ZONA ZU-1 — Comercial Preferente y Residencial (página 12/DO, columna izquierda)

**Usos permitidos (texto literal):**
1. **RESIDENCIAL:** "Vivienda, sin perjuicio de lo cual se autoriza la implantación de comercio en el 1er. piso. Aquellos usos definidos en el Art. 2.1.25. de la O.G.U.C. y los complementos a vivienda establecidos en el Art. 2.1.26. de la O.G.U.C."
2. **EQUIPAMIENTO:** "Científico, comercio, culto y cultura, deporte, educación, esparcimiento, salud, seguridad, servicios, social. Cuando los servicios de carácter artesanal sean calificadas `[sic, por "calificados"]` como 'actividades productivas' no corresponderán a equipamiento de servicios, sin perjuicio de lo señalado en el Art. 2.1.28. de la O.G.U.C."
3. **INFRAESTRUCTURA:** "De transporte como vías, estaciones de metro y estacionamientos. Sanitaria como canales de riego e Infraestructura energética como ductos de distribución de gas."
4. **ÁREAS VERDES** `[sic: la fuente imprime "4. ÁREAS VERDES ." con un punto suelto antes del salto de línea]`**:** "Bandejones y platabandas, parque, parque adyacente a cauce, parque intercomunal, plaza, jardines."

**Usos prohibidos (texto literal, 8 ítems):**
- Equipamiento de comercio correspondiente a discotecas y ferias libres.
- Equipamiento de culto y cultura correspondientes a canal de televisión y radioemisoras.
- Equipamiento de esparcimiento correspondiente a autocine, cabaret, pista de espectáculos, quinta de recreo, sala de eventos, salón de baile, zona de picnic y zoológicos.
- Equipamiento de seguridad correspondiente a cárceles y centros de detención.
- Equipamiento de salud correspondiente a hospital.
- Actividades productivas exceptuando las señaladas en el art. 2.1.26 de la O.G.U.C.
- Actividades de servicio de carácter similar al industrial.
- Infraestructura correspondiente a disposición transitoria o final de residuos sólidos, estación ferroviaria, instalaciones de telecomunicaciones, Plantas de tratamiento de aguas servidas, rodoviarios y terminales de locomoción colectiva urbana, terminales de taxis y radiotaxis, terminales de transporte terrestre.

### Cuadro de normas urbanísticas

| Superficie predial m² (desde-hasta) | Altura máxima N° pisos | Coeficiente constructibilidad | Ocup. suelo 1 a 3 pisos | Ocup. suelo sobre 3 pisos | Sistema agrupamiento | Rasantes y distanciamientos | Antejardín mínimo | Adosamiento máximo % |
|---|---|---|---|---|---|---|---|---|
| 0 - 500 | Rasante | 1.8 | 0.80 | 0.50 | A-P-C* | O.G.U.C. | Art. 11 | 40 |
| 501 – 1000 | " | 2.0 | 0.80 | 0.50 | A-P-C* | " | Art. 11 | 40 |
| 1001 – 2000 | " | 2.5 | 0.80 | 0.50 | A-P-C* | " | Art. 11 | 40 |
| 2001 y más | " | 3.0 | 0.80 | 0.50 | A-P-C* | " | Art. 11 | 40 |

`* A=Aislado, * P=Pareado, * C=Continuo`

**Disposiciones complementarias (texto literal, 8 ítems):**
- Densidad bruta mínima: 700 Hab./Há.
- Densidad neta mínima: 900 Hab./Há.
- La altura máxima de edificación para sistema de agrupamiento continuo es de 14 m medidos en el deslinde con los predios vecinos, sobre esta altura el sistema de agrupamiento es aislado.
- La profundidad de la continuidad puede alcanzar hasta un 70% del fondo del predio.
- El coeficiente correspondiente al área libre podrá usarse para estacionamientos.
- Las construcciones pareadas no podrán sobrepasar los 14 m de altura medidos en el deslinde con los predios vecinos y su profundidad máxima será de 15 m o el equivalente al 40% del fondo del predio cuando la profundidad de éste sea inferior a 25 m. Sobre esta altura el sistema de agrupamiento es aislado.
- El equipamiento comercial y talleres tendrán una superficie predial mínima de 500 m² o deberán formar parte de un conjunto de esas dimensiones y cumplirán la norma de estacionamientos señalada en el artículo 14º de esta Ordenanza.
- Se aplicará, para todos los sistemas de agrupamiento, cuando sea el caso, el inciso tercero del Art. 8º de la presente Ordenanza.
- En esta zona, se aplica la restricción de altura de edificación correspondiente a áreas de aproximación de aeródromo, indicada en el Art. 26° de esta Ordenanza.

**Confianza: ALTA.**

---

## 6. ZONA ZU-2 — Residencial de Renovación (página 12/DO, columna derecha)

**Usos permitidos (texto literal):**
1. **RESIDENCIAL:** "Vivienda, sin perjuicio de lo cual, se autoriza la implantación de comercio en el 1er. piso. Aquellos usos definidos en el Art. 2.1.25. de la O.G.U.C. y los complementos a vivienda establecidos en el Art. 2.1.26. de la O.G.U.C."
2. **EQUIPAMIENTO:** "Comercio, culto y cultura, deportes, educación, esparcimiento, salud, seguridad, servicios, social. Cuando los servicios de carácter artesanal sean calificadas `[sic]` como 'actividades productivas' no corresponderán a equipamiento de servicios, sin perjuicio de lo señalado en el Art. 2.1.28. de la O.G.U.C."
3. **INFRAESTRUCTURA:** "De transporte como vías y estaciones de metro, estacionamientos. Sanitaria como canales de riego e Infraestructura Energética como ductos de distribución de gas."
4. **ÁREAS VERDES:** "Bandejones y platabandas, parque, plaza, jardines."

**Usos prohibidos (texto literal, 12 ítems):**
- Equipamiento científico correspondiente a Centro de investigación científica y tecnológica.
- Equipamiento de comercio correspondiente a discotecas, empresa de control de peso de vehículos de carga, estación de servicio, grandes tiendas, mercados, multitiendas, supermercados.
- Equipamiento de culto y cultura correspondientes a canal de televisión, radioemisoras.
- Equipamiento de deporte correspondiente a estadio.
- Equipamiento de esparcimiento correspondiente a autocine, cabaret, circo, club de campo, hotel, hostería, motel, parque de diversiones, pista de espectáculos, quinta de recreo, sala de eventos, salón de baile, salón de juegos, zona de picnic y zoológicos.
- Equipamiento de salud correspondiente a casa de reposo, clínica de recuperación médica, clínica psiquiátrica, hogar de ancianos, hospital.
- Equipamiento de seguridad correspondiente a cárceles y centros de detención.
- Equipamiento de servicios correspondiente a banco e institución financiera, asociación de fondos de pensiones, notario.
- Equipamiento social correspondiente a sede asociación política, sede gremial, sede sindical.
- Actividades productivas, exceptuando las señaladas en el art. 2.1.26. de la O.G.U.C.
- Actividades de servicio de carácter similar al industrial.
- Infraestructura correspondiente a disposición transitoria o final de residuos sólidos, estación ferroviaria, instalaciones de telecomunicaciones, instalaciones de televisión, plantas de tratamiento de aguas servidas, rodoviarios y terminales de locomoción colectiva urbana, terminales de taxis y radiotaxis, terminales de transporte terrestre.

### Cuadro de normas urbanísticas

| Superficie predial m² (desde-hasta) | Altura máxima N° pisos | Coeficiente constructibilidad | Ocupación suelo (coeficiente) | Sistema agrupamiento | Rasantes y distanciamientos | Antejardín mínimo | Adosamiento máximo % |
|---|---|---|---|---|---|---|---|
| 0 – 1000 | Rasante | 1.8 | 0.70 | A-P* | O.G.U.C. | Art.11 | 40 |
| 1001 – 2000 | " | 2.0 | 0.65 | A* | " | Art.11 | 40 |
| 2001 – 3000 | " | 2.3 | 0.60 | A* | " | Art.11 | 40 |
| 3001 y más | " | 2.5 | 0.55 | A* | " | Art.11 | 40 |

`* A=Aislado, * P=Pareado`

**Disposiciones complementarias (texto literal, 8 ítems):**
- Densidad bruta mínima: 400 Hab./Há.
- Densidad neta mínima: 500 Hab./Há.
- Los antejardines no pueden utilizarse para estacionamiento de vehículos.
- Los estacionamientos a nivel de terreno sólo podrán ocupar el 20% del área libre o, de requerirse mayor porcentaje deberá destinar al menos un 30% de la superficie predial exclusivamente a prados y jardines incluyendo el área de antejardín.
- Los estacionamientos en subterráneo sólo podrán ocupar el 70% de la superficie del terreno.
- El equipamiento comercial de esta zona deberá tener una superficie mínima de 200 m² construidos y cumplir la norma de estacionamientos señalada en el artículo 14 de esta Ordenanza.
- Las construcciones pareadas no podrán sobrepasar los 9 m de altura medidos en el deslinde con los predios vecinos y su profundidad máxima será de 15 m o el equivalente al 40% del fondo del predio cuando la profundidad de éste sea inferior a 25 m. Sobre esta altura el sistema de agrupamiento es aislado.
- Se aplicará, para todos los sistemas de agrupamiento, cuando sea el caso, el inciso tercero del Art. 8º de la presente Ordenanza.
- En esta zona, se aplica la restricción de altura de edificación correspondiente a áreas de aproximación de aeródromo, indicada en el Art.26° de esta Ordenanza.

**Confianza: ALTA.** *(Nota: la zona ZU-2 fue posteriormente objeto de una "Disposición Especial" por el Decreto Exento N° 3.164/2014, ya transcrita en `san_miguel_3164_zu2_disposicion_especial.md` de este mismo repositorio — sin conflicto con lo aquí transcrito, es una adición puntual posterior sobre un polígono específico.)*

---

## 7. ZONA ZU-3 — Industrial Exclusiva (páginas 12→13/DO)

> **Descripción (texto literal):** "Corresponde a las Áreas Industriales Exclusivas con Actividades Molestas definida en el Artículo 6.1.3.4. del P.R.M.S."

**Usos permitidos (texto literal, encabezado fuente "USOS PERMITIDOS :" con espacio antes de los dos puntos `[sic]`):**
1. **EQUIPAMIENTO:** "Científico, comercio, deporte, educación sólo cuando se destine a establecimientos de formación técnico profesional y jardín infantil, salud sólo cuando se destine a servicios de atención ambulatoria, seguridad, servicios, social. Cuando los servicios de carácter artesanal sean calificadas `[sic]` como 'actividades productivas' no corresponderán a equipamiento de servicios, sin perjuicio de lo señalado en el art. 2.1.28. de la O.G.U.C."
2. **ACTIVIDADES PRODUCTIVAS:** "Almacenamiento y Actividades de Servicio de Impacto similar al Industrial calificados como molestas y/o inofensivas, industrias calificadas como molestas y/o inofensivas, talleres calificados como molestos y/o inofensivos, talleres o servicios artesanales calificados como molestos y/o inofensivos, vivienda del cuidador. Los 'terminales de distribución' de cualquier tipo se considerarán para estos efectos como establecimientos de almacenamiento o bodegas. Todas estas actividades se autorizarán conforme al certificado de calificación que acredite su calidad de actividades productivas 'INOFENSIVAS' o 'MOLESTAS'. Este certificado es emitido por la Secretaría Regional Ministerial de Salud de la Región Metropolitana, sin perjuicio de otras calificaciones o informes a ser emitidos por otros organismos competentes, lo anterior conforme a lo señalado en el capítulo 6.1 del P.R.M.S. y en el capítulo 14, título 4 de la O.G.U.C."
3. **INFRAESTRUCTURA:** "De transporte como estacionamientos, instalaciones de telecomunicaciones y antenas de telefonía celular, rodoviarios y terminales de locomoción colectiva urbana, terminal de locomoción colectiva interurbana, terminales de taxis y radiotaxis, terminales de transporte terrestre. Sanitaria como canales de riego e Infraestructura energética como ductos de distribución de gas."
4. **ÁREAS VERDES:** "Bandejones y platabandas, parque, plaza, jardines."

**Usos prohibidos (texto literal, 12 ítems):**
- Residencial excepto vivienda de cuidador.
- Equipamiento de comercio correspondiente a arriendo de automóviles y/o maquinaria, grandes tiendas, mercados, multitiendas, supermercados.
- Equipamiento de culto y cultura.
- Equipamiento de deporte correspondiente a coliseo, estadio, gimnasio, medialuna, piscina, sauna o baño turco.
- Equipamiento de educación correspondiente a colegio, escuela básica, escuela prebásica, escuela especial, instituto, instituto superior, jardín infantil, liceo, liceo comercial, parvulario, universidad.
- Equipamiento de esparcimiento.
- Equipamiento de salud correspondiente a casa de reposo, centro de diálisis, clínica de recuperación médica, clínica psiquiátrica, clínica veterinaria, dispensario, hogar de ancianos, hospital.
- Equipamiento de seguridad correspondiente a cárceles y centros de detención.
- Equipamiento de servicios correspondiente a Centro de homeopatía, centro ortopédico, centro psicopedagógico, centro de medicina veterinaria, conservador de bienes raíces, corte de justicia, asociación de fondos de pensiones, empresas tales como administradora de inversiones y otros, juzgado, servicios e instituciones ministeriales y/o estatales, servicios públicos.
- Equipamiento social correspondiente a clubes deportivos, juntas de vecinos, organizaciones juveniles.
- Establecimientos industriales insalubres o contaminantes y peligrosos.
- Infraestructura correspondiente a disposición transitoria o final de residuos sólidos, estación ferroviaria, estaciones y talleres del metro, plantas de tratamiento de aguas servidas.

*(Nota: el primer ítem, "Residencial excepto vivienda de cuidador", confirma por contraste que ZU-3 —a diferencia de ZU-1, ZU-2 y ZU-4— no incluye "RESIDENCIAL" entre sus categorías de uso permitido en el numerado de arriba; solo admite vivienda del cuidador, ya mencionada dentro de "2. ACTIVIDADES PRODUCTIVAS".)*

### Cuadro de normas urbanísticas (estructurado por tipo de uso, no por rango de superficie predial)

| Usos | Superficie predial m² (desde-hasta) | Altura máxima N° pisos | Coeficiente constructibilidad | Ocupación del suelo | Sistema agrupamiento | Distanciamientos mínimos a medianeros (m) | Antejardín mínimo (m) | Adosamiento máximo % |
|---|---|---|---|---|---|---|---|---|
| Equipamientos | 500 y más | Rasante | 1.0 | 0.70 | A* | 5 | 5 | 0 |
| Talleres | 500 y más | Rasante | 2.0 | 0.70 | A* | 5 | 5 | 0 |
| Actividades complementarias a la vialidad y transporte | 1500 y más | Rasante | 1.0 | 0.70 | A* | 5 | 5 | 0 |
| Industria, almacenamiento y actividades de carácter similar al industrial | 1500 y más | Rasante | 2.0 | 0.70 | A* | 5 | 5 | 0 |

`* A=Aislado`

**Disposiciones complementarias (texto literal, 9 ítems):**
- Se deberá disponer de una superficie mínima de 100 m² para carga y descarga de vehículos mayores.
- Las guarderías de camiones o depósitos de vehículos solo podrán instalarse en predios mayores a 1.000 m² y frente a calles de 20 m o más de ancho.
- Los sitios en que se instale equipamiento tendrán una superficie mínima de 500 m².
- En cada predio de carácter industrial solo podrán consultarse viviendas para cuidadores.
- Se aplicarán todas las disposiciones respectivas a "Zonas Industriales Molestas" de acuerdo al Art. 6.1.3.4 del P.R.M.S.
- La Dirección de Obras Municipales solicitará a la Secretaría Regional Ministerial de Salud de la Región Metropolitana la fiscalización y seguimiento de los establecimientos industriales de acuerdo a Resolución 5081 del 12.03.93 de SESMA - MINSAL – Diario Oficial de 18 de marzo de 1993 y al Programa de Control de Emisiones de Fuentes Fijas en cuanto a residuos industriales sólidos y generación de contaminantes atmosféricos.
- Se aplicará, cuando sea el caso, el inciso tercero del Art. 8º de la presente ordenanza.
- En esta zona, se aplica la restricción de altura de edificación correspondiente a áreas de aproximación de aeródromo, indicada en el Art.26° de esta ordenanza.
- Ante la eventualidad de término de actividades de la industria actualmente existente, quedan sin efecto las disposiciones de la zona ZU-3 y se aplicarán las disposiciones correspondientes a la zona ZU-2 "Residencial de renovación".

**Confianza: ALTA.**

---

## 8. ZONA ZU-4 — Industrial Mixta (páginas 13→14/DO)

**Usos permitidos (texto literal):**
1. **RESIDENCIAL:** "Vivienda, sin perjuicio de lo cual, se autoriza la implantación de comercio en el 1er. piso. Aquellos uso `[sic, por "usos"]` definidos en el Art. 2.1.25 de la O.G.U.C. y los complementos a vivienda establecidos en el Art. 2.1.26 de la O.G.U.C."
2. **EQUIPAMIENTO:** "Científico, comercio, culto y cultura correspondiente a canales de televisión y radioemisoras, deporte, educación, esparcimiento, salud, seguridad, servicios, social. Cuando los servicios de carácter artesanal sean calificadas `[sic]` como 'actividades productivas' no corresponderán a equipamiento de servicios, sin perjuicio de lo señalado en el art. 2.1.28. de la O.G.U.C."
3. **ACTIVIDADES PRODUCTIVAS:** "Almacenamiento y Actividades de Servicio de Impacto similar al Industrial calificados como inofensivos, industrias calificadas como inofensivas, talleres calificados como inofensivos, talleres o servicios artesanales calificados como inofensivos, vivienda del cuidador. Los 'terminales de distribución' de cualquier tipo se considerarán para estos efectos como establecimientos de almacenamiento o bodegas. Todas estas actividades se autorizarán conforme al certificado de calificación que acredite su calidad de actividades productivas 'INOFENSIVAS'. Este certificado es emitido por la Secretaría Regional Ministerial de Salud de la Región Metropolitana, sin perjuicio de otras calificaciones o informes a ser emitidos por otros organismos competentes, lo anterior conforme a lo señalado en el capítulo 6.1 del P.R.M.S y en el capítulo 14, título 4 de la O.G.U.C."
4. **INFRAESTRUCTURA:** "De transporte como estacionamientos, estación ferroviaria, instalaciones de telecomunicaciones y antenas de telefonía celular, rodoviarios y terminales de locomoción colectiva urbana, terminal de locomoción colectiva interurbana, terminales de taxis y radiotaxis, terminales de transporte terrestre. Sanitaria como canales de riego e Infraestructura energética como ductos de distribución de gas."
5. **ÁREAS VERDES:** "Bandejones y platabandas, parque, plaza, jardines."

**Usos prohibidos (texto literal, 10 ítems):**
- Equipamiento de comercio correspondiente a centro comercial, grandes tiendas, mercados, multitiendas, supermercados.
- Equipamiento de culto y cultura exceptuando canales de televisión y radioemisoras.
- Equipamiento de deporte correspondiente a coliseos, estadios, gimnasio, medialuna, piscina, sauna y baño turco.
- Equipamiento de educación correspondiente a colegio, escuela básica, escuela prebásica, escuela especial, guardería infantil, instituto, instituto superior, jardín infantil, liceo, liceo comercial, parvulario, universidad.
- Equipamiento de esparcimiento correspondiente a hoteles y moteles.
- Equipamiento de salud correspondiente a casa de reposo, centro de diálisis, clínica de recuperación médica, clínica psiquiátrica, clínica veterinaria, consultorio, dispensario, hogar de ancianos, hospital.
- Equipamiento de seguridad correspondiente a cárceles y centros de detención.
- Equipamiento de servicios correspondiente a centro de homeopatía, centro ortopédico, centro psicopedagógico, centro de medicina veterinaria, conservador de bienes raíces, corte de justicia, asociación de fondos de pensiones, juzgado.
- Establecimientos industriales peligrosos, insalubres o contaminantes y molestos.
- Infraestructura correspondiente a disposición transitoria o final de residuos sólidos, estación ferroviaria, estaciones y talleres del metro, plantas de tratamiento de aguas servidas.

### Cuadro de normas urbanísticas

| Superficie predial m² (desde-hasta) | Altura máxima N° pisos | Coeficiente constructibilidad | Ocupación suelo (coeficiente) | Sistema agrupamiento | Rasantes y distanciamiento | Antejardín mínimo (m) | Adosamiento máximo % |
|---|---|---|---|---|---|---|---|
| 0 – 500 | Rasante | 1.5 | 0.70 | A* | O.G.U.C. | 3 | 40 |
| 501 – 1000 | " | 2.0 | 0.60 | A* | " | " | 40 |
| 1001 y más | " | 2.5 | 0.50 | A* | " | " | 40 |

`* A=Aislado`

**Disposiciones complementarias (texto literal, 9 ítems, partidas entre página 13 y 14):**
- Densidad bruta mínima: 200 hab/Há.
- Densidad neta mínima: 250 hab/Há.
- Los terrenos para equipamiento de comercio y actividades productivas deberán disponer de un patio mínimo de 100 m² para carga y descarga de camiones proveedores, y enfrentar calles de un ancho mínimo de 15 m.
- Los sitios en que se instale equipamiento tendrán una superficie predial mínima de 500 m² y deberán enfrentar calles de un ancho mínimo de 15 m.
- Las guarderías de camiones o depósitos de vehículos sólo podrán instalarse en predios mayores a 1.000 m² y frente a calles de 20 m o más de ancho.
- En cada predio de carácter industrial solo podrán consultarse viviendas para cuidadores.
- La Dirección de Obras Municipales solicitará a la Secretaría Regional Ministerial de Salud de la Región Metropolitana la fiscalización y seguimiento de los establecimientos industriales de acuerdo a Resolución 5081 del 12.03.93 de SESMA – MINSAL – Diario Oficial de 18 de marzo de 1993 y al Programa de Control de Emisiones de Fuentes Fijas en cuanto a residuos industriales sólidos y generación de contaminantes atmosféricos.
- Se aplicará, cuando sea el caso, el inciso tercero del Art. 8º de la presente Ordenanza.
- En esta zona, se aplica la restricción de altura de edificación correspondiente a áreas de aproximación de aeródromo, indicada en el Art. 26° de esta Ordenanza.

*(Los dos primeros ítems de densidad quedan al pie de la página 13/DO y los 7 restantes al inicio de la página 14/DO, sin solución de continuidad. **Nota de reconciliación con AMIGO1:** una segunda transcripción independiente de este mismo documento, hecha por otra sesión, atribuyó estos mismos 7 ítems a ZU-4 solo "tentativamente", documentando como caveat explícito que la estructura de columnas de la página no permitía descartar con certeza absoluta que pertenecieran a ZU-3 en vez de a ZU-4. Esta transcripción los asigna a ZU-4 sin reservas — verificado que el bloque aparece inmediatamente a continuación del cierre de ZU-4 en el flujo de columna, sin marca de encabezado de otra zona interpuesta — pero se dej a constancia de que la otra sesión consideró el punto genuinamente ambiguo, para que una revisión futura con acceso directo a la imagen pueda zanjarlo con un tercer chequeo si se estima necesario.)*

**Confianza: ALTA.** *(Nota: la zona ZU-4 fue posteriormente objeto de una nueva zona derivada "ZU-4'" — Industrial Mixta con condiciones distintas — creada por el Decreto Exento N° 3.162/2014, ya transcrita en `san_miguel_dex3162_zona_zu4prima_industrial_mixta_pag2-5.md` de este repositorio; no hay conflicto, es una zona nueva sobre un polígono acotado, no una modificación de ZU-4 en general.)*

---

## 9. ZONA ZU-5 — Equipamiento Regional de Salud (página 14/DO)

**Usos permitidos (texto literal):** "Equipamiento de salud correspondiente a centro de diálisis, consultorio, hospital, policlínico, posta de primeros auxilios, vivienda de cuidadores, dependencias, servicios y talleres complementarios a la actividad principal."

**Usos prohibidos (texto literal):** "Todos aquellos no indicados como permitidos."

### Cuadro de normas urbanísticas

| Superficie predial m² (desde-hasta) | Altura máxima N° pisos | Coeficiente constructibilidad | Ocupación suelo (coeficiente) | Sistema agrupamiento | Rasantes y distanciamiento | Antejardín mínimo (m) | Adosamiento máximo % |
|---|---|---|---|---|---|---|---|
| 4000 y más | Rasante | 2 | 0.60 | A-P* | O.G.U.C. | Art. 11 | 40 |

`* A=Aislado, * P=Pareado`

**Disposiciones complementarias (texto literal, 2 ítems):**
- Las construcciones pareadas no podrán sobrepasar los 6 metros de altura medidos en el deslinde con los predios vecinos y su profundidad máxima será de 15 m o el equivalente al 40% del fondo del predio cuando la profundidad de este sea inferior a 25 metros. Sobre esta altura el sistema de agrupamiento es aislado.
- Se aplicará, cuando sea el caso, el inciso tercero del Art. 8º de la presente Ordenanza.

**Confianza: ALTA.** *(Nota: la zona ZU-5 fue posteriormente objeto de una ampliación por reclasificación de polígono — Decreto Exento N° 2.371/2009, sector Hospital Barros Luco, ya transcrito en `san_miguel_2371_reclasificacion_zu5_barros_luco.md` de este repositorio, que remite explícitamente a "las normas de la Zona ZU-5, Ordenanza Local del PRC de San Miguel, artículo 25" — es decir, remite exactamente a este cuadro. Coherente, sin conflicto.)*

---

## 10. ZONA ZU-6 — Ferroviaria (página 14/DO)

> **Descripción (texto literal):** "Corresponde al área de terreno donde se encuentra la faja vía del ferrocarril de Circunvalación y sus instalaciones complementarias."

**Límites (texto literal):**

| Deslinde | Descripción |
|---|---|
| Al Norte | Eje de la línea del Ferrocarril de Circunvalación |
| Al Sur | La línea recta que corre paralela a 78 m al Norte de la línea oficial de cierros proyectada de la acera Sur de la Avenida Carlos Silva Vildósola |
| Al Oriente | Avenida Santa Rosa |
| Al Poniente | Gran Avenida José Miguel Carrera |

> "Zona sujeta a área de resguardo de vías férreas correspondiente a faja de resguardo de 20 m de ancho a ambos costados de la vía férrea."

**Usos permitidos / usos prohibidos / cuadro de normas urbanísticas: Sin valor específico en la fuente.** Esta zona es la única de las 14 que no trae ninguno de los tres elementos — coherente con ser una franja de infraestructura ferroviaria delimitada por deslindes geográficos, no una zona de edificación/subdivisión estándar. No es una omisión de esta transcripción: se verificó contra la imagen que el texto de ZU-6 termina en la frase de la faja de resguardo y pasa directamente al título de la siguiente sección ("ZONAS DE EQUIPAMIENTO Y ÁREAS VERDES, NIVEL METROPOLITANO E INTERCOMUNAL").

**Confianza: ALTA.**

---

## 11. ZONA EM-1 — Equipamiento Intercomunal (páginas 14→15/DO)

> **Descripción (texto literal):** "Corresponde a propiedad del Consejo de Defensa del Niño y equipamientos de comercio (Megamercado)."

**Usos permitidos (texto literal):** "Equipamiento Intercomunal de comercio y servicios, culto y cultura, deporte, educación, esparcimiento, salud y áreas verdes. Vivienda, vivienda para cuidador."

**Usos prohibidos (texto literal, 6 ítems):**
- Equipamiento de comercio correspondiente a Ferias libres, discotecas.
- Equipamiento de cultura correspondiente a canales de televisión y radioemisoras.
- Equipamiento de esparcimiento correspondiente a Autocine, cabaret, hotel, motel, pista de espectáculos, quinta de recreo, sala de eventos, salón de baile, zona de picnic, zoológicos.
- Equipamiento de salud correspondiente a hospital.
- Equipamiento de seguridad correspondiente a cárceles y centros de detención.
- Infraestructura correspondiente a cementerios, disposición transitoria o final de residuos sólidos, Instalaciones de telecomunicaciones, plantas de tratamiento de aguas servidas, terminales de carga, rodoviarios y terminales de locomoción colectiva urbana, terminales de taxis, radiotaxis.
- "Todos aquellos n o indicados como permitidos." `[sic: espacio suelto dentro de "no"]`

### Cuadro de normas urbanísticas

| Superficie predial m² (desde-hasta) | Altura máxima N° pisos | Coeficiente constructibilidad | Ocup. suelo 1 a 3 pisos | Ocup. suelo sobre 3 pisos | Sistema agrupamiento | Rasantes y distanciamiento | Antejardín mínimo | Adosamiento máximo % |
|---|---|---|---|---|---|---|---|---|
| 1000-2000 | Rasante | 2.5 | 0.60 | 0.50 | A* | O.G.U.C. | Art. 11 | 0 |
| 2001-5000 | " | 3.0 | 0.60 | 0.50 | A* | " | Art. 11 | 0 |
| 5001 y más | " | 3.5 | 0.60 | 0.50 | A* | " | Art. 11 | 0 |

`* A=Aislado`

**Disposiciones complementarias (texto literal, 4 ítems):**
- Los predios existentes inferiores a 1000 m² se regirán por las normas del primer tramo del cuadro anterior.
- El área libre después de aplicado el coeficiente de ocupación de suelo podrá usarse para estacionamientos.
- El equipamiento comercial tendrá una superficie mínima de 500 m² o deberán formar parte de un conjunto de esas dimensiones y cumplirán la norma de estacionamientos señalada en el artículo 14 de esta Ordenanza.
- En esta zona, aplica la restricción de altura de edificación correspondiente a áreas de aproximación de aeródromo, indicada en el Art. 26° de esta Ordenanza.

**Confianza: ALTA.** *(Nota: el Decreto N° 515/2009, ya transcrito en `san_miguel_do515_zonas_em3_em4_restriccion_d_e_pag1-2_11-13.md`, agrega un inciso puntual a EM-1 sobre un polígono acotado del sector Gran Avenida/Walker Martínez/Lo Ovalle/Tannenbaum, permitiendo un coeficiente de ocupación de suelo de 0,80 [1-3 pisos] y 0,50 [sobre 3 pisos] para "Equipamiento Clase Comercio" — valores puntuales adicionales a, no en conflicto con, el cuadro general aquí transcrito.)*

---

## 12. ZONA EM-2 — Equipamiento Recreacional y Deportivo (página 15/DO)

**Nota de nomenclatura `[sic]`:** el listado del Art. 25° (§4) rotula esta área como "**Area** EM-2"; el encabezado del propio desarrollo de la zona, en cambio, dice literalmente "**ZONA** EM-2" (mismo patrón "ZONA" que usan ZU-1 a ZU-6 y EM-1, no "ÁREA" como sí usan EM-3, EM-4 y EC-1 a EC-3). Inconsistencia real de la fuente, preservada tal cual.

> **Composición (texto literal):** "Corresponde a los que siguen:" — Estadio El Llano del Banco del Estado; Estadio La Montura.

**Usos permitidos (texto literal):** "Equipamientos de deporte correspondiente a canchas, centro deportivo, gimnasio, multicanchas, piscina, servicios complementarios a la actividad principal y áreas recreacionales."

**Usos prohibidos (texto literal):** "Todos aquellos no indicados como permitidos."

### Cuadro de normas urbanísticas

| Superficie predial m² (desde-hasta) | Altura máxima N° pisos | Coeficiente constructibilidad | Ocupación del suelo (coeficiente, en 1er. piso) | Sistema agrupamiento | Rasantes y distanciamientos | Antejardín mínimo | Adosamiento máximo % |
|---|---|---|---|---|---|---|---|
| 2000-5000 | Rasante | 0.2 | 0.10 | A* | O.G.U.C. | Art. 11 | --- |
| 5001 y más | " | 0.1 | 0.05 | A* | O.G.U.C. | Art. 11 | --- |

`* A=Aislado`

**Disposiciones complementarias (texto literal, 3 ítems):**
- Prohibido el uso residencial.
- Las canchas deportivas, piscinas y graderías al aire libre no se contabilizan para el cálculo de ocupación del terreno.
- El equipamiento "Estadio El Llano", se encuentra afecto a la restricción de altura de edificación correspondiente a áreas de aproximación de aeródromo, indicada en el Art. 26° de esta Ordenanza.

**Confianza: ALTA.**

---

## 13. ÁREA EM-3 — Áreas Verdes Existentes Intercomunales (Avenidas Parque) (páginas 15→16/DO)

> **Descripción (texto literal):** "Están dispuestas por el P.R.M.S en su Artículo 5.2.3.4 como Avenidas Parque, son bienes nacionales de uso público y corresponden a las siguientes:" — Parque Isabel Riquelme (Parque Adyacente a Cauce) – Tramo Avda. Pdte. J. Alessandri R. – Gran Avda. J. M. Carrera; Parque El Llano Subercaseaux (Parque Adyacente a Sistema Vial).

**Usos permitidos (texto literal):** "Equipamientos de cultura, de deporte, de esparcimiento, de comercio complementario al área verde correspondiente a kioskos y ferias temáticas, caseta de vigilancia, juegos infantiles, graderías, mobiliario de áreas verdes."

**Usos prohibidos (texto literal):** "Todos aquellos no indicados como permitidos."

### Cuadro de normas urbanísticas

| Superficie predial m² | Altura máxima N° pisos | Coeficiente constructibilidad | Ocupación del suelo (coeficiente) | Sistema agrupamiento | Rasantes y distanciamientos | Antejardín mínimo | Adosamiento máximo % |
|---|---|---|---|---|---|---|---|
| No divisible | Rasante | 0.05 | 0.05 | A* | O.G.U.C. | Art. 11 | --- |

`* A=Aislado`

**Disposiciones complementarias (texto literal, 5 ítems, partidas entre página 14/15):**
- Prohibido el uso residencial.
- Las canchas deportivas, piscinas y graderías al aire libre no se contabilizan para el cálculo de ocupación del terreno.
- Los proyectos específicos del equipamiento permitido deberán ser aprobados por la Dirección de Obras.
- En esta zona, aplica la restricción de altura de edificación correspondiente a áreas de aproximación de aeródromo, indicada en el Art. 26° de esta Ordenanza.
- Rige la restricción de áreas de resguardo de líneas de alta tensión para el Parque Isabel Riquelme en toda su longitud.

**Confianza: ALTA.** **Hallazgo relevante (ver también §25):** esta zona está **completa** en este documento, a diferencia del decreto hermano N° 515/2009 (`san_miguel_do515_...md`), donde EM-3 quedó **fuera del rango entregado** en esa ocasión y tuvo que marcarse "Dato no determinable". Aquí, en cambio, sí se pudo verificar su cuadro completo: **No divisible | Rasante | 0.05 | 0.05 | A* | O.G.U.C. | Art. 11 | ---**.

---

## 14. ÁREA EM-4 — Áreas Verdes Proyectadas Intercomunales (Avenida Parque) (página 15/DO)

> **Descripción (texto literal):** "Las áreas verdes proyectadas o no consolidadas corresponden al sector del Parque Isabel Riquelme entre Avenida Santa Rosa por el Oriente y la Gran Avenida José Miguel Carrera por el Poniente."

**Usos de suelo:** "Rigen para esta área los usos permitidos y prohibidos del área EM-3" — remisión íntegra, sin lista propia.

### Cuadro de normas urbanísticas

| Superficie predial m² | Altura máxima N° pisos | Coeficiente constructibilidad | Ocupación del suelo (coeficiente) | Sistema agrupamiento | Rasantes y distanciamientos | Antejardín mínimo | Adosamiento máximo % |
|---|---|---|---|---|---|---|---|
| No divisible | Rasante | 0.20 | 0.20 | A* | O.G.U.C. | Art. 11 | --- |

`* A=Aislado`

**Disposiciones complementarias (texto literal, 3 ítems):**
- Las señaladas para el área EM-3.
- Las impuestas por el Art. 2.1.30 de la O.G.U.C. para los casos de áreas verdes que no son Bienes Nacionales de Uso Público.
- De cambiar la calidad jurídica de los predios a "Bien Nacional de Uso Público" la zona "EM-4" queda sin efecto pasando esta zona a formar parte de "EM-3".

**Confianza: ALTA.** Cuadro y disposiciones **idénticos** a los transcritos en el decreto hermano N° 515/2009 (misma zona, snapshot 2009) — fuerte validación cruzada entre ambos documentos de este repositorio (ver §25).

---

## 15. ÁREA EC-1 — Recreacional y Deportivo (página 15/DO)

> **Composición (texto literal):** "Las Áreas de Equipamiento Recreacional y Deportivo son las que siguen:" Canchas de Tenis Soto Aguilar; Complejo Deportivo Tatio; Estadio Municipal de San Miguel; Gimnasio Colón América; Multicancha Villa Austral.

**Usos permitidos (texto literal):** "Equipamientos de deporte correspondiente a canchas, centro deportivo, gimnasio, multicanchas, piscina, servicios complementarios a la actividad principal y áreas recreacionales."

**Usos prohibidos (texto literal):** "Todos aquellos no indicados como permitidos."

### Cuadro de normas urbanísticas

| Superficie predial m² (desde-hasta) | Altura máxima N° pisos | Coeficiente constructibilidad | Ocupación del suelo (coeficiente, en 1er. piso) | Sistema agrupamiento | Rasantes y distanciamientos | Antejardín mínimo | Adosamiento máximo % |
|---|---|---|---|---|---|---|---|
| Existente | Rasante | 0.2 | 0.1 | A* | O.G.U.C. | Art. 11 | --- |

`* A=Aislado`

**Disposiciones complementarias (texto literal, 3 ítems):**
- Prohibido el uso residencial.
- Las canchas deportivas, piscinas y graderías al aire libre no se contabilizan para el cálculo de ocupación del terreno.
- Según su ubicación (Ver plano PRSM-1), algunos de estos equipamientos se encuentran afectos a la restricción de altura de edificación correspondiente a áreas de aproximación de aeródromo, indicada en el Art. 26° de esta Ordenanza.

**Confianza: ALTA.** Cuadro idéntico al del decreto hermano N° 515/2009. **Nota de continuidad:** dos decretos posteriores (N° 3.163/2014 y N° 3.164/2014, ya transcritos en este repositorio) eliminan la línea "Complejo Deportivo Tatio" de esta lista de 5 instalaciones — consistente con que la lista de 2005 aquí transcrita es la versión original, base de esa modificación de 2014.

---

## 16. ÁREA EC-2 — Áreas Verdes Comunales (páginas 15→16/DO)

> **Descripción (texto literal):** "Las áreas verdes existentes comunales corresponden a las graficadas en el Plano PRSM-1."

**Usos permitidos (texto literal):** "Equipamientos de cultura, de deporte, de esparcimiento, de comercio complementario al área verde correspondiente a kioskos y ferias temáticas, caseta de vigilancia, juegos infantiles, graderías, mobiliario de áreas verdes."

**Usos prohibidos (texto literal):** "Todos aquellos no indicados como permitidos."

### Cuadro de normas urbanísticas

| Superficie predial m² | Altura máxima N° pisos | Coeficiente constructibilidad | Ocupación del suelo (coeficiente) | Sistema agrupamiento | Rasantes y distanciamientos | Antejardín mínimo | Adosamiento máximo % |
|---|---|---|---|---|---|---|---|
| No divisible | Rasante | 0.05 | 0.05 | A* | O.G.U.C. | Art. 11 | --- |

`A=Aislado` `[sic: la leyenda de esta zona aparece sin el asterisco "*" que sí llevan las demás zonas, pese a que la celda de la tabla usa "A*" con asterisco — mismo detalle exacto que en el decreto hermano N° 515/2009 para esta misma zona; se preserva tal cual]`

**Disposiciones complementarias (texto literal, 4 ítems):**
- Prohibido el uso residencial.
- Las canchas deportivas, piscinas y graderías al aire libre no se contabilizan para el cálculo de ocupación del terreno.
- Los proyectos específicos del equipamiento permitido deberán ser aprobados por la Dirección de Obras.
- Según su ubicación (Ver plano PRSM-1), algunas de estas áreas verdes se encuentran afectas a la restricción de altura de edificación correspondiente a áreas de aproximación de aeródromo, indicada en el Art. 26° de esta Ordenanza.

**Confianza: ALTA.** Cuadro y anomalía tipográfica de la leyenda idénticos a los del decreto hermano N° 515/2009 — fuerte validación cruzada.

---

## 17. ÁREA EC-3 — Áreas Verdes Comunales Proyectadas (página 16/DO)

**Nota de nomenclatura `[sic]`:** el Art. 25° (§4) rotula esta área "ÁREAS VERDES **PROYECTADAS COMUNALES**"; el encabezado del propio desarrollo dice "ÁREAS VERDES **COMUNALES PROYECTADAS**" (orden de palabras invertido). Ambas variantes se preservan tal cual aparecen en su respectivo lugar.

> **Descripción (texto literal):** "Las áreas verdes proyectadas corresponden a las graficadas en el Plano PRSM-1."

**Usos permitidos (texto literal):** "Equipamientos de cultura, de deporte, de esparcimiento, de comercio complementario al área verde correspondiente a kioskos y ferias temáticas, caseta de vigilancia, juegos infantiles, graderías, mobiliario de áreas verdes."

**Usos prohibidos (texto literal):** "Todos aquellos no incluidos como permitidos." *(nótese "incluidos", distinto de "indicados" que usan EC-1/EC-2/EM-2/EM-3 — variación literal de la fuente, ver también ICH §18 y consolidado en §25)*

### Cuadro de normas urbanísticas

| Superficie predial m² | Altura máxima N° pisos | Coeficiente constructibilidad | Ocupación del suelo (coeficiente) | Sistema agrupamiento | Rasantes y distanciamientos | Antejardín mínimo | Adosamiento máximo % |
|---|---|---|---|---|---|---|---|
| No divisible | Rasante | 0.1 | 0.1 | A* | O.G.U.C. | Art. 11 | --- |

`* A=Aislado`

**Disposiciones complementarias (texto literal, 5 ítems):**
- Prohibido el uso residencial.
- Las canchas deportivas, piscinas y graderías al aire libre no se contabilizan para el cálculo de ocupación del terreno.
- Los proyectos específicos del equipamiento permitido deberán ser aprobados por la Dirección de Obras.
- En esta zona, aplica la restricción de altura de edificación correspondiente a áreas de aproximación de aeródromo, indicada en el Art. 26° de esta Ordenanza.
- Las impuestas por el Art. 2.1.30 de la O.G.U.C. para los casos de áreas verdes que no son Bienes Nacionales de Uso Público.

**Confianza: ALTA.** Cuadro idéntico al del decreto hermano N° 515/2009. **Nota de continuidad:** el Decreto Exento N° 2.371/2009 (ya transcrito en este repositorio) relocaliza esta misma zona EC-3 en torno a los inmuebles de conservación histórica, con un leve aumento de superficie — consistente con que se trata de la misma área aquí definida por primera vez.

---

## 18. ICH — Inmuebles de Conservación Histórica (página 16/DO)

> **Listado (texto literal, "Son los que se detallan:", 11 ítems):**
1. Cierro exterior y portal de acceso al Hospital Barros Luco (Gran Avenida José Miguel Carrera N° 3204)
2. Capilla Hospital Barros Luco (Gran Avenida José Miguel Carrera N° 3204 - Interior)
3. Casa Municipal de la Cultura (Llano Subercaseaux N° 3519-B)
4. Bodegas Viña Concha y Toro (Fernando Lazcano N° 1220 esq. Llano Subercaseaux)
5. Iglesia de San Miguel (Gran Avenida José Miguel Carrera N° 3520)
6. Capilla y Colegio Claretiano (Gran Avenida José Miguel Carrera N° 4160)
7. Liceo A-90 (Darío Salas N° 5270)
8. Antigua casa de don Ramón Subercaseaux (Llano Subercaseaux N° 3519-B)
9. Bodegas Subterráneas de la Viña Subercaseaux (Llano Subercaseaux N° 3519-B)
10. Edificio Consistorial (Gran Avenida José Miguel Carrera N° 3418)
11. Estadio El Llano (José Joaquín Vallejos N° 1406)

**Usos permitidos (texto literal):** "Equipamientos de culto y cultura, de educación, uso actual y en general aquéllos que no alteren la configuración y conservación de los mismos."

**Usos prohibidos (texto literal):** "Todos aquellos no incluidos como permitidos."

**Cuadro de normas urbanísticas: Sin valor específico en la fuente** — por diseño, esta zona no trae cuadro numérico propio; remite a la zona circundante.

**Disposiciones complementarias (texto literal):** "Los Inmuebles de Conservación Histórica se regirán por lo dispuesto en el Artículo 20º de la presente ordenanza y se aplicarán las normas urbanísticas y disposiciones complementarias de la zona circundante cuando se autorice su intervención." *(el Artículo 20° no está en el rango de páginas de este documento — pertenece al Capítulo III, Definiciones y Normas Generales, en las páginas 1-5 no entregadas)*

**Confianza: ALTA.** Listado de 11 inmuebles **idéntico, en el mismo orden y con las mismas direcciones**, al transcrito en el decreto hermano N° 515/2009 — fuerte validación cruzada adicional.

---

## 19. Artículo 26° — Áreas con Restricciones (AR-1 a AR-4) (páginas 15→16/DO)

Al igual que en el decreto hermano N° 515/2009, estas 4 áreas **no son zonas de uso de suelo primarias**: son restricciones que se superponen a la zonificación de base (ya remitidas brevemente desde el Art. 25°, §4). Se documentan aquí de forma breve por continuidad, siguiendo el mismo criterio aplicado en el documento hermano.

**AR-1 — Área de protección de Canales de riego** (Zanjón de la Aguada y Canal San Joaquín): área de protección a lo largo del trazado de los cauces abovedados, sin edificaciones; incluye dos franjas libres de protección de **3 metros a cada lado**, donde se permiten obras de infraestructura sanitaria y energética. Tránsito y limpieza rigen por el Código de Aguas y el D.F.L. N° 1.122 de 1981 (DO 29-oct-1981).

**AR-2 — Áreas de resguardo de Aeródromos** (El Bosque y Los Cerrillos), regidas por Ley N° 18.916/1990 (Código Aeronáutico), D.S. N° 146/1992 (Ministerio de Defensa) y normas de la DGAC (plano PP-91-01):

| Área | Definición | Restricción de altura |
|---|---|---|
| "C" | Bajo riesgo, bajo la trayectoria de aproximación-despegue al Aeródromo El Bosque; sentido Sur-Norte, 13.182 m a continuación del área "B" (no definida en el rango entregado) | Rasante desde extremos de la Franja de Pista, pendiente 2%, hasta 150 m sobre nivel medio de pista → **101,5 metros** en el punto más desfavorable (eje Av. Lo Ovalle entre 2ª Transversal y Nicolás Gorab) |
| "D" | Riesgo medio, superficie horizontal interna, arcos de 4.000 m de radio; sector poniente, según Pista de Los Cerrillos | Uniforme, **45 metros** desde nivel medio de pista |
| "E" | Bajo riesgo, superficie cónica, franja concéntrica de 2.000 m de ancho, a continuación del área "D" | Rasante desde límite exterior de "D", altura 45 m, pendiente ascendente 5%, hasta **altura final de 145 metros** |

**AR-3 — Áreas de resguardo de Líneas de Alta Tensión**, según Art. 8.4.3 letra "b" del P.R.M.S. y circular ORD. N° 230/2002 (DDU 106) MINVU:

| Tensión (KV) | Distancia mínima a cada costado del eje de la línea (m) | Ancho total (m) |
|---|---|---|
| 66 | 7 | 14 |
| 110 | 10 | 20 |
| 154 | 15 | 30 |
| 220 | 20 | 40 |
| 500 | 27 | 54 |

Aplicación puntual: tendido de 110 KV paralelo al Zanjón de la Aguada, abovedado en la comuna.

**AR-4 — Áreas de resguardo de vías férreas** (Ferrocarril de Circunvalación y Línea de Metro): sin edificaciones sobre las franjas de superficie del túnel abovedado del Metro y de la línea del Ferrocarril de Circunvalación, sin autorización previa. Faja de resguardo de **20 metros a ambos costados** para el Ferrocarril de Circunvalación (Art. 34 Ley de Ferrocarriles; Art. 8.4.1.1 P.R.M.S.).

**Confianza: ALTA.** Las 4 áreas y sus cifras (101,5 m / 45 m / 45-145 m; tabla de 5 filas de tensión; 3 m y 20 m de fajas) son **idénticas** a las transcritas en el decreto hermano N° 515/2009 para las mismas áreas — fuerte validación cruzada (ver §25).

---

## 20. Capítulo VI — Instalación de Torres y Antenas para cualquier tipo de Telecomunicación (Art. 27°-34°) (página 16/DO)

Documentado en forma breve, siguiendo el mismo criterio del decreto hermano N° 515/2009 (no es norma de zona, son condiciones narrativas puntuales).

| Artículo | Contenido |
|---|---|
| Art. 27° | Ámbito: instalación de antenas y torres para radio, TV, telefonía celular y cualquier señal electromagnética; excluye a radioaficionados |
| Art. 28° | Definiciones de "antena", "torre" y "estación de telefonía celular" |
| Art. 29° | Edificaciones asociadas requieren permiso de la D.O.M., sin perjuicio de excepciones del Art. 5.1.2 O.G.U.C. |
| Art. 30° | Debe cumplir línea de edificación vigente y distanciamiento mínimo O.G.U.C. |
| Art. 31° a-f | Autorización MTT/DGAC; distanciamiento **no inferior a 30 metros** en zonas industriales respecto de inmuebles residenciales; autorización municipal específica para vivienda/educación y espacios públicos (**distanciamiento mínimo de 30 metros** en este último caso); instalación preferente sobre mástil en azoteas; prohibición sobre monumentos nacionales/ICH salvo autorización del Consejo de Monumentos Nacionales |
| Art. 32° a-c | Aviso previo a la D.O.M., cumplimiento de distanciamientos del D.S. N° 505/2000 MTT, fotocopia legalizada de autorizaciones |
| Art. 33° | Antenas existentes sin autorización: **plazo de 180 días** para regularizar |
| Art. 34° | Fiscalización por la D.O.M.; **multas de hasta 5 UTM mensuales** |

**Confianza: ALTA.** Las cifras (30 metros ×2, 180 días, 5 UTM) coinciden exactamente con las del decreto hermano N° 515/2009 — el capítulo de antenas no fue modificado entre 2005 y 2009.

---

## 21. Capítulo VII — Vialidad Estructurante (Art. 35°-38°, INCOMPLETO dentro del rango entregado) (página 16/DO)

**Advertencia central de este documento — ver detalle completo en §25.** El material entregado (6 páginas, hasta el pie de página "Página 16") **termina a media disposición de este capítulo**, en el Art. 38°:

| Artículo | Contenido |
|---|---|
| Art. 35° | Las vías públicas del Plan son las actualmente existentes, con calidad de bienes nacionales de uso público; mantienen sus anchos salvo ensanches, prolongaciones o apertura de vías nuevas dispuestos por el Plan |
| Art. 36° | Los perfiles geométricos y estructurales se definen en proyectos de loteo/planos seccionales aprobados por SERVIU, SEREMI MINVU y la Municipalidad, ateniéndose al Manual de Vialidad Urbana Vol. 3 (REDEVU) |
| Art. 37° | Las vías de carácter regional (p. ej. Avda. Norte Sur Jorge Alessandri Rodríguez) quedan sujetas a la Dirección Regional de Vialidad del M.O.P. |
| Art. 38° | Las vías generadas por división predial o loteo se rigen por los artículos 2.3.1 a 2.3.10 y 3.2.5 a 3.2.11 de la O.G.U.C. |

El Art. 38° cierra con una oración gramaticalmente completa ("...y el artículo 3.2.5 al 3.2.11 de la O.G.U.C."), pero el capítulo continúa más allá de este punto (con toda probabilidad un Art. 39° con la tabla de vías, tal como aparece en el decreto hermano N° 515/2009 —no transcrita en ese documento tampoco, por estar fuera de su rango— y luego las disposiciones finales del decreto). **Ninguno de esos elementos posteriores está dentro de las 6 páginas entregadas para este encargo.** No se transcribe contenido inventado más allá de este punto.

**Confianza: ALTA** en lo efectivamente transcrito (Art. 35°-38°, narrativo, sin tabla); **fuera de rango** todo lo posterior.

---

## 22. Tabla comparativa resumen — cuadros de normas urbanísticas de las 14 zonas/áreas

| Zona | Superficie predial | Altura máxima | Coef. Constructibilidad | Ocupación suelo | Agrupamiento | Antejardín mín. | Adosamiento máx. |
|---|---|---|---|---|---|---|---|
| ZU-1 | 0 a 2001+ m² (4 tramos) | Rasante | 1.8 – 3.0 | 0.80 (1-3p) / 0.50 (+3p) | A-P-C | Art.11 | 40% |
| ZU-2 | 0 a 3001+ m² (4 tramos) | Rasante | 1.8 – 2.5 | 0.70 – 0.55 | A-P / A | Art.11 | 40% |
| ZU-3 | 500-1500+ m² (por uso) | Rasante | 1.0 – 2.0 | 0.70 | A | 5 m | 0% |
| ZU-4 | 0 a 1001+ m² (3 tramos) | Rasante | 1.5 – 2.5 | 0.70 – 0.50 | A | 3 m | 40% |
| ZU-5 | 4000 y más | Rasante | 2 | 0.60 | A-P | Art.11 | 40% |
| ZU-6 | Sin valor específico¹ | Sin valor específico¹ | Sin valor específico¹ | Sin valor específico¹ | Sin valor específico¹ | Sin valor específico¹ | Sin valor específico¹ |
| EM-1 | 1000 a 5001+ m² (3 tramos) | Rasante | 2.5 – 3.5 | 0.60 (1-3p) / 0.50 (+3p) | A | Art.11 | 0% |
| EM-2 | 2000 a 5001+ m² (2 tramos) | Rasante | 0.2 – 0.1 | 0.10 – 0.05 (1er piso) | A | Art.11 | --- |
| EM-3 | No divisible | Rasante | 0.05 | 0.05 | A | Art.11 | --- |
| EM-4 | No divisible | Rasante | 0.20 | 0.20 | A | Art.11 | --- |
| EC-1 | Existente | Rasante | 0.2 | 0.1 (1er piso) | A | Art.11 | --- |
| EC-2 | No divisible | Rasante | 0.05 | 0.05 | A | Art.11 | --- |
| EC-3 | No divisible | Rasante | 0.1 | 0.1 | A | Art.11 | --- |
| ICH | Sin valor específico² | Sin valor específico² | Sin valor específico² | Sin valor específico² | Sin valor específico² | Sin valor específico² | Sin valor específico² |

¹ ZU-6 es zona de infraestructura ferroviaria delimitada por deslindes, sin cuadro de edificación por diseño (ver §10).
² ICH remite a las normas de la zona circundante en vez de traer cuadro propio (ver §18).

---

## 23. Verificación de "trampa comuna ajena"

Se revisaron las 6 páginas íntegramente en busca de contenido de otra comuna u otro asunto ajeno mezclado en el material. **Resultado: no se encontró ninguno.** Evidencia:

- Las 6 páginas muestran de forma consistente el mismo encabezado de masthead: "DIARIO OFICIAL DE LA REPUBLICA DE CHILE — Nº 38.323 — Lunes 28 de Noviembre de 2005", sin discontinuidad.
- El contenido fluye de forma lógica y continua: Art. 23° → 24° → 25° → 26° → Capítulo VI → Capítulo VII (Art. 35°-38°), sin saltos ni inserciones de otro instrumento legal.
- Todas las referencias geográficas y de infraestructura citadas son propias y específicas de San Miguel/entorno metropolitano inmediato: Gran Avenida José Miguel Carrera, Avenida Santa Rosa, Llano Subercaseaux, Zanjón de la Aguada, Canal San Joaquín, Hospital Barros Luco, Parque Isabel Riquelme, Estadio El Llano, Ferrocarril de Circunvalación, Aeródromos El Bosque y Los Cerrillos — todos elementos reales y verificables de la comuna y su entorno inmediato (Metropolitana de Santiago).
- Se verificó además que el archivo PDF de origen de este documento (Diario Oficial N° 38.323, 28-nov-2005) es un ejemplar **distinto** del usado para `san_miguel_do515_...md` (Diario Oficial N° 39.326, 31-mar-2009) — dos ediciones distintas del Diario Oficial en años distintos, sin superposición de páginas ni riesgo de mezcla entre ambos documentos.

**No se detectó ninguna "trampa de comuna ajena" dentro del material entregado para este encargo.**

---

## 24. Cruce con los demás documentos de San Miguel ya existentes en este repositorio

Se leyeron los 5 documentos de San Miguel ya presentes en `extraccion_normas/san_miguel/` antes de escribir este documento, específicamente para descartar solapamiento o contradicción de zonificación:

| Documento existente | Decreto / año | Relación con este documento (2401/2005) |
|---|---|---|
| `san_miguel_do515_zonas_em3_em4_restriccion_d_e_pag1-2_11-13.md` | N° 515/2009 | Texto refundido posterior de la misma Ordenanza; EM-4, EC-1 a EC-3, ICH y AR-1 a AR-4 **coinciden en cifras exactamente** con lo aquí transcrito (ver notas cruzadas en cada zona). EM-3 estaba fuera de rango en ese documento y aquí sí se pudo completar. |
| `san_miguel_2371_reclasificacion_zu5_barros_luco.md` | N° 2.371/2009 | Reclasifica un polígono de ZU-1/ZU-2 a ZU-5, remitiendo explícitamente al cuadro de ZU-5 aquí transcrito |
| `san_miguel_3164_zu2_disposicion_especial.md` | N° 3.164/2014 | Agrega una disposición especial puntual a ZU-2 (aquí transcrita en su versión base, §6) |
| `san_miguel_dex3162_zona_zu4prima_industrial_mixta_pag2-5.md` | N° 3.162/2014 | Crea zona derivada ZU-4' sobre un polígono de la antigua ZU-2, sin modificar la ZU-4 aquí transcrita |
| `san_miguel_dex3163_zona_zu2prima_residencial_renovacion_pag2-5.md` | N° 3.163/2014 | Crea zona derivada ZU-2' sobre parte de EC-1, eliminando "Complejo Deportivo Tatio" de la lista de EC-1 aquí transcrita (§15) |

**Conclusión:** no hay solapamiento problemático ni contradicción. Los 5 documentos existentes son todos modificaciones/reclasificaciones **posteriores** que presuponen y remiten a la zonificación original que este documento transcribe por primera vez en este repositorio (Decreto 2401/2005, el "NUEVO PRC" fundacional). La consistencia numérica encontrada entre este documento y el decreto hermano 515/2009 —para 8 de las 14 zonas— es una fuerte confirmación cruzada de la exactitud de ambas transcripciones, no una señal de mezcla indebida.

---

## 25. Discrepancias y hallazgos respecto de la nota de Fase 3

1. **Conteo de zonas — discrepancia mayor.** Fase 3 anticipaba "ZU-1 a ZU-5, EC-1 a EC-3" (8 zonas). El conteo directo contra la imagen de la página 06 (Art. 25°) da **14 códigos de zona/área**: ZU-1 a **ZU-6** (6, no 5 — falta ZU-6 Ferroviaria en la nota), **EM-1 a EM-4** (4 zonas/áreas completas, no mencionadas en absoluto por Fase 3), EC-1 a EC-3 (3, correctamente anticipadas) y **ICH** (1, no mencionada). Se transcribieron las 14 en este documento.
2. **Página 11 (PDF) / Página 16 (DO) — discrepancia mayor.** Fase 3 describía esta página como "tabla de vialidad (calles/anchos) + artículos finales (vigencia, derogación Dec.916/1951, publicación)". La imagen real muestra: cierre de AR-1, AR-2, AR-3 (con tabla de tensión eléctrica, no de calles), AR-4, el Capítulo VI completo (Antenas, Art. 27°-34°) y el Capítulo VII **apenas iniciado** (Vialidad Estructurante, Art. 35°-38°, puramente narrativo). **No hay tabla de calles/anchos ni artículos finales de vigencia/derogación/publicación en ninguna de las 6 páginas entregadas.** Se buscó explícitamente "916", "1951", "derogación" y "vigencia" en el `.txt` de las 6 páginas: "1951", "derogación" y "vigencia" no aparecen en ningún punto; "916" aparece una sola vez, pero como parte de "Ley Nº **18.916**" (Código Aeronáutico, citada en AR-2 y en el Art. 27° de antenas) — sin relación alguna con un eventual "Decreto 916/1951". El documento se corta a media disposición del Capítulo VII, mucho antes de llegar a ese contenido — de existir, estaría en páginas posteriores a la 11 (PDF), no entregadas para este encargo. Se documenta esto como corrección explícita a Fase 3, sin inventar el contenido faltante.
3. **Número de decreto "2401" no verificable dentro del rango entregado.** Las 6 páginas (Cap. IV en adelante) no incluyen el encabezado con "vistos" y número de decreto (que normalmente figura en la página 1 del PDF, fuera de este encargo). Se confía en el número aportado por el encargo, pero no se pudo confirmar de forma independiente con este material — a diferencia de la fecha y el número de edición del Diario Oficial (Nº 38.323, 28-nov-2005), que sí están visibles y se confirmaron en las 6 páginas.
4. **Confirmado: el `.txt` tiene el mismo problema de desorden de columnas ya advertido para el documento hermano 515.** Ver ejemplo concreto en §0 (ZU-2 antes que ZU-1 en el `.txt` crudo). Resuelto leyendo las imágenes directamente.
5. **Hallazgo no anticipado por Fase 3 — fuerte validación cruzada con el Decreto 515/2009.** 8 de las 14 zonas de este documento (EM-3, EM-4, EC-1, EC-2, EC-3, ICH, y las 4 áreas AR-1 a AR-4, más el capítulo de antenas) tienen cifras **idénticas** en ambos decretos (ver §24), lo cual es un fuerte indicio de transcripción correcta en ambos documentos, no una contradicción.
6. **Hallazgo no anticipado por Fase 3 — la carpeta `zoom/` de este mismo directorio de render contiene material de otras comunas/documentos**, con nombres de archivo que podrían confundirse con crops de este documento (ver advertencia detallada en §0). Se dejó constancia explícita para evitar que una fase posterior la use por error.
7. **Confirmado, sin discrepancia:** "p6 Cap.IV Tipología y Escalas Equipamiento + inicio Cap.V" (Fase 3) — correcto. "p6-10 desarrollo de cada zona ... en TEXTO extraíble" (Fase 3) — correcto: es texto nativo, no escaneado, de alta fidelidad.
8. **Erratas y variaciones tipográficas `[sic]` consolidadas** (detalle en cada zona): "calificadas" en vez de "calificados" (recurrente, ZU-1/ZU-2/ZU-3/ZU-4); "4. ÁREAS VERDES ." con punto suelto (ZU-1); "Aquellos uso definidos" sin "s" (ZU-4); "n o indicados" con espacio suelto (EM-1); "USOS PERMITIDOS :" con espacio antes de los dos puntos (ZU-3); leyenda "A=Aislado" sin asterisco (EC-2, igual que en 515/2009); "ZONA EM-2" en el cuerpo vs. "Area EM-2" en el Art. 25° (inconsistencia de nomenclatura); "ÁREAS VERDES COMUNALES PROYECTADAS" (cuerpo) vs. "ÁREAS VERDES PROYECTADAS COMUNALES" (Art. 25°) para EC-3; alternancia "no indicados" (ZU-5, EM-2, EM-3, EC-1, EC-2) vs. "no incluidos" (EC-3, ICH) en el catch-all de usos prohibidos.

---

## 26. Notas finales de verificación

**Confianza global: ALTA.** Las 14 zonas/áreas de la lista del Art. 25° fueron localizadas y transcritas completas (usos permitidos, usos prohibidos, cuadro de normas urbanísticas donde corresponde, disposiciones complementarias), leyendo directamente las 6 imágenes a 250 dpi y verificando contra el `.txt` de apoyo carácter por carácter en cada caso, reordenando según el layout real de columnas de cada página. No se encontró ningún valor ilegible; no fue necesario usar "Dato no determinable" en ningún campo.

**Confianza por página/sección:**

| Página (DO) | Contenido | Confianza |
|---|---|---|
| 11 | Cap. IV (Art. 23°-24°), Art. 25° (listado de 14 zonas), reglas de límites, remisión a AR-1/AR-4 | Alta |
| 12 | ZU-1 completa, ZU-2 completa, inicio ZU-3 | Alta |
| 13 | ZU-3 completa, ZU-4 (usos+cuadro, inicio disposiciones) | Alta |
| 14 | ZU-4 disposiciones (cont.), ZU-5 completa, ZU-6 completa, EM-1 (usos+cuadro+disposiciones), EM-2 completa, inicio EM-3 | Alta |
| 15 | EM-3 (cont.), EM-4 completa, EC-1 completa, EC-2 completa, EC-3 completa, ICH completa, inicio Art. 26° AR-1 | Alta |
| 16 | AR-1 (cont.), AR-2, AR-3, AR-4 completas, Cap. VI completo, Cap. VII Art. 35°-38° (incompleto, sin tabla de vías ni artículos finales) | Alta en lo transcrito; el resto del Cap. VII y los artículos finales del decreto están **fuera de rango**, no inventados |

**No se inventó ningún valor.** Todo campo sin dato se marcó "Sin valor específico en la fuente" con motivo de diseño explicado (ZU-6, ICH); no se usó "Dato no determinable" en ningún punto porque no hubo ilegibilidad real en las 6 páginas entregadas. La discrepancia de conteo de zonas (§25.1) y la discrepancia de contenido de la página 11/PDF (§25.2) se documentan explícitamente como correcciones a la nota de Fase 3, verificadas por lectura directa de imagen, no asumidas.
