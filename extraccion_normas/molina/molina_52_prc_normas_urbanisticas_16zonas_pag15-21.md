# Normas Urbanísticas — Plan Regulador Comunal de Molina (Decreto N° 52)

**Fuente:** Decreto N° 52, Municipalidad de Molina, "Promulga Plan Regulador Comunal de Molina y deja sin efecto resoluciones afectas" (Diario Oficial N° 43.420, miércoles 7 de diciembre de 2022)
**Documento (registro Fase 3/4):** id `molina_b33b044b0c` — `Ordenanzas ordenadas\OCR ok\molina_52_promulga_plan_regulador_comunal_de_molina_y_deja_sin_efecto_resoluciones_afec__Publicacion-del-Miercoles-7-de-Diciembre-de-2022-DIARIO-OFICIAL.pdf`
**Extracción:** páginas 15-21 de 30 — Título 4 "Áreas Restringidas y Zonificación": Art. 4.1 (áreas restringidas, sin tabla), Art. 4.2 (zonificación, listado de zonas) y Art. 4.3 (normas urbanísticas por zona, tablas completas). La página 22 ya es Título 5 "Vialidad" (fuera de rango).
**Método:** VISUAL — lectura directa de las 7 imágenes PNG renderizadas a 250 dpi. El `.txt` de apoyo NO se usó para los valores numéricos (ver Nota de alcance).

---

## Nota de alcance (léase antes que las tablas)

**"Trampa nueva" confirmada:** el veredicto automático de la página es TEXTO en promedio porque `pdftotext` extrae con normalidad los encabezados de artículo y los nombres/códigos de zona, pero **todas las tablas de Art. 4.3 (usos de suelo y normas de subdivisión y edificación) están insertadas como imagen** dentro de este PDF nativo del Diario Oficial digital (2022). El `.txt` de apoyo (`molina_p15-21.txt`) confirma esto: entre cada encabezado de zona solo hay líneas en blanco donde debería estar la tabla. Toda cifra de este documento proviene de lectura visual directa de las imágenes (con recortes en zoom para las filas con formato numérico ambiguo), no del texto extraído.

**Conteo de zonas — verificado, no asumido:** el Art. 4.2 (p.15) lista **18 códigos** en total, agrupados en tres categorías. De ellos, **16 tienen cuadro normativo completo** (usos de suelo + normas de subdivisión y edificación, con COS/CC/altura/etc.) y **2 son áreas de protección sin parámetros urbanísticos** (listados de identificación, no zonas edificables):

- **Área urbana (16 zonas con cuadro completo):** ZU-1, ZU-2, ZU-2b, ZU-3, ZU-4, ZU-5, ZU-6, ZU-7, ZE-1, ZE-2, ZE-3, ZE-4, ZE-5, ZE-6, ZAP, ZAV.
- **Área de protección de recursos de valor natural (1):** ZPL — **no trae cuadro de COS/CC/altura**; es un listado de 2 áreas naturales protegidas por decreto externo (Parque Nacional y Reserva Nacional Radal Siete Tazas), con columnas Identificación/Localidad/Decreto.
- **Áreas de protección de recursos de valor patrimonial cultural (1):** ICH — tampoco trae cuadro de COS/CC/altura; es un listado de 11 inmuebles individuales protegidos, con columnas N°/Identificación/Ubicación/Localidad/Rol Predial.

Esto **resuelve la duda que dejó abierta la nota heredada de Fase 3** ("terminando en ZAV/ZPL/ICH patrimonial", sin precisar si ZPL/ICH traían cuadro propio): **sí son categorías propias de Art. 4.2 con su propio artículo y tabla en Art. 4.3, pero NINGUNA de las dos es una "zona" edificable con norma de subdivisión** — son catastros de elementos protegidos. Ver evidencia directa en las secciones ZPL e ICH más abajo. La lista de Fase 3 ("ZU-1 a ZU-7, ZE-1 a ZE-6, ZAP, ZAV") era substancialmente correcta pero no mencionaba ZU-2b de forma explícita ni el hecho de que ZPL/ICH no llevan cuadro numérico — ambos puntos se verifican y documentan aquí.

**Erratas de la fuente preservadas [sic] (no corregidas):**
- El documento **mezcla coma y punto como separador decimal** entre — e incluso dentro de — distintos cuadros. Zonas con **punto decimal** en vez de coma chilena: ZU-2 (COS Residencial "0.4", COS Equipamiento "0.5", CC Equipamiento "1.0"; nótese que en la misma fila de CC el valor Residencial sí usa coma: "0,8"), ZU-6 (COS "0.3", CC "0.6"), ZU-7 (COS "0.1", CC "0.2"). Se transcribe tal cual con `[sic]` en cada celda afectada.
- El separador de miles de "predial mínima" también es inconsistente: ZU-7 trae "2500 m2" (sin punto) mientras que el decreto 2.922 (modificación 2023, ver `molina_2922_modificacion_zu_zap.md`) transcribe la misma cifra como "2.500 m²"; ZE-5 trae "2500 m2" sin punto; ZE-2/ZE-3 traen "1000 m2" sin punto; ZE-4/ZE-6 sí traen "1.000 m2" con punto. Se preserva cada una como aparece en su cuadro.
- **ZAP** aparece nombrada de dos formas distintas dentro del mismo documento: en el listado del Art. 4.2 (p.15) es *"ZAP ZONA ACTIVIDAD PRODUCTIVA"* (sin "DE"); en el encabezado de su cuadro en Art. 4.3 (p.20) es *"ZAP ZONA DE ACTIVIDAD PRODUCTIVA"* (con "DE"). Ambas formas se citan donde corresponde.
- **ICH 5 "El Chalet":** la ubicación trae "Sector Santa Elsa-**Cerrrillo** Bascuñán" con triple "r" — se preserva `[sic]`.
- Variantes menores de rótulo de tabla que no afectan datos: "NORMAS DE SUBDIVISIÓN Y EDIFICACION" (sin tilde en "EDIFICACION") en la mayoría de los cuadros, salvo el de ZE-6 que trae "EDIFICACIÓN" con tilde; "ANTEJARDÍN" vs "ANTEJARDIN" (ZAV, sin tilde); ZE-6 usa "TIPO" (singular) en vez de "TIPOS". Se normalizaron los encabezados de columna en esta transcripción por legibilidad; los **valores** de cada celda sí son literales.

