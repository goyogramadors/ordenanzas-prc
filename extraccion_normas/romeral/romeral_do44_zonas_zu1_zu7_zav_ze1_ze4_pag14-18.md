# Cuadro Normativo por Zona — PRC Romeral (Decreto N°44/2017)

**Fuente:** Diario Oficial de la República de Chile, Núm. 41.766, jueves 25 de mayo de 2017, páginas 14 a 18 de 25. CVE 1218536. Decreto N°44/2017, Ilustre Municipalidad de Romeral, Región del Maule — Plan Regulador Comunal de Romeral, texto de la Ordenanza Local, **Artículo 4.2 (Zonificación del Área Urbana)** y **Artículo 4.3 (Normas Urbanísticas por Zona)**.

**Material fuente utilizado:** imágenes PNG renderizadas a 250dpi (`romeral_p14-18-14.png` a `romeral_p14-18-18.png`) como fuente primaria y confiable. El archivo de texto plano `romeral_p14-18.txt` se usó solo como orientación de estructura (títulos de zona) — **se confirmó la "trampa"**: el `.txt` no contiene ninguno de los valores numéricos de los cuadros de "Usos de Suelo" ni de "Normas de Subdivisión y Edificación"; esos cuadros están incrustados como imagen. Todos los valores de este documento provienen de la lectura visual de los PNG, no del `.txt`.

**Convenciones usadas en este documento:**
- `-` (guion simple): valor literal tal como aparece en la fuente. En las tablas "Usos de Suelo" es la propia notación del documento para "sin excepciones / no aplica" en la columna EXCEPTO.
- **"Sin valor específico en la fuente"**: la celda aparece vacía en el original (ni siquiera tiene un guion), o la fila/campo completo no existe en la tabla de esa zona porque no aplica por diseño (p. ej. zonas sin uso residencial no tienen fila de Densidad Bruta Máxima). Se explica el motivo entre paréntesis en cada caso.
- **"Dato no determinable"**: reservado para valores que deberían existir pero no son legibles o no están en el corpus. **No se usó ninguna vez en este documento** — todos los campos observados fueron o bien legibles, o bien ausentes por diseño (ver "Notas finales de verificación").
- En las tablas "Normas de Subdivisión y Edificación" que distinguen columnas RESIDENCIAL / EQUIPAMIENTO (o RESIDENCIAL / INFRAESTRUCTURA Y EQUIPAMIENTO), cuando la fuente presenta una **celda combinada (colspan)** con un único valor para ambas columnas, este documento repite el mismo valor en las dos columnas de la tabla Markdown (Markdown no soporta colspan) y lo indica explícitamente en una nota bajo la tabla.
- Los códigos de zona se normalizan a formato `ZU-1`, `ZE-1`, etc. en los encabezados de este documento. La fuente usa tipografías mixtas: guion medio con espacios para las zonas ZU (`ZU – 1`) y guion simple con espacios para las zonas ZE (`ZE - 1`); no es una diferencia normativa, solo tipográfica.

---

## Artículo 4.2 — Área Urbana / Zonificación (página 14)

Transcripción literal del listado: *"El Área Urbana de la Comuna de Romeral se divide en las siguientes zonas:"*

| Código | Denominación |
|---|---|
| ZU – 1 | ZONA MIXTA 1 |
| ZU – 2 | ZONA MIXTA 2 |
| ZU – 3 | ZONA MIXTA 3 |
| ZU – 4 | ZONA MIXTA RESIDENCIAL 4 |
| ZU – 5 | ZONA MIXTA RESIDENCIAL 5 |
| ZU – 6 | ZONA MIXTA RESIDENCIAL 6 |
| ZU – 7 | ZONA MIXTA RESIDENCIAL 7 |
| ZAV | ZONA DE ÁREA VERDE |
| ZE – 1 | ZONA DE EQUIPAMIENTO 1 |
| ZE – 2 | ZONA DE EQUIPAMIENTO 2 |
| ZE – 3 | ZONA DE EQUIPAMIENTO 3 |
| ZE – 4 | ZONA DE EQUIPAMIENTO 4 |

**Total: 12 zonas** (7 ZU + 1 ZAV + 4 ZE). Esto **confirma exactamente** el conteo anticipado por la nota de Fase 3 (7 ZU + ZAV + 4 ZE).

