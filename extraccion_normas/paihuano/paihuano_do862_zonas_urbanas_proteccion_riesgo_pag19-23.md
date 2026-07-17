# Normas Urbanísticas — Plan Regulador Comunal de Paihuano (Decreto N°862/2019), Zonificación Área Urbana, Áreas de Protección Patrimonial y Áreas de Riesgo

**Fuente:** Diario Oficial de la República de Chile, Núm. 42.400, miércoles 10 de julio de 2019, páginas 19 a 23 de 25 — Decreto N°862, que promulga el Plan Regulador Comunal de Paihuano. Título II "Zonificación de Usos de Suelo y Normas Específicas", Capítulo 1 "Zonificación y Áreas de Riesgo": Artículo 8 (enumeración de zonas y áreas), Artículo 9 (Área Urbana: zonas, usos de suelo y normas urbanísticas), Artículo 10 (Áreas de Protección de Recursos de Valor Patrimonial Cultural) y Artículo 11 (Áreas Restringidas al Desarrollo Urbano / Áreas de Riesgo). CVE 1618610.

**Extracción:** páginas 19 a 23 del documento (5 páginas). Fuera de este rango, y por tanto no cubiertos por este archivo: página 18 (estándares de estacionamiento) y página 24 (vialidad) — ninguna de las dos es "norma de zona" en el sentido de superficie predial/COS/altura, y quedaron explícitamente fuera del encargo.

**Advertencia sobre el PDF fuente (trampa MIXTO confirmada):** el veredicto general de este documento es TEXTO, pero en el rango páginas 19-23 casi todo el contenido normativo relevante (los cuadros de zona con superficie predial, densidad, COS, coeficiente de constructibilidad, sistema de agrupamiento, altura máxima y antejardín) está **incrustado como imagen/tabla escaneada**, no como texto extraíble — se verificó contra `paihuano_p19-23.txt` (extracción de `pdftotext` del mismo rango) y ese archivo prácticamente no contiene ninguno de los valores numéricos de las tablas: solo trae los títulos de artículo, los encabezados de "ÁREA URBANA" / "ÁREAS DE PROTECCIÓN..." / "ÁREAS DE RESTRICCIÓN" sin ningún cuadro, y el pie de imprenta repetido de cada página. Por lo tanto, **toda la transcripción de este archivo se hizo leyendo visualmente los 5 PNG renderizados** (imágenes fuente primaria), con recortes ampliados (2×-3.5×) sobre las zonas con celdas combinadas o números pequeños, tal como indica el encargo.

## Nota metodológica

- **Patrón de celdas combinadas (merge) identificado y verificado cruzando páginas sin salto de página:** en casi todas las zonas, la columna "Superficie de Subdivisión Predial Mínima (m²)" es **una sola celda combinada** que aplica al bloque Residencial + Equipamiento en conjunto (no un valor por cada fila de uso), mientras que Actividad Productiva e Infraestructura (cuando existen como filas separadas) quedan **fuera** de esa celda combinada y sin valor propio (en blanco) salvo que se indique lo contrario. Igual patrón aplica a las columnas de Ocupación de Suelo, Coeficiente de Constructibilidad, Sistema de Agrupamiento, Altura máxima y Antejardín para el bloque Equipamiento (se combinan en una sola celda que cubre todas las "Clases" de Equipamiento listadas, salvo excepción expresa). Este patrón se confirmó de forma inequívoca en las zonas ZH2, ZH3, ZT y ZAP —que caben completas en una sola página, sin salto— cotejando visualmente la ausencia de líneas horizontales divisorias dentro de la celda combinada. Se aplicó el mismo criterio para interpretar zonas cuya tabla queda partida por un salto de página (ZH1, entre p.19 y p.20; ZCH, entre p.22 y p.23), en las que el valor combinado aparece impreso en la mitad de la página donde cae el centro vertical de la celda (no necesariamente junto a la primera fila del grupo). Se marca explícitamente cualquier caso residual de duda.
- **Notación numérica:** los coeficientes (Ocupación de Suelo, Constructibilidad) se imprimen con **punto** decimal (ej. "0.60", "1.2", "0.04", "0.005"); las superficies prediales usan también punto pero como separador de miles (ej. "3.000" = tres mil m², "1.500" = mil quinientos m²). Se transcribe tal cual aparece en la fuente, sin convertir a coma decimal chilena, siguiendo el mismo criterio que otras extracciones de esta carpeta cuando la fuente imprime con punto.
- **Discrepancia relevante respecto a la nota de Fase 3 (se corrige aquí tras verificación visual):** la nota de Fase 3 indicaba "7 zonas Área Urbana (ZH1, ZH2, ZH3, ZD, ZT1, ZT2, ZAP)" y asignaba "ZIS, ZAV, ZT, ZCH, MH1/2/3" en bloque al Art. 10 (protección). **Verificado contra las imágenes, esto no es exacto:** el Art. 8 enumera **9** zonas de Área Urbana —las 7 anteriores **más ZIS y ZAV**— y las 9 tienen cuadro normativo propio bajo el Art. 9 (el cuadro de ZIS y de ZAV simplemente continúa en la página 22, después de ZAP, y **antes** del encabezado "Artículo 10" que aparece más abajo en esa misma página). El Art. 10 (Áreas de Protección de Recursos de Valor Patrimonial Cultural) agrupa realmente **5** áreas con cuadro normativo: **ZT** (Zona Típica), **ZCH** (Zona de Conservación Histórica), **MH1**, **MH2** y **MH3** (Monumentos Históricos) — sin ZIS ni ZAV. El resto de la nota de Fase 3 (AR1/AR2 en Art. 11, p.23) sí se confirma correcto.
- **Alerta de colisión de sigla:** el documento usa **"ZT1" y "ZT2"** para "Zona Turismo 1/2" (Área Urbana, Art. 9) y, por separado, **"ZT"** (sin número) para "Zona Típica" (Área de Protección Patrimonial, Art. 10, Sector Montegrande). Son tres siglas distintas que comparten el prefijo "ZT" — no confundir en el geolocalizador.
- **Estructura repetida en todas las tablas de zona:** cada cuadro trae dos bloques: (a) "Usos de Suelo Permitidos" (columnas Tipo / Clase / Actividades Prohibidas dentro de esa clase — es decir, la clase está permitida salvo las actividades ahí listadas) más las columnas normativas (superficie, densidad, coeficientes, agrupamiento, altura, antejardín); y (b) "Usos de Suelo No Permitidos" (categoría completa excluida). Se transcriben ambos bloques. La fila "Área Verde y Espacio Público" es, en todas las zonas de este rango, "Según OGUC" — se indica una sola vez por zona.
- Todas las zonas fueron releídas con recortes ampliados (factor 1.8×–3.5×) específicamente para las celdas combinadas y los números pequeños; los casos con incertidumbre real (no resuelta con zoom) se marcan explícitamente como "Dato no determinable" con su motivo, no se completan por analogía sin advertirlo.