**Estructura de tabla no uniforme entre zonas (verificado, no es omisión de esta transcripción):**
- Algunas zonas usan cuadro de normas con **una sola columna de valor** (sin distinguir Residencial/Equipamiento): ZU-5, ZU-6, ZU-7, ZE-2, ZE-3, ZE-6. Esto coincide exactamente con el formato "Actual" de ZU-5/ZU-6/ZU-7 ya transcrito en `molina_2922_modificacion_zu_zap.md`, lo que confirma independientemente la lectura visual de este documento.
- ZU-4 **no trae fila "SERVICIOS"** en su cuadro de usos de suelo (sí la traen ZU-1, ZU-2, ZU-2b, ZU-3, ZU-6). Verificado con recorte en zoom — no es un salto de lectura.
- ZU-2 y ZU-2b **no traen fila "CIENTIFICO"** en equipamiento (sí la trae ZU-1).
- ZE-4 y ZAP introducen una categoría **"INFRAESTRUCTURA"** (Transporte/Sanitaria/Energética) ausente en las demás zonas — son las únicas dos zonas con infraestructura de urbanización pesada permitida.
- Filas "DISTANCIAMIENTO" solo aparecen en ZE-4, ZE-5 y ZAP. Filas "DENSIDAD BRUTA MÁXIMA" solo aparecen en zonas con uso residencial habilitado.
- ZAV es la única zona cuyo cuadro de usos de suelo no trae columna "EXCEPTO" (solo Tipo de uso/Destino/Permitidos), y su cuadro de normas **no trae fila de Coeficiente de Ocupación de Suelo** (COS) — solo Coeficiente de Constructibilidad.

**Convenciones usadas en esta transcripción** (siguiendo `molina_2922_modificacion_zu_zap.md`):
- "(única)" = el cuadro fuente muestra una sola celda fusionada para Residencial y Equipamiento (mismo valor, no dos valores iguales por coincidencia).
- "—" = el cuadro fuente trae "-" (no aplica / sin dato para esa columna).
- "Sin valor específico en la fuente" no fue necesario en ningún cuadro: cada fila transcrita corresponde a una fila que existe realmente en el cuadro fuente; las filas ausentes en una zona (p.ej. antejardín en ZU-1/ZU-3) simplemente no aparecen en esa zona, tal como en el cuadro original — no se completó ninguna con placeholder.
- No hubo ninguna cifra ilegible tras zoom — no fue necesario usar "Dato no determinable".

**Verificación "comuna ajena":** revisada — sin hallazgos. Los únicos topónimos de localidad que aparecen en el rango p.15-21 son **Molina** (ICH 1-5), **Lontué** (ICH 6-11, poblado/distrito de la comuna de Molina), **Radal** y **Siete Taza(s)** (ZPL, sector rural de Molina donde está el Parque Nacional Radal Siete Tazas). Los cuatro son localidades dentro de la comuna de Molina — no hay mención de otra comuna. Esto además coincide con la nota independiente del registro Fase 3 para el PDF escaneado alternativo de esta misma ordenanza (id `molina_b3e4da9918`): *"Zonas de Molina/Lontué/Itahue/Radal, sin comuna ajena"*.

**Cruce de validación externo:** 6 de las 16 zonas (ZU-2b, ZU-3, ZU-4, ZU-5, ZU-6, ZU-7) fueron modificadas por el Decreto N° 2.922 de 2023, ya transcrito en `molina_2922_modificacion_zu_zap.md` con sus valores "Actual" (= los vigentes antes de esa modificación, es decir, los que promulga este Decreto 52 de 2022). Los valores leídos aquí coinciden exactamente con los valores "Actual" de esas 6 zonas en dicho archivo (COS, CC, altura, agrupamiento, antejardín y densidad, celda por celda) — cross-check de alta confianza que corrobora la lectura visual de este documento. **CORRECCION relevante detectada en esta reconciliacion:** una version paralela e independiente de este mismo registro (sesion GREGO1) omitio por error la fila "Antejardin" de ZU-4 y ZU-5 en su cuadro de normas -- se verifico contra `molina_2922_modificacion_zu_zap.md` que ambas zonas SI tienen fila Antejardin en su version "Actual" (ZU-4: 3m/3m; ZU-5: 3m), confirmando que esta transcripcion (que si incluye esa fila) es la completa.

**Índice de cobertura (Art. 4.2, verificación de que cada código listado tiene su sección más abajo):**

| Código | Nombre completo | Página(s) del cuadro | Tipo de cuadro |
|---|---|---|---|
| ZU-1 | Zona Mixta 1 | 16 | Normas completas |
| ZU-2 | Zona Mixta 2 | 16 | Normas completas |
| ZU-2b | Zona Mixta 2b | 16-17 | Normas completas (cuadro de normas cruza a p.17) |
| ZU-3 | Zona Mixta Residencial 3 | 17 | Normas completas |
| ZU-4 | Zona Mixta Residencial 4 | 17 | Normas completas |
| ZU-5 | Zona Mixta Residencial 5 | 17-18 | Normas completas (usos de suelo cruza a p.18) |
| ZU-6 | Zona Mixta Residencial 6 | 18 | Normas completas |
| ZU-7 | Zona Mixta Residencial 7 | 18 | Normas completas |
| ZE-1 | Zona de Equipamiento 1 | 19 | Normas completas |
| ZE-2 | Zona de Equipamiento 2 | 19 | Normas completas |
| ZE-3 | Zona de Equipamiento 3 | 19 | Normas completas |
| ZE-4 | Zona de Equipamiento 4 | 19-20 | Normas completas (cuadro de normas cruza a p.20) |
| ZE-5 | Zona de Equipamiento 5 | 20 | Normas completas |
| ZE-6 | Zona de Equipamiento 6 | 20 | Normas completas |
| ZAP | Zona (de) Actividad Productiva | 20-21 | Normas completas (cruza a p.21) |
| ZAV | Zona Área Verde | 21 | Normas completas |
| ZPL | Zona de Protección Legal (Parque Nacional Radal 7 Tazas) | 21 | Listado de áreas protegidas (sin COS/CC) |
| ICH | Inmuebles de Conservación Histórica | 21 | Listado de inmuebles protegidos (sin COS/CC) |