A continuación, Artículo 4.3 ("Normas Urbanísticas por Zona"): *"Las normas específicas para las zonas indicadas en el Cuadro anterior se establecen en los artículos siguientes."* Inmediatamente después comienza el cuadro de ZU-1, en la misma página 14.

---

## ZU-1 — Zona Mixta 1
*(página 14 — cuadro completo: Usos de Suelo + Normas de Subdivisión y Edificación, ambos en la misma página)*

### Usos de suelo

| Tipo | Destino/Clases | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Todos los destinos de este uso | - |
| EQUIPAMIENTO | CIENTIFICO | Grupo1 | - |
| EQUIPAMIENTO | COMERCIO | Grupo 1, 2 y 3 | - |
| EQUIPAMIENTO | CULTO Y CULTURA | Grupo 1, 2, 3 y 4 | - |
| EQUIPAMIENTO | DEPORTE | Grupo 1, 2 y 3 | - |
| EQUIPAMIENTO | EDUCACION | Grupo 2, 3 y 4 | - |
| EQUIPAMIENTO | ESPARCIMIENTO | Grupo 1, 2 y 3 | Parques de entretenciones, casinos, juegos mecánicos, y similares. |
| EQUIPAMIENTO | SALUD | Grupo 1, 2 y 3 | - |
| EQUIPAMIENTO | SEGURIDAD | Grupo 1, 2 y 3 | **Sin valor específico en la fuente** (celda vacía en el original, sin guion — a diferencia de las demás filas de esta misma tabla que sí muestran "-") |
| EQUIPAMIENTO | SERVICIOS | Grupo 1, 2, 3 y 4 | - |
| EQUIPAMIENTO | SOCIAL | Grupo 1, 2, 3 y 4 | - |

### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 500 m² |
| Coeficiente de ocupación de suelo | 0,6 |
| Coeficiente de constructibilidad | 1,2 |
| Sistema de agrupamiento | Continuo |
| Altura máxima de edificación | 8 m |
| Densidad bruta máxima | 75 hab./há |

**Nota de contexto (no forma parte del Decreto 44/2017, agregada para trazabilidad del corpus):** en la misma carpeta de extracción existen dos actos posteriores que modifican estas normas de subdivisión y edificación de ZU-1, pero **solo para dos polígonos municipales específicos** (terreno de la Municipalidad y polígono colindante a Surfrut), no para el resto de la zona: Enmienda N°1 (Decreto 2.782/2019, ver `romeral_2782_enmienda1_zu1.md`: 500 m² / COS 0,78 / CC 1,56 / Continuo / 9,6 m / 75 hab/há) y Enmienda N°2 (Decreto 2056/2021, ver `romeral_2056_enmienda_n2_zu1_pag3.md`: 350 m² / COS 0,78 / CC 1,56 / Continuo / 9,6 m / 90 y 75 hab/há según el polígono). El cuadro transcrito arriba es el texto **original** de Decreto 44/2017 y sigue vigente para el resto de los predios de ZU-1 no cubiertos por esas enmiendas.

---

## ZU-2 — Zona Mixta 2
*(usos de suelo en página 14; tabla de Normas de Subdivisión y Edificación **partida entre página 14 y 15** — ver discrepancia con nota de Fase 3 más abajo)*

### Usos de suelo

| Tipo | Destino/Clases | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Todos los destinos de este uso | - |
| EQUIPAMIENTO | COMERCIO | Grupo 1, 2 y 3 | - |
| EQUIPAMIENTO | CULTO Y CULTURA | Grupo 1, 2 y 3 | Templos, Cines, Teatros, Auditorios, Medios de comunicación. |
| EQUIPAMIENTO | DEPORTE | Grupo 1, 2 y 3 | - |
| EQUIPAMIENTO | EDUCACION | Grupo 1, 2 y 3 | Centros de rehabilitación conductual. |
| EQUIPAMIENTO | ESPARCIMIENTO | Grupo 1, 2, 3 y 4 | - |
| EQUIPAMIENTO | SALUD | Grupo 1 y 2 | - |
| EQUIPAMIENTO | SEGURIDAD | Grupo 1, 2 y 3 | - |
| EQUIPAMIENTO | SOCIAL | Grupo 1, 2, 3 y 4 | - |

