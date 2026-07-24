# Ordenanza Local PRC Quilpué (Decreto 2732, 2019) — Capítulo 5 "Normas Urbanísticas", Artículo 5.1 "Usos de Suelo y Normas de Edificación", 53 zonas/subzonas (ZR1-ZR10, ZRM1-ZRM2, ZM1-ZM3, ZE1-ZE4, C1/C1-a, C2-C6/C4-a, F, SC, ET, ETR, EI/EI-a, E, EDR/EDR-a, EE, ES/ES1, EP, CE, PT, PI, INT, INS, AVC1-AVC4, AVI1-AVI4)

**Fuente:** Decreto 2732 (2019), "Aprueba actualización al Plan Regulador Comunal de Quilpué", publicado en el Diario Oficial de la República de Chile, Núm. 42.413, viernes 26 de julio de 2019. Archivo: `Ordenanzas ordenadas/OCR ok/quilpue_2732_aprueba_actualizacion_al_plan_regulador_comunal_de_quilpue__2732.pdf` (79 páginas totales).

**Rango de páginas de este documento:** páginas 28 a 51 de 79 (numeración impresa "Página X de 79" en el encabezado de cada página, coincide con la numeración del PDF). Cubre el Capítulo 5 completo, Artículo 5.1 íntegro (todas las 53 zonas y subzonas de edificación del plan, desde el listado de "ZONAS HABITACIONALES MIXTAS" en pág. 28 hasta el cierre de la Zona AVI4 en pág. 51), y se detiene exactamente donde comienza el Artículo 5.2 "Incentivos normativos" (mismo párrafo introductorio, en prosa, al final de la página 51). No incluye la página 52 (tablas de incentivos normativos por zona, fuera del alcance de este encargo).

**Material usado:** imágenes PNG a 250 dpi (`pag-28.png` … `pag-51.png`, 2125×3250 px cada una, generadas con `pdftoppm -r 250`) y texto plano de apoyo (`pdftotext -layout`) para el rango. Se hicieron recortes con zoom (1,3×-3×, con `PIL`, varios con `autocontrast`) sobre las celdas estructuralmente dudosas (filas ausentes, encabezados con erratas, valores atípicos) para verificar antes de transcribir.

**Confirmación de la "trampa" de Fase 3 — tablas como imagen:** se extrajo el `.txt` (pdftotext) del rango completo 28-51 y se filtró todo el texto repetitivo de pie/encabezado de página (Diario Oficial, CVE, firma electrónica). El resultado es que **el 100% del contenido normativo de las 53 zonas (todas las tablas de usos de suelo y de condiciones de edificación) es imagen pura — cero texto extraíble** salvo tres excepciones puntuales que sí son texto real: (1) el párrafo introductorio del Art. 5.1 en la página 28 ("Las normas urbanísticas aplicables a cada zona..."), (2) la nota de la Sub-Zona C1-a sobre el artículo 2.1.36 de la OGUC (página 38), y (3) el párrafo introductorio completo del Art. 5.2 "Incentivos normativos" en la página 51 (fuera de este rango de zonas, pero confirma dónde termina el Art. 5.1). Todos los valores numéricos y textos de tabla transcritos a continuación provienen **exclusivamente de lectura visual del render**, tal como anticipaba la nota de Fase 3.

---

## 0. Verificación del listado completo de zonas (paso más importante del encargo)

El documento **no trae un listado-índice explícito** de todos los códigos de zona antes de las tablas (a diferencia de otros PRC del corpus que sí traen un "cuadro de zonificación" separado) — el Art. 5.1 pasa directo del párrafo introductorio (pág. 28) a la primera tabla de zona (ZR1). Por lo tanto, siguiendo la instrucción del encargo para este caso, **se enumeraron las 53 zonas y subzonas a medida que aparecieron sus tablas**, página por página, y se verificó al cierre que no hubiera saltos de numeración ni de lógica interna. Resultado:

- **Secuencia ZR1→ZR10:** correlativa, sin saltos (verificado uno por uno, págs. 28-33).
- **Secuencia ZRM1→ZRM2, ZM1→ZM3:** correlativa (págs. 33-35).
- **Secuencia ZE1→ZE4:** correlativa, las 4 ligadas a poblaciones con nombre propio (Carozzi, Wiegand, California, Las Rosas) — nombres reales de sectores de Quilpué, confirma que el documento corresponde a la comuna correcta (págs. 36-38).
- **Secuencia C1(+C1-a)→C6(+C4-a):** correlativa (págs. 38-42).
- **F, SC:** sin numeración correlativa propia, zonas únicas de su tipo (págs. 42-43).
- **ET, ETR:** correlativa (pág. 43-44).
- **EI(+EI-a):** correlativa (pág. 44-45).
- **E, EDR(+EDR-a), EE, ES(+ES1), EP, CE:** zonas de equipamiento local/salud/deporte, sin numeración correlativa entre sí — cada código es único (págs. 45-48).
- **PT, PI:** correlativa dentro de "ZONAS DE ACTIVIDADES PRODUCTIVAS" (págs. 48-49).
- **INT, INS:** correlativa dentro de "ZONAS DE INFRAESTRUCTURA" (pág. 49).
- **AVC1→AVC4:** correlativa (pág. 50-51).
- **AVI1→AVI4:** correlativa — **última zona del Art. 5.1**, inmediatamente después comienza el Art. 5.2 "Incentivos normativos" en la misma página 51 (pág. 51).

**No se encontró ningún salto de numeración sospechoso** (p. ej. ZR2 seguido de ZR4 sin ZR3) en ninguna de las familias de zonas. La pista de `nota_fase3` — "ZR1/ZR2 ... hasta AVI4" — **se confirma exactamente**: la primera zona del rango es ZR1 (pág. 28, primera tabla después del párrafo introductorio) y la última es AVI4 (pág. 51, justo antes del Art. 5.2). Entre ambas hay **53 códigos de zona/subzona**, agrupados en 6 categorías con banner propio (gris, ancho de página):

1. **"ZONAS HABITACIONALES MIXTAS"** (banner en pág. 28, antes de ZR1) → ZR1-ZR10, ZRM1-ZRM2, ZM1-ZM3, ZE1-ZE4 (19 zonas).
2. **"ZONAS DE EQUIPAMIENTO PREFERENTE"** (banner en pág. 38, antes de C1) → C1, C1-a, C2, C3, C4, C4-a, C5, C6, F, SC, ET, ETR, EI, EI-a, E, EDR, EDR-a, EE, ES, ES1, EP, CE (22 zonas/subzonas).
3. **"ZONAS DE ACTIVIDADES PRODUCTIVAS"** (banner en pág. 48, antes de PT) → PT, PI (2 zonas).
4. **"ZONAS DE INFRAESTRUCTURA"** (banner en pág. 49, antes de INT) → INT, INS (2 zonas).
5. **"ÁREA VERDE Y ESPACIOS PÚBLICOS"** (banner en pág. 50, antes de AVC1) → AVC1-AVC4, AVI1-AVI4 (8 zonas).

