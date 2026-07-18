# Normas Urbanísticas — Decreto 1698 Exento, "Plan Regulador y Ordenanza Municipal" de San Fernando (1997)

## Fuente y contexto

- **Comuna:** San Fernando.
- **Instrumento:** "Plan Regulador y Ordenanza Municipal", Decreto 1698 Exento, San Fernando (1997).
- **Fuente de la transcripción:** Biblioteca del Congreso Nacional de Chile — www.leychile.cl (documento generado el 09-jul-2026). El documento completo tiene 23 páginas.
- **Rango extraído:** páginas 14 a 19 de 23 (numeración del pie de página BCN: "página XX de 23").
- **Material fuente usado:** renders PNG a 250 dpi de las 6 páginas (`sanfernando_p14-19-14.png` a `sanfernando_p14-19-19.png`) + texto plano de apoyo (`sanfernando_p14-19.txt`), ambos ya provistos por la fase previa. No se re-renderizó nada.
- **Método de verificación de esta extracción:** lectura visual completa (100%) de las 6 páginas render, cotejada línea por línea contra el texto plano. Coincidencia exacta en las 6 páginas — no se detectaron caracteres ilegibles, tablas ocultas, ni discrepancias entre imagen y texto.

### ALERTA heredada de Fase 3 — CONFIRMADA de forma independiente por esta extracción

Fase 3 (confianza MEDIA) advirtió: *"El CUADRO NUMERICO PRINCIPAL (superficie predial minima, COS, coef. constructibilidad, altura, agrupamiento) esta AUSENTE en las 13 zonas del PRC San Fernando (ZU-0 a ZU-9, ZE-1 a ZE-4): cada zona dice literalmente 'Cuadro de normas urbanisticas: VER D.O. DE FECHA 10.09.1998'. Verificado texto+render de p14 (no es imagen oculta, es una omision real del documento BCN/leychile)."*

**Esta extracción confirma la alerta de forma independiente, con matices** (ver sección "Discrepancias y hallazgos" al final para el detalle completo):

- Se verificó, zona por zona, con lectura del render de las 6 páginas (no solo p.14 como hizo Fase 3), que **las 14 zonas** (no 13 — ver discrepancia de conteo más abajo) del rango 14-19 remiten literalmente a "VER D.O. DE FECHA 10.09.1998" (con una variante tipográfica en ZU-4, ver abajo) en lugar de consignar el cuadro numérico.
- Se confirma que **no es una trampa de imagen escondida**: el render de las 6 páginas es texto tipográfico nativo (fuente monoespaciada, propia del render HTML→PDF de leychile.cl), no una imagen escaneada. No hay ningún cuadro, tabla ni gráfico oculto cerca de la frase "VER D.O." en ninguna de las 6 páginas — el espacio que ocuparía el cuadro simplemente no existe en el documento, se pasa directamente a "Disposiciones complementarias".
- **Causa más probable (inferencia, no confirmada por fuente directa):** el Decreto 1698 Exento (1997) aprobó el texto de la ordenanza (usos de suelo, disposiciones complementarias) pero remitió la definición numérica de cada zona (predial mínima, COS, CC, altura, agrupamiento) a un instrumento posterior publicado en el Diario Oficial del 10-09-1998 (más de un año después del decreto base). Ese Diario Oficial **no forma parte de este corpus** y no fue posible acceder a él en el marco de esta tarea. Sin conseguirlo, San Fernando queda sin el cuadro numérico completo de sus 14 zonas.

## Convenciones usadas en este documento

- **"Sin valor específico en la fuente":** para celdas vacías en el original o campos/filas que no aplican por diseño a esa zona (p. ej., una zona sin densidad declarada porque su uso predominante no es residencial).
- **"Dato no determinable":** reservado para el cuadro numérico principal (superficie predial mínima, COS, coeficiente de constructibilidad, altura máxima, sistema de agrupamiento) ausente de cada zona — el documento remite a un Diario Oficial de 1998 que no está disponible en este corpus. Esta convención se usa **extensamente** en este documento, a diferencia de la mayoría de los demás documentos del proyecto, precisamente por la naturaleza de esta fuente. Ver excepciones puntuales (ZU-4 y ZE-1) donde el predial mínimo sí se pudo determinar por otra vía — documentadas explícitamente en cada caso.
- **Erratas tipográficas de la fuente:** se preservan tal cual y se marcan **[sic]**.
- Los números se transcriben tal como aparecen en la fuente (separador de miles con punto: `1.000`, `2.000`; no hay decimales en este documento, todos los valores son enteros o "hab/há").

## Índice de las 14 zonas verificadas (páginas 14-19)

Nota preliminar sobre el conteo: la nota de Fase 3 dice "13 zonas (ZU-0 a ZU-9, ZE-1 a ZE-4)". Esta extracción, por enumeración directa de cada encabezado de zona efectivamente presente en el texto, encontró **14 zonas** en el rango 14-19. El propio rango que cita Fase 3 ("ZU-0 a ZU-9" = 10 zonas + "ZE-1 a ZE-4" = 4 zonas = 14) ya sumaba 14; el "13" parece un error aritmético de esa nota. Ver detalle en "Discrepancias y hallazgos".