### Normas de subdivisión y edificación

| Norma | Residencial | Equipamiento |
|---|---|---|
| Superficie de subdivisión predial mínima | 200 m² | 200 m² |
| Coeficiente de ocupación de suelo | 0,4 | 0,5 |
| Coeficiente de constructibilidad | 0,8 | 1,0 |
| Sistema de agrupamiento | Aislado y Pareado | Aislado |
| Altura máxima de edificación | 8 m | 11 m |
| Antejardín | 3,00 m | 3,00 m |
| Densidad bruta máxima | 120 hab./há | 120 hab./há |

*Nota de formato: en la fuente, las filas "Superficie de subdivisión predial mínima", "Antejardín" y "Densidad bruta máxima" son una única celda combinada que abarca ambas columnas (mismo valor para Residencial y Equipamiento); se replicó el valor en ambas columnas de esta tabla Markdown. Las filas de COS, Coeficiente de Constructibilidad, Sistema de Agrupamiento y Altura Máxima sí tienen valores distintos por columna en la fuente.*

---

## ZU-3 — Zona Mixta 3
*(página 15 — cuadro completo)*

### Usos de suelo

| Tipo | Destino/Clases | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Todos los destinos de este uso | Viviendas y Hogares de Acogida. |
| EQUIPAMIENTO | COMERCIO | Grupo 1, 2 y 3 | Supermercados, Mercados. |
| EQUIPAMIENTO | CULTO Y CULTURA | Grupo 1, 2, 3 y 4 | Templos. |
| EQUIPAMIENTO | DEPORTE | Grupo 1, 2, 3 y 4 | - |
| EQUIPAMIENTO | EDUCACION | Grupo 3 | Establecimientos destinados a educación media y media técnica. Centros de rehabilitación conductual. |
| EQUIPAMIENTO | ESPARCIMIENTO | Grupo 1, 2, 3 y 4 | Casinos |

### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 2.000 m² |
| Coeficiente de ocupación de suelo | 0,2 |
| Coeficiente de constructibilidad | 0,4 |
| Sistema de agrupamiento | Aislado |
| Altura máxima de edificación | 8 m |
| Antejardín | 5,00 m |
| Densidad bruta máxima | 30 hab./há |

---

## ZU-4 — Zona Mixta Residencial 4
*(página 15 — cuadro completo)*

### Usos de suelo

| Tipo | Destino/Clases | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Todos los destinos de este uso. | - |
| EQUIPAMIENTO | COMERCIO | Grupo 1, 2 y 3 | Restaurantes, Fuentes de Soda, Bares diurnos. |
| EQUIPAMIENTO | CULTO Y CULTURA | Grupo 1 y 2 | Salas de concierto o espectáculos Galerías de arte, Medios de comunicación. *(así aparece en la fuente: sin coma entre "espectáculos" y "Galerías", posible omisión tipográfica del original — se transcribe literal, sin corregir)* |
| EQUIPAMIENTO | DEPORTE | Grupo 1 y 2 | Piscinas, Saunas, Baños turcos. |
| EQUIPAMIENTO | EDUCACION | Grupo 1 y 2 | - |
| EQUIPAMIENTO | ESPARCIMIENTO | Grupo 1 | - |
| EQUIPAMIENTO | SALUD | Grupo 1 y 2 | - |
| EQUIPAMIENTO | SEGURIDAD | Grupo 1, 2 y 3 | - |
| EQUIPAMIENTO | SERVICIOS | Grupo 1, 2 y 3 | Oficinas, Notarías, Instituciones de Salud Previsional, Administradoras de Fondos de Pensiones, Compañías de Seguros, Bancos, Financieras, Servicios Públicos en General. |
| EQUIPAMIENTO | SOCIAL | Grupo 1, 2, 3 y 4 | - |

### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 140 m² |
| Coeficiente de ocupación de suelo | 0,5 |
| Coeficiente de constructibilidad | 1 |
| Sistema de agrupamiento | Aislado, Pareado |
| Altura máxima de edificación | 8 m |
| Antejardín | 2,00 m |
| Densidad bruta máxima | 180 hab./ha |