19+22+2+2+8 = **53 zonas y subzonas transcritas**, coincidente con el conteo hecho al recorrer el documento.

---

## 1. Convenciones usadas en este documento

- **"No especificado":** para parámetros que la fuente deja genuinamente sin llenar en una fila que sí existe en la tabla (no se usó casi nunca — la fuente casi siempre escribe explícitamente "No aplica" en vez de dejar la celda en blanco).
- **"No aplica":** transcripción literal cuando la fuente escribe exactamente esa frase (típicamente en la columna "Residencial" cuando la zona no tiene uso residencial, o para Densidad bruta máxima de la columna "Otros usos").
- **Fila ausente:** cuando una zona no trae una fila que sí traen otras zonas de su misma familia (p. ej. sin "Actividades Productivas", sin "Infraestructura", sin "Científico"), se indica explícitamente "Fila ausente en la fuente" en vez de inventar un valor.
- **`[sic]`:** marca erratas o redacciones atípicas de la fuente (duplicaciones, discordancias de género/número, encabezados mal escritos), preservadas tal cual, sin corregir. Todas están además verificadas con zoom cuando la errata es estructural (no solo ortográfica).
- **Coma y punto decimal/millares:** se preserva tal como aparece en la fuente — la fuente usa **punto como separador de miles** ("2.500", "20.000") y **coma o punto indistintamente como separador decimal** (aparecen tanto "0,6" como "0.6" en distintas tablas; se transcribe exactamente el símbolo usado en cada celda).
- **Distanciamiento a medianeros:** la inmensa mayoría de las zonas remiten a "Art. 2.6.3 de la OGUC" (sin cifra propia). Un grupo pequeño de zonas de infraestructura/productivas (CE, PT, PI, INT, INS) **sí fija un valor numérico directo** en metros — se transcribe la diferencia explícitamente en cada caso, es un hallazgo relevante documentado en la sección 9.
- **Estructura estándar de "a. Usos de suelo":** columnas "Uso de Suelo" (categoría gruesa: RESIDENCIAL, EQUIPAMIENTO, ACTIVIDADES PRODUCTIVAS, INFRAESTRUCTURA, ESPACIO PÚBLICO, ÁREA VERDE) / "Destino o Clase" (subcategoría) / "Actividades permitidas". Cierra siempre con la fila fija "USOS DE SUELO PROHIBIDOS: TODOS LOS NO SEÑALADOS COMO PERMITIDOS". El conjunto de sub-filas presentes **varía mucho por zona** — se documenta cada ausencia notable.
- **Estructura estándar de "b. Normas urbanísticas":** columnas "Condiciones de edificación" / "Residencial" / "Otros usos" (algunas zonas sin uso residencial colapsan a una sola columna, p. ej. CE, PT, PI, INT, INS, AVC1-4, AVI1-4 — se indica expresamente cuando ocurre). Cuando el valor es único para ambas columnas se transcribe una sola vez con nota "(valor único para toda la zona)".

---

## 2. Correspondencia de páginas — dónde vive cada zona

| Página | Zonas cuyo contenido aparece (título y/o tablas) |
|---|---|
| 28 | Banner "ZONAS HABITACIONALES MIXTAS"; **ZR1** completa; **ZR2** usos de suelo (edificación en pág. 29) |
| 29 | ZR2 edificación; **ZR3** completa; **ZR4** usos de suelo |
| 30 | ZR4 edificación; **ZR5** completa; **ZR6** usos de suelo |
| 31 | ZR6 edificación; **ZR7** completa; **ZR8** usos de suelo |
| 32 | ZR8 edificación; **ZR9** completa; **ZR10** usos de suelo |
| 33 | ZR10 edificación; **ZRM1** completa; **ZRM2** usos de suelo |
| 34 | ZRM2 edificación; **ZM1** completa |
| 35 | **ZM2** completa; **ZM3** completa |
| 36 | **ZE1** completa; **ZE2** usos de suelo |
| 37 | ZE2 edificación; **ZE3** completa; **ZE4** usos de suelo |
| 38 | ZE4 edificación; Banner "ZONAS DE EQUIPAMIENTO PREFERENTE"; **C1** completa; **Sub-Zona C1-a** (nota OGUC 2.1.36 + usos de suelo, inicio) |
| 39 | Sub-Zona C1-a (cont. + edificación); **C2** completa |
| 40 | **C3** completa; **C4** usos de suelo |
| 41 | C4 edificación; **C4-a** completa; **C5** usos de suelo (inicio) |
| 42 | C5 (cont. + edificación); **C6** completa; **Zona F** usos de suelo (inicio) |
| 43 | Zona F (cont. + edificación); **SC** completa; **ET** usos de suelo (inicio) |
| 44 | ET (cont. + edificación); **ETR** completa; **EI** usos de suelo (inicio) |
| 45 | EI (cont. + edificación); **EI-a** completa; **Zona E** usos de suelo (inicio) |
| 46 | Zona E (cont. + edificación inicio); **EDR** completa; **Sub-Zona EDR-A** completa; **Zona EE** usos de suelo |
| 47 | EE edificación; **ES** completa; **ES1** completa |
| 48 | **EP** completa; **CE** completa; Banner "ZONAS DE ACTIVIDADES PRODUCTIVAS"; **PT** usos de suelo |
| 49 | PT edificación; **PI** completa; Banner "ZONAS DE INFRAESTRUCTURA"; **INT** completa; **INS** completa |
| 50 | Banner "ÁREA VERDE Y ESPACIOS PÚBLICOS"; **AVC1** completa; **AVC2** completa; **AVC3** completa; **AVC4** usos de suelo |
| 51 | AVC4 edificación; **AVI1** completa; **AVI2** completa; **AVI3** completa; **AVI4** completa; inicio Art. 5.2 "Incentivos normativos" (fuera de alcance) |

**Verificación de cortes de página:** en ningún caso una tabla se corta a mitad de una cifra — el corte de página siempre cae en el borde de una fila completa o entre el título de una zona y el inicio de su tabla, igual que en el resto del corpus.

---

# BANNER: "ZONAS HABITACIONALES MIXTAS" (pág. 28)

## 3. ZR1 — Habitacional, densidad alta, en altura (pág. 28)