---

## Artículo 8 — Enumeración de zonas y áreas (cuadro de clasificación)

### Área Urbana (Art. 9 — 9 zonas)

| Sigla | Nombre |
|---|---|
| ZH1 | Zona Densidad Alta |
| ZH2 | Zona Densidad Media |
| ZH3 | Zona Densidad Baja |
| ZD | Zona Deporte |
| ZT1 | Zona Turismo 1 |
| ZT2 | Zona Turismo 2 |
| ZAP | Zona Actividades Productivas |
| ZIS | Zona Infraestructura Sanitaria |
| ZAV | Zona Área Verde |

### Áreas de Protección de Recursos de Valor Patrimonial Cultural (Art. 10 — 5 áreas)

| Sigla | Nombre / identificación | Instrumento de constitución legal |
|---|---|---|
| ZT | Zona Típica Sector de Montegrande | DS 621 (MINEDUC), promulgación 31.07.1990; publicación en D.O. 03.09.1990 |
| MH1 | Tumba de Gabriela Mistral en Montegrande | Ley 14.693, publicación D.O. 28.11.1961 (Ministerio de Educación Pública) |
| MH2 | Casa Escuela Rural de Gabriela Mistral en Montegrande | DS 2174 (MINEDUC), promulgación 24.08.1979; publicación en D.O. 20.09.1979 |
| MH3 | Escuela N°10, Jerónimo Godoy Villanueva, Pisco Elqui | Decreto 401 (MINEDUC), promulgación 10.10.2014 (\*); publicación en D.O. 07.11.2014 |
| ZCH | Zona de Conservación Histórica en localidades de Paihuano, Pisco Elqui y Montegrande | (categoría propia del PRC, sin decreto externo listado) |

(\*) La fecha de promulgación de MH3 se imprime en la fuente como "10.10..2014" (doble punto tras el segundo "10"); se transcribe como 10.10.2014, con nota de que el doble punto es un defecto tipográfico del documento original, no de esta transcripción.

### Áreas Restringidas / Áreas de Riesgo (Art. 11 — 2 áreas)

| Sigla | Descripción |
|---|---|
| AR1 | Inundables o Potencialmente Inundables por proximidad a Ríos y Quebradas |
| AR2 | Propensas a Avalanchas, Rodados, Aluviones o Erosiones Acentuadas |

Nota: esta misma tabla AR1/AR2 aparece impresa dos veces en el rango (resumen en p.19, dentro del Art. 8; detalle en p.23, dentro del Art. 11), con una diferencia textual menor entre ambas copias: la p.19 imprime "...Erosiones Acentuad**os**" (concordancia con "Rodados") y la p.23 imprime "...Erosiones Acentuad**as**" (concordancia con "Erosiones"). Se verificó con zoom en ambas páginas — no es error de lectura, es una inconsistencia real del documento fuente entre sus dos apariciones del mismo cuadro. Se preferitó la versión de Art. 11 (p.23, la que trae el detalle normativo) para el cuerpo del artículo, y se deja esta nota para no perder la variante de p.19.

---

## ÁREA URBANA (Artículo 9)

> Texto del Art. 9: *"Los usos de suelo, condiciones de subdivisión predial mínima y edificación para las Zonas indicadas en el Artículo precedente, se han sistematizado en los siguientes Cuadros de Zonas del Área Urbana del Plan Regulador Comunal de Paihuano que se indican a continuación."*

### ZH1 — Zona Densidad Alta (páginas 19-20)