También se observa que la secuencia real en el documento no es ZU-0,1,2…9: **ZU-0 aparece al final del bloque ZU** (después de ZU-9), no al principio — se preserva ese orden real en este documento.

| # | Código | Nombre en el documento (verbatim) | Página(s) | Remisión del cuadro numérico (cita literal) |
|---|---|---|---|---|
| 1 | ZU-1 | "ZONA ZU - 1 Preferentemente Comercial" | 14 | "VER D.O. DE FECHA 10.09.1998" |
| 2 | ZU-2 | "ZONA ZU - 2 Comercial - Artesanal" | 14-15 | "VER D.O. DE FECHA 10.09.1998" |
| 3 | ZU-3 | "ZONA ZU - 3 Mixta de Densificación" | 15 | "VER D.O. DE FECHA 10.09.1998" |
| 4 | ZU-4 | "ZONA ZU - 4 Vivienda" | 15-16 | "VER D.O.DE FECHA 10.09.1998" **[sic, sin espacio entre "D.O." y "DE"]** |
| 5 | ZU-5 | "ZONA ZU - 5 Vivienda Restringida" | 16 | "VER D.O. DE FECHA 10.09.1998" |
| 6 | ZU-6 | "ZONA ZU - 6 Industria Inofensiva" | 16 | "VER D.O. DE FECHA 10.09.1998" |
| 7 | ZU-7 | "ZONA ZU - 7 Industria Molesta" | 16-17 | "VER D.O. DE FECHA 10.09.1998" |
| 8 | ZU-8 | "ZONA ZU - 8 Equipamiento Exclusivo" | 17 | "VER D.O. DE FECHA 10.09.1998" |
| 9 | ZU-9 | "ZONA ZU - 9 Parque Municipal" | 17 | "VER D.O. DE FECHA 10.09.1998" |
| 10 | ZU-0 | "Zona ZU - 0 Centro Cívico." | 17-18 | "VER D.O. DE FECHA 10.09.1998" |
| 11 | ZE-1 | "Zona ZE - 1 Expansión Densidad Media" | 18 | "VER D.O. DE FECHA 10.09.1998" |
| 12 | ZE-2 | "Zona ZE - 2 Expansión Densidad Baja." | 18-19 | "VER D.O. DE FECHA 10.09.1998" |
| 13 | ZE-3 | "Zona ZE - 3 Expansión Mixta" | 19 | "VER D.O. DE FECHA 10.09.1998" (con doble salto de línea antes, ver nota en su sección) |
| 14 | ZE-4 | "Zona ZE - 4 Zona de Expansión Industrial" | 19 | "VER D.O. DE FECHA 10.09.1998" |

**Observación de formato:** las zonas ZU-1 a ZU-9 usan el encabezado en mayúsculas "ZONA ZU - N"; las zonas ZU-0 y todas las ZE-N usan "Zona" en minúscula-título. Es consistente dentro de cada grupo, no parece un error puntual sino un cambio de estilo entre bloques del documento original — se deja constancia, se preserva tal cual en cada sección.

---

## ZU-1 — Preferentemente Comercial

**Página:** 14. **Encabezado verbatim:** "ZONA ZU - 1 Preferentemente Comercial".

### Usos permitidos
- Comercio
- Equipamiento vecinal
- Equipamiento comunal
- Vivienda

### Usos prohibidos
- Cementerios
- Botaderos de basura
- Estadios
- Canchas
- Piscinas
- Quintas de recreo
- Ferias
- Terminales de buses

### Cuadro de normas urbanísticas (cuadro numérico principal)

| Parámetro | Valor |
|---|---|
| Superficie predial mínima | Dato no determinable |
| Coeficiente de ocupación de suelo (COS) | Dato no determinable |
| Coeficiente de constructibilidad (CC) | Dato no determinable |
| Altura máxima | Dato no determinable |
| Sistema de agrupamiento | Dato no determinable |

→ Motivo: el documento dice textualmente "Cuadro de normas urbanísticas: VER D.O. DE FECHA 10.09.1998" (p.14) en vez de consignar estos valores. Ese Diario Oficial no está disponible en este corpus.

### Disposiciones complementarias (verbatim)
- Los predios existentes inferiores a 1.000 m² o 20 m. de frente se regirán por las mismas normas.
- Sobre el 3º piso el sistema de agrupamiento será aislado.
- El porcentaje de área libre podrá utilizarse para estacionamiento.
- La vivienda sólo podrá ubicarse en los pisos superiores.
- Las propiedades que adopten la línea oficial y reconstruyan durante los próximos 3 años gozarán de una rebaja del 50% en los permisos de construcción. Además, las que se efectúen en las futuras áreas comerciales gozarán de un aumento de un 10% en el coeficiente de constructibilidad.

**Densidad:** Sin valor específico en la fuente (no se declara densidad mínima ni máxima para esta zona).