### a. Usos de suelo

| Uso de suelo | Destino/Clase | Actividades permitidas |
|---|---|---|
| RESIDENCIAL | Vivienda | Vivienda. |
| RESIDENCIAL | Hospedaje | Hotel, edificaciones o locales destinados al hospedaje, pensiones, internados de estudiantes, albergues, moteles. |
| RESIDENCIAL | Hogares de acogida | Hogares de acogida en general, hogares de estadía para adultos mayores u hogares de ancianos. |
| EQUIPAMIENTO | Comercio | Supermercados, locales comerciales, restaurantes, cafeterías, salones de té, fuentes de soda, pubs. |
| EQUIPAMIENTO | Culto y Cultura | Templos, centros culturales, museos, bibliotecas, galerías de arte, centros de difusión o exposiciones. |
| EQUIPAMIENTO | Deporte | Gimnasios, saunas, baños turcos, centros y clubes deportivos, multicanchas, piscinas. |
| EQUIPAMIENTO | Educación | Establecimientos de educación pre básica, básica, media, técnica; establecimientos de educación especial, escuelas de lenguaje, centros de capacitación, academias, institutos, jardines infantiles, salas cuna. |
| EQUIPAMIENTO | Salud | Hospitales, clínicas, policlínicos, consultorios, centros médicos, postas, centros de rehabilitación de salud. |
| EQUIPAMIENTO | Seguridad | Unidades policiales, cuarteles de bomberos. |
| EQUIPAMIENTO | Servicios | Servicios públicos y privados de todo tipo. Servicios artesanales y profesionales. Oficinas, centros médicos, centros dentales, notarías, centros de pago, centros de belleza, peluquerías, lavanderías, lavasecos, cibercafés, fotocopiadoras, servicios informáticos. |
| EQUIPAMIENTO | Social | Sedes de todo tipo de organización social. |
| ACTIVIDADES PRODUCTIVAS | — | Talleres. |
| INFRAESTRUCTURA | Transporte | Terminales de vehículos de locomoción colectiva. |
| ESPACIO PÚBLICO | — | Vialidad, parques y plazas. |
| ÁREA VERDE | — | Parques y plazas. |
| **USOS DE SUELO PROHIBIDOS** | | TODOS LOS NO SEÑALADOS COMO PERMITIDOS |

### b. Normas urbanísticas (condiciones de edificación)

| Parámetro | Residencial | Otros usos |
|---|---|---|
| Superficie de subdivisión predial mínima (m²) | 1000 (valor único) | 1000 (valor único) |
| Densidad bruta máxima (hab./ha) | 450 | No aplica |
| Coeficiente de ocupación del suelo | 0,25 | 0,4 |
| Coeficiente de constructibilidad | 1,3 | 1,6 |
| Sistema de agrupamiento | Aislado, pareado (valor único) | Aislado, pareado (valor único) |
| Altura máxima de la edificación | 8 pisos o 28 m (valor único) | 8 pisos o 28 m (valor único) |
| Distanciamiento a medianeros | Art. 2.6.3 de la OGUC (valor único) | Art. 2.6.3 de la OGUC (valor único) |
| Antejardín | 5 metros (valor único) | 5 metros (valor único) |
| Adosamiento | No se permite (valor único) | No se permite (valor único) |

---

## 4. ZR2 — Habitacional, densidad media-alta, mediana altura (pág. 28-29)

### a. Usos de suelo

| Uso de suelo | Destino/Clase | Actividades permitidas |
|---|---|---|
| RESIDENCIAL | Vivienda | Vivienda. |
| RESIDENCIAL | Hospedaje | Hotel, edificaciones o locales destinados al hospedaje, pensiones, internados de estudiantes, albergues, cabañas, moteles. |
| RESIDENCIAL | Hogares de acogida | Hogares de acogida en general, hogares de estadía para adultos mayores u hogares de ancianos. |
| EQUIPAMIENTO | Comercio | Locales comerciales, restaurantes, cafeterías, salones de té, fuentes de soda, pubs. |
| EQUIPAMIENTO | Culto y Cultura | Parroquias, centros culturales, museos, bibliotecas, galerías de arte, centros de difusión o exposiciones. |
| EQUIPAMIENTO | Deporte | Gimnasios, saunas, baños turcos, centros y clubes deportivos, multicanchas, piscinas. |
| EQUIPAMIENTO | Educación | Establecimientos de educación pre básica, básica, media, técnica; establecimientos de educación especial, escuelas de lenguaje, centros de capacitación, academias, institutos, jardines infantiles, salas cuna. |
| EQUIPAMIENTO | Salud | Policlínicos, consultorios, centros médicos, postas, centros de rehabilitación de salud. |
| EQUIPAMIENTO | Seguridad | Unidades policiales, cuarteles de bomberos. |
| EQUIPAMIENTO | Servicios | Servicios públicos y privados de todo tipo. Servicios artesanales y profesionales. Oficinas, centros médicos, centros dentales, notarías, centros de pago, centros de belleza, peluquerías, lavanderías, lavasecos, cibercafés, fotocopiadoras, servicios informáticos. |
| EQUIPAMIENTO | Social | Sedes de todo tipo de organización social. |
| INFRAESTRUCTURA | Transporte | Terminales de vehículos de locomoción colectiva. |
| ESPACIO PÚBLICO | — | Vialidad, parques y plazas. |
| ÁREA VERDE | — | Parques y plazas. |
| **USOS DE SUELO PROHIBIDOS** | | TODOS LOS NO SEÑALADOS COMO PERMITIDOS |

**Nota:** sin fila "ACTIVIDADES PRODUCTIVAS" (fila ausente en la fuente) — a diferencia de ZR1, que sí la trae ("Talleres").

### b. Normas urbanísticas

| Parámetro | Residencial | Otros usos |
|---|---|---|
| Superficie de subdivisión predial mínima (m²) | 1000 (valor único) | 1000 (valor único) |
| Densidad bruta máxima (hab./ha) | 340 | No aplica |
| Coeficiente de ocupación del suelo | 0,3 | 0,5 |
| Coeficiente de constructibilidad | 1,2 | 1,5 |
| Sistema de agrupamiento | Aislado, pareado (valor único) | Aislado, pareado (valor único) |
| Altura máxima de la edificación | 5 pisos o 17,5 m (valor único) | 5 pisos o 17,5 m (valor único) |
| Distanciamiento a medianeros | Art. 2.6.3 de la OGUC (valor único) | Art. 2.6.3 de la OGUC (valor único) |
| Antejardín | 5 metros (valor único) | 5 metros (valor único) |
| Adosamiento | No se permite (valor único) | No se permite (valor único) |