---

## Artículo 4.1 — Áreas Restringidas al Desarrollo Urbano (p.15, contexto, sin cifras de zona)

Las áreas de riesgo establecidas por el plan son: Áreas Inundables por Canal; Áreas Potencialmente Inundables por Cauces Naturales; Áreas Potencialmente Inundables por Anegamiento; Áreas Propensas a Avalancha, Rodados, Aluviones o Erosiones Acentuadas. Una vez cumplido lo dispuesto en la OGUC sobre estudios fundados, se aplican las normas urbanísticas de la zona del Plan en que se encuentre el terreno.

## Artículo 4.2 — Zonificación (p.15, listado íntegro de zonas)

> "El área al interior del límite urbano de la comuna de Molina se divide en las siguientes zonas:"

**ÁREA URBANA**
- ZU-1 ZONA MIXTA 1
- ZU-2 ZONA MIXTA 2
- ZU-2b ZONA MIXTA 2b
- ZU-3 ZONA MIXTA RESIDENCIAL 3
- ZU-4 ZONA MIXTA RESIDENCIAL 4
- ZU-5 ZONA MIXTA RESIDENCIAL 5
- ZU-6 ZONA MIXTA RESIDENCIAL 6
- ZU-7 ZONA MIXTA RESIDENCIAL 7
- ZE-1 ZONA DE EQUIPAMIENTO 1
- ZE-2 ZONA DE EQUIPAMIENTO 2
- ZE-3 ZONA DE EQUIPAMIENTO 3
- ZE-4 ZONA DE EQUIPAMIENTO 4
- ZE-5 ZONA DE EQUIPAMIENTO 5
- ZE-6 ZONA DE EQUIPAMIENTO 6
- ZAP ZONA ACTIVIDAD PRODUCTIVA
- ZAV ZONA ÁREA VERDE

**ÁREA DE PROTECCIÓN DE RECURSOS DE VALOR NATURAL**
- ZPL ZONA DE PROTECCIÓN LEGAL PARQUE NACIONAL RADAL 7 TAZAS

**ÁREAS DE PROTECCIÓN DE RECURSOS DE VALOR PATRIMONIAL CULTURAL**
- ICH INMUEBLES DE CONSERVACIÓN HISTÓRICA

**Total: 18 códigos** (16 zonas urbanas + 1 área de protección natural + 1 área de protección patrimonial).

---

## Artículo 4.3 — Normas Urbanísticas por Zona

### ZU-1 (Zona Mixta 1) — p.16

#### Usos de suelo

| Tipo | Clase / Destino | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Todos los destinos de este uso. | — |
| EQUIPAMIENTO | CIENTIFICO | Grupo 1 | — |
| EQUIPAMIENTO | COMERCIO | Grupo 1, 2, 3 y 4 | Estaciones o centros de Servicio Automotor. |
| EQUIPAMIENTO | CULTO Y CULTURA | Grupo 1, 2, 3 y 4 | — |
| EQUIPAMIENTO | DEPORTE | Grupo 2 | Centros Deportivos, Multicanchas. |
| EQUIPAMIENTO | EDUCACION | Grupo 1, 2, 3 y 4 | Centros de rehabilitación conductual. |
| EQUIPAMIENTO | ESPARCIMIENTO | Grupo 1 | — |
| EQUIPAMIENTO | SALUD | Grupo 1, 2 y 3 | — |
| EQUIPAMIENTO | SEGURIDAD | Grupo 1, 2 y 3 | — |
| EQUIPAMIENTO | SERVICIOS | Grupo 1, 2 y 3 | — |
| EQUIPAMIENTO | SOCIAL | Grupo 1 y 2 | — |

#### Normas de subdivisión y edificación

| Norma | Residencial | Equipamiento |
|---|---|---|
| Superficie de subdivisión predial mínima | 300 m² (única) | 300 m² (única) |
| Coeficiente de ocupación de suelo | 0,5 | 1 |
| Coeficiente de constructibilidad | 1 | 1,2 |
| Sistema de agrupamiento | Continuo (única) | Continuo (única) |
| Altura máxima de edificación | 8 m | 13 m |
| Densidad bruta máxima | 50 hab/ha | — |

---

### ZU-2 (Zona Mixta 2) — p.16

#### Usos de suelo

| Tipo | Clase / Destino | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Todos los destinos de este uso. | — |
| EQUIPAMIENTO | COMERCIO | Grupo 1, 2, 3 y 4 | Estaciones o centros de servicio automotor |
| EQUIPAMIENTO | CULTO Y CULTURA | Grupo 1, 2 y 3 | Edificios de Culto, Cines, Teatros, Auditorios, Centros de difusión de toda especie, Medios de comunicación, tales como canales de televisión, radio y prensa escrita |
| EQUIPAMIENTO | DEPORTE | Grupo 1, 2 y 3 | — |
| EQUIPAMIENTO | EDUCACION | Grupo 1, 2 y 3 | Academias, Centros de rehabilitación conductual. |
| EQUIPAMIENTO | ESPARCIMIENTO | Grupo 1, 2, 3 y 4 | — |
| EQUIPAMIENTO | SALUD | Grupo 1, 2 y 3 | Centros de rehabilitación ambulatoria |
| EQUIPAMIENTO | SEGURIDAD | Grupo 1, 2 y 3 | — |
| EQUIPAMIENTO | SERVICIOS | Grupo 1, 2 y 3 | — |
| EQUIPAMIENTO | SOCIAL | Grupo 1, 2 y 3 | — |