**Usos de suelo permitidos**

| Tipo | Clase | Actividades prohibidas |
|---|---|---|
| Residencial | Vivienda, Hospedaje | -- |
| Equipamiento | Científico | -- |
| Equipamiento | Comercio | Terminales de distribución |
| Equipamiento | Culto y Cultura | -- |
| Equipamiento | Deporte | Estadio, Medialuna |
| Equipamiento | Educación | Centro de Rehabilitación Conductual |
| Equipamiento | Salud | Cementerio, Crematorio |
| Equipamiento | Seguridad | Cárcel, Centro de Detención |
| Equipamiento | Servicios | -- |
| Equipamiento | Social | -- |
| Actividad Productiva | Inofensiva | Calificadas como: molestas, insalubres o contaminantes y peligrosas. Plantas de Revisión Técnica |

**Condiciones de subdivisión y edificación**

| Grupo de uso | Superficie predial mín. (m²) | Densidad bruta (Hab/Há) | Ocupación de suelo (COS) | Coef. constructibilidad | Sistema de agrupamiento | Altura máx. edif. (m) | Antejardín (m) |
|---|---|---|---|---|---|---|---|
| Residencial (Vivienda, Hospedaje) | 200 (\*) | 185 | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente |
| Equipamiento (las 9 clases de arriba) | 200 (\*) | -- | 0.60 | 1.2 | Aislado, Pareado, Continuo (\*\*) | 7.5 | 3.0 |
| Actividad Productiva (Inofensiva) | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente |

Área Verde y Espacio Público: Según OGUC.

(\*) La celda "200" de Superficie de Subdivisión Predial Mínima está combinada e imprime su valor una sola vez, en la posición vertical que —por el salto de página entre p.19 y p.20— cae junto a la fila "Seguridad" en el render; se interpreta, por el mismo patrón confirmado sin ambigüedad en ZH2/ZH3/ZT (ver nota metodológica), que aplica al bloque Residencial + Equipamiento completo, no solo a la fila Seguridad.
(\*\*) El valor de Sistema de Agrupamiento queda partido por el salto de página: "Aislado" y "Pareado" se leen al pie de la p.19 (junto a la fila Salud) y "Continuo" se lee al inicio de la p.20 (junto a la fila Seguridad), sin línea divisoria visible entre ambos fragmentos ni entre las filas Científico-Social. Se reconstruye como un solo valor de tres opciones "Aislado, Pareado, Continuo", consistente con el mismo patrón de tabla no ambiguo (sin salto de página) verificado en la Zona Típica (ZT, Art. 10, misma plantilla con distintos números).

**Usos de suelo no permitidos**

| Categoría | Actividades prohibidas |
|---|---|
| Equipamiento | Esparcimiento |
| Actividades Productivas | Calificadas como: molestas, insalubres o contaminantes y peligrosas |
| Infraestructura | Edificaciones o instalaciones destinadas a Infraestructura de Transporte, Sanitaria y Energética |

---

### ZH2 — Zona Densidad Media (página 20)

**Usos de suelo permitidos**

| Tipo | Clase | Actividades prohibidas |
|---|---|---|
| Residencial | Vivienda, Hospedaje | -- |
| Equipamiento | Científico | -- |
| Equipamiento | Comercio | Terminales de distribución |
| Equipamiento | Culto y Cultura | -- |
| Equipamiento | Deporte | Estadio, Medialuna |
| Equipamiento | Educación | Centro de Rehabilitación Conductual |
| Equipamiento | Salud | Cementerio, Crematorio |
| Equipamiento | Seguridad | Cárcel, Centro de Detención |
| Equipamiento | Servicios | -- |
| Equipamiento | Social | -- |
| Actividad Productiva | Inofensiva | Calificadas como: molestas, insalubres o contaminantes y peligrosas. Plantas de Revisión Técnica |
| Infraestructura de Transporte | (sin clase específica) | -- |
| Infraestructura Sanitaria | (sin clase específica) | Planta de Tratamiento de Aguas Servidas; Relleno Sanitario, Estación de Transferencia de Residuos |

**Condiciones de subdivisión y edificación**

| Grupo de uso | Superficie predial mín. (m²) | Densidad bruta (Hab/Há) | Ocupación de suelo (COS) | Coef. constructibilidad | Sistema de agrupamiento | Altura máx. edif. (m) | Antejardín (m) |
|---|---|---|---|---|---|---|---|
| Residencial (Vivienda, Hospedaje) | 800 | 60 | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente |
| Equipamiento (las 9 clases de arriba) | 800 | -- | 0.4 | 0.8 | Aislado | 7.5 | 3.0 |
| Actividad Productiva (Inofensiva) | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente |
| Infraestructura de Transporte | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente |
| Infraestructura Sanitaria | Sin valor específico en la fuente | Sin valor específico en la fuente | Distanciamiento: 5 m | Distanciamiento: 5 m | Adosamiento: no se permite | Sin valor específico en la fuente | Sin valor específico en la fuente |

Área Verde y Espacio Público: Según OGUC.