**Nota:** el primer punto ("predios existentes inferiores a 1.000 m² o 20 m. de frente se regirán por las mismas normas") es una cláusula de resguardo para predios preexistentes bajo el estándar, no una declaración directa del predial mínimo oficial de la zona — es un indicio indirecto de que el estándar podría rondar esa cifra, pero no reemplaza el dato ausente del cuadro; se mantiene "Dato no determinable" arriba.

---

## ZU-2 — Comercial - Artesanal

**Página:** 14 (usos + inicio del cuadro) → 15 (disposiciones complementarias). **Encabezado verbatim:** "ZONA ZU - 2 Comercial - Artesanal".

### Usos permitidos
- Comercio
- Talleres
- Bodegas
- Terminales Ferroviarios y Rodoviarios
- Equipamiento vecinal y comunal
- Vivienda

### Usos prohibidos
- Cementerios
- Botaderos de basura
- Estadios

### Cuadro de normas urbanísticas (cuadro numérico principal)

| Parámetro | Valor |
|---|---|
| Superficie predial mínima | Dato no determinable |
| Coeficiente de ocupación de suelo (COS) | Dato no determinable |
| Coeficiente de constructibilidad (CC) | Dato no determinable |
| Altura máxima | Dato no determinable |
| Sistema de agrupamiento | Dato no determinable |

→ Motivo: "Cuadro de normas urbanísticas: VER D.O. DE FECHA 10.09.1998" (p.14). Diario Oficial no disponible en este corpus.

### Disposiciones complementarias (verbatim, p.15)
- Los sitios existentes inferiores a 500 m² o 15 m. de frente se regirán por la misma normativa.
- Sobre el 3º piso el sistema de agrupamiento será aislado.
- El porcentaje de área libre podrá utilizarse para estacionamiento.
- La vivienda sólo podrá ubicarse en los pisos superiores.

**Densidad:** Sin valor específico en la fuente.

---

## ZU-3 — Mixta de Densificación

**Página:** 15. **Encabezado verbatim:** "ZONA ZU - 3 Mixta de Densificación".

### Usos permitidos
- Vivienda
- Equipamiento vecinal
- Equipamiento comunal

### Usos prohibidos
- Cementerios
- Botaderos de basura
- Estadios
- Canchas
- Quintas de recreo

### Cuadro de normas urbanísticas (cuadro numérico principal)

| Parámetro | Valor |
|---|---|
| Superficie predial mínima | Dato no determinable |
| Coeficiente de ocupación de suelo (COS) | Dato no determinable |
| Coeficiente de constructibilidad (CC) | Dato no determinable |
| Altura máxima | Dato no determinable |
| Sistema de agrupamiento | Dato no determinable |

→ Motivo: "Cuadro de normas urbanísticas: VER D.O. DE FECHA 10.09.1998" (p.15). Diario Oficial no disponible en este corpus.

### Disposiciones complementarias (verbatim)
- Los sitios existentes inferiores a 500 m² o 15 m. de frente se regirán por la misma normativa.
- Los estacionamientos que no quepan en el 25% de patio deberán ubicarse en subterráneo.
- **Densidad mínima: 400 hab/há.**
- Las propiedades que se reconstruyan y densifiquen durante los próximos 3 años gozarán de una rebaja del 50% en los permisos de construcción.
- El equipamiento comercial no podrá ocupar más del 5% de la superficie de cada manzana.
- Los predios destinados a talleres, garajes, reparación de automóviles y venta de gas licuado deberán tener una superficie y frente mínimos de **1.000 m² y 25 ml.** respectivamente (caso especial, no es el predial mínimo general de la zona, sino un mínimo específico para esos usos).

---

## ZU-4 — Vivienda

**Página:** 15 (usos + inicio del cuadro) → 16 (disposiciones complementarias). **Encabezado verbatim:** "ZONA ZU - 4 Vivienda".

### Usos permitidos
- Vivienda
- Equipamiento vecinal
- Equipamiento comunal

### Usos prohibidos
- Cementerios
- Botaderos de basura
- Quintas de recreo

### Cuadro de normas urbanísticas (cuadro numérico principal)

| Parámetro | Valor |
|---|---|
| **Superficie predial mínima** | **160 m²** — excepción: SÍ está disponible, ver nota abajo |
| Coeficiente de ocupación de suelo (COS) | Dato no determinable |
| Coeficiente de constructibilidad (CC) | Dato no determinable |
| Altura máxima | Dato no determinable |
| Sistema de agrupamiento | Dato no determinable |

→ Motivo (COS/CC/altura/agrupamiento): "Cuadro de normas urbanísticas: VER D.O.DE FECHA 10.09.1998" **[sic, falta espacio entre "D.O." y "DE"; única zona de las 14 con esta variante tipográfica]** (p.15-16). Diario Oficial no disponible en este corpus.

