# Plan Regulador Comunal de Molina (Decreto N°52, 2022)

**Comuna:** Molina
**Instrumento:** Decreto N°52, "Promulga Plan Regulador Comunal de Molina y Deja sin Efecto Resoluciones Afectas", Diario Oficial N° 43.420, publicación miércoles 7 de diciembre de 2022

## Contexto

**Trampa TEXTO/imagen confirmada.** Se ejecutó `pdftotext -layout -f 15 -l 21` sobre el PDF fuente y el resultado confirma la advertencia de Fase 3: el texto extraíble recupera perfectamente los títulos y encabezados de cada zona (p. ej. "ZU-1 ZONA MIXTA 1", "ZE-3 ZONA DE EQUIPAMIENTO 3") y los párrafos narrativos (Art. 3.6, Art. 4.1, Art. 4.2), pero en el lugar donde debería aparecer cada cuadro normativo (usos de suelo, COS, CC, altura, sistema de agrupamiento, antejardín, densidad) solo hay una **página en blanco** en el `.txt` — ninguna cifra de COS/CC/altura es recuperable por extracción directa de texto. Las tablas están insertadas como imagen dentro del PDF nativo del Diario Oficial digital. Se procedió a render visual con `pdftoppm -f 15 -l 21 -r 200 -png` y lectura página por página a 200dpi.

**Zonificación completa según Art. 4.2 (página 15):**

ÁREA URBANA (16 zonas): ZU-1, ZU-2, ZU-2b, ZU-3, ZU-4, ZU-5, ZU-6, ZU-7, ZE-1, ZE-2, ZE-3, ZE-4, ZE-5, ZE-6, ZAP, ZAV.
ÁREA DE PROTECCIÓN DE RECURSOS DE VALOR NATURAL: ZPL (Zona de Protección Legal Parque Nacional Radal Siete Tazas).
ÁREAS DE PROTECCIÓN DE RECURSOS DE VALOR PATRIMONIAL CULTURAL: ICH (Inmuebles de Conservación Histórica).

Nota: el listado real del Art. 4.2 incluye **ZU-2b** (zona intermedia no mencionada explícitamente en el encargo de esta tarea, pero presente en el documento) además de las 15 zonas mínimas esperadas. Total: 18 unidades de zonificación.

**Cobertura lograda dentro del rango páginas 15-21 (Art. 4.3, "Normas Urbanísticas por Zona"):**

Las 16 zonas de ÁREA URBANA (ZU-1 a ZU-7 incluyendo ZU-2b, ZE-1 a ZE-6, ZAP y ZAV) tienen su cuadro completo de usos de suelo y normas de edificación **íntegramente contenido** dentro del rango páginas 16-21 (algunas tablas cruzan el salto de página, p. ej. ZU-2b entre p.16-17, ZU-5 entre p.17-18, ZE-4 entre p.19-20, ZAP entre p.20-21; en todos los casos se verificó visualmente la continuidad de la tabla en la página siguiente antes de darla por completa).

ZPL también tiene su cuadro completo (identificación de las 2 áreas protegidas) dentro del rango, en la página 21.

**ICH queda incompleta dentro del rango**: la tabla de inmuebles de conservación histórica comienza en la página 21 (se alcanzan a listar ICH 1 a ICH 11) pero continúa más allá de la página 21 — la página 22 es Título 5 "Vialidad" y estaba explícitamente fuera del rango asignado, por lo que no fue transcrita. No se puede confirmar si ICH 11 es el último inmueble de la lista o si hay más registros en la página 22.

---

## ZONA ZU-1 (ZONA MIXTA 1)

### Usos de suelo