Nota de verificación: la celda combinada de Superficie (800) y la de Ocupación/Constructibilidad/Sistema/Altura/Antejardín (0.4/0.8/Aislado/7.5/3.0) terminan exactamente en la fila "Social" — se confirmó con un recorte a máximo zoom que hay línea horizontal divisoria entre "Social" y "Actividad Productiva" en todas esas columnas, por lo que Actividad Productiva e Infraestructura quedan en blanco con certeza (no es una omisión de lectura).

**Usos de suelo no permitidos**

| Categoría | Actividades prohibidas |
|---|---|
| Equipamiento | Esparcimiento |
| Actividades Productivas | Calificadas como: molestas, insalubres o contaminantes y peligrosas |
| Infraestructura | Edificaciones o instalaciones destinadas a Infraestructura Energética |

---

### ZH3 — Zona Densidad Baja (página 20)

**Usos de suelo permitidos**

| Tipo | Clase | Actividades prohibidas |
|---|---|---|
| Residencial | Vivienda, Hospedaje | -- |
| Equipamiento | Científico | -- |
| Equipamiento | Comercio | Terminales de distribución |
| Equipamiento | Culto y Cultura | -- |
| Equipamiento | Deporte | Estadio, Medialuna, Gimnasio |
| Actividad Productiva | Inofensiva | Calificadas como: molestas, insalubres o contaminantes y peligrosas |

**Condiciones de subdivisión y edificación**

| Grupo de uso | Superficie predial mín. (m²) | Densidad bruta (Hab/Há) | Ocupación de suelo (COS) | Coef. constructibilidad | Sistema de agrupamiento | Altura máx. edif. (m) | Antejardín (m) |
|---|---|---|---|---|---|---|---|
| Residencial (Vivienda, Hospedaje) | 1.500 | 33 | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente |
| Equipamiento (Científico, Comercio, Culto y Cultura, Deporte) | 1.500 | -- | 0.5 | 0.5 | Aislado | 7.5 | 3.0 |
| Actividad Productiva (Inofensiva) | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente |

Área Verde y Espacio Público: Según OGUC.

Nota: en ZH3 el catálogo de Equipamiento permitido es más acotado que en ZH1/ZH2 (solo 4 clases, no 9) — consistente con que su lista de "no permitidos" (abajo) incluye explícitamente Educación, Salud, Seguridad, Servicios y Social, que en ZH1/ZH2 sí estaban permitidos.

**Usos de suelo no permitidos**

| Categoría | Actividades prohibidas |
|---|---|
| Equipamiento | Educación, Esparcimiento, Salud, Seguridad, Servicios, Social |
| Actividades Productivas | Calificadas como: molestas, insalubres o contaminantes y peligrosas |
| Infraestructura | Edificaciones o instalaciones destinadas a Infraestructura de Transporte, Sanitaria y Energética |

---

### ZD — Zona Deporte (página 21)

**Usos de suelo permitidos**

| Tipo | Clase | Actividades prohibidas |
|---|---|---|
| Equipamiento | Deporte | -- |

**Condiciones de subdivisión y edificación**

| Grupo de uso | Superficie predial mín. (m²) | Densidad bruta (Hab/Há) | Ocupación de suelo (COS) | Coef. constructibilidad | Sistema de agrupamiento | Altura máx. edif. (m) | Antejardín (m) |
|---|---|---|---|---|---|---|---|
| Equipamiento (Deporte) | 1.000 | -- | 0.4 | 0.8 | Aislado | 10 | 3.0 |

Área Verde y Espacio Público: Según OGUC.

**Usos de suelo no permitidos**

| Categoría | Actividades prohibidas |
|---|---|
| Residencial | Vivienda, Hospedaje |
| Equipamiento | Científico, Comercio, Culto y Cultura, Educación, Esparcimiento, Salud, Seguridad, Servicios, Social |
| Actividades Productivas | Calificadas como: inofensivas, molestas, insalubres o contaminantes y peligrosas |
| Infraestructura | Edificaciones o instalaciones destinadas a Infraestructura de Transporte, Sanitaria y Energética |

---

### ZT1 — Zona Turismo 1 (página 21)

**Usos de suelo permitidos**

| Tipo | Clase | Actividades prohibidas |
|---|---|---|
| Equipamiento | Comercio | Todas, excepto: restoranes |
| Equipamiento | Esparcimiento | Todas, excepto: balnearios, áreas de picnic |

**Condiciones de subdivisión y edificación**

| Grupo de uso | Superficie predial mín. (m²) | Densidad bruta (Hab/Há) | Ocupación de suelo (COS) | Coef. constructibilidad | Sistema de agrupamiento | Altura máx. edif. (m) | Antejardín (m) |
|---|---|---|---|---|---|---|---|
| Equipamiento (Comercio, Esparcimiento) | 400 | -- | 0.6 | 1.2 | Aislado | 7.5 | 3.0 |

Área Verde y Espacio Público: Según OGUC.

**Usos de suelo no permitidos**

| Categoría | Actividades prohibidas |
|---|---|
| Residencial | Vivienda, Hospedaje |
| Equipamiento | Científico, Culto y Cultura, Deporte, Educación, Salud, Seguridad, Servicios, Social |
| Actividades Productivas | Calificadas como: inofensivas, molestas, insalubres o contaminantes y peligrosas |
| Infraestructura | Edificaciones o instalaciones destinadas a Infraestructura de Transporte, Sanitaria y Energética |