**Nota importante — hallazgo no cubierto por Fase 3:** a diferencia de las demás zonas, en ZU-4 la superficie predial mínima **sí figura explícitamente**, aunque no en el "cuadro" formal sino en las disposiciones complementarias: *"No obstante el tamaño mínimo predial (160 m2) podrá ser disminuido en los casos de construcción simultánea (Art. 7.2.6 de la Ord. Gral.)."* Es decir, 160 m² es el predial mínimo vigente de ZU-4, con una rebaja adicional posible bajo el Art. 7.2.6 de la Ordenanza General de Urbanismo y Construcciones para construcción simultánea (típicamente programas de vivienda social). COS, CC, altura y agrupamiento siguen ausentes. Ver el mismo patrón en ZE-1 más abajo (texto idéntico).

### Disposiciones complementarias (verbatim, p.16)
- No obstante el tamaño mínimo predial (160 m²) podrá ser disminuido en los casos de construcción simultánea (Art. 7.2.6 de la Ord. Gral.).
- **Densidad mínima: 300 hab/há.**

---

## ZU-5 — Vivienda Restringida

**Página:** 16. **Encabezado verbatim:** "ZONA ZU - 5 Vivienda Restringida".

### Usos permitidos
- Vivienda, solamente una por predio

### Usos prohibidos
- Botaderos de basura.

### Cuadro de normas urbanísticas (cuadro numérico principal)

| Parámetro | Valor |
|---|---|
| Superficie predial mínima | Dato no determinable |
| Coeficiente de ocupación de suelo (COS) | Dato no determinable |
| Coeficiente de constructibilidad (CC) | Dato no determinable |
| Altura máxima | Dato no determinable |
| Sistema de agrupamiento | Dato no determinable |

→ Motivo: "Cuadro de normas urbanísticas: VER D.O. DE FECHA 10.09.1998" (p.16). Diario Oficial no disponible en este corpus.

### Disposiciones complementarias (verbatim)
- Los sitios existentes inferiores a 1.000 m² o 10 m. de frente se regirán por la misma normativa.
- **Densidad máxima: 100 hab/há.**

---

## ZU-6 — Industria Inofensiva

**Página:** 16. **Encabezado verbatim:** "ZONA ZU - 6 Industria Inofensiva".

### Usos permitidos
- Industria inofensiva
- Talleres
- Bodegas
- Garajes

### Usos prohibidos
*(encabezado en la fuente: "Usos prohibidos" [sic, sin los dos puntos ":" que sí llevan todas las demás zonas])*
- Todos los demás, excepto casa del cuidador.

### Cuadro de normas urbanísticas (cuadro numérico principal)

| Parámetro | Valor |
|---|---|
| Superficie predial mínima | Dato no determinable |
| Coeficiente de ocupación de suelo (COS) | Dato no determinable |
| Coeficiente de constructibilidad (CC) | Dato no determinable |
| Altura máxima | Dato no determinable |
| Sistema de agrupamiento | Dato no determinable |

→ Motivo: "Cuadro de normas urbanísticas: VER D.O. DE FECHA 10.09.1998" (p.16). Diario Oficial no disponible en este corpus.

### Disposiciones complementarias (verbatim)
- Los sitios existentes inferiores a 1.000 m² o 25 m. de frente se regirán por la misma normativa.

**Densidad:** Sin valor específico en la fuente.

---

## ZU-7 — Industria Molesta

**Página:** 16 (usos + inicio del cuadro) → 17 (disposiciones complementarias). **Encabezado verbatim:** "ZONA ZU - 7 Industria Molesta".

### Usos permitidos
- Industria de todo tipo
- Talleres
- Bodegas
- Garajes

### Usos prohibidos
- Todos los demás, excepto casa del cuidador.

### Cuadro de normas urbanísticas (cuadro numérico principal)

| Parámetro | Valor |
|---|---|
| Superficie predial mínima | Dato no determinable |
| Coeficiente de ocupación de suelo (COS) | Dato no determinable |
| Coeficiente de constructibilidad (CC) | Dato no determinable |
| Altura máxima | Dato no determinable |
| Sistema de agrupamiento | Dato no determinable |

→ Motivo: "Cuadro de normas urbanísticas: VER D.O. DE FECHA 10.09.1998" (p.16). Diario Oficial no disponible en este corpus.

### Disposiciones complementarias (verbatim, p.17; el encabezado "Disposiciones complementarias:" queda al final de p.16 y el único punto de la lista aparece ya en p.17 — es un corte de página, no un vacío de contenido)
- Los sitios existentes inferiores a 2.000 m² o 30 m. de frente se regirán por la misma normativa.

**Densidad:** Sin valor específico en la fuente.

---

## ZU-8 — Equipamiento Exclusivo

**Página:** 17. **Encabezado verbatim:** "ZONA ZU - 8 Equipamiento Exclusivo".

### Usos permitidos
- Estadio Municipal
- Hospital
- Cementerio
- Áreas verdes
- Estación ferroviaria
- Subestación eléctrica
- Aeródromo civil.

### Usos prohibidos
- Todos los demás, excepto vivienda del cuidador.

### Cuadro de normas urbanísticas (cuadro numérico principal)

| Parámetro | Valor |
|---|---|
| Superficie predial mínima | Dato no determinable |
| Coeficiente de ocupación de suelo (COS) | Dato no determinable |
| Coeficiente de constructibilidad (CC) | Dato no determinable |
| Altura máxima | Dato no determinable |
| Sistema de agrupamiento | Dato no determinable |