---

## 5. ZR3 — Habitacional, densidad media, mediana altura (pág. 29)

### a. Usos de suelo

| Uso de suelo | Destino/Clase | Actividades permitidas |
|---|---|---|
| RESIDENCIAL | Vivienda | Vivienda. |
| RESIDENCIAL | Hospedaje | Locales destinados al hospedaje, pensiones, internados de estudiantes. |
| RESIDENCIAL | Hogares de acogida | Hogares de acogida en general, hogares de estadía para adultos mayores u hogares de ancianos. |
| EQUIPAMIENTO | Comercio | Locales comerciales, restaurantes, cafeterías, salones de té, fuentes de soda. |
| EQUIPAMIENTO | Culto y Cultura | Parroquias, centros culturales, bibliotecas, auditorios, galerías de arte. |
| EQUIPAMIENTO | Deporte | Gimnasios, saunas, baños turcos, centros y clubes deportivos, multicanchas, piscinas. |
| EQUIPAMIENTO | Educación | Establecimientos de educación pre básica, básica, media, técnica; establecimientos de educación especial, escuelas de lenguaje, centros de capacitación, academias, institutos, jardines infantiles, salas cuna. |
| EQUIPAMIENTO | Salud | Policlínicos, centros de salud, consultorios, postas, centros de rehabilitación de salud. |
| EQUIPAMIENTO | Seguridad | Unidades policiales, cuarteles de bomberos. |
| EQUIPAMIENTO | Servicios | Servicios públicos y privados de todo tipo. Servicios artesanales y profesionales. Oficinas, centros médicos, centros dentales, notarías, centros de pago, centros de belleza, peluquerías, lavanderías, lavasecos, cibercafés, fotocopiadoras, servicios informáticos. |
| EQUIPAMIENTO | Social | Sedes de todo tipo de organización social. |
| INFRAESTRUCTURA | Transporte | Terminales de vehículos de locomoción colectiva. |
| ESPACIO PÚBLICO | — | Vialidad, parques y plazas. |
| ÁREA VERDE | — | Parques y plazas. |
| **USOS DE SUELO PROHIBIDOS** | | TODOS LOS NO SEÑALADOS COMO PERMITIDOS |

### b. Normas urbanísticas

| Parámetro | Residencial | Otros usos |
|---|---|---|
| Superficie de subdivisión predial mínima (m²) | 800 (valor único) | 800 (valor único) |
| Densidad bruta máxima (hab./ha) | 200 | No aplica |
| Coeficiente de ocupación del suelo | 0,5 | 0,5 |
| Coeficiente de constructibilidad | 1,5 | 1,9 |
| Sistema de agrupamiento | Aislado, pareado (valor único) | Aislado, pareado (valor único) |
| Altura máxima de la edificación | 4 pisos o 14 m (valor único) | 4 pisos o 14 m (valor único) |
| Distanciamiento a medianeros | Art. 2.6.3 de la OGUC (valor único) | Art. 2.6.3 de la OGUC (valor único) |
| Antejardín | 5 metros (valor único) | 5 metros (valor único) |
| Adosamiento | No se permite (valor único) | No se permite (valor único) |

---

## 6. ZR4 — Habitacional, densidad media, baja altura (pág. 29-30)

### a. Usos de suelo

| Uso de suelo | Destino/Clase | Actividades permitidas |
|---|---|---|
| RESIDENCIAL | Vivienda | Vivienda. |
| RESIDENCIAL | Hospedaje | Locales destinados al hospedaje, pensiones, internados de estudiantes. |
| RESIDENCIAL | Hogares de acogida | Hogares de acogida en general, hogares de estadía para adultos mayores u hogares de ancianos. |
| EQUIPAMIENTO | Comercio | Locales comerciales, restaurantes, cafeterías, salones de té, fuentes de soda. |
| EQUIPAMIENTO | Culto y Cultura | Parroquias, centros culturales, bibliotecas, auditorios, galerías de arte. |
| EQUIPAMIENTO | Deporte | Gimnasios, centros y clubes deportivos, multicanchas. |
| EQUIPAMIENTO | Educación | Establecimientos de educación pre básica, básica, media, técnica; establecimientos de educación especial, escuelas de lenguaje, centros de capacitación, academias, institutos, jardines infantiles, salas cuna. |
| EQUIPAMIENTO | Salud | Policlínicos, consultorios, centros médicos, postas, centros de rehabilitación de salud. |
| EQUIPAMIENTO | Seguridad | Unidades policiales, cuarteles de bomberos. |
| EQUIPAMIENTO | Servicios | Servicios públicos y privados de todo tipo. Servicios artesanales y profesionales. Oficinas, centros médicos, centros dentales, notarías, centros de pago, centros de belleza, peluquerías, lavanderías, lavasecos, cibercafés, fotocopiadoras, servicios informáticos. |
| EQUIPAMIENTO | Social | Sedes de todo tipo de organización social. |
| INFRAESTRUCTURA | Transporte | Terminales de vehículos de locomoción colectiva. |
| ESPACIO PÚBLICO | — | Vialidad y plazas. |
| ÁREA VERDE | — | Plazas. |
| **USOS DE SUELO PROHIBIDOS** | | TODOS LOS NO SEÑALADOS COMO PERMITIDOS |

**Nota:** Deporte se reduce (sin saunas/baños turcos/piscinas respecto de ZR3); Espacio Público y Área Verde se reducen (sin "parques") — patrón que se repite en ZR5, ZR6, ZR7.

### b. Normas urbanísticas

| Parámetro | Residencial | Otros usos |
|---|---|---|
| Superficie de subdivisión predial mínima (m²) | 250 (valor único) | 250 (valor único) |
| Densidad bruta máxima (hab./ha) | 110 | No aplica |
| Coeficiente de ocupación del suelo | 0,6 | 0,6 |
| Coeficiente de constructibilidad | 1,0 | 1,0 |
| Sistema de agrupamiento | Aislado, pareado, continuo (valor único) | Aislado, pareado, continuo (valor único) |
| Altura máxima de la edificación | 2 pisos o 7 m (valor único) | 2 pisos o 7 m (valor único) |
| Distanciamiento a medianeros | Art. 2.6.3 de la OGUC (valor único) | Art. 2.6.3 de la OGUC (valor único) |
| Antejardín | 3 metros (valor único) | 3 metros (valor único) |
| Adosamiento | Se permite (valor único) | Se permite (valor único) |

---

## 7. ZR5 — Habitacional, densidad media, baja altura (pág. 30)

### a. Usos de suelo