| Tipos | Destino/Clases | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Todos los destinos de este uso. | - |
| EQUIPAMIENTO | Científico | Grupo 1 | - |
| EQUIPAMIENTO | Comercio | Grupo 1, 2, 3 y 4 | Estaciones o centros de Servicio Automotor. |
| EQUIPAMIENTO | Culto y Cultura | Grupo 1, 2, 3 y 4 | - |
| EQUIPAMIENTO | Deporte | Grupo 2 | Centros Deportivos, Multicanchas. |
| EQUIPAMIENTO | Educación | Grupo 1, 2, 3 y 4 | Centros de rehabilitación conductual. |
| EQUIPAMIENTO | Esparcimiento | Grupo 1 | - |
| EQUIPAMIENTO | Salud | Grupo 1, 2 y 3 | - |
| EQUIPAMIENTO | Seguridad | Grupo 1, 2 y 3 | - |
| EQUIPAMIENTO | Servicios | Grupo 1, 2 y 3 | - |
| EQUIPAMIENTO | Social | Grupo 1 y 2 | - |

### Normas de subdivisión y edificación

| Norma | Residencial | Equipamiento |
|---|---|---|
| Superficie de subdivisión predial mínima | 300 m² (única) | 300 m² (única) |
| Coeficiente de ocupación de suelo | 0,5 | 1 |
| Coeficiente de constructibilidad | 1 | 1,2 |
| Sistema de agrupamiento | Continuo | Continuo |
| Altura máxima de edificación | 8 m | 13 m |
| Densidad bruta máxima | 50 hab/ha | - |

---

## ZONA ZU-2 (ZONA MIXTA 2)

### Usos de suelo

| Tipos | Destino/Clases | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Todos los destinos de este uso. | - |
| EQUIPAMIENTO | Comercio | Grupo 1, 2, 3 y 4 | Estaciones o centros de servicio automotor |
| EQUIPAMIENTO | Culto y Cultura | Grupo 1, 2 y 3 | Edificios de Culto, Cines, Teatros, Auditorios, Centros de difusión de toda especie, Medios de comunicación, tales como canales de televisión, radio y prensa escrita |
| EQUIPAMIENTO | Deporte | Grupo 1, 2 y 3 | - |
| EQUIPAMIENTO | Educación | Grupo 1, 2 y 3 | Academias, Centros de rehabilitación conductual. |
| EQUIPAMIENTO | Esparcimiento | Grupo 1, 2, 3 y 4 | - |
| EQUIPAMIENTO | Salud | Grupo 1, 2 y 3 | Centros de rehabilitación ambulatoria |
| EQUIPAMIENTO | Seguridad | Grupo 1, 2 y 3 | - |
| EQUIPAMIENTO | Servicios | Grupo 1, 2 y 3 | - |
| EQUIPAMIENTO | Social | Grupo 1, 2 y 3 | - |

### Normas de subdivisión y edificación

| Norma | Residencial | Equipamiento |
|---|---|---|
| Superficie de subdivisión predial mínima | 300 m² (única) | 300 m² (única) |
| Coeficiente de ocupación de suelo | 0,4 | 0,5 |
| Coeficiente de constructibilidad | 0,8 | 1,0 |
| Altura máxima de edificación | 8 m aislado-Pareado y 8 m Continuo | 11 m |
| Sistema de agrupamiento | Aislado - Pareado - Continuo | Aislado |
| Densidad bruta máxima | 120 hab/ha | - |

---

## ZONA ZU-2b (ZONA MIXTA 2b)

### Usos de suelo

| Tipos | Destino/Clases | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Todos los destinos de este uso. | Hogares de Acogida |
| EQUIPAMIENTO | Comercio | Grupo 1, 2 y 3 | - |
| EQUIPAMIENTO | Culto y Cultura | Grupo 1, 2, 3 y 4 | - |
| EQUIPAMIENTO | Deporte | Grupo 1, 2 y 3 | - |
| EQUIPAMIENTO | Educación | Grupo 1, 2 y 3 | Centros de rehabilitación conductual. |
| EQUIPAMIENTO | Esparcimiento | Grupo 1, 2, 3 y 4 | - |
| EQUIPAMIENTO | Salud | Grupo 1 y 2 | - |
| EQUIPAMIENTO | Seguridad | Grupo 1, 2 y 3 | - |
| EQUIPAMIENTO | Servicios | Grupo 1, 2 y 3 | - |
| EQUIPAMIENTO | Social | Grupo 1 y 2 | - |

### Normas de subdivisión y edificación