---

### ZT2 — Zona Turismo 2 (página 21)

**Usos de suelo permitidos**

| Tipo | Clase | Actividades prohibidas |
|---|---|---|
| Residencial | Hospedaje | -- |
| Equipamiento | Comercio | Todas, excepto: restoranes |
| Equipamiento | Culto y Cultura | -- |
| Equipamiento | Deporte | -- |
| Equipamiento | Esparcimiento | Todas, excepto: balnearios, áreas de picnic, campings |

**Condiciones de subdivisión y edificación**

| Grupo de uso | Superficie predial mín. (m²) | Densidad bruta (Hab/Há) | Ocupación de suelo (COS) | Coef. constructibilidad | Sistema de agrupamiento | Altura máx. edif. (m) | Antejardín (m) |
|---|---|---|---|---|---|---|---|
| Residencial (Hospedaje) + Equipamiento (Comercio, Culto y Cultura, Deporte, Esparcimiento) | 800 | -- | 0.6 | 1.2 | Aislado | 7.5 | 5.0 |

Área Verde y Espacio Público: Según OGUC.

**Usos de suelo no permitidos**

| Categoría | Actividades prohibidas |
|---|---|
| Residencial | Vivienda |
| Equipamiento | Científico, Educación, Salud, Seguridad, Servicios, Social |
| Actividades Productivas | Calificadas como: inofensivas, molestas, insalubres o contaminantes y peligrosas |
| Infraestructura | Edificaciones o instalaciones destinadas a Infraestructura de Transporte, Sanitaria y Energética |

---

### ZAP — Zona Actividades Productivas (página 21)

**Usos de suelo permitidos**

| Tipo | Clase | Actividades prohibidas |
|---|---|---|
| Equipamiento | Comercio | Todas, excepto: restoranes |
| Actividades Productivas | Inofensivas y Molestas | Calificadas como: insalubres o contaminantes y peligrosas |

**Condiciones de subdivisión y edificación**

| Grupo de uso | Superficie predial mín. (m²) | Densidad bruta (Hab/Há) | Ocupación de suelo (COS) | Coef. constructibilidad | Sistema de agrupamiento | Altura máx. edif. (m) | Antejardín (m) |
|---|---|---|---|---|---|---|---|
| Equipamiento (Comercio) + Actividades Productivas (Inofensivas y Molestas) | 2.000 | -- | 0.5 | 1.0 | Aislado | 10.5 | 3.0 |

Área Verde y Espacio Público: Según OGUC.

**Usos de suelo no permitidos**

| Categoría | Actividades prohibidas |
|---|---|
| Residencial | Vivienda, Hospedaje |
| Equipamiento | Científico, Culto y Cultura, Deporte, Educación, Esparcimiento, Salud, Seguridad, Servicios, Social |
| Actividades Productivas | Calificadas como: insalubres o contaminantes y peligrosas |
| Infraestructura | Edificaciones o instalaciones destinadas a Infraestructura de Transporte, Sanitaria y Energética |

---

### ZIS — Zona Infraestructura Sanitaria (página 22)

**Usos de suelo permitidos**

| Tipo | Clase | Actividades prohibidas |
|---|---|---|
| Infraestructura Sanitaria | (sin clase específica) | Relleno Sanitario, Estación de Transferencia de Residuos |

**Condiciones de subdivisión y edificación**

| Grupo de uso | Superficie predial mín. (m²) | Densidad bruta (Hab/Há) | Ocupación de suelo (COS) | Coef. constructibilidad | Sistema de agrupamiento | Altura máx. edif. (m) | Antejardín (m) |
|---|---|---|---|---|---|---|---|
| Infraestructura Sanitaria | 100 | -- | 0.5 | 0.5 | Aislado | 10 | 3.5 |

Nota adicional impresa junto a esta fila: "Distanciamiento: 5 m. Adosamiento: no se permite."

Área Verde y Espacio Público: Según OGUC.

**Usos de suelo no permitidos**

| Categoría | Actividades prohibidas |
|---|---|
| Residencial | Vivienda, Hospedaje |
| Equipamiento | Científico, Comercio, Culto y Cultura, Deporte, Educación, Esparcimiento, Salud, Seguridad, Servicios, Social |
| Actividades Productivas | Calificadas como: inofensivas, molestas, insalubres o contaminantes y peligrosas |
| Infraestructura | Edificaciones o instalaciones destinadas a Infraestructura de Transporte y Energética |

---

### ZAV — Zona Área Verde (página 22)

**Usos de suelo permitidos** (rótulo de la fuente: "Edificaciones con destinos complementarios al uso de suelo Área Verde")

| Tipo | Clase | Actividades prohibidas |
|---|---|---|
| Equipamiento | Científico | -- |
| Equipamiento | Culto y Cultura | -- |
| Equipamiento | Deporte | Medialuna |
| Equipamiento | Esparcimiento | Zoológico, juegos mecánicos y electrónicos, casinos |

**Condiciones de subdivisión y edificación**