Idéntica a ZR4 (verificado, mismo texto exacto en todas las filas: Vivienda/Hospedaje/Hogares de acogida, Comercio, Culto y Cultura, Deporte reducido, Educación, Salud, Seguridad, Servicios, Social, Infraestructura/Transporte, Espacio Público "Vialidad y plazas", Área Verde "Plazas").

| Uso de suelo | Destino/Clase | Actividades permitidas |
|---|---|---|
| RESIDENCIAL | Vivienda | Vivienda. |
| RESIDENCIAL | Hospedaje | Locales destinados al hospedaje, pensiones, internados de estudiantes. |
| RESIDENCIAL | Hogares de acogida | Hogares de acogida en general, hogares de estadía para adultos mayores u hogares de ancianos. |
| EQUIPAMIENTO | Comercio | Locales comerciales, restaurantes, cafeterías, salones de té, fuentes de soda. |
| EQUIPAMIENTO | Culto y Cultura | Parroquias, centros culturales, bibliotecas, auditorios, galerías de arte. |
| EQUIPAMIENTO | Deporte | Gimnasios, centros y clubes deportivos, multicanchas. |
| EQUIPAMIENTO | Educación | Establecimientos de educación pre básica, básica, media, técnica; establecimientos de educación especial, escuelas de lenguaje, centros de capacitación, academias, institutos, jardines infantiles, salas cuna. |
| EQUIPAMIENTO | Salud | Policlínicos, consultorios, centros médicos, postas, centros de rehabilitación de salud. |
| EQUIPAMIENTO | Seguridad | Unidades policiales, cuarteles de bomberos. |
| EQUIPAMIENTO | Servicios | Servicios públicos y privados de todo tipo. Servicios artesanales y profesionales. Oficinas, centros médicos, centros dentales, notarías, centros de pago, centros de belleza, peluquerías, lavanderías, lavasecos, cibercafés, fotocopiadoras, servicios informáticos. |
| EQUIPAMIENTO | Social | Sedes de todo tipo de organización social. |
| INFRAESTRUCTURA | Transporte | Terminales de vehículos de locomoción colectiva. |
| ESPACIO PÚBLICO | — | Vialidad y plazas. |
| ÁREA VERDE | — | Plazas. |
| **USOS DE SUELO PROHIBIDOS** | | TODOS LOS NO SEÑALADOS COMO PERMITIDOS |

### b. Normas urbanísticas

| Parámetro | Residencial | Otros usos |
|---|---|---|
| Superficie de subdivisión predial mínima (m²) | 400 (valor único) | 400 (valor único) |
| Densidad bruta máxima (hab./ha) | 85 | No aplica |
| Coeficiente de ocupación del suelo | 0,5 | 0,5 |
| Coeficiente de constructibilidad | 0,8 | 1,0 |
| Sistema de agrupamiento | Aislado, pareado, continuo (valor único) | Aislado, pareado, continuo (valor único) |
| Altura máxima de la edificación | 2 pisos o 7 m (valor único) | 2 pisos o 7 m (valor único) |
| Distanciamiento a medianeros | Art. 2.6.3 de la OGUC (valor único) | Art. 2.6.3 de la OGUC (valor único) |
| Antejardín | 3 metros (valor único) | 3 metros (valor único) |
| Adosamiento | Se permite (valor único) | Se permite (valor único) |

---

## 8. ZR6 — Habitacional, densidad media, baja altura (pág. 30-31)

### a. Usos de suelo

Igual patrón que ZR4/ZR5, salvo la fila Social que dice "organizaciones sociales" (plural) en vez de "organización social" (singular) — variante menor de redacción, preservada tal cual.

| Uso de suelo | Destino/Clase | Actividades permitidas |
|---|---|---|
| RESIDENCIAL | Vivienda | Vivienda. |
| RESIDENCIAL | Hospedaje | Locales destinados al hospedaje, pensiones, internados de estudiantes. |
| RESIDENCIAL | Hogares de acogida | Hogares de acogida en general, hogares de estadía para adultos mayores u hogares de ancianos. |
| EQUIPAMIENTO | Comercio | Locales comerciales, restaurantes, cafeterías, salones de té, fuentes de soda. |
| EQUIPAMIENTO | Culto y Cultura | Parroquias, centros culturales, bibliotecas, auditorios, galerías de arte. |
| EQUIPAMIENTO | Deporte | Gimnasios, centros y clubes deportivos, multicanchas. |
| EQUIPAMIENTO | Educación | Establecimientos de educación pre básica, básica, media, técnica; establecimientos de educación especial, escuelas de lenguaje, centros de capacitación, academias, institutos, jardines infantiles, salas cuna. |
| EQUIPAMIENTO | Salud | Policlínicos, consultorios, centros médicos, postas, centros de rehabilitación de salud. |
| EQUIPAMIENTO | Seguridad | Unidades policiales, cuarteles de bomberos. |
| EQUIPAMIENTO | Servicios | Servicios públicos y privados de todo tipo. Servicios artesanales y profesionales. Oficinas, centros médicos, centros dentales, notarías, centros de pago, centros de belleza, peluquerías, lavanderías, lavasecos, cibercafés, fotocopiadoras, servicios informáticos. |
| EQUIPAMIENTO | Social | Sedes de todo tipo de organizaciones sociales. |
| INFRAESTRUCTURA | Transporte | Terminales de vehículos de locomoción colectiva. |
| ESPACIO PÚBLICO | — | Vialidad y plazas. |
| ÁREA VERDE | — | Plazas. |
| **USOS DE SUELO PROHIBIDOS** | | TODOS LOS NO SEÑALADOS COMO PERMITIDOS |

### b. Normas urbanísticas

| Parámetro | Residencial | Otros usos |
|---|---|---|
| Superficie de subdivisión predial mínima (m²) | 400 (valor único) | 400 (valor único) |
| Densidad bruta máxima (hab./ha) | 75 | No aplica |
| Coeficiente de ocupación del suelo | 0,4 | 0,4 |
| Coeficiente de constructibilidad | 0,7 | 0,7 |
| Sistema de agrupamiento | Aislado, pareado, continuo (valor único) | Aislado, pareado, continuo (valor único) |
| Altura máxima de la edificación | 2 pisos o 7 m (valor único) | 2 pisos o 7 m (valor único) |
| Distanciamiento a medianeros | Art. 2.6.3 de la OGUC (valor único) | Art. 2.6.3 de la OGUC (valor único) |
| Antejardín | 3 metros (valor único) | 3 metros (valor único) |
| Adosamiento | Se permite (valor único) | Se permite (valor único) |

---

## 9. ZR7 — Habitacional, densidad media, baja altura (pág. 31)