| Norma | Residencial | Equipamiento |
|---|---|---|
| Superficie de subdivisión predial mínima | 500 m² (única) | 500 m² (única) |
| Coeficiente de ocupación de suelo | 0,2 | 0,4 |
| Coeficiente de constructibilidad | 1,5 | 1,0 |
| Altura máxima de edificación | 11 m | 11 m |
| Sistema de agrupamiento | Aislado | Aislado |
| Antejardín | 5 m | 5 m |
| Densidad bruta máxima | 80 hab/ha | - |

*(Nota: tabla verificada de forma cruzada contra `molina_2922_modificacion_zu_zap.md` — decreto posterior de modificación N°2.922/2023 — cuyo cuadro "Actual" para ZU-2b coincide exactamente con estos valores, confirmando la lectura visual.)*

---

## ZONA ZU-3 (ZONA MIXTA RESIDENCIAL 3)

### Usos de suelo

| Tipos | Destino/Clases | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Todos los destinos de este uso. | - |
| EQUIPAMIENTO | Comercio | Grupo 1 y 2 | Restaurantes, Fuentes de Soda |
| EQUIPAMIENTO | Culto y Cultura | Grupo 1 y 2 | - |
| EQUIPAMIENTO | Deporte | Grupo 1 y 3 | Piscinas |
| EQUIPAMIENTO | Educación | Grupo 1, 2 y 3 | Establecimientos destinados principalmente a la formación o capacitación en educación superior, técnica, Centros de rehabilitación conductual. |
| EQUIPAMIENTO | Esparcimiento | Grupo 1 | - |
| EQUIPAMIENTO | Salud | Grupo 1 y 2 | - |
| EQUIPAMIENTO | Seguridad | Grupo 1, 2 y 3 | - |
| EQUIPAMIENTO | Servicios | Grupo 1 y 2 | Oficinas, Notarías |
| EQUIPAMIENTO | Social | Grupo 1 y 2 | - |

### Normas de subdivisión y edificación

| Norma | Residencial | Equipamiento |
|---|---|---|
| Superficie de subdivisión predial mínima | 160 m² (única) | 160 m² (única) |
| Coeficiente de ocupación de suelo | 0,4 | 0,4 |
| Coeficiente de constructibilidad | 0,6 | 0,6 |
| Altura máxima de edificación | 8 m | 8 m |
| Sistema de agrupamiento | Continuo | Aislado, Pareado |
| Densidad bruta máxima | 200 hab/ha | - |

---

## ZONA ZU-4 (ZONA MIXTA RESIDENCIAL 4)

### Usos de suelo

| Tipos | Destino/Clases | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Todos los destinos de este uso. | - |
| EQUIPAMIENTO | Comercio | Grupo 1 y 2 | Restaurantes, Fuentes de Soda |
| EQUIPAMIENTO | Culto y Cultura | Grupo 1, 2, 3 y 4 | - |
| EQUIPAMIENTO | Deporte | Grupo 1, 2 y 3 | - |
| EQUIPAMIENTO | Educación | Grupo 1, 2 y 3 | Establecimientos destinados principalmente a la formación o capacitación en educación superior, técnica, Centros de rehabilitación conductual. |
| EQUIPAMIENTO | Esparcimiento | Grupo 1 | - |
| EQUIPAMIENTO | Salud | Grupo 1 y 2 | - |
| EQUIPAMIENTO | Seguridad | Grupo 1, 2 y 3 | - |
| EQUIPAMIENTO | Social | Grupo 1 y 2 | - |

### Normas de subdivisión y edificación

| Norma | Residencial | Equipamiento |
|---|---|---|
| Superficie de subdivisión predial mínima | 160 m² (única) | 160 m² (única) |
| Coeficiente de ocupación de suelo | 0,6 | 0,5 |
| Coeficiente de constructibilidad | 0,8 | 1,0 |
| Altura máxima de edificación | 8 m | 8 m |
| Sistema de agrupamiento | Aislado, Pareado | Aislado, Pareado |
| Antejardín | 3 m | 3 m |
| Densidad bruta máxima | 160 hab/ha | - |

---

## ZONA ZU-5 (ZONA MIXTA RESIDENCIAL 5)