| Grupo de uso | Superficie predial mín. (m²) | Densidad bruta (Hab/Há) | Ocupación de suelo (COS) | Coef. constructibilidad máxima | Sistema de agrupamiento | Altura máx. edif. (m) | Antejardín (m) |
|---|---|---|---|---|---|---|---|
| Equipamiento (las 4 clases de arriba) | 1.500 | -- | 0.2 | 0.2 | Aislado | 3.5 | 5.0 |

Área Verde y Espacio Público: Según OGUC.

**Usos de suelo no permitidos**

| Categoría | Actividades prohibidas |
|---|---|
| Residencial | Vivienda, Hospedaje |
| Equipamiento | Comercio, Educación, Salud, Seguridad, Servicios, Social |
| Actividades Productivas | Calificadas como: inofensivas, molestas, insalubres o contaminantes y peligrosas |
| Infraestructura | Edificaciones o instalaciones destinadas a Infraestructura de Transporte, Sanitaria y Energética |

---

## ÁREAS DE PROTECCIÓN DE RECURSOS DE VALOR PATRIMONIAL CULTURAL (Artículo 10, páginas 22-23)

Ver también el cuadro legal de constitución de cada área al inicio de este archivo (Art. 8). Las cinco áreas comparten la misma estructura de tabla (Usos de Suelo Permitidos / Condiciones de subdivisión y edificación / Usos de Suelo No Permitidos) que las zonas de Área Urbana.

### ZT — Zona Típica (Sector Montegrande) (página 22)

**Usos de suelo permitidos**

| Tipo | Clase | Actividades prohibidas |
|---|---|---|
| Residencial | Vivienda, Hospedaje | -- |
| Equipamiento | Científico | -- |
| Equipamiento | Comercio | Terminales de distribución |
| Equipamiento | Culto y Cultura | -- |
| Equipamiento | Deporte | Estadio, Medialuna |
| Equipamiento | Educación | Centro de Rehabilitación Conductual |
| Equipamiento | Salud | Cementerio, Crematorio |
| Equipamiento | Seguridad | Cárcel, Centro de Detención |
| Equipamiento | Servicios | -- |
| Equipamiento | Social | -- |
| Actividades Productivas | Inofensivas | Calificadas como: molestas, insalubres o contaminantes y peligrosas. Plantas de Revisión Técnica |

**Condiciones de subdivisión y edificación**

| Grupo de uso | Superficie predial mín. (m²) | Densidad bruta (Hab/Há) | Ocupación de suelo (COS) | Coef. constructibilidad | Sistema de agrupamiento | Altura máx. edif. (m) | Antejardín (m) |
|---|---|---|---|---|---|---|---|
| Residencial (Vivienda, Hospedaje) | 200 | 185 | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente |
| Equipamiento (las 9 clases de arriba) | 200 | -- | 0.6 | 1.2 | Aislado, Pareado, Continuo | 7.0 | 3.0 |
| Actividades Productivas (Inofensivas) | Sin valor específico en la fuente | -- | 0.5 | 1.0 | Aislado | 9 | 3.0 |

Área Verde y Espacio Público: Según OGUC.

Esta tabla es la que permitió confirmar, sin ambigüedad de salto de página, que "Aislado, Pareado, Continuo" es un solo valor de tres opciones para Sistema de Agrupamiento del bloque Equipamiento (ver nota metodológica y nota (\*\*) de ZH1). A diferencia de ZH1/ZH2/ZH3, aquí Actividades Productivas sí trae coeficientes propios (0.5 / 1.0 / Aislado / 9 / 3.0).

**Usos de suelo no permitidos**

| Categoría | Actividades prohibidas |
|---|---|
| Equipamiento | Esparcimiento |
| Actividades Productivas | Calificadas como: molestas, insalubres o contaminantes y peligrosas |
| Infraestructura | Edificaciones o instalaciones destinadas a Infraestructura de Transporte, Sanitaria y Energética |

---

### ZCH — Zona de Conservación Histórica (páginas 22-23)

**Usos de suelo permitidos**

| Tipo | Clase | Actividades prohibidas |
|---|---|---|
| Residencial | Vivienda, Hospedaje | -- |
| Equipamiento | Científico | -- |
| Equipamiento | Comercio | Terminales de distribución |
| Equipamiento | Culto y Cultura | -- |
| Equipamiento | Deporte | Estadio, Medialuna |
| Equipamiento | Educación | Centro de Rehabilitación Conductual |
| Equipamiento | Salud | Cementerio, Crematorio |
| Equipamiento | Seguridad | Cárcel, Centro de Detención |
| Equipamiento | Servicios | -- |
| Equipamiento | Social | -- |
| Actividad Productiva | Inofensiva | Calificadas como: molestas, insalubres o contaminantes y peligrosas. Plantas de Revisión Técnica |

**Condiciones de subdivisión y edificación**

| Grupo de uso | Superficie predial mín. (m²) | Densidad bruta (Hab/Há) | Ocupación de suelo (COS) | Coef. constructibilidad | Sistema de agrupamiento | Altura máx. edif. (m) | Antejardín (m) |
|---|---|---|---|---|---|---|---|
| Residencial (Vivienda, Hospedaje) | 270 (\*) | 185 | 0.60 | 1.2 | Sin valor específico en la fuente | 7.5 | Sin valor específico en la fuente |
| Equipamiento (las 9 clases de arriba) | 270 (\*) | -- | 0.8 | 1.6 | Continuo | 10.5 | -- |
| Actividad Productiva (Inofensiva) | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente | Sin valor específico en la fuente |