→ Motivo: "Cuadro de normas urbanísticas: VER D.O. DE FECHA 10.09.1998" (p.17). Diario Oficial no disponible en este corpus.

### Disposiciones complementarias (verbatim)
- Las construcciones sólo pueden corresponder al uso que es propio de cada actividad existente.

**Densidad:** Sin valor específico en la fuente (zona de equipamiento, no residencial; no aplica por diseño).

---

## ZU-9 — Parque Municipal

**Página:** 17. **Encabezado verbatim:** "ZONA ZU - 9 Parque Municipal".

### Usos permitidos
- Equipamiento Parque Municipal

### Usos prohibidos
- Todos los demás.

### Cuadro de normas urbanísticas (cuadro numérico principal)

| Parámetro | Valor |
|---|---|
| Superficie predial mínima | Dato no determinable |
| Coeficiente de ocupación de suelo (COS) | Dato no determinable |
| Coeficiente de constructibilidad (CC) | Dato no determinable |
| Altura máxima | Dato no determinable |
| Sistema de agrupamiento | Dato no determinable |

→ Motivo: "Cuadro de normas urbanísticas: VER D.O. DE FECHA 10.09.1998" (p.17). Diario Oficial no disponible en este corpus.

### Disposiciones complementarias (verbatim)
- Las construcciones sólo pueden corresponder al uso que es propio de cada actividad existente.

**Nota:** esta disposición es literalmente idéntica a la de ZU-8 (misma oración exacta). No parece error de transcripción — ambas son zonas de destino único (equipamiento exclusivo / parque municipal) y comparten la misma lógica de restricción de uso.

**Densidad:** Sin valor específico en la fuente (no aplica por diseño).

---

## ZU-0 — Centro Cívico

**Página:** 17 (usos) → 18 (cuadro + disposiciones complementarias). **Encabezado verbatim:** "Zona ZU - 0 Centro Cívico." (nótese "Zona" en minúscula-título, distinto del resto del bloque ZU que usa "ZONA" en mayúsculas — ver observación de formato en el índice).

### Usos permitidos
- Equipamiento Comunal
- Equipamiento Vecinal
- Comercio
- Vivienda

### Usos prohibidos
- Cementerios
- Botaderos de basura
- Estadios
- Canchas
- Piscinas
- Ferias
- Terminales de buses

### Cuadro de normas urbanísticas (cuadro numérico principal)

| Parámetro | Valor |
|---|---|
| Superficie predial mínima | Dato no determinable |
| Coeficiente de ocupación de suelo (COS) | Dato no determinable |
| Coeficiente de constructibilidad (CC) | Dato no determinable |
| Altura máxima | Dato no determinable |
| Sistema de agrupamiento | Dato no determinable |

→ Motivo: "Cuadro de normas urbanísticas: VER D.O. DE FECHA 10.09.1998" (p.18). Diario Oficial no disponible en este corpus.

### Disposiciones complementarias (verbatim, p.18)
- Los predios existentes inferiores a 1.000 m² ó 25 m. de frente se regirán por las mismas normas.
- El porcentaje de área libre podrá utilizarse para estacionamiento.
- La vivienda sólo podrá ubicarse en los pisos superiores.
- Los pisos 4, 5 y 6 deberán retirarse de la línea oficial en 5 mts.
- Las propiedades que se reconstruyan y densifiquen durante los próximos tres años gozarán de una rebaja del 50% en los permisos de construcción.

**Densidad:** Sin valor específico en la fuente.

---

## ZE-1 — Expansión Densidad Media

**Página:** 18. **Encabezado verbatim:** "Zona ZE - 1 Expansión Densidad Media".

### Usos permitidos
- Vivienda.
- Equipamiento Vecinal.
- Equipamiento Comunal.

### Usos prohibidos
- Cementerios.
- Botaderos de basura.
- Quintas de recreo.

### Cuadro de normas urbanísticas (cuadro numérico principal)

| Parámetro | Valor |
|---|---|
| **Superficie predial mínima** | **160 m²** — excepción: SÍ está disponible, ver nota abajo |
| Coeficiente de ocupación de suelo (COS) | Dato no determinable |
| Coeficiente de constructibilidad (CC) | Dato no determinable |
| Altura máxima | Dato no determinable |
| Sistema de agrupamiento | Dato no determinable |

→ Motivo (COS/CC/altura/agrupamiento): "Cuadro de normas urbanísticas: VER D.O. DE FECHA 10.09.1998" (p.18). Diario Oficial no disponible en este corpus.

**Nota importante — hallazgo no cubierto por Fase 3:** igual que ZU-4, la superficie predial mínima de ZE-1 sí figura de forma explícita en disposiciones complementarias, con el texto **idéntico palabra por palabra** al de ZU-4: *"No obstante el tamaño mínimo predial (160 m2) podrá ser disminuido en los casos de construcción simultánea (Art. 7.2.6 de la Ord. Gral.)."*