*Nota de formato menor: la fuente escribe "1" (sin decimales) para el Coeficiente de Constructibilidad, y "ha" sin tilde (a diferencia de "há" con tilde usado en la mayoría de las demás zonas) para la unidad de densidad. Se transcribe literal.*

---

## ZU-5 — Zona Mixta Residencial 5
*(página 16 — cuadro completo)*

### Usos de suelo

| Tipo | Destino/Clases | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Todos los destinos de este uso. | - |
| INFRAESTRUCTURA | Sanitaria | Plantas de captación, distribución o tratamiento de agua potable | - |
| EQUIPAMIENTO | CIENTIFICO | Grupo 1 | - |
| EQUIPAMIENTO | COMERCIO | Grupo 2, 3 | - |
| EQUIPAMIENTO | CULTO Y CULTURA | Grupo 3 y 4 | - |
| EQUIPAMIENTO | DEPORTE | Grupo 2 | - |
| EQUIPAMIENTO | EDUCACION | Grupo 2, 3 y 4 | Centros de rehabilitación conductual. |
| EQUIPAMIENTO | ESPARCIMIENTO | Grupo 1 | - |
| EQUIPAMIENTO | SALUD | Grupo 1 y 2 | - |
| EQUIPAMIENTO | SEGURIDAD | Grupo 3 | - |
| EQUIPAMIENTO | SERVICIOS | Grupo 2, 3 y 4 | - |
| EQUIPAMIENTO | SOCIAL | Grupo 2, 3 y 4 | - |

### Normas de subdivisión y edificación

| Norma | Residencial | Infraestructura y Equipamiento |
|---|---|---|
| Superficie de subdivisión predial mínima | 300 m² | 300 m² |
| Coeficiente de ocupación de suelo | 0,5 | 0,5 |
| Coeficiente de constructibilidad | 0,8 | 1,0 |
| Sistema de agrupamiento | Aislado y Pareado | Aislado y Pareado |
| Altura máxima de edificación | 8 m | 8 m |
| Antejardín | 3,00 m | 3,00 m |
| Densidad bruta máxima | 80 hab./há | 80 hab./há |

*Nota de formato: en la fuente son celdas combinadas (mismo valor en ambas columnas) las filas de Superficie, COS, Sistema de Agrupamiento, Altura Máxima, Antejardín y Densidad Bruta Máxima — se verificó visualmente con zoom que el COS "0,5" también es un valor único centrado, no partido. La única fila con valores distintos por columna es Coeficiente de Constructibilidad (0,8 Residencial / 1,0 Infraestructura y Equipamiento).*

---

## ZU-6 — Zona Mixta Residencial 6
*(página 16 — cuadro completo)*

### Usos de suelo

| Tipo | Destino/Clases | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Todos los destinos de este uso. | - |
| EQUIPAMIENTO | COMERCIO | Grupo 1 y 2 | - |
| EQUIPAMIENTO | CULTO Y CULTURA | Grupo 1, 2 y 3 | Salas de concierto o espectáculos, Cines, Teatros, Auditorios, Centros de eventos, Centros de convenciones, Medios de comunicación. |
| EQUIPAMIENTO | DEPORTE | Grupo 1, 2, 3 | - |
| EQUIPAMIENTO | ESPARCIMIENTO | Grupo 1 y 3 | - |
| EQUIPAMIENTO | SOCIAL | Grupo 1 y 2 | - |

### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 800 m² *(la fuente usa "2" en línea base, no superíndice "²", a diferencia de casi todas las demás zonas — se normaliza aquí a "m²" por consistencia; el valor numérico 800 no cambia)* |
| Coeficiente de ocupación de suelo | 0,3 |
| Coeficiente de constructibilidad | 0,6 |
| Sistema de agrupamiento | Aislado |
| Altura máxima de edificación | 8 m |
| Antejardín | 3,00 m |
| Densidad bruta máxima | 30 hab./há |

---

## ZU-7 — Zona Mixta Residencial 7
*(usos de suelo en página 16; tabla de Normas de Subdivisión y Edificación **partida entre página 16 y 17** — mismo patrón de partición de tabla ya visto en ZU-2 entre p.14/15, no mencionado por Fase 3)*

### Usos de suelo