Área Verde y Espacio Público: Según OGUC.

(\*) ZCH es la única zona del rango donde Residencial y Equipamiento tienen Ocupación de Suelo y Coeficiente de Constructibilidad **distintos entre sí** (0.60/1.2 vs 0.8/1.6) en lugar de la celda combinada única vista en ZH1/ZH2/ZH3/ZT. Dado que la fuente no muestra un valor de Superficie separado junto a la fila Residencial (celda "270" impresa una sola vez, junto al bloque Equipamiento), se transcribe 270 m² como aplicable a ambos grupos siguiendo el patrón general del resto de las tablas, pero se marca esta interpretación con menor certeza que en el resto de zonas, por la ruptura del patrón en Ocupación/Constructibilidad. Antejardín "--" en Equipamiento se interpreta como "no exigido" (mismo símbolo usado en toda la tabla para "no aplica"), consistente con sistema de agrupamiento Continuo.

**Usos de suelo no permitidos**

| Categoría | Actividades prohibidas |
|---|---|
| Equipamiento | Esparcimiento |
| Actividades Productivas | Calificadas como: molestas, insalubres o contaminantes y peligrosas |
| Infraestructura | Edificaciones o instalaciones destinadas a Infraestructura de Transporte, Sanitaria y Energética |

---

### MH1 — Monumento Histórico 1: Tumba de Gabriela Mistral (página 23)

**Usos de suelo permitidos**

| Tipo | Clase | Actividades prohibidas |
|---|---|---|
| Equipamiento | Culto y Cultura | -- |
| Equipamiento | Salud | Todas, excepto: Cementerio |

**Condiciones de subdivisión y edificación**

| Grupo de uso | Superficie predial mín. (m²) | Ocupación de suelo (COS) | Coef. constructibilidad máxima | Sistema de agrupamiento | Altura máx. edif. (m) | Antejardín (m) |
|---|---|---|---|---|---|---|
| Equipamiento — Culto y Cultura | 3.000 | 0.04 | 0.04 | Aislado | 3.5 | 10 |
| Equipamiento — Salud (Cementerio) | 3.000 | 0.005 | 0.005 | Aislado | 3.5 | 10 |

(Esta tabla no trae columna de Densidad Bruta — no aplica a esta área, solo equipamiento puntual.)

Área Verde: Según OGUC.

**Usos de suelo no permitidos**

| Categoría | Actividades prohibidas |
|---|---|
| Residencial | Vivienda, Hospedaje |
| Equipamiento | Científico, Comercio, Deporte, Educación, Esparcimiento, Seguridad, Servicios, Social |
| Actividades Productivas | Calificadas como: inofensivas, molestas, insalubres o contaminantes y peligrosas |
| Infraestructura | Edificaciones o instalaciones destinadas a Infraestructura de Transporte y Energética |
| Espacio Público | -- |

---

### MH2 — Monumento Histórico 2: Casa Escuela Rural de Gabriela Mistral (página 23)

**Usos de suelo permitidos**

| Tipo | Clase | Actividades prohibidas |
|---|---|---|
| Equipamiento | Culto y Cultura | -- |

**Condiciones de subdivisión y edificación**

| Grupo de uso | Superficie predial mín. (m²) | Ocupación de suelo (COS) | Coef. constructibilidad máxima | Sistema de agrupamiento | Altura máx. edif. (m) | Antejardín (m) |
|---|---|---|---|---|---|---|
| Equipamiento — Culto y Cultura | 300 | 0.6 | 0.6 | Aislado | 4.5 | 4 |

**Usos de suelo no permitidos**

| Categoría | Actividades prohibidas |
|---|---|
| Residencial | Vivienda, Hospedaje |
| Equipamiento | Científico, Comercio, Deporte, Educación, Esparcimiento, Salud, Seguridad, Servicios, Social |
| Actividades Productivas | Calificadas como: inofensivas, molestas, insalubres o contaminantes y peligrosas |
| Infraestructura | Edificaciones o instalaciones destinadas a Infraestructura de Transporte y Energética |
| Espacio Público y Área Verde | -- |

---

### MH3 — Monumento Histórico 3: Escuela N°10, Jerónimo Godoy Villanueva (página 23)

**Usos de suelo permitidos**

| Tipo | Clase | Actividades prohibidas |
|---|---|---|
| Equipamiento | Culto y Cultura | -- |

**Condiciones de subdivisión y edificación**

| Grupo de uso | Superficie predial mín. (m²) | Ocupación de suelo (COS) | Coef. constructibilidad máxima | Sistema de agrupamiento | Altura máx. edif. (m) | Antejardín (m) |
|---|---|---|---|---|---|---|
| Equipamiento — Culto y Cultura | 1.000 | 0.5 | 0.5 | Continuo | 7.5 | -- |

**Usos de suelo no permitidos**