### Usos de suelo

| Tipos | Clasificación/Destino/Clases | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Todos los destinos de este uso. | - |
| ACTIVIDADES PRODUCTIVAS | Inofensiva | Talleres y bodegas de tipo inofensivo | Industria y toda instalación de impacto similar al Industrial sólo las calificadas como molestas, insalubres o contaminantes. |
| EQUIPAMIENTO | Científico | Grupo 1 | - |
| EQUIPAMIENTO | Comercio | Grupo 1, 2, 3 y 4 | - |
| EQUIPAMIENTO | Culto y Cultura | Grupo 1, 2, 3 y 4 | - |
| EQUIPAMIENTO | Deporte | Grupo 1, 2, 3 y 4 | - |
| EQUIPAMIENTO | Educación | Grupo 1, 2, 3 y 4 | - |
| EQUIPAMIENTO | Esparcimiento | Grupo 1, 2, 3 y 4 | Parques Zoológicos |
| EQUIPAMIENTO | Salud | Grupo 1, 2 y 3 | - |
| EQUIPAMIENTO | Seguridad | Grupo 1, 2 y 3 | - |
| EQUIPAMIENTO | Servicios | Grupo 1, 2 y 3 | - |
| EQUIPAMIENTO | Social | Grupo 1 y 2 | - |

### Normas de subdivisión y edificación

*(tabla de columna única, aplica por igual sin distinción Residencial/Equipamiento)*

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 500 m² |
| Coeficiente de ocupación de suelo | 0,5 |
| Coeficiente de constructibilidad | 1,0 |
| Altura máxima de edificación | 11 m |
| Sistema de agrupamiento | Aislado, Pareado |
| Antejardín | 3 m |
| Densidad bruta máxima | 80 hab/ha |

---

## ZONA ZU-6 (ZONA MIXTA RESIDENCIAL 6)

### Usos de suelo

| Tipos | Destino/Clases | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Todos los destinos de este uso. | - |
| EQUIPAMIENTO | Comercio | Grupo 1, 2 y 3 | Estaciones o centros de servicio automotor |
| EQUIPAMIENTO | Culto y Cultura | Grupo 1, 2 y 3 | Edificios de Culto, Salas de concierto o espectáculos, Cines, Teatros, Auditorios, Centros de eventos, Centros de convenciones, Centros de exposiciones, Centros de difusión de toda especie, Medios de comunicación, tales como canales de televisión, radio y prensa escrita |
| EQUIPAMIENTO | Deporte | Grupo 1, 2 y 3 | - |
| EQUIPAMIENTO | Educación | Grupo 1, 2 y 3 | Academias, Institutos, Universidades. Centros de rehabilitación conductual. |
| EQUIPAMIENTO | Esparcimiento | Grupo 1, 2, 3 y 4 | Casinos |
| EQUIPAMIENTO | Salud | Grupo 1 y 2 | - |
| EQUIPAMIENTO | Seguridad | Grupo 1, 2 y 3 | - |
| EQUIPAMIENTO | Servicios | Grupo 1 y 2 | Notarías, Correos, Telégrafos, Centros de Pago. |
| EQUIPAMIENTO | Social | Grupo 1 y 2 | - |

### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 800 m² |
| Coeficiente de ocupación de suelo | 0,3 |
| Coeficiente de constructibilidad | 0,6 |
| Altura máxima de edificación | 8 m |
| Sistema de agrupamiento | Aislado - Pareado |
| Antejardín | 3 m |
| Densidad bruta máxima | 40 hab/ha |

---

## ZONA ZU-7 (ZONA MIXTA RESIDENCIAL 7)

### Usos de suelo

| Tipos | Destino/Clases | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Todos los destinos de este uso. | - |
| EQUIPAMIENTO | Científico | Grupo 1 | - |
| EQUIPAMIENTO | Culto y Cultura | Grupo 1, 2, 3 y 4 | Edificios de Culto |

### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 2.500 m² |
| Coeficiente de ocupación de suelo | 0,1 |
| Coeficiente de constructibilidad | 0,2 |
| Altura máxima de edificación | 8 m |
| Sistema de agrupamiento | Aislado |
| Antejardín | 5 m |
| Densidad bruta máxima | 12 hab/ha |