*(No trae fila "CIENTIFICO", a diferencia de ZU-1.)*

#### Normas de subdivisión y edificación

| Norma | Residencial | Equipamiento |
|---|---|---|
| Superficie de subdivisión predial mínima | 300 m² (única) | 300 m² (única) |
| Coeficiente de ocupación de suelo | 0.4 [sic, punto en el original] | 0.5 [sic, punto en el original] |
| Coeficiente de constructibilidad | 0,8 | 1.0 [sic, punto en el original] |
| Altura máxima de edificación | 8 m aislado-Pareado y 8 m Continuo | 11 m |
| Sistema de agrupamiento | Aislado - Pareado - Continuo | Aislado |
| Densidad bruta máxima | 120 hab/ha | — |

---

### ZU-2b (Zona Mixta 2b) — p.16-17

#### Usos de suelo

| Tipo | Clase / Destino | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Todos los destinos de este uso. | Hogares de Acogida |
| EQUIPAMIENTO | COMERCIO | Grupo 1, 2 y 3 | — |
| EQUIPAMIENTO | CULTO Y CULTURA | Grupo 1, 2, 3 y 4 | — |
| EQUIPAMIENTO | DEPORTE | Grupo 1, 2 y 3 | — |
| EQUIPAMIENTO | EDUCACION | Grupo 1, 2 y 3 | Centros de rehabilitación conductual. |
| EQUIPAMIENTO | ESPARCIMIENTO | Grupo 1, 2, 3 y 4 | — |
| EQUIPAMIENTO | SALUD | Grupo 1 y 2 | — |
| EQUIPAMIENTO | SEGURIDAD | Grupo 1, 2 y 3 | — |
| EQUIPAMIENTO | SERVICIOS | Grupo 1, 2 y 3 | — |
| EQUIPAMIENTO | SOCIAL | Grupo 1 y 2 | — |

*(Tabla de usos de suelo íntegra en p.16; el cuadro de normas de subdivisión que sigue está impreso al inicio de p.17, antes del encabezado "ZU-3".)*

#### Normas de subdivisión y edificación

| Norma | Residencial | Equipamiento |
|---|---|---|
| Superficie de subdivisión predial mínima | 500 m² (única) | 500 m² (única) |
| Coeficiente de ocupación de suelo | 0,2 | 0,4 |
| Coeficiente de constructibilidad | 1,5 | 1,0 |
| Altura máxima de edificación | 11 m (única) | 11 m (única) |
| Sistema de agrupamiento | Aislado (única) | Aislado (única) |
| Antejardín | 5 m (única) | 5 m (única) |
| Densidad bruta máxima | 80 hab/ha | — |

*(Coincide exactamente con los valores "Actual" de ZU-2b en `molina_2922_modificacion_zu_zap.md`.)*

---

### ZU-3 (Zona Mixta Residencial 3) — p.17

#### Usos de suelo

| Tipo | Clase / Destino | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Todos los destinos de este uso. | — |
| EQUIPAMIENTO | COMERCIO | Grupo 1 y 2 | Restaurantes, Fuentes de Soda |
| EQUIPAMIENTO | CULTO Y CULTURA | Grupo 1 y 2 | — |
| EQUIPAMIENTO | DEPORTE | Grupo 1 y 3 | Piscinas |
| EQUIPAMIENTO | EDUCACION | Grupo 1, 2 y 3 | Establecimientos destinados principalmente a la formación o capacitación en educación superior, técnica, Centros de rehabilitación conductual. |
| EQUIPAMIENTO | ESPARCIMIENTO | Grupo 1 | — |
| EQUIPAMIENTO | SALUD | Grupo 1 y 2 | — |
| EQUIPAMIENTO | SEGURIDAD | Grupo 1, 2 y 3 | — |
| EQUIPAMIENTO | SERVICIOS | Grupo 1 y 2 | Oficinas, Notarías |
| EQUIPAMIENTO | SOCIAL | Grupo 1 y 2 | — |

#### Normas de subdivisión y edificación

| Norma | Valor (única, sin distinguir Residencial/Equipamiento salvo donde se indica) |
|---|---|
| Superficie de subdivisión predial mínima | 160 m² |
| Coeficiente de ocupación de suelo | 0,4 |
| Coeficiente de constructibilidad | 0,6 |
| Altura máxima de edificación | 8 m |
| Sistema de agrupamiento | Residencial: Continuo — Equipamiento: Aislado, Pareado |
| Densidad bruta máxima | 200 hab/ha |

*(Coincide exactamente con los valores "Actual" de ZU-3 en `molina_2922_modificacion_zu_zap.md`.)*

---

### ZU-4 (Zona Mixta Residencial 4) — p.17

#### Usos de suelo

| Tipo | Clase / Destino | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Todos los destinos de este uso. | — |
| EQUIPAMIENTO | COMERCIO | Grupo 1 y 2 | Restaurantes, Fuentes de Soda |
| EQUIPAMIENTO | CULTO Y CULTURA | Grupo 1, 2, 3 y 4 | — |
| EQUIPAMIENTO | DEPORTE | Grupo 1, 2 y 3 | — |
| EQUIPAMIENTO | EDUCACION | Grupo 1, 2 y 3 | Establecimientos destinados principalmente a la formación o capacitación en educación superior, técnica, Centros de rehabilitación conductual. |
| EQUIPAMIENTO | ESPARCIMIENTO | Grupo 1 | — |
| EQUIPAMIENTO | SALUD | Grupo 1 y 2 | — |
| EQUIPAMIENTO | SEGURIDAD | Grupo 1, 2 y 3 | — |
| EQUIPAMIENTO | SOCIAL | Grupo 1 y 2 | — |

*(No trae fila "SERVICIOS" — verificado con recorte en zoom, no es omisión de lectura.)*