Se verificó con zoom que esta tabla termina genuinamente en la fila ESPARCIMIENTO (borde de cierre de tabla visible antes del salto de página); ZU-7 **no tiene filas** SALUD, SEGURIDAD, SERVICIOS ni SOCIAL, a diferencia de ZU-4 y ZU-5.

| Tipo | Destino/Clases | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Todos los destinos de este uso. | Vivienda, Hogares de Acogida |
| EQUIPAMIENTO | COMERCIO | Grupo 1, 2 y 3 | Supermercados, Mercados, y Discotecas. |
| EQUIPAMIENTO | CULTO Y CULTURA | Grupo 1, 2, 3 y 4 | Templos. |
| EQUIPAMIENTO | DEPORTE | Grupo 1, 2, 3 y 4 | - |
| EQUIPAMIENTO | EDUCACION | Grupo 3 | Establecimientos destinados a educación media y media técnica. Centros de rehabilitación conductual. |
| EQUIPAMIENTO | ESPARCIMIENTO | Grupo 1, 2, 3 y 4 | Casinos. |

### Normas de subdivisión y edificación

| Norma | Residencial | Equipamiento |
|---|---|---|
| Superficie de subdivisión predial mínima | 2.000 m² | 2.000 m² |
| Coeficiente de ocupación de suelo | 0,2 | 0,1 |
| Coeficiente de constructibilidad | 0,4 | 0,1 |
| Sistema de agrupamiento | Aislado | Aislado |
| Altura máxima de edificación | 8 m | 3,5 m |
| Antejardín | 10,0 m | 10,0 m |
| Densidad bruta máxima | 30 hab./há | 30 hab./há |

*Nota de formato: Superficie, Sistema de Agrupamiento, Antejardín y Densidad Bruta Máxima son celda combinada (mismo valor ambas columnas) en la fuente; COS, Coeficiente de Constructibilidad y Altura Máxima tienen valores distintos por columna. Se confirmó visualmente que el inicio de esta tabla en la página 17 es el primer contenido de la página (no hay continuación de filas de Usos de Suelo perdida en el salto de página).*

---

## ZE-1 — Zona de Equipamiento 1
*(página 17 — cuadro completo)*

### Usos de suelo

| Tipo | Destino/Clases | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Todos los destinos de este uso. | Hogares de Acogida |
| EQUIPAMIENTO | COMERCIO | Grupo 1 y 2 | - |
| EQUIPAMIENTO | CULTO Y CULTURA | Grupo 1, 2, 3 y 4 | Templos. |
| EQUIPAMIENTO | DEPORTE | Grupo 1, 2 y 3 | - |
| EQUIPAMIENTO | EDUCACION | Grupo 3 | Establecimientos destinados a educación media y media técnica. Centros de rehabilitación conductual. |
| EQUIPAMIENTO | ESPARCIMIENTO | Grupo 1, 2, 3 y 4 | Casinos |

### Normas de subdivisión y edificación

| Norma | Residencial | Equipamiento |
|---|---|---|
| Superficie de subdivisión predial mínima | 500 m² | 500 m² |
| Coeficiente de ocupación de suelo | 0,4 | 0,2 |
| Coeficiente de constructibilidad | 0,8 | 0,4 |
| Sistema de agrupamiento | Aislado | Aislado |
| Altura máxima de edificación | 7 m | 7 m |
| Antejardín | 5,00 m | 5,00 m |
| Densidad bruta máxima | 80 hab./há | 80 hab./há |

*Nota de formato: Superficie, Sistema de Agrupamiento, Altura Máxima, Antejardín y Densidad Bruta Máxima son celda combinada en la fuente; COS y Coeficiente de Constructibilidad tienen valores distintos por columna.*

---

## ZE-2 — Zona de Equipamiento 2
*(página 17 — cuadro completo)*

Esta zona **no admite uso residencial** (no hay fila RESIDENCIAL en la tabla de Usos de Suelo, y consistentemente no hay fila de Densidad Bruta Máxima en Normas de Subdivisión).

### Usos de suelo