### Disposiciones complementarias (verbatim)
- No obstante el tamaño mínimo predial (160 m²) podrá ser disminuido en los casos de construcción simultánea (Art. 7.2.6 de la Ord. Gral.).
- **Densidad mínima: 350 hab/há.**
- Los predios destinados a talleres, garajes, reparación de automóviles y venta de gas licuado deberán tener una superficie y frente mínimos de **500 m² y 15 ml.** respectivamente (caso especial, no es el predial mínimo general de la zona).

---

## ZE-2 — Expansión Densidad Baja

**Página:** 18 (usos + inicio del cuadro) → 19 (disposiciones complementarias). **Encabezado verbatim:** "Zona ZE - 2 Expansión Densidad Baja." (con punto final).

### Usos permitidos
- Vivienda.
- Equipamiento vecinal de educación, culto y deportes.

### Usos prohibidos
- Todos los demás.

### Cuadro de normas urbanísticas (cuadro numérico principal)

| Parámetro | Valor |
|---|---|
| Superficie predial mínima | Dato no determinable |
| Coeficiente de ocupación de suelo (COS) | Dato no determinable |
| Coeficiente de constructibilidad (CC) | Dato no determinable |
| Altura máxima | Dato no determinable |
| Sistema de agrupamiento | Dato no determinable |

→ Motivo: "Cuadro de normas urbanísticas: VER D.O. DE FECHA 10.09.1998" (p.18). Diario Oficial no disponible en este corpus.

### Disposiciones complementarias (verbatim, p.19)
- Los sitios existentes inferiores a 300 m² o 15 m. de frente se regirán por la misma normativa.
- **Densidad máxima: 200 hab/há.**

---

## ZE-3 — Expansión Mixta

**Página:** 19. **Encabezado verbatim:** "Zona ZE - 3 Expansión Mixta".

### Usos permitidos
- Vivienda.
- Equipamiento Vecinal.
- Equipamiento Comunal.
- Equipamiento Regional.

### Usos prohibidos
- Cementerios.
- Botaderos de basura.
- Zoológicos.
- Talleres.

### Cuadro de normas urbanísticas (cuadro numérico principal)

| Parámetro | Valor |
|---|---|
| Superficie predial mínima | Dato no determinable |
| Coeficiente de ocupación de suelo (COS) | Dato no determinable |
| Coeficiente de constructibilidad (CC) | Dato no determinable |
| Altura máxima | Dato no determinable |
| Sistema de agrupamiento | Dato no determinable |

→ Motivo: "Cuadro de normas urbanísticas:" seguido de un salto de línea doble (formato ligeramente distinto al resto: doble espacio en blanco antes de la remisión, en vez de uno) y luego "VER D.O. DE FECHA 10.09.1998" (p.19). Diario Oficial no disponible en este corpus.

### Disposiciones complementarias (verbatim)
- No se consultan.

**Nota:** a diferencia de las demás zonas, aquí el propio documento declara expresamente que no hay disposiciones complementarias ("No se consultan."), en vez de omitir la sección o dejarla en blanco. Se transcribe literal; no se aplica la convención "Sin valor específico en la fuente" porque sí hay un valor textual explícito (la propia declaración de ausencia), solo que no es un "dato suelto" utilizable.

**Densidad:** Sin valor específico en la fuente (consistente con "no se consultan" disposiciones complementarias para esta zona).

---

## ZE-4 — Zona de Expansión Industrial

**Página:** 19. **Encabezado verbatim:** "Zona ZE - 4 Zona de Expansión Industrial".

### Usos permitidos
- Industrias inofensivas y molestas.
- Talleres de todo tipo.
- Bodegas de todo tipo.
- Garajes.

### Usos prohibidos
- Industrias peligrosas, insalubres y contaminantes.
- Todos los demás, excepto casa del cuidador.

### Cuadro de normas urbanísticas (cuadro numérico principal)

| Parámetro | Valor |
|---|---|
| Superficie predial mínima | Dato no determinable |
| Coeficiente de ocupación de suelo (COS) | Dato no determinable |
| Coeficiente de constructibilidad (CC) | Dato no determinable |
| Altura máxima | Dato no determinable |
| Sistema de agrupamiento | Dato no determinable |

→ Motivo: "Cuadro de normas urbanísticas: VER D.O. DE FECHA 10.09.1998" (p.19). Diario Oficial no disponible en este corpus.

### Disposiciones complementarias (verbatim)
- Las industrias ubicadas frente a la Ruta 5 dentro del área urbana no pueden acceder directamente a ella, sino a una calle de tránsito local. En el área rural ellas deberán obtener la autorización de la Dirección de Vialidad del M.O.P.

**Densidad:** Sin valor específico en la fuente.

---

## Zonas ZR — Restricciones

El documento abre esta sección (p.19, inmediatamente después de ZE-4) con el título "Zonas ZR - Restricciones" y el subtítulo "A. Determinadas por el Plan Regulador.", seguido de la primera (y única, dentro del rango 14-19) zona de restricción:

### ZR-0 — Riberas del Estero Antivero