#### Normas de subdivisión y edificación

| Norma | Residencial | Equipamiento |
|---|---|---|
| Superficie de subdivisión predial mínima | 160 m² (única) | 160 m² (única) |
| Coeficiente de ocupación de suelo | 0,6 | 0,5 |
| Coeficiente de constructibilidad | 0,8 | 1,0 |
| Altura máxima de edificación | 8 m (única) | 8 m (única) |
| Sistema de agrupamiento | Aislado, Pareado (única) | Aislado, Pareado (única) |
| Antejardín | 3 m (única) | 3 m (única) |
| Densidad bruta máxima | 160 hab/ha | — |

*(Coincide exactamente con los valores "Actual" de ZU-4 en `molina_2922_modificacion_zu_zap.md`.)*

---

### ZU-5 (Zona Mixta Residencial 5) — p.17-18

#### Usos de suelo

*(Tabla con estructura propia: agrega la categoría "Actividades Productivas" que no aparece en ZU-1 a ZU-4. Fila Residencial impresa al pie de p.17; el resto —Actividades Productivas y Equipamiento— continúa al inicio de p.18.)*

| Tipo | Clase / Destino | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Todos los destinos de este uso. | — |
| ACTIVIDADES PRODUCTIVAS | Inofensiva | Talleres y bodegas de tipo inofensivo | Industria y toda instalación de impacto similar al Industrial sólo las calificadas como molestas, insalubres o contaminantes. |
| EQUIPAMIENTO | CIENTIFICO | Grupo 1 | — |
| EQUIPAMIENTO | COMERCIO | Grupo 1, 2, 3 y 4 | — |
| EQUIPAMIENTO | CULTO Y CULTURA | Grupo 1, 2, 3 y 4 | — |
| EQUIPAMIENTO | DEPORTE | Grupo 1, 2, 3 y 4 | — |
| EQUIPAMIENTO | EDUCACION | Grupo 1, 2, 3 y 4 | — |
| EQUIPAMIENTO | ESPARCIMIENTO | Grupo 1, 2, 3 y 4 | Parques Zoológicos |
| EQUIPAMIENTO | SALUD | Grupo 1, 2 y 3 | — |
| EQUIPAMIENTO | SEGURIDAD | Grupo 1, 2 y 3 | — |
| EQUIPAMIENTO | SERVICIOS | Grupo 1, 2 y 3 | — |
| EQUIPAMIENTO | SOCIAL | Grupo 1 y 2 | — |

#### Normas de subdivisión y edificación

| Norma | Valor (única, sin distinguir Residencial/Equipamiento) |
|---|---|
| Superficie de subdivisión predial mínima | 500 m² |
| Coeficiente de ocupación de suelo | 0,5 |
| Coeficiente de constructibilidad | 1,0 |
| Altura máxima de edificación | 11 m |
| Sistema de agrupamiento | Aislado, Pareado |
| Antejardín | 3 m |
| Densidad bruta máxima | 80 hab/ha |

*(Coincide exactamente con los valores "Actual" de ZU-5 en `molina_2922_modificacion_zu_zap.md`.)*

---

### ZU-6 (Zona Mixta Residencial 6) — p.18

#### Usos de suelo

| Tipo | Clase / Destino | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Todos los destinos de este uso. | — |
| EQUIPAMIENTO | COMERCIO | Grupo 1, 2 y 3 | Estaciones o centros de servicio automotor |
| EQUIPAMIENTO | CULTO Y CULTURA | Grupo 1, 2 y 3 | Edificios de Culto, Salas de concierto o espectáculos, Cines, Teatros, Auditorios, Centros de eventos, Centros de convenciones, Centros de exposiciones, Centros de difusión de toda especie, Medios de comunicación, tales como canales de televisión, radio y prensa escrita |
| EQUIPAMIENTO | DEPORTE | Grupo 1, 2 y 3 | — |
| EQUIPAMIENTO | EDUCACION | Grupo 1, 2 y 3 | Academias, Institutos, Universidades. Centros de rehabilitación conductual. |
| EQUIPAMIENTO | ESPARCIMIENTO | Grupo 1, 2, 3 y 4 | Casinos |
| EQUIPAMIENTO | SALUD | Grupo 1 y 2 | — |
| EQUIPAMIENTO | SEGURIDAD | Grupo 1, 2 y 3 | — |
| EQUIPAMIENTO | SERVICIOS | Grupo 1 y 2 | Notarías, Correos, Telégrafos, Centros de Pago. |
| EQUIPAMIENTO | SOCIAL | Grupo 1 y 2 | — |

#### Normas de subdivisión y edificación

| Norma | Valor (única, sin distinguir Residencial/Equipamiento) |
|---|---|
| Superficie de subdivisión predial mínima | 800 m² |
| Coeficiente de ocupación de suelo | 0.3 [sic, punto en el original] |
| Coeficiente de constructibilidad | 0.6 [sic, punto en el original] |
| Altura máxima de edificación | 8 m |
| Sistema de agrupamiento | Aislado - Pareado |
| Antejardín | 3 m |
| Densidad bruta máxima | 40 hab/ha |