| Tipo | Destino/Clases | Permitidos | Excepto |
|---|---|---|---|
| EQUIPAMIENTO | CULTO Y CULTURA | Grupo 1, 2, 3 y 4 | Medios de comunicación. |
| EQUIPAMIENTO | DEPORTE | Grupo 1, 2, 3 y 4 | - |
| EQUIPAMIENTO | ESPARCIMIENTO | Grupo 1, 2, 3 y 4 | - |
| EQUIPAMIENTO | SEGURIDAD | Grupo 2 | - |

### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 1000 m² |
| Coeficiente de ocupación de suelo | 0,1 |
| Coeficiente de constructibilidad | 0,2 |
| Sistema de agrupamiento | Aislado |
| Altura máxima de edificación | 7 m |
| Antejardín | 5,00 m |
| Densidad bruta máxima | **Sin valor específico en la fuente** (fila ausente en la tabla; no aplica — la zona no contempla uso residencial) |

---

## ZE-3 — Zona de Equipamiento 3
*(página 17 — cuadro completo)*

Al igual que ZE-2, **no admite uso residencial** y no tiene fila de Densidad Bruta Máxima. Se verificó con zoom que la tabla de Normas termina genuinamente en Antejardín (10,0 m), con espacio en blanco real antes del pie de página — no es un corte de página que perdiera una fila adicional.

### Usos de suelo

| Tipo | Destino/Clases | Permitidos | Excepto |
|---|---|---|---|
| EQUIPAMIENTO | CULTO Y CULTURA | Grupo 1 | Bibliotecas y Galerías de arte. |
| EQUIPAMIENTO | SALUD | Grupo 1 y 4 | - |

### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 1000 m² |
| Coeficiente de ocupación de suelo | 0,5 |
| Coeficiente de constructibilidad | 0,7 |
| Sistema de agrupamiento | Aislado |
| Altura máxima de edificación | 7 m |
| Antejardín | 10,0 m |
| Densidad bruta máxima | **Sin valor específico en la fuente** (fila ausente en la tabla; no aplica — la zona no contempla uso residencial) |

---

## ZE-4 — Zona de Equipamiento 4
*(página 18 — cuadro completo)*

### Usos de suelo

| Tipo | Destino/Clases | Permitidos | Excepto |
|---|---|---|---|
| RESIDENCIAL | — | Todos los destinos de este uso. | - |
| INFRAESTRUCTURA | Sanitaria | Plantas de captación, distribución o tratamiento de agua potable, Plantas de tratamiento de aguas servidas. | - |
| EQUIPAMIENTO | COMERCIO | Grupo 1 y 2 | **Sin valor específico en la fuente** (celda vacía en el original, sin guion — mismo patrón que ZU-1/SEGURIDAD) |
| EQUIPAMIENTO | CULTO Y CULTURA | Grupo 2 y 3 | Templos, Cines, Teatros, Medios de comunicación. |
| EQUIPAMIENTO | DEPORTE | Grupo 1, 2, 3 y 4 | - |
| EQUIPAMIENTO | EDUCACION | Grupo 3 | Centros de rehabilitación conductual. |

### Normas de subdivisión y edificación

| Norma | Residencial | Infraestructura y Equipamiento |
|---|---|---|
| Superficie de subdivisión predial mínima | 400 m² | 400 m² |
| Coeficiente de ocupación de suelo | 0,7 | 0,5 |
| Coeficiente de constructibilidad | 1,2 | 0,8 |
| Sistema de agrupamiento | Aislado, Pareado | Aislado |
| Altura máxima de edificación | 7 m | 7 m |
| Antejardín | 5,00 m | 5,00 m |
| Densidad bruta máxima | 50 hab./há | 50 hab./há |

*Nota de formato: Superficie, Altura Máxima, Antejardín y Densidad Bruta Máxima son celda combinada en la fuente; COS, Coeficiente de Constructibilidad y Sistema de Agrupamiento tienen valores distintos por columna.*

---

## ZAV — Zona de Área Verde
*(página 18 — cuadro completo)*

**Diferencia estructural relevante:** ZAV es la única de las 12 zonas que **no tiene tabla de "Usos de Suelo"**. En su lugar, el Decreto presenta un párrafo descriptivo, transcrito aquí de forma literal:

> "Corresponden a las zonas declaradas por el Plan Regulador que pueden ser terrenos particulares como fiscales, que no son bienes nacionales de uso público, de acuerdo a lo establecido en la OGUC."