*(Nota: se verificó que esta es la tabla completa para ZU-7 — el listado de equipamiento permitido en esta zona es intencionalmente muy restringido, consistente con los parámetros de baja densidad de la tabla de edificación.)*

---

## ZONA ZE-1 (ZONA DE EQUIPAMIENTO 1)

### Usos de suelo

| Tipos | Destino/Clases | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Edificaciones y locales destinados al hospedaje | Vivienda, Hogares de Acogida. |
| EQUIPAMIENTO | Comercio | Grupo 1 y 2 | - |
| EQUIPAMIENTO | Culto y Cultura | Grupo 1, 2, 3 y 4 | Edificios de Culto |
| EQUIPAMIENTO | Deporte | Grupo 1, 2, 3 y 4 | - |
| EQUIPAMIENTO | Educación | Grupo 3 | Liceos, Colegios, Academias, Institutos, Universidades. Centros de rehabilitación conductual. |
| EQUIPAMIENTO | Esparcimiento | Grupo 1, 2, 3 y 4 | Casinos |

### Normas de subdivisión y edificación

| Norma | Residencial | Equipamiento |
|---|---|---|
| Superficie de subdivisión predial mínima | 500 m² (única) | 500 m² (única) |
| Coeficiente de ocupación de suelo | 0,4 | 0,2 |
| Coeficiente de constructibilidad | 0,8 | 0,4 |
| Altura máxima de edificación | 7 m | 7 m |
| Sistema de agrupamiento | Aislado | Aislado |
| Antejardín | 5 m | 5 m |
| Densidad bruta máxima | 80 hab/ha | - |

---

## ZONA ZE-2 (ZONA DE EQUIPAMIENTO 2)

### Usos de suelo

| Tipos | Clases | Permitidos | Excepto |
|---|---|---|---|
| EQUIPAMIENTO | Culto y Cultura | Grupo 2 y 3 | Edificios de Culto, Museos, Cines Teatros |
| EQUIPAMIENTO | Deporte | Grupo 1, 2, 3 y 4 | - |
| EQUIPAMIENTO | Esparcimiento | Grupo 1, 2, 3 y 4 | - |

### Normas de subdivisión y edificación

*(tabla de columna única)*

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 1.000 m² |
| Coeficiente de ocupación de suelo | 0,1 |
| Coeficiente de constructibilidad | 0,2 |
| Altura máxima de edificación | 7 m |
| Sistema de agrupamiento | Aislado |

---

## ZONA ZE-3 (ZONA DE EQUIPAMIENTO 3)

### Usos de suelo

| Tipos | Clases | Permitidos | Excepto |
|---|---|---|---|
| EQUIPAMIENTO | Culto y Cultura | Grupo 1 | - |
| EQUIPAMIENTO | Salud | Grupo 4 | - |

### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 1.000 m² |
| Coeficiente de ocupación de suelo | 0,1 |
| Coeficiente de constructibilidad | 0,2 |
| Altura máxima de edificación | 7 m |
| Sistema de agrupamiento | Aislado |

---

## ZONA ZE-4 (ZONA DE EQUIPAMIENTO 4)

### Usos de suelo

| Tipos | Destino/Clases | Permitidos | Excepto |
|---|---|---|---|
| INFRAESTRUCTURA | Transporte | Terminales de transporte terrestre y Estaciones Ferroviarias | - |
| INFRAESTRUCTURA | Sanitaria | Plantas de captación, distribución o tratamiento de agua potable o de aguas servidas, de aguas lluvia. | - |
| INFRAESTRUCTURA | Energética | Todas las actividades de esta clase | Centrales de generación energía |
| EQUIPAMIENTO | Científico | Grupo 1 | - |
| EQUIPAMIENTO | Comercio | Grupo 2 | - |
| EQUIPAMIENTO | Culto y Cultura | Grupo 1, 2, 3 y 4 | Edificios de Culto, Bibliotecas, Cines, Teatros, Medios de comunicación, tales como canales de televisión, radio y prensa escrita. |
| EQUIPAMIENTO | Deporte | Grupo 1 y 3 | - |
| EQUIPAMIENTO | Seguridad | Grupo 1, 2 y 3 | - |