### a. Usos de suelo

Idéntica a ZR6 (mismo texto exacto, incluida "organizaciones sociales").

| Uso de suelo | Destino/Clase | Actividades permitidas |
|---|---|---|
| RESIDENCIAL | Vivienda | Vivienda. |
| RESIDENCIAL | Hospedaje | Locales destinados al hospedaje, pensiones, internados de estudiantes. |
| RESIDENCIAL | Hogares de acogida | Hogares de acogida en general, hogares de estadía para adultos mayores u hogares de ancianos. |
| EQUIPAMIENTO | Comercio | Locales comerciales, restaurantes, cafeterías, salones de té, fuentes de soda. |
| EQUIPAMIENTO | Culto y Cultura | Parroquias, centros culturales, bibliotecas, auditorios, galerías de arte. |
| EQUIPAMIENTO | Deporte | Gimnasios, centros y clubes deportivos, multicanchas. |
| EQUIPAMIENTO | Educación | Establecimientos de educación pre básica, básica, media, técnica; establecimientos de educación especial, escuelas de lenguaje, centros de capacitación, academias, institutos, jardines infantiles, salas cuna. |
| EQUIPAMIENTO | Salud | Policlínicos, consultorios, centros médicos, postas, centros de rehabilitación de salud. |
| EQUIPAMIENTO | Seguridad | Unidades policiales, cuarteles de bomberos. |
| EQUIPAMIENTO | Servicios | Servicios públicos y privados de todo tipo. Servicios artesanales y profesionales. Oficinas, centros médicos, centros dentales, notarías, centros de pago, centros de belleza, peluquerías, lavanderías, lavasecos, cibercafés, fotocopiadoras, servicios informáticos. |
| EQUIPAMIENTO | Social | Sedes de todo tipo de organizaciones sociales. |
| INFRAESTRUCTURA | Transporte | Terminales de vehículos de locomoción colectiva. |
| ESPACIO PÚBLICO | — | Vialidad y plazas. |
| ÁREA VERDE | — | Plazas. |
| **USOS DE SUELO PROHIBIDOS** | | TODOS LOS NO SEÑALADOS COMO PERMITIDOS |

### b. Normas urbanísticas

| Parámetro | Residencial | Otros usos |
|---|---|---|
| Superficie de subdivisión predial mínima (m²) | 400 (valor único) | 400 (valor único) |
| Densidad bruta máxima (hab./ha) | 70 | No aplica |
| Coeficiente de ocupación del suelo | 0,35 | 0,35 |
| Coeficiente de constructibilidad | 0,65 | 0,65 |
| Sistema de agrupamiento | Aislado, pareado, continuo (valor único) | Aislado, pareado, continuo (valor único) |
| Altura máxima de la edificación | 2 pisos o 7 m (valor único) | 2 pisos o 7 m (valor único) |
| Distanciamiento a medianeros | Art. 2.6.3 de la OGUC (valor único) | Art. 2.6.3 de la OGUC (valor único) |
| Antejardín | 3 metros (valor único) | 3 metros (valor único) |
| Adosamiento | Se permite (valor único) | Se permite (valor único) |

---

## 10. ZR8 — Habitacional, densidad baja, baja altura (pág. 31-32)

### a. Usos de suelo

| Uso de suelo | Destino/Clase | Actividades permitidas |
|---|---|---|
| RESIDENCIAL | Vivienda | Vivienda. |
| RESIDENCIAL | Hospedaje | Locales destinados al hospedaje, pensiones, internados de estudiantes. |
| RESIDENCIAL | Hogares de acogida | Hogares de acogida en general, hogares de estadía para adultos mayores u hogares de ancianos. |
| EQUIPAMIENTO | Comercio | Locales comerciales, restaurantes, cafeterías, salones de té, fuentes de soda. |
| EQUIPAMIENTO | Culto y Cultura | Parroquias, centros culturales, bibliotecas, auditorios, galerías de arte. |
| EQUIPAMIENTO | Deporte | Gimnasios, centros y clubes deportivos, multicanchas. |
| EQUIPAMIENTO | Educación | Establecimientos de educación pre básica, básica, media, técnica; establecimientos de educación especial, escuelas de lenguaje, centros de capacitación, academias, institutos, jardines infantiles, salas cuna. |
| EQUIPAMIENTO | Esparcimiento | Zonas de picnic, zonas de camping, actividades al aire libre. |
| EQUIPAMIENTO | Salud | Policlínicos, consultorios, centros médicos, postas, centros de rehabilitación de salud. |
| EQUIPAMIENTO | Seguridad | Unidades policiales, cuarteles de bomberos. |
| EQUIPAMIENTO | Servicios | Servicios públicos y privados de todo tipo. Servicios artesanales y profesionales. Oficinas, centros médicos, centros dentales, notarías, centros de pago, centros de belleza, peluquerías, lavanderías, lavasecos, cibercafés, fotocopiadoras, servicios informáticos. |
| EQUIPAMIENTO | Social | Sedes de todo tipo de organizaciones sociales. |
| INFRAESTRUCTURA | — | Terminales de vehículos de locomoción colectiva. |
| ESPACIO PÚBLICO | — | Vialidad y plazas. |
| ÁREA VERDE | — | Plazas. |
| **USOS DE SUELO PROHIBIDOS** | | TODOS LOS NO SEÑALADOS COMO PERMITIDOS |

**Hallazgo:** primera zona con fila "Esparcimiento" (zonas de picnic/camping/aire libre) — no aparecía en ZR1-ZR7. La fila INFRAESTRUCTURA aparece sin la etiqueta "Transporte" en la columna Destino (celda fusionada), a diferencia de ZR1-ZR7.

### b. Normas urbanísticas

| Parámetro | Residencial | Otros usos |
|---|---|---|
| Superficie de subdivisión predial mínima (m²) | 500 (valor único) | 500 (valor único) |
| Densidad bruta máxima (hab./ha) | 65 | No aplica |
| Coeficiente de ocupación del suelo | 0,3 | 0,4 |
| Coeficiente de constructibilidad | 0,4 | 0,4 |
| Sistema de agrupamiento | Aislado y pareado (valor único) | Aislado y pareado (valor único) |
| Altura máxima de la edificación | 2 pisos o 7 m (valor único) | 2 pisos o 7 m (valor único) |
| Distanciamiento a medianeros | Art. 2.6.3 de la OGUC (valor único) | Art. 2.6.3 de la OGUC (valor único) |
| Antejardín | 5 metros (valor único) | 5 metros (valor único) |
| Adosamiento | No se permite (valor único) | No se permite (valor único) |