Tampoco tiene fila de Densidad Bruta Máxima (consistente con no tener uso residencial ni tabla de usos de suelo).

### Normas de subdivisión y edificación

| Norma | Valor |
|---|---|
| Superficie de subdivisión predial mínima | 2.500 m² |
| Coeficiente de ocupación de suelo | 0,1 |
| Coeficiente de constructibilidad | 0,1 |
| Altura máxima de edificación | 3,5 m |
| Sistema de agrupamiento | Aislado |
| Antejardín | 10 m |
| Densidad bruta máxima | **Sin valor específico en la fuente** (fila ausente en la tabla; no aplica — zona de área verde, sin uso residencial) |

*Nota: el orden de filas de esta tabla en la fuente es distinto al de las demás zonas (Altura Máxima aparece antes que Sistema de Agrupamiento); se preservó el orden literal de la fuente.*

---

## Discrepancias y hallazgos respecto de la nota de Fase 3

1. **Conteo y códigos de zona: confirmados sin discrepancia.** Las 12 zonas (ZU-1 a ZU-7, ZAV, ZE-1 a ZE-4) existen exactamente como las listó Fase 3, con los mismos códigos y denominaciones.

2. **"Tabla ZU-1 y ZU-2 completas en la misma página [14]" — impreciso.** ZU-1 sí está completa en la página 14 (Usos de Suelo + Normas de Subdivisión). ZU-2, en cambio, solo tiene su tabla de Usos de Suelo completa en la página 14; su tabla de "Normas de Subdivisión y Edificación" está **partida**: la fila de encabezado y los valores completos aparecen recién al inicio de la página 15, antes del título de ZU-3. No es un error grave de Fase 3 (el contenido de ZU-2 efectivamente "empieza" en la página 14), pero "completas" no es exacto para ZU-2.

3. **Patrón de partición de tabla no detectado por Fase 3 para ZU-7.** El mismo fenómeno de la tabla de Normas de Subdivisión partida entre páginas se repite entre ZU-7 (usos de suelo en p.16) y su tabla de normas (que continúa al inicio de p.17, antes de ZE-1). La nota de Fase 3 no menciona este segundo caso. Se verificó con zoom en ambos saltos de página (p.14→15 y p.16→17) que no se perdió ninguna fila adicional de "Usos de Suelo" en el corte — cada página siguiente comienza directamente con la tabla de "Normas de Subdivisión y Edificación".

4. **Contenido adicional en página 18 no mencionado por Fase 3.** La nota de Fase 3 dice "p19 ya es Título 5 Vialidad Estructurante (fuera de rango)", lo que podría sugerir que las páginas 14-18 están dedicadas íntegramente a las zonas del Art. 4.3. En realidad, después de completarse la zona ZAV (última de las 12 zonas) en la página 18, **comienza el Artículo 4.4 "Áreas de Protección de Recursos de Valor Patrimonial Cultural"** (categorías M — Monumento Histórico, con 1 inmueble listado: "Aduana Los Queñes"; e ICH — Inmuebles de Conservación Histórica, con 3 inmuebles listados: Edificio Municipal, Edificio Biblioteca, Iglesia Católica de Romeral), que ocupa el resto de la página 18. Esto **no es parte de las 12 zonas solicitadas** y no se transcribió en detalle (está fuera del alcance de esta tarea), pero se documenta su existencia porque contradice la impresión de que el Art. 4.3 (zonas) ocupa toda la página 18. No se pudo verificar directamente si el Título 5 efectivamente comienza en la página 19, ya que esa página está fuera del rango de material entregado (14-18); solo se puede confirmar que, dentro del rango entregado, después del Art. 4.4 no hay más contenido de zonas.

5. **Estructura no uniforme entre zonas, tal como anticipaba la instrucción de la tarea:** ZAV carece de tabla de Usos de Suelo (solo párrafo descriptivo); ZE-2 y ZE-3 carecen de fila RESIDENCIAL y de fila Densidad Bruta Máxima; ZU-7 carece de las filas SALUD/SEGURIDAD/SERVICIOS/SOCIAL que sí tienen ZU-4 y ZU-5. Ninguna de estas variaciones estaba señalada por Fase 3, pero tampoco la contradice — son detalle adicional descubierto en la verificación exhaustiva.