### Normas de subdivisión y edificación

| Norma | Equipamiento | Infraestructura |
|---|---|---|
| Superficie de subdivisión predial mínima | 1.000 m² (única) | 1.000 m² (única) |
| Coeficiente de ocupación de suelo | 0,5 | 0,1 |
| Coeficiente de constructibilidad | 0,7 | 0,1 |
| Altura máxima de edificación | 7 m | - |
| Sistema de agrupamiento | Aislado | Aislado |
| Distanciamiento | 5 m (única) | 5 m (única) |
| Antejardín | 5 m | 10 m |

---

## ZONA ZE-5 (ZONA DE EQUIPAMIENTO 5)

### Usos de suelo

| Tipos | Destino/Clases | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Edificaciones y locales destinados al hospedaje | Vivienda, Hogares de Acogida. |
| EQUIPAMIENTO | Científico | Grupo 1 | - |
| EQUIPAMIENTO | Comercio | Grupo 2 | - |
| EQUIPAMIENTO | Culto y Cultura | Grupo 1, 2, 3 y 4 | Edificios de Culto, Cines, Teatros, Medios de comunicación, tales como canales de televisión, radio y prensa escrita |
| EQUIPAMIENTO | Esparcimiento | Grupo 1 y 3 | Parques de entretenciones y Juegos electrónicos. |
| EQUIPAMIENTO | Seguridad | Grupo 1, 2 y 3 | - |

### Normas de subdivisión y edificación

*(tabla de columna única)*

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 2.500 m² |
| Coeficiente de ocupación de suelo | 0,05 |
| Coeficiente de constructibilidad | 0,05 |
| Altura máxima de edificación | 8 m |
| Sistema de agrupamiento | Aislado |
| Distanciamiento | 5 m |
| Antejardín | 10 m |

---

## ZONA ZE-6 (ZONA DE EQUIPAMIENTO 6)

### Usos de suelo

| Tipos | Clases | Permitidos | Excepto |
|---|---|---|---|
| EQUIPAMIENTO | Científico | Grupo 1 | - |
| EQUIPAMIENTO | Culto y Cultura | Grupo 1, 2, 3 y 4 | - |
| EQUIPAMIENTO | Deporte | Grupo 1 y 3 | - |
| EQUIPAMIENTO | Esparcimiento | Grupo 3 y 4 | - |

### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 1.000 m² |
| Coeficiente de ocupación de suelo | 0,1 |
| Coeficiente de constructibilidad | 0,1 |
| Altura máxima de edificación | 3,5 m |
| Sistema de agrupamiento | Aislado |
| Antejardín | 10 m |

---

## ZONA ZAP (ZONA DE ACTIVIDAD PRODUCTIVA)

### Usos de suelo

| Tipos | Clasificación/Destino/Clases | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Vivienda | Hogares de Acogida, Edificaciones y locales destinados al hospedaje |
| ACTIVIDADES PRODUCTIVAS | Inofensiva | Industria y toda instalación de impacto similar al Industrial sólo las calificadas como Inofensivas. Grandes Depósitos, Talleres o Bodegas Industriales | Industria y toda instalación de impacto similar al Industrial sólo las calificadas como molestas, insalubres o contaminantes. |
| INFRAESTRUCTURA | Transporte | Terminales de transporte terrestre | Estaciones Ferroviarias, Recintos marítimos o portuarios, Recintos aeroportuarios |
| INFRAESTRUCTURA | Sanitaria | Plantas de captación, distribución o tratamiento de agua potable o de aguas servidas, de aguas lluvia. | Rellenos sanitarios, vertederos, botaderos, almacenamiento y acopios de Cenizas, Plantas de tratamiento de residuos industriales, Estaciones exclusivas de transferencia de residuos |
| INFRAESTRUCTURA | Energética | Todas las actividades de esta clase | Centrales de generación energía |
| EQUIPAMIENTO | Comercio | Grupo 2 y 4 | - |
| EQUIPAMIENTO | Deporte | Grupo 1, 2, 3 y 4 | - |
| EQUIPAMIENTO | Seguridad | Grupo 1, 2 y 3 | - |