---

## 11. ZR9 — Habitacional, densidad media, baja altura (pág. 32)

### a. Usos de suelo

| Uso de suelo | Destino/Clase | Actividades permitidas |
|---|---|---|
| RESIDENCIAL | Vivienda | Vivienda. |
| RESIDENCIAL | Hospedaje | Locales destinados al hospedaje, pensiones, internados de estudiantes, moteles, cabañas. |
| RESIDENCIAL | Hogares de acogida | Hogares de acogida en general, hogares de estadía para adultos mayores u hogares de ancianos. |
| EQUIPAMIENTO | Comercio | Locales comerciales, restaurantes, cafeterías, salones de té, fuentes de soda. |
| EQUIPAMIENTO | Culto y Cultura | Parroquias, centros culturales, bibliotecas, auditorios, galerías de arte. |
| EQUIPAMIENTO | Deporte | Gimnasios, centros y clubes deportivos, multicanchas, piscinas. |
| EQUIPAMIENTO | Educación | Establecimientos de educación pre básica, básica, media, técnica; establecimientos de educación especial, escuelas de lenguaje, centros de capacitación, academias, institutos, jardines infantiles, salas cuna. |
| EQUIPAMIENTO | Esparcimiento | Zonas de picnic, zonas de camping, actividades al aire libre. |
| EQUIPAMIENTO | Salud | Policlínicos, consultorios, centros médicos, postas, centros de rehabilitación de salud. |
| EQUIPAMIENTO | Seguridad | Unidades policiales, cuarteles de bomberos. |
| EQUIPAMIENTO | Servicios | Servicios públicos y privados de todo tipo. Servicios artesanales y profesionales. Oficinas, centros médicos, centros dentales, notarías, centros de pago, centros de belleza, peluquerías, lavanderías, lavasecos, cibercafés, fotocopiadoras, servicios informáticos. |
| EQUIPAMIENTO | Social | Sedes de todo tipo de organizaciones sociales. |
| INFRAESTRUCTURA | — | Terminales de vehículos de locomoción colectiva. |
| ESPACIO PÚBLICO | — | Vialidad y plazas. |
| ÁREA VERDE | — | Plazas. |
| **USOS DE SUELO PROHIBIDOS** | | TODOS LOS NO SEÑALADOS COMO PERMITIDOS |

### b. Normas urbanísticas

| Parámetro | Residencial | Otros usos |
|---|---|---|
| Superficie de subdivisión predial mínima (m²) | 500 (valor único) | 500 (valor único) |
| Densidad bruta máxima (hab./ha) | 50 | No aplica |
| Coeficiente de ocupación del suelo | 0,4 | 0,4 |
| Coeficiente de constructibilidad | 0,6 | 0,6 |
| Sistema de agrupamiento | Aislado, pareado, continuo (valor único) | Aislado, pareado, continuo (valor único) |
| Altura máxima de la edificación | 2 pisos o 7 m (valor único) | 2 pisos o 7 m (valor único) |
| Distanciamiento a medianeros | Art. 2.6.3 de la OGUC (valor único) | Art. 2.6.3 de la OGUC (valor único) |
| Antejardín | 3 metros (valor único) | 3 metros (valor único) |
| Adosamiento | Se permite (valor único) | Se permite (valor único) |

---

## 12. ZR10 — Habitacional, densidad media, baja altura (pág. 32-33)

### a. Usos de suelo

Igual patrón que ZR9 (Hospedaje con moteles/cabañas, Deporte con piscinas, Esparcimiento presente), pero Espacio Público/Área Verde vuelven a la forma larga ("Vialidad, parques y plazas" / "Parques y plazas").

| Uso de suelo | Destino/Clase | Actividades permitidas |
|---|---|---|
| RESIDENCIAL | Vivienda | Vivienda. |
| RESIDENCIAL | Hospedaje | Locales destinados al hospedaje, pensiones, internados de estudiantes, moteles, cabañas. |
| RESIDENCIAL | Hogares de acogida | Hogares de acogida en general, hogares de estadía para adultos mayores u hogares de ancianos. |
| EQUIPAMIENTO | Comercio | Locales comerciales, restaurantes, cafeterías, salones de té, fuentes de soda. |
| EQUIPAMIENTO | Culto y Cultura | Parroquias, centros culturales, bibliotecas, auditorios, galerías de arte. |
| EQUIPAMIENTO | Deporte | Gimnasios, centros y clubes deportivos, multicanchas, piscinas. |
| EQUIPAMIENTO | Educación | Establecimientos de educación pre básica, básica, media, técnica; establecimientos de educación especial, escuelas de lenguaje, centros de capacitación, academias, institutos, jardines infantiles, salas cuna. |
| EQUIPAMIENTO | Esparcimiento | Zonas de picnic, zonas de camping, actividades al aire libre. |
| EQUIPAMIENTO | Salud | Policlínicos, consultorios, centros médicos, postas, centros de rehabilitación de salud. |
| EQUIPAMIENTO | Seguridad | Unidades policiales, cuarteles de bomberos. |
| EQUIPAMIENTO | Servicios | Servicios públicos y privados de todo tipo. Servicios artesanales y profesionales. Oficinas, centros médicos, centros dentales, notarías, centros de pago, centros de belleza, peluquerías, lavanderías, lavasecos, cibercafés, fotocopiadoras, servicios informáticos. |
| EQUIPAMIENTO | Social | Sedes de todo tipo de organizaciones sociales. |
| INFRAESTRUCTURA | — | Terminales de vehículos de locomoción colectiva. |
| ESPACIO PÚBLICO | — | Vialidad, parques y plazas. |
| ÁREA VERDE | — | Parques y plazas. |
| **USOS DE SUELO PROHIBIDOS** | | TODOS LOS NO SEÑALADOS COMO PERMITIDOS |

### b. Normas urbanísticas

| Parámetro | Residencial | Otros usos |
|---|---|---|
| Superficie de subdivisión predial mínima (m²) | 800 (valor único) | 800 (valor único) |
| Densidad bruta máxima (hab./ha) | 40 | No aplica |
| Coeficiente de ocupación del suelo | 0,2 | 0,3 |
| Coeficiente de constructibilidad | 0,35 | 0,35 |
| Sistema de agrupamiento | Aislado, pareado (valor único) | Aislado, pareado (valor único) |
| Altura máxima de la edificación | 2 pisos o 7 m (valor único) | 2 pisos o 7 m (valor único) |
| Distanciamiento a medianeros | Art. 2.6.3 de la OGUC (valor único) | Art. 2.6.3 de la OGUC (valor único) |
| Antejardín | 5 metros (valor único) | 5 metros (valor único) |
| Adosamiento | No se permite (valor único) | No se permite (valor único) |