**Página:** 19 (última zona del rango asignado; el contenido continúa en la página 20, **fuera del rango de esta tarea**).

**Texto completo (verbatim):**

> "ZR - 0. Riberas del Estero Antivero.
> Esta se extiende a ambos lados de Estero Antivero, con un ancho variable según lo señalado en el Plano PR SF-1."

No trae cuadro de edificación ni parámetros numéricos — es una zona descriptiva de restricción (protección de cauce), definida por su extensión geográfica variable remitida al plano oficial "PR SF-1", no por un cuadro de normas. No corresponde marcar "Dato no determinable" aquí, porque no hay indicio de que esta zona tenga o deba tener un cuadro de edificación (es "Sin valor específico en la fuente" por diseño — zona de restricción/protección de cauce, no edificable).

**Importante — límite del rango asignado:** la página 19 termina inmediatamente después de este párrafo (el pie de página "página 19 de 23" aparece a continuación). Fase 3 anticipó, en su nota, que las zonas ZR incluyen además oleoductos, líneas de alta tensión y aeródromos ("p19-20 en adelante"), pero **esas zonas ZR adicionales no están dentro del rango de páginas 14-19 asignado a esta tarea** — deben estar en la página 20 en adelante, fuera de alcance. Solo se pudo confirmar y transcribir ZR-0 (la zona de "ríos"/cauces que menciona Fase 3); no se puede confirmar ni transcribir contenido sobre oleoductos, líneas de alta tensión o aeródromos porque ese contenido, si existe, está fuera del rango entregado.

---

## Discrepancias y hallazgos respecto de la nota de Fase 3

1. **Conteo de zonas — corrección de "13" a "14".** La nota de Fase 3 dice "las 13 zonas del PRC San Fernando (ZU-0 a ZU-9, ZE-1 a ZE-4)". Enumerando directamente los encabezados de zona efectivamente presentes en el texto (p.14-19), esta extracción encontró **14 zonas**: ZU-1, ZU-2, ZU-3, ZU-4, ZU-5, ZU-6, ZU-7, ZU-8, ZU-9, ZU-0 (10 zonas del bloque ZU) + ZE-1, ZE-2, ZE-3, ZE-4 (4 zonas del bloque ZE) = 14. El propio rango textual que cita Fase 3 ("ZU-0 a ZU-9" son 10 códigos inclusive, más "ZE-1 a ZE-4" son 4 códigos) ya suma 14 — el "13" parece un error aritmético de esa nota (posiblemente 9 + 4 = 13, omitiendo contar ZU-0 pese a incluirlo en el rango descrito). Cada una de las 14 zonas tiene su propio bloque completo de usos permitidos/prohibidos + remisión al cuadro + disposiciones complementarias — ninguna es un duplicado ni una sub-entrada de otra.

2. **Confirmación central de la alerta: correcta, y verificada de forma independiente en las 6 páginas (no solo p.14).** Las 14 zonas remiten literalmente a "VER D.O. DE FECHA 10.09.1998" en vez de un cuadro numérico. Se confirma que no es imagen oculta: el render es texto tipográfico nativo en las 6 páginas, sin ningún elemento gráfico cerca de la frase.

3. **Variante tipográfica no citada por Fase 3.** Fase 3 parafraseó la remisión sin dar la cita exacta por zona. Esta extracción encontró que **ZU-4** usa "VER D.O.DE FECHA 10.09.1998" (sin espacio entre "D.O." y "DE") — único caso entre las 14 zonas; las 13 restantes usan "VER D.O. DE FECHA 10.09.1998" (con espacio). Verificado tanto en el texto plano como en el render de la página 15-16.

4. **Hallazgo no cubierto por Fase 3: el predial mínimo SÍ está disponible en 2 de las 14 zonas (ZU-4 y ZE-1).** Fase 3 generalizó la ausencia a los 5 parámetros del cuadro para "las 13 zonas" sin distinción. Esta extracción encontró que en ZU-4 y ZE-1, pese a que el "cuadro" formal remite igualmente al D.O. de 1998, las disposiciones complementarias declaran explícitamente un predial mínimo de **160 m²** (con posibilidad de rebaja bajo Art. 7.2.6 de la Ordenanza General de Urbanismo y Construcciones para construcción simultánea), con texto idéntico palabra por palabra en ambas zonas. COS, CC, altura y sistema de agrupamiento siguen "Dato no determinable" en ambas. Este matiz no aparece en la nota de Fase 3.

5. **Zonas ZR: solo ZR-0 cae dentro del rango asignado.** Fase 3 agrupó "p19-20 en adelante: Zonas ZR de restricción (oleoductos, líneas alta tensión, ríos, aeródromos)" como si todo eso fuera revisable. Dentro del rango efectivamente asignado a esta tarea (14-19), solo alcanza a aparecer **ZR-0 (Riberas del Estero Antivero)** — la zona de "ríos" que Fase 3 menciona — justo antes de que termine la página 19. Las zonas de oleoductos, líneas de alta tensión y aeródromos que Fase 3 anticipa deben estar en la página 20 en adelante, **fuera del alcance de esta tarea**; no se pueden confirmar ni transcribir aquí.