### Normas de subdivisión y edificación

| Norma | Residencial | Equipamiento | Actividades Productivas / Infraestructura |
|---|---|---|---|
| Superficie de subdivisión predial mínima | 600 m² (única para todas) | 600 m² (única para todas) | 600 m² (única para todas) |
| Coeficiente de ocupación de suelo | 0,2 | 0,2 | 0,4 |
| Coeficiente de constructibilidad | 0,2 | 0,2 | 0,8 |
| Altura máxima de edificación | 8 m | 8 m | 11 m |
| Sistema de agrupamiento | Aislado | Aislado | Aislado |
| Distanciamiento | - | 5 m | 5 m |
| Antejardín | - | 5 m | 10 m |
| Densidad bruta máxima | 30 hab/ha | - | - |

*(Nota: COS/CC/Altura/Sistema comparten el mismo valor entre Residencial y Equipamiento en la tabla original — la columna "Actividades Productivas/Infraestructura" trae el valor diferenciado.)*

---

## ZONA ZAV (ZONA ÁREA VERDE)

### Usos de suelo

| Tipo de uso | Destino | Permitidos |
|---|---|---|
| ÁREA VERDE | Complementarias y compatibles según OGUC | Equipamiento científico, Culto y Cultura, Deporte y Esparcimiento |

### Normas de subdivisión y edificación

*(tabla de columna única; no incluye fila de Coeficiente de Ocupación de Suelo — no aparece en el cuadro original de esta zona, no se asume valor)*

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 2.500 m² |
| Coeficiente de constructibilidad | 0,1 |
| Altura máxima de edificación | 3,5 m |
| Sistema de agrupamiento | Aislado |
| Antejardín | 10 m |

---

## ÁREA DE PROTECCIÓN DE RECURSOS DE VALOR NATURAL

## ZONA ZPL (ZONA DE PROTECCIÓN LEGAL)

Corresponde a las áreas reconocidas por el presente Plan en las que existen zonas o elementos naturales protegidos por el ordenamiento jurídico vigente. Esta zona no tiene cuadro de usos de suelo/edificación (COS, CC, altura, etc.) — su tabla normativa es de identificación de las áreas protegidas:

| Identificación | Localidad | Decreto |
|---|---|---|
| Parque Nacional Radal Siete Tazas | Radal | Decreto N°15, 27.MAR.2008, Ministerio de Bienes Nacionales. |
| Reserva Nacional Siete Tazas | Siete Taza | Decreto N°89, 20.MAR.1996, Ministerio de Bienes Nacionales. |

Tabla completa dentro del rango (2 registros, sin indicios de continuación en página 22).

---

## ÁREAS DE PROTECCIÓN DE RECURSOS DE VALOR PATRIMONIAL CULTURAL

## ZONA ICH (INMUEBLES DE CONSERVACIÓN HISTÓRICA) — INCOMPLETA EN EL RANGO

Los Inmuebles establecidos de Conservación Histórica por el presente Plan, en conformidad a lo que establece la LGUC y la OGUC, son los que se indican a continuación. Esta tabla **NO alcanzó a completarse dentro del rango páginas 15-21**: en la página 21 (última página del rango asignado) se alcanzan a leer los registros ICH 1 a ICH 11, y la tabla continúa visiblemente más allá del pie de página 21. La página 22 es Título 5 "Vialidad" según lo indicado en el encargo y quedó fuera del rango — por lo tanto **no se transcribió** y no se puede confirmar si existen más inmuebles (ICH 12 en adelante) en esa página.