---

## Cuadro comparativo — familia ZR1-ZR10 (resumen rápido de edificación)

| Zona | Predial mín. | Densidad | COS | CC | Altura | Adosamiento |
|---|---|---|---|---|---|---|
| ZR1 | 1000 | 450/No aplica | 0,25/0,4 | 1,3/1,6 | 8 pisos o 28 m | No se permite |
| ZR2 | 1000 | 340/No aplica | 0,3/0,5 | 1,2/1,5 | 5 pisos o 17,5 m | No se permite |
| ZR3 | 800 | 200/No aplica | 0,5/0,5 | 1,5/1,9 | 4 pisos o 14 m | No se permite |
| ZR4 | 250 | 110/No aplica | 0,6/0,6 | 1,0/1,0 | 2 pisos o 7 m | Se permite |
| ZR5 | 400 | 85/No aplica | 0,5/0,5 | 0,8/1,0 | 2 pisos o 7 m | Se permite |
| ZR6 | 400 | 75/No aplica | 0,4/0,4 | 0,7/0,7 | 2 pisos o 7 m | Se permite |
| ZR7 | 400 | 70/No aplica | 0,35/0,35 | 0,65/0,65 | 2 pisos o 7 m | Se permite |
| ZR8 | 500 | 65/No aplica | 0,3/0,4 | 0,4/0,4 | 2 pisos o 7 m | No se permite |
| ZR9 | 500 | 50/No aplica | 0,4/0,4 | 0,6/0,6 | 2 pisos o 7 m | Se permite |
| ZR10 | 800 | 40/No aplica | 0,2/0,3 | 0,35/0,35 | 2 pisos o 7 m | No se permite |

**Patrón general:** la intensidad de edificación decrece de ZR1 a ZR10 en altura/COS/CC (con la excepción de que ZR3 tiene mayor CC en "Otros usos" que ZR1/ZR2), mientras que el predial mínimo no sigue un orden estrictamente monótono (baja de ZR1 a ZR4, luego sube y baja de forma irregular en ZR5-ZR10) — reflejo de que la numeración ZR1-ZR10 no es un único eje de densidad sino una combinación de densidad y localización de cada polígono.

---

## 13. ZRM1 — Habitacional mixta, densidad media-alta, media altura (pág. 33)

### a. Usos de suelo

| Uso de suelo | Destino/Clase | Actividades permitidas |
|---|---|---|
| RESIDENCIAL | Vivienda | Vivienda. |
| RESIDENCIAL | Hospedaje | Hotel, edificaciones o locales destinados al hospedaje, pensiones, internados de estudiantes, albergues. |
| RESIDENCIAL | Hogares de Acogida | Hogares de acogida en general, hogares de estadía para adultos mayores u hogares de ancianos. |
| EQUIPAMIENTO | Científico | Laboratorios, centros científicos y/o de investigación. |
| EQUIPAMIENTO | Comercio | Supermercados, Locales comerciales, restaurantes, cafeterías, salones de té, fuentes de soda, pubs. |
| EQUIPAMIENTO | Culto y Cultura | Templos, santuarios, parroquias, centros culturales, museos, bibliotecas, auditorios, galerías de arte, centros de convenciones, centros de difusión o exposiciones, centros de eventos. |
| EQUIPAMIENTO | Deporte | Gimnasios, saunas, baños turcos, centros y clubes deportivos, multicanchas, piscinas. |
| EQUIPAMIENTO | Educación | Establecimientos de educación pre básica, básica, media, técnica y superior; establecimientos de educación especial, escuelas de lenguaje, centros de capacitación, academias, institutos, jardines infantiles, salas cuna. |
| EQUIPAMIENTO | Salud | Clínicas, policlínicos, consultorios, centros médicos, postas, centros de rehabilitación de salud. |
| EQUIPAMIENTO | Seguridad | Unidades policiales, cuarteles de bomberos. |
| EQUIPAMIENTO | Servicios | Servicios públicos y privados de todo tipo. Servicios artesanales y profesionales. Oficinas, centros médicos, centros dentales, notarías, instituciones de salud previsional, AFPs, Compañías de seguros, correos, centros de pago, bancos, financieras, centros de belleza, peluquerías, lavanderías, lavasecos, cibercafés, fotocopiadoras, servicios informáticos, servicios técnicos. |
| EQUIPAMIENTO | Social | Sedes de todo tipo de organización social. |
| INFRAESTRUCTURA | Transporte | Terminales de transporte terrestre, terminales de vehículos de locomoción colectiva. |
| ESPACIO PÚBLICO | — | Vialidad, parques y plazas. |
| ÁREA VERDE | — | Parques y plazas. |
| **USOS DE SUELO PROHIBIDOS** | | TODOS LOS NO SEÑALADOS COMO PERMITIDOS |

**Hallazgo:** primera zona con clase "Científico" en Equipamiento (no aparecía en ninguna ZR1-ZR10). Educación agrega "y superior". Comercio, Culto y Cultura y Servicios se amplían notoriamente respecto de la familia ZR.

### b. Normas urbanísticas

| Parámetro | Residencial | Otros usos |
|---|---|---|
| Superficie de subdivisión predial mínima (m²) | 1000 (valor único) | 1000 (valor único) |
| Densidad bruta máxima (hab./ha) | 340 | No aplica |
| Coeficiente de ocupación del suelo | 0,4 | 0,5 |
| Coeficiente de constructibilidad | 1,6 | 2,0 |
| Sistema de agrupamiento | Aislado, pareado, continuo. Para edificación continua, aislado y retranqueo desde el tercer piso: 5 metros desde la línea de edificación. (valor único) | (ídem) |
| Altura máxima de la edificación | 5 pisos o 17,5 m (valor único) | 5 pisos o 17,5 m (valor único) |
| Altura máxima de la edificación continua | 2 pisos o 7 m (valor único) | 2 pisos o 7 m (valor único) |
| Distanciamiento a medianeros | Art. 2.6.3 de la OGUC (valor único) | Art. 2.6.3 de la OGUC (valor único) |
| Antejardín | 5 metros. No consulta para edificación continua. (valor único) | (ídem) |
| Adosamiento | No se permite (valor único) | No se permite (valor único) |

**Hallazgo:** primera zona con fila adicional "Altura máxima de la edificación continua" (distinta de la altura general) y con cláusula de retranqueo desde el tercer piso para edificación continua — patrón que se repite en ZRM2, ZM1-ZM3 (sin retranqueo en ZM1-3), C1, C1-a y C6.

---