6. **No se detectó "trampa comuna ajena".** Las 6 páginas mantienen el encabezado "Decreto 1698 EXENTO, SAN FERNANDO (1997)" de forma consistente en la parte superior, y el pie de página BCN avanza correlativamente "página 14 de 23" → "página 19 de 23" sin discontinuidad. Todo el contenido de usos de suelo, disposiciones complementarias y la zona ZR-0 (Estero Antivero, curso de agua real de la comuna de San Fernando) es consistente con San Fernando; no se encontró contenido de otra comuna ni de otra institución mezclado en el rango 14-19.

7. **Hallazgos adicionales menores, no cubiertos por Fase 3 (no afectan el cuadro numérico, se documentan por rigor):**
   - **ZU-6** tiene el encabezado "Usos prohibidos" sin los dos puntos (":") que sí llevan las 13 zonas restantes — errata de formato, preservada [sic].
   - El texto de disposiciones complementarias de **ZU-8** y **ZU-9** ("Las construcciones sólo pueden corresponder al uso que es propio de cada actividad existente.") es idéntico palabra por palabra entre ambas zonas.
   - Las zonas **ZU-1 a ZU-9** usan el encabezado "ZONA" en mayúsculas; **ZU-0** y las cuatro zonas **ZE** usan "Zona" en minúscula-título. Es un patrón consistente por bloque, no un error aislado.
   - Varias zonas (ZU-1, ZU-2, ZU-3, ZU-5, ZU-6, ZU-7, ZU-0, ZE-2) tienen una cláusula de resguardo para "predios/sitios existentes inferiores a [X] m² o [Y] m. de frente" que se regirán "por la misma normativa". Estos valores (1.000/20, 500/15, 500/15, 1.000/10, 1.000/25, 2.000/30, 1.000/25, 300/15 respectivamente) son indicios indirectos de cuál podría ser el predial mínimo/frente mínimo real de cada zona en el cuadro ausente, pero **no son una confirmación** de esos valores — se mantienen como "Dato no determinable" en las tablas de cada zona, y el indicio se deja solo como nota.
   - **ZE-3** es la única zona cuyas disposiciones complementarias declaran expresamente "No se consultan." (ausencia declarada, no omitida).

## Notas finales de verificación y nivel de confianza

- **Nivel de confianza global: ALTA** en la fidelidad de la transcripción (texto nativo, no imagen escaneada; verificación 1:1 entre texto plano y render en las 6 páginas, sin caracteres ilegibles ni ambigüedades). Esto es independiente del nivel de **completitud** de las normas urbanísticas de San Fernando, que es estructuralmente bajo por causas ajenas a esta extracción (el cuadro numérico de las 14 zonas depende de un Diario Oficial de 1998 no disponible en este corpus).
- **Por página:**

| Página | Contenido | Confianza | Método |
|---|---|---|---|
| 14 | Encabezado de sección ("Ver Plano PR SF - 1"), ZU-1 completa, ZU-2 (usos + inicio de cuadro) | ALTA | Texto nativo + render visual completo |
| 15 | ZU-2 (disposiciones complementarias), ZU-3 completa, ZU-4 (usos + inicio de cuadro, con variante "D.O.DE") | ALTA | Texto nativo + render visual completo |
| 16 | ZU-4 (disposiciones complementarias), ZU-5 completa, ZU-6 completa, ZU-7 (usos + inicio de cuadro) | ALTA | Texto nativo + render visual completo |
| 17 | ZU-7 (disposiciones complementarias), ZU-8 completa, ZU-9 completa, ZU-0 (usos) | ALTA | Texto nativo + render visual completo |
| 18 | ZU-0 (cuadro + disposiciones complementarias), ZE-1 completa, ZE-2 (usos + inicio de cuadro) | ALTA | Texto nativo + render visual completo |
| 19 | ZE-2 (disposiciones complementarias), ZE-3 completa, ZE-4 completa, inicio de "Zonas ZR - Restricciones" + ZR-0 completa | ALTA | Texto nativo + render visual completo |

- **Limitación estructural (no de esta extracción, sino de la fuente):** el cuadro numérico principal (superficie predial mínima, COS, coeficiente de constructibilidad, altura máxima, sistema de agrupamiento) de las 14 zonas ZU/ZE está genuinamente ausente del documento disponible en este corpus, con la única excepción parcial de la superficie predial mínima de ZU-4 y ZE-1 (160 m², vía disposiciones complementarias). Completar el resto del cuadro para San Fernando requeriría conseguir el Diario Oficial del 10-09-1998, tarea fuera del alcance de este encargo (confirma la recomendación de Fase 3 de conseguir ese Diario Oficial).
- **No se identificó ninguna zona faltante dentro del rango 14-19**: las 14 zonas listadas en el índice cubren el 100% de los encabezados de zona presentes en el texto de las 6 páginas. La zona ZR-0 es el único contenido de restricción alcanzable dentro del rango; el resto de las zonas ZR (fuera del alcance) queda pendiente para quien procese la página 20 en adelante.