| N° | Identificación | Ubicación | Localidad | Rol Predial |
|---|---|---|---|---|
| ICH 1 | Iglesia Parroquial Nuestra Señora del Tránsito | Calle Quechereguas N°1819 Esquina Yerbas Buenas | Molina | 114-1 |
| ICH 2 | Casa Patrimonial Maritza Zúñiga y Otros | Calle Maipú N°1818 Esquina Yerbas Buenas | Molina | 113-9 |
| ICH 3 | Casa Patrimonial Olivia Olave | Calle Maipú N°1898 Esquina Luis Cruz Martínez | Molina | 113-13 |
| ICH 4 | Casa Patrimonial Esquina Quechereguas | Calle Quechereguas Esquina Camino a Itahue | Molina | 607-6 |
| ICH 5 | El Chalet | Calle Quechereguas Esquina Camino A Itahue, Sector Santa Elsa-Cerrillo Bascuñán. | Molina | 612-3 |
| ICH 6 | Parroquia San Bonifacio, Lontué | Plazuela Lontué, Lontué. | Lontué | 441-5 |
| ICH 7 | Casa Esquina Av. 7 de Abril | Av. 7 de Abril Esquina Vial, Lontué. | Lontué | 462-2 |
| ICH 8 | Antigua Escuela de Lontué | Luz Pereira S/N° Esquina Echeverría, Lontué. | Lontué | 481-1 |
| ICH 9 | Casa Tipo Castillo | Lote 1 Luz Pereira N°1976, Lontué. | Lontué | 450-1 |
| ICH 10 | Casona Esquina Propiedad de Doña Susana Espinoza | Luz Pereira N°1986 Esquina Av. 7 de Abril, Lontué. | Lontué | 450-2 |
| ICH 11 | Casona Esquina Propiedad de Don Jorge Estay | Avenida 7 de Abril S/N° Esquina Luz Pereira, Lontué. | Lontué | 460-8 |

**IMPORTANTE — datos ausentes no inventados:** cualquier registro ICH posterior a ICH 11 (si existe) NO fue transcrito por quedar fuera del rango de páginas asignado (15-21). No se debe asumir que ICH 11 es el último registro de la tabla.

---

## Nota final de fuente y método

- **Fuente:** Diario Oficial de la República de Chile, Núm. 43.420, miércoles 7 de diciembre de 2022, páginas 15 a 21 de 30 (Decreto N°52, "Promulga Plan Regulador Comunal de Molina y Deja sin Efecto Resoluciones Afectas", Art. 4.1 a 4.3 de la Ordenanza Local). CVE 2225537.
- **Método:** (1) `pdftotext -layout -f 15 -l 21` confirmó que las tablas normativas están insertadas como imagen (solo se recuperan títulos y párrafos narrativos, ninguna cifra de COS/CC/altura); (2) render visual con `pdftoppm -f 15 -l 21 -r 200 -png` y lectura manual página por página, con recortes ampliados (zoom) en celdas de lectura ambigua (tablas de ZU-2 y ZAP) para verificación adicional; (3) validación cruzada de ZU-2b contra el archivo `molina_2922_modificacion_zu_zap.md` (decreto de modificación posterior, N°2.922/2023), que reproduce el cuadro "Actual" de ZU-2b con valores idénticos a los aquí transcritos.
- **Confianza:** ALTA para las 16 zonas de Área Urbana (ZU-1 a ZU-7 incluido ZU-2b, ZE-1 a ZE-6, ZAP, ZAV) y para ZPL — todas tienen su cuadro completo dentro del rango, leído visualmente a 200dpi sin ambigüedad tipográfica relevante.
- **Zonas del Art. 4.2 (página 15) que NO alcanzaron a tener cuadro completo dentro del rango 15-21:**
  - **ICH (Inmuebles de Conservación Histórica):** tabla de identificación de inmuebles patrimoniales incompleta — se transcribieron ICH 1 a ICH 11 (los únicos visibles antes del corte de página), pero la lista continúa en la página 22, fuera del rango asignado, por lo que el listado completo de inmuebles ICH no está disponible en esta extracción.
- **Todas las demás zonas listadas en el Art. 4.2** (ZU-1, ZU-2, ZU-2b, ZU-3, ZU-4, ZU-5, ZU-6, ZU-7, ZE-1, ZE-2, ZE-3, ZE-4, ZE-5, ZE-6, ZAP, ZAV, ZPL) tienen su cuadro completo transcrito arriba, sin datos inventados ni asumidos.