| Categoría | Actividades prohibidas |
|---|---|
| Residencial | Vivienda, Hospedaje |
| Equipamiento | Científico, Comercio, Deporte, Educación, Esparcimiento, Salud, Seguridad, Servicios, Social |
| Actividades Productivas | Calificadas como: inofensivas, molestas, insalubres o contaminantes y peligrosas |
| Infraestructura | Edificaciones o instalaciones destinadas a Infraestructura de Transporte y Energética |
| Espacio Público y Área Verde | -- |

---

## ÁREAS RESTRINGIDAS AL DESARROLLO URBANO / ÁREAS DE RIESGO (Artículo 11, página 23)

> Texto del Art. 11: *"Por constituir un peligro potencial para los asentamientos humanos, se establecen las siguientes Áreas de Riesgo."*

| Sigla | Condición de riesgo |
|---|---|
| AR1 | Inundables o Potencialmente Inundables por proximidad a Ríos y Quebradas |
| AR2 | Propensas a Avalanchas, Rodados, Aluviones o Erosiones Acentuadas |

**Régimen normativo aplicable (no traen cuadro propio de superficie/COS/altura):** el Art. 11 no fija parámetros de subdivisión o edificación distintos para AR1/AR2. En su lugar, remite a la zona subyacente. Texto literal: *"Las normas urbanísticas aplicables a los proyectos localizados en estas áreas y que cumplan los requisitos establecidos en el inciso quinto del artículo 2.1.17 de la Ordenanza General de Urbanismo y Construcciones, serán las correspondientes a la zona donde se emplaza el proyecto según los planos señalados en el art.1 de esta OL y cuyas normas urbanísticas se detallan en los Arts. 9 y 10 precedentes."*

En otras palabras: AR1 y AR2 son polígonos de restricción superpuestos a las zonas de Área Urbana (Art. 9) o de Protección Patrimonial (Art. 10); un proyecto dentro de AR1/AR2 que cumpla los requisitos del art. 2.1.17 inciso quinto de la OGUC (norma que regula la edificación en áreas de riesgo mitigadas o con estudio fundado) se rige por los parámetros de la zona de base (ZH1, ZH2, ZH3, ZD, ZT1, ZT2, ZAP, ZIS, ZAV, ZT, ZCH, MH1, MH2 o MH3, según corresponda al polígono) ya transcritos arriba, no por una tabla propia de AR1/AR2.

---

## Fuera de alcance de este archivo (confirmado, no se transcribe aquí)

- **Página 18** — estándares de estacionamiento: no es norma de zona (superficie/COS/altura), y además queda fuera del rango de páginas asignado a esta extracción (19-23).
- **Página 24** — vialidad: mismo criterio, fuera del rango asignado.

---

## Resumen de confianza y nota de verificación de imagen

- **Total de zonas/áreas transcritas:** 16 — 9 de Área Urbana (ZH1, ZH2, ZH3, ZD, ZT1, ZT2, ZAP, ZIS, ZAV), 5 de Protección de Recursos de Valor Patrimonial Cultural (ZT, ZCH, MH1, MH2, MH3) y 2 Áreas de Riesgo (AR1, AR2).
- **Método:** las 5 páginas (19 a 23) se examinaron primero a resolución completa y luego con recortes ampliados (PIL, factor 1.8×-3.5×) sobre cada tabla, cabecera de columnas y, en particular, sobre las celdas combinadas y los bordes entre filas, para confirmar de forma visual —no solo por posición aproximada del texto— qué valores están realmente combinados entre filas/columnas y cuáles son distintos. Se usó la Zona Típica (ZT, Art. 10) y ZH2/ZH3/ZAP, que no quedan partidas por un salto de página, como referencia cruzada para resolver con confianza el patrón de combinación de celdas de ZH1 y ZCH, que sí quedan partidas entre dos páginas.
- **Alta confianza:** ZH2, ZH3, ZD, ZT1, ZT2, ZAP, ZIS, ZAV, ZT, MH1, MH2, MH3 y el cuadro AR1/AR2 — tablas completas en una sola página o sin ambigüedad de combinación de celdas, todos los valores confirmados con zoom.
- **Confianza media (valores transcritos con nota explícita de la interpretación aplicada, no de ilegibilidad):** ZH1 (Sistema de Agrupamiento y Superficie predial mínima reconstruidos a través del salto de página p.19/p.20, con respaldo cruzado en la plantilla idéntica de ZT) y ZCH (Superficie predial mínima 270 m² con incertidumbre sobre si aplica también a Residencial, dado que esta zona rompe el patrón general en Ocupación de Suelo/Constructibilidad).
- **Ningún valor fue inventado ni interpolado sin marcarlo.** Todas las celdas que la fuente deja en blanco se transcriben como "Sin valor específico en la fuente"; no hubo celdas realmente ilegibles que ameritaran "Dato no determinable" en este rango — la dificultad encontrada fue de estructura de tabla (celdas combinadas y saltos de página), no de nitidez de imagen; los 5 renders están nítidos y a resolución suficiente (2125×3250 px) para leer todos los dígitos con zoom.
- **Contenido ajeno detectado en el rango 19-23:** ninguno. Las 5 páginas corresponden íntegramente al Decreto N°862 / PRC de Paihuano, con el mismo pie de imprenta consecutivo (CVE 1618610, Núm. 42.400, 10 de julio de 2019, páginas 19 a 23 de 25).