## Notas finales de verificación

**Confianza global: alta.** Las cinco páginas se leyeron en imagen completa y luego se re-verificaron con recortes ampliados (zoom 1.5x–2.5x) para cada tabla de "Usos de Suelo" y de "Normas de Subdivisión y Edificación" de las 12 zonas, más los bordes de cada salto de página, para descartar pérdida de filas en los cortes. El escaneo a 250dpi es nítido; no se encontró texto ilegible ni ambiguo en ningún cuadro normativo.

**Confianza por sección de páginas:**
- Página 14 (Art. 4.2 listado + Art. 4.3 intro + ZU-1 completa + ZU-2 usos de suelo): alta.
- Página 15 (ZU-2 normas cont. + ZU-3 completa + ZU-4 completa): alta.
- Página 16 (ZU-5 completa + ZU-6 completa + ZU-7 usos de suelo): alta.
- Página 17 (ZU-7 normas cont. + ZE-1 completa + ZE-2 completa + ZE-3 completa): alta.
- Página 18 (ZE-4 completa + ZAV completa + inicio Art. 4.4, fuera de alcance): alta.

**Sobre "Dato no determinable":** esta convención no se usó en ningún campo de este documento. Todos los vacíos encontrados correspondían a uno de dos casos claramente identificables en la fuente: (a) celdas vacías por diseño dentro de una tabla existente (ZU-1/SEGURIDAD y ZE-4/COMERCIO, ambas en la columna EXCEPTO — verificadas dos veces con zoom 2.5x para descartar que fuera un guion muy tenue: están genuinamente en blanco), o (b) filas/tablas completas ausentes por no aplicar el concepto a la zona (Densidad Bruta Máxima ausente en ZE-2, ZE-3 y ZAV por no tener uso residencial; tabla de Usos de Suelo ausente en ZAV). No hubo texto cortado, borroso o fuera de la página que impidiera la lectura de algún valor esperado.

**Inconsistencias tipográficas menores de la fuente (no normativas, transcritas literalmente donde correspondía):** espaciado irregular en "m²" (a veces "500 m²", a veces "500m²"), un caso de "m2" sin superíndice (ZU-6), "há" con tilde vs. "ha" sin tilde entre zonas (ZU-4 es la única con "ha"), y un posible error de puntuación en ZU-4/CULTO Y CULTURA (falta una coma entre "espectáculos" y "Galerías"). Ninguna de estas variaciones afecta el valor numérico o el sentido normativo de los campos.

**Limitación de alcance a señalar:** las tablas de "Usos de Suelo" remiten a categorías "Grupo 1", "Grupo 2", "Grupo 3", "Grupo 4" para cada clase de equipamiento (Comercio, Salud, Deporte, etc.). La definición de qué actividades específicas componen cada "Grupo" **no aparece en las páginas 14-18** — probablemente está definida en un artículo anterior de la Ordenanza (fuera del rango entregado para esta tarea). Este documento transcribe fielmente las referencias a "Grupo N" tal como aparecen, pero no puede expandir su contenido.

**No se encontraron notas al pie numeradas** (del tipo "(1)", "(2)", asteriscos, superíndices remitiendo a un texto aclaratorio) en ninguna de las 12 zonas, pese a que la instrucción de la tarea anticipaba posible complejidad de notas al pie. La complejidad real de este corpus está concentrada en las celdas de la columna "EXCEPTO", que en varias zonas contienen listas largas (hasta 6 ítems, ver ZU-4/SERVICIOS) — todas fueron transcritas completas, sin abreviar.

**Contexto cruzado con otros archivos ya existentes en la carpeta `romeral/`:** se detectaron y referenciaron dos actos de enmienda posteriores (Decreto 2.782/2019 y Decreto 2056/2021) que modifican las normas de subdivisión y edificación de ZU-1 para dos polígonos municipales específicos. El cuadro de ZU-1 transcrito en este documento es el texto original de Decreto 44/2017 y no incorpora esas enmiendas (correctamente, ya que esta tarea es sobre el decreto base); se dejó nota cruzada en la sección de ZU-1 para quien integre ambos documentos.