*(Coincide exactamente con los valores "Actual" de ZU-6 en `molina_2922_modificacion_zu_zap.md"; ese archivo transcribe los mismos valores con coma "0,3"/"0,6" — confirma que son los mismos números pese al separador decimal distinto en cada fuente.)*

---

### ZU-7 (Zona Mixta Residencial 7) — p.18

#### Usos de suelo

| Tipo | Clase / Destino | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Todos los destinos de este uso. | — |
| EQUIPAMIENTO | CIENTIFICO | Grupo 1 | — |
| EQUIPAMIENTO | CULTO Y CULTURA | Grupo 1, 2, 3 y 4 | Edificios de Culto |

*(Zona más restrictiva del área urbana: solo 2 clases de equipamiento permitidas.)*

#### Normas de subdivisión y edificación

| Norma | Valor (única, sin distinguir Residencial/Equipamiento) |
|---|---|
| Superficie de subdivisión predial mínima | 2500 m² [sic, sin separador de miles en el original] |
| Coeficiente de ocupación de suelo | 0.1 [sic, punto en el original] |
| Coeficiente de constructibilidad | 0.2 [sic, punto en el original] |
| Altura máxima de edificación | 8 m |
| Sistema de agrupamiento | Aislado |
| Antejardín | 5 m |
| Densidad bruta máxima | 12 hab/ha |

*(Coincide exactamente con los valores "Actual" de ZU-7 en `molina_2922_modificacion_zu_zap.md` — ese archivo transcribe la predial mínima como "2.500 m²".)*

---

### ZE-1 (Zona de Equipamiento 1) — p.19

#### Usos de suelo

| Tipo | Clase / Destino | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Edificaciones y locales destinados al hospedaje | Vivienda, Hogares de Acogida. |
| EQUIPAMIENTO | COMERCIO | Grupo 1 y 2 | — |
| EQUIPAMIENTO | CULTO Y CULTURA | Grupo 1, 2, 3 y 4 | Edificios de Culto |
| EQUIPAMIENTO | DEPORTE | Grupo 1, 2, 3 y 4 | — |
| EQUIPAMIENTO | EDUCACION | Grupo 3 | Liceos, Colegios, Academias, Institutos, Universidades. Centros de rehabilitación conductual. |
| EQUIPAMIENTO | ESPARCIMIENTO | Grupo 1, 2, 3 y 4 | Casinos |

*(Nótese que en esta zona la vivienda normal NO está permitida; solo hospedaje.)*

#### Normas de subdivisión y edificación

| Norma | Residencial | Equipamiento |
|---|---|---|
| Superficie de subdivisión predial mínima | 500 m² (única) | 500 m² (única) |
| Coeficiente de ocupación de suelo | 0,4 | 0,2 |
| Coeficiente de constructibilidad | 0,8 | 0,4 |
| Altura máxima de edificación | 7 m (única) | 7 m (única) |
| Sistema de agrupamiento | Aislado (única) | Aislado (única) |
| Antejardín | 5 m (única) | 5 m (única) |
| Densidad bruta máxima | 80 hab/ha | — |

---

### ZE-2 (Zona de Equipamiento 2) — p.19

#### Usos de suelo

*(Sin fila Residencial — esta zona no admite uso residencial en ninguna forma.)*

| Tipo | Clase / Destino | Permitidos | Excepto |
|---|---|---|---|
| EQUIPAMIENTO | CULTO Y CULTURA | Grupo 2 y 3 | Edificios de Culto, Museos, Cines Teatros |
| EQUIPAMIENTO | DEPORTE | Grupo 1, 2, 3 y 4 | — |
| EQUIPAMIENTO | ESPARCIMIENTO | Grupo 1, 2, 3 y 4 | — |

#### Normas de subdivisión y edificación

| Norma | Valor (única) |
|---|---|
| Superficie de subdivisión predial mínima | 1000 m² [sic, sin separador de miles en el original] |
| Coeficiente de ocupación de suelo | 0,1 |
| Coeficiente de constructibilidad | 0,2 |
| Altura máxima de edificación | 7 m |
| Sistema de agrupamiento | Aislado |

*(No trae filas de antejardín ni densidad bruta — coherente con ser zona sin uso residencial.)*

---

### ZE-3 (Zona de Equipamiento 3) — p.19

#### Usos de suelo

| Tipo | Clase / Destino | Permitidos | Excepto |
|---|---|---|---|
| EQUIPAMIENTO | CULTO Y CULTURA | Grupo 1 | — |
| EQUIPAMIENTO | SALUD | Grupo 4 | — |

#### Normas de subdivisión y edificación

| Norma | Valor (única) |
|---|---|
| Superficie de subdivisión predial mínima | 1000 m² [sic, sin separador de miles en el original] |
| Coeficiente de ocupación de suelo | 0,1 |
| Coeficiente de constructibilidad | 0,2 |
| Altura máxima de edificación | 7 m |
| Sistema de agrupamiento | Aislado |

---

### ZE-4 (Zona de Equipamiento 4) — p.19-20

#### Usos de suelo

| Tipo | Clase / Destino | Permitidos | Excepto |
|---|---|---|---|
| INFRAESTRUCTURA | Transporte | Terminales de transporte terrestre y Estaciones Ferroviarias | — |
| INFRAESTRUCTURA | Sanitaria | Plantas de captación, distribución o tratamiento de agua potable o de aguas servidas, de aguas lluvia. | — |
| INFRAESTRUCTURA | Energética | Todas las actividades de esta clase | Centrales de generación energía |
| EQUIPAMIENTO | CIENTIFICO | Grupo 1 | — |
| EQUIPAMIENTO | COMERCIO | Grupo 2 | — |
| EQUIPAMIENTO | CULTO Y CULTURA | Grupo 1, 2, 3 y 4 | Edificios de Culto, Bibliotecas, Cines, Teatros, Medios de comunicación, tales como canales de televisión, radio y prensa escrita. |
| EQUIPAMIENTO | DEPORTE | Grupo 1 y 3 | — |
| EQUIPAMIENTO | SEGURIDAD | Grupo 1, 2 y 3 | — |

*(Sin uso Residencial. Primera zona del listado con categoría "Infraestructura".)*

#### Normas de subdivisión y edificación

| Norma | Equipamiento | Infraestructura |
|---|---|---|
| Superficie de subdivisión predial mínima | 1.000 m² (única) | 1.000 m² (única) |
| Coeficiente de ocupación de suelo | 0,5 | 0,1 |
| Coeficiente de constructibilidad | 0,7 | 0,1 |
| Altura máxima de edificación | 7 m | — |
| Sistema de agrupamiento | Aislado (única) | Aislado (única) |
| Distanciamiento | 5 m (única) | 5 m (única) |
| Antejardín | 5 m | 10 m |

---

### ZE-5 (Zona de Equipamiento 5) — p.20

#### Usos de suelo

| Tipo | Clase / Destino | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Edificaciones y locales destinados al hospedaje | Vivienda, Hogares de Acogida. |
| EQUIPAMIENTO | CIENTIFICO | Grupo 1 | — |
| EQUIPAMIENTO | COMERCIO | Grupo 2 | — |
| EQUIPAMIENTO | CULTO Y CULTURA | Grupo 1, 2, 3 y 4 | Edificios de Culto, Cines, Teatros, Medios de comunicación, tales como canales de televisión, radio y prensa escrita |
| EQUIPAMIENTO | ESPARCIMIENTO | Grupo 1 y 3 | Parques de entretenciones y Juegos electrónicos. |
| EQUIPAMIENTO | SEGURIDAD | Grupo 1, 2 y 3 | — |

#### Normas de subdivisión y edificación

| Norma | Valor (única) |
|---|---|
| Superficie de subdivisión predial mínima | 2500 m² [sic, sin separador de miles en el original] |
| Coeficiente de ocupación de suelo | 0,05 |
| Coeficiente de constructibilidad | 0,05 |
| Altura máxima de edificación | 8 m |
| Sistema de agrupamiento | Aislado |
| Distanciamiento | 5 m |
| Antejardín | 10 m |

---

### ZE-6 (Zona de Equipamiento 6) — p.20

#### Usos de suelo

*(Sin fila Residencial.)*

| Tipo | Clase / Destino | Permitidos | Excepto |
|---|---|---|---|
| EQUIPAMIENTO | CIENTIFICO | Grupo 1 | — |
| EQUIPAMIENTO | CULTO Y CULTURA | Grupo 1, 2, 3 y 4 | — |
| EQUIPAMIENTO | DEPORTE | Grupo 1 y 3 | — |
| EQUIPAMIENTO | ESPARCIMIENTO | Grupo 3 y 4 | — |

#### Normas de subdivisión y edificación

| Norma | Valor (única) |
|---|---|
| Superficie de subdivisión predial mínima | 1.000 m² |
| Coeficiente de ocupación de suelo | 0,1 |
| Coeficiente de constructibilidad | 0,1 |
| Altura máxima de edificación | 3,5 m |
| Sistema de agrupamiento | Aislado |
| Antejardín | 10 m |

---

### ZAP (Zona [de] Actividad Productiva) — p.20-21

> Nombrada "ZAP ZONA ACTIVIDAD PRODUCTIVA" en el listado del Art. 4.2 (p.15) y "ZAP ZONA DE ACTIVIDAD PRODUCTIVA" en el encabezado de su propio cuadro (p.20) — discrepancia de la fuente, ver Nota de alcance.

#### Usos de suelo

*(Tabla larga: la fila Residencial y las categorías Actividades Productivas/Infraestructura están en p.20; la categoría Equipamiento continúa al inicio de p.21.)*

| Tipo | Clase / Destino | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Vivienda | Hogares de Acogida, Edificaciones y locales destinados al hospedaje |
| ACTIVIDADES PRODUCTIVAS | Inofensiva | Industria y toda instalación de impacto similar al Industrial sólo las calificadas como Inofensivas. Grandes Depósitos, Talleres o Bodegas Industriales | Industria y toda instalación de impacto similar al Industrial sólo las calificadas como molestas, insalubres o contaminantes. |
| INFRAESTRUCTURA | Transporte | Terminales de transporte terrestre | Estaciones Ferroviarias, Recintos marítimos o portuarios, Recintos aeroportuarios |
| INFRAESTRUCTURA | Sanitaria | Plantas de captación, distribución o tratamiento de agua potable o de aguas servidas, de aguas lluvia. | Rellenos sanitarios, vertederos, botaderos, almacenamiento y acopios de Cenizas, Plantas de tratamiento de residuos industriales, Estaciones exclusivas de transferencia de residuos |
| INFRAESTRUCTURA | Energética | Todas las actividades de esta clase | Centrales de generación energía |
| EQUIPAMIENTO | COMERCIO | Grupo 2 y 4 | — |
| EQUIPAMIENTO | DEPORTE | Grupo 1, 2, 3 y 4 | — |
| EQUIPAMIENTO | SEGURIDAD | Grupo 1, 2 y 3 | — |

*(Nótese el patrón inverso a ZE-1/ZE-5: aquí la vivienda normal SÍ está permitida y lo excluido son los hogares de acogida y el hospedaje.)*

#### Normas de subdivisión y edificación

*(El cuadro de normas no separa Actividades Productivas de Infraestructura — usa una columna combinada, a diferencia del cuadro de usos de suelo.)*

| Norma | Residencial | Equipamiento | Actividades Productivas / Infraestructura |
|---|---|---|---|
| Superficie de subdivisión predial mínima | 600 m² (única) | 600 m² (única) | 600 m² (única) |
| Coeficiente de ocupación de suelo | 0,2 | 0,2 | 0,4 |
| Coeficiente de constructibilidad | 0,2 | 0,2 | 0,8 |
| Altura máxima de edificación | 8 m | 8 m | 11 m |
| Sistema de agrupamiento | Aislado | Aislado | Aislado |
| Distanciamiento | — | 5 m | 5 m |
| Antejardín | — | 5 m | 10 m |
| Densidad bruta máxima | 30 hab/ha | — | — |

*(Coincide exactamente con los valores "Actual" de ZAP en `molina_2922_modificacion_zu_zap.md`.)*

---

### ZAV (Zona Área Verde) — p.21

#### Usos de suelo

*(Única zona sin columna "Excepto" en su cuadro de usos de suelo.)*

| Tipo de uso | Destino | Permitidos |
|---|---|---|
| ÁREA VERDE | Complementarias y compatibles según OGUC | Equipamiento científico, Culto y Cultura, Deporte y Esparcimiento |

#### Normas de subdivisión y edificación

*(Única zona cuyo cuadro no trae fila de Coeficiente de Ocupación de Suelo.)*

| Norma | Valor (única) |
|---|---|
| Superficie de subdivisión predial mínima | 2.500 m² |
| Coeficiente de constructibilidad | 0,1 |
| Altura máxima de edificación | 3,5 m |
| Sistema de agrupamiento | Aislado |
| Antejardín | 10 m |

---

## Área de Protección de Recursos de Valor Natural

### ZPL (Zona de Protección Legal) — p.21

**Qué es (evidencia directa de la imagen):** no es una zona edificable con cuadro de COS/CC/altura. El texto del propio artículo lo define así: *"Corresponde a las áreas reconocidas por el presente Plan en las que existen zonas o elementos naturales protegidos por el ordenamiento jurídico vigente."* En vez de un cuadro de normas de subdivisión, trae un cuadro de identificación de las 2 áreas protegidas reconocidas:

| Identificación | Localidad | Decreto |
|---|---|---|
| Parque Nacional Radal Siete Tazas | Radal | Decreto N°15 27.MAR.2008, Ministerio de Bienes Nacionales. |
| Reserva Nacional Siete Tazas | Siete Taza | Decreto N°89 20.MAR.1996, Ministerio de Bienes Nacionales. |

## Áreas de Protección de Recursos de Valor Patrimonial Cultural

### ICH (Inmuebles de Conservación Histórica) — p.21

**Qué es (evidencia directa de la imagen):** tampoco es una zona con cuadro de COS/CC/altura. El artículo lo introduce así: *"Los Inmuebles establecidos de Conservación Histórica por el presente Plan, en conformidad a lo que establece la LGUC y la OGUC, son los que se indican a continuación:"* — y trae un catastro de 11 inmuebles individuales (no una tabla de parámetros urbanísticos de zona):

| N° | Identificación | Ubicación | Localidad | Rol Predial |
|---|---|---|---|---|
| ICH 1 | Iglesia Parroquial Nuestra Señora del Tránsito | Calle Quechereguas N°1819 Esquina Yerbas Buenas | Molina | 114-1 |
| ICH 2 | Casa Patrimonial Maritza Zúñiga y Otros | Calle Maipú N°1818 Esquina Yerbas Buenas | Molina | 113-9 |
| ICH 3 | Casa Patrimonial Olivia Olave | Calle Maipú N°1898 Esquina Luis Cruz Martínez | Molina | 113-13 |
| ICH 4 | Casa Patrimonial Esquina Quechereguas | Calle Quechereguas Esquina Camino a Itahue | Molina | 607-6 |
| ICH 5 | El Chalet | Calle Quechereguas Esquina Camino A Itahue, Sector Santa Elsa-Cerrrillo [sic] Bascuñán. | Molina | 612-3 |
| ICH 6 | Parroquia San Bonifacio, Lontué | Plazuela Lontué, Lontué. | Lontué | 441-5 |
| ICH 7 | Casa Esquina Av. 7 de Abril | Av. 7 de Abril Esquina Vial, Lontué. | Lontué | 462-2 |
| ICH 8 | Antigua Escuela de Lontué | Luz Pereira S/N° Esquina Echeverría, Lontué. | Lontué | 481-1 |
| ICH 9 | Casa Tipo Castillo | Lote 1 Luz Pereira N°1976, Lontué. | Lontué | 450-1 |
| ICH 10 | Casona Esquina Propiedad de Doña Susana Espinoza | Luz Pereira N°1986 Esquina Av. 7 de Abril, Lontué. | Lontué | 450-2 |
| ICH 11 | Casona Esquina Propiedad de Don Jorge Estay | Avenida 7 de Abril S/N° Esquina Luz Pereira, Lontué. | Lontué | 460-8 |

*(11 inmuebles: 5 en Molina, 6 en Lontué. La tabla termina en ICH 11 — no hay continuación en página 22, que corresponde ya a Título 5 "Vialidad".)*

---

## Resumen de hallazgos vs. nota heredada de Fase 3

1. **Confirmado:** el patrón "trampa nueva" (tablas de zona como imagen dentro de PDF nativo de Diario Oficial digital, veredicto TEXTO engañoso) es exactamente como lo describió Fase 3.
2. **Confirmado y precisado:** 16 zonas con cuadro normativo completo (Fase 3 decía "ZU-1 a ZU-7, ZE-1 a ZE-6, ZAP, ZAV" — correcto en total, pero no mencionaba explícitamente que "ZU-1 a ZU-7" incluye además a ZU-2b, que trae numeración propia con letra).
3. **Resuelto (era la pregunta abierta de Fase 3):** ZPL e ICH NO son zonas edificables con cuadro de COS/CC/altura — son catastros de áreas/inmuebles protegidos con columnas propias (Identificación/Localidad/Decreto para ZPL; N°/Identificación/Ubicación/Localidad/Rol Predial para ICH). Confirmado con evidencia textual directa de página 21.
4. **Hallazgo nuevo (no mencionado por Fase 3):** mezcla de separador decimal (coma/punto) dentro del mismo documento, incluso dentro de una misma fila de tabla (ZU-2, CC: "0,8" y "1.0" en la misma fila). Preservado con `[sic]`.
5. **Hallazgo nuevo:** discrepancia de nombre "ZAP ZONA ACTIVIDAD PRODUCTIVA" (Art. 4.2) vs. "ZAP ZONA DE ACTIVIDAD PRODUCTIVA" (Art. 4.3, encabezado de cuadro).
6. **Hallazgo nuevo, no de este documento pero detectado al revisar el registro compartido:** el mismo patrón "trampa nueva" fue detectado también en el PRC de **Romeral** (id `romeral_e854e79e6b`, nota: *"Misma trampa nueva que Molina"*) — confirma la recomendación de Fase 3 de revisar todos los PDF de Diario Oficial digital 2020+ con este patrón; queda para quien procese ese documento en Fase 4.
7. **Sin comuna ajena.** Único hallazgo de localidades: Molina, Lontué, Radal y Siete Taza(s), las cuatro dentro de la comuna de Molina.
