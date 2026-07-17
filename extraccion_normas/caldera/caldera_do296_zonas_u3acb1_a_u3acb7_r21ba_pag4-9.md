# Modificación PRC Caldera — Sector Playa Ramada (Decreto 296) — Zonas U3ACB-1 a U3ACB-7 y R21B-a

**Fuente:** Decreto 296, "Aprueba Modificación y Publicación al Proyecto Modificación Plan Regulador", Comuna de Caldera (2002), sector Playa Ramada. Publicado/republicado vía Biblioteca del Congreso Nacional de Chile — BCN LeyChile (www.leychile.cl).

**Rango de páginas de este documento:** páginas 4 a 9 de 10 (numeración impresa en el pie de página de la fuente, footer "página X de 10"). No incluye la página 3 (encabezado de capítulo, sin cuadro, fuera de rango) ni la página 10 (tabla de Vialidad, fuera de rango y fuera de alcance de este encargo).

**Material usado:** imágenes PNG a 250 dpi (`caldera_p4-9-04.png` … `caldera_p4-9-09.png`) y texto plano de apoyo (`caldera_p4-9.txt`). Cada una de las 6 páginas fue leída directamente en la imagen y cotejada línea por línea contra el `.txt`; **coinciden exactamente en las 6 páginas, sin ninguna discrepancia detectada** entre imagen y texto (ver §0).

---

## 0. Formato de la fuente

Confirmación del punto solicitado sobre el formato "narrativo por zona en texto plano":

- **No es una tabla tradicional de filas y columnas con bordes.** No hay líneas divisorias, celdas ni grilla. Cada página es texto corrido en fuente monoespaciada.
- Cada zona sigue siempre la misma macro-estructura narrativa:
  1. Título `ZONA <código>` (línea propia).
  2. Un párrafo de descripción en prosa ("Corresponde a...").
  3. Encabezado `USOS DE SUELO` seguido de uno o más párrafos en prosa corrida que enumeran categorías y usos separados por comas y puntos (no en filas ni viñetas en el original).
  4. Encabezado `INTENSIDAD DE OCUPACION` seguido de una **lista letrada** `a.-) `, `b.-) `, `c.-) `... donde cada ítem trae una etiqueta de parámetro y su valor, separados por espacios/tabulaciones para simular alineación en dos columnas — pero sin ser una tabla real (no hay bordes ni celdas; es alineación por espacios en blanco dentro de texto plano).
- Esta lista letrada **sí constituye, en sustancia, un cuadro normativo estructurado** (parámetro → valor, uno por línea, con letra correlativa), aunque tipográficamente esté implementada como texto plano y no como tabla HTML/PDF con bordes. Es la razón por la que en este documento se transcribe como tabla Markdown (columnas "Letra fuente / Parámetro / Valor"): reproduce fielmente la estructura lógica del original sin alterar su contenido.
- **Verificación de origen del texto:** el pie de página de cada imagen dice "...documento generado el 09-Jul-2026" — el PDF de LeyChile se regenera dinámicamente desde una base de datos de texto normalizado, no es un escaneo de papel. Esto es consistente con lo observado: el archivo `.txt` de apoyo coincide **carácter por carácter** con lo visible en las 6 imágenes PNG, incluyendo errores tipográficos, mayúsculas anómalas y espaciados irregulares del original (ver §1 y hallazgos por zona). Esto da un nivel de confianza más alto que un documento escaneado con OCR: no hay ambigüedad de reconocimiento óptico, solo transcripción de una capa de texto nativa ya presente en el PDF.
- Implicancia para la transcripción: como no hay celdas reales, el riesgo de error no es "leer mal un carácter borroso" (no aplica aquí, el texto es nítido y nativo) sino confundir a qué zona pertenece un valor cuando una lista letrada se corta entre dos páginas, o mezclar valores de zonas con códigos parecidos (U3ACB-1 a U3ACB-7). Por eso cada valor de este documento fue cotejado contra la imagen de origen, zona por zona, letra por letra.

---

## 1. Convenciones usadas

- **"Sin valor específico en la fuente":** para celdas vacías en el original, o para campos/parámetros que no aplican por diseño de la zona (se explica el motivo en cada caso — p. ej., zona de restricción donde no se contempla edificación, o parámetro que la propia zona no define porque no corresponde a su naturaleza).
- **"Dato no determinable":** reservado exclusivamente para valores que deberían existir pero no son legibles o no están en el corpus disponible. **No se usó ninguna vez en este documento** — el texto fuente es nítido y completo en las 6 páginas entregadas; no hubo ningún valor ilegible ni faltante por corte de imagen.
- **`[sic]`:** marca erratas tipográficas o gramaticales de la fuente, preservadas tal cual (no corregidas). Se listan también de forma consolidada en cada sección de zona y en "Discrepancias y hallazgos" (§13).
- **Puntuación de valores numéricos:** se preserva exactamente como aparece en la fuente, incluida la presencia/ausencia inconsistente de punto final tras la unidad ("15 m." vs "100 m"), el uso de punto como separador de miles ("2.000 m2", "5.000 m2") y coma decimal invertida a punto decimal tal como la fuente la usa ("1.5", "17.5", "0.8" — la fuente usa punto decimal, no coma, de forma consistente en estos valores). No se normalizó ninguna cifra.
- **Unidad de superficie:** la fuente imprime literalmente `m2` (sin superíndice, por ser texto plano monoespaciado). Se preserva `m2` tal cual en vez de convertir a "m²", por fidelidad al original.
- **Letras de lista anómalas:** en dos zonas la fuente usa una letra mayúscula donde el patrón general usa minúscula (U3ACB-3 ítem "**I**.-)" y U3ACB-5 ítem "**D**.-)"). Se preserva la mayúscula tal como aparece, señalada en la columna "Letra (fuente)" de cada tabla.

---

## 2. Correspondencia de páginas y continuidad de cuadros entre páginas

| Archivo | Página impresa (footer) | Contenido |
|---|---|---|
| `caldera_p4-9-04.png` | página 4 de 10 | Encabezado "PLAYA RAMADA"; **ZONA U3ACB-1** completa; **ZONA U3ACB-2** (descripción + usos + intensidad ítems a-i, corta en "...de acuerdo al artículo 12 de la Ordenanza Local del PRC") |
| `caldera_p4-9-05.png` | página 5 de 10 | U3ACB-2 continuación ("Vigente." + j + k); **ZONA U3ACB-3** completa; **ZONA U3ACB-4** (descripción + usos + intensidad, solo ítem a) |
| `caldera_p4-9-06.png` | página 6 de 10 | U3ACB-4 continuación (ítems b-j); **ZONA U3ACB-5** completa; **ZONA U3ACB-6** (descripción + usos + intensidad, solo ítem a) |
| `caldera_p4-9-07.png` | página 7 de 10 | U3ACB-6 continuación (ítems b-k); **ZONA U3ACB-7** completa; **ZONA ZP-1** (descripción + punto 1, corta en "Sectores de Playa Arenosa.") |
| `caldera_p4-9-08.png` | página 8 de 10 | ZP-1 continuación (resto del punto 1 + punto 2 completo); **ZONA ZP-2** completa; **ZONA R22a** completa; **ZONA A.V** completa; **ZONA R21B-a** (descripción larga, corta en "...deberán consultar una completa y satisfactoria solución de") |
| `caldera_p4-9-09.png` | página 9 de 10 | R21B-a continuación (resto de la descripción + 6 referencias legales + cuadro INTENSIDAD DE OCUPACION completo a-j); **CAPITULO IV Vialidad** (Art. 9, Art. 10) |

### ¿Hay cuadros/listas partidas entre páginas? (verificación punto 5 del encargo)

Sí, varias. Detalle exacto de qué se parte y dónde:

| Zona | ¿Lista "INTENSIDAD DE OCUPACION" partida? | Detalle |
|---|---|---|
| U3ACB-1 | No | Completa en p.4 |
| U3ACB-2 | **Sí** | Ítem i (inicio) en p.4 → "Vigente." + ítems j, k en p.5 |
| U3ACB-3 | No | Completa en p.5 |
| U3ACB-4 | **Sí** | Ítem a en p.5 → ítems b-j en p.6 |
| U3ACB-5 | No | Completa en p.6 |
| U3ACB-6 | **Sí** | Ítem a en p.6 → ítems b-k en p.7 |
| U3ACB-7 | No | Completa en p.7 |
| ZP-1 (descripción, sin cuadro) | **Sí** (prosa, no cuadro) | Descripción + punto 1) en p.7 → resto del punto 1 + punto 2) en p.8 |
| ZP-2, R22a, A.V | No | Cada una completa dentro de p.8 |
| R21B-a | **Sí, solo la descripción/preámbulo** | Descripción larga + prohibiciones + referencias legales: p.8 → p.9. El cuadro INTENSIDAD DE OCUPACION (a-j) en sí **no se parte**: queda íntegro dentro de p.9. |

En ningún caso un valor numérico quedó dividido a mitad de línea entre dos páginas (los cortes de página siempre caen entre ítems completos, nunca a mitad de un valor), lo que reduce el riesgo de error de continuidad.

---

## 3. ZONA U3ACB-1 (página 4)

> **Descripción (texto literal):** "Corresponde a las zonas de baja densidad destinadas preferentemente a vivienda en extensión y equipamiento de esparcimiento y turismo."

> **Usos de suelo (texto literal):** "Vivienda y equipamiento de esparcimiento y turismo a escala regional y comunal. Equipamiento a escala regional: Esparcimiento y Turismo: Cines, Clubes Sociales, Parques de entretenciones, Zonas de picnic, Hoteles, Moteles. Equipamiento a escala comunal: Esparcimiento y Turismo: Restaurantes, Hosterías, Moteles, Hospederías, Hoteles."

No se enuncia un listado separado de "usos prohibidos" para esta zona en el texto fuente (**Sin valor específico en la fuente** — el documento solo define usos permitidos, no incluye una cláusula explícita de usos prohibidos para U3ACB-1).

### Intensidad de ocupación

| Letra (fuente) | Parámetro | Valor |
|---|---|---|
| a.-) | Superficie predial mínima | 300 m2 |
| b.-) | Frente predial mínimo | 15 m. |
| c.-) | Ocupación máxima de suelo | 50% |
| d.-) | Coeficiente máximo de constructibilidad | 1.5 |
| e.-) | Sistema de agrupamiento | Aislado y pareado |
| f.-) | Distanciamiento | Según O.G de U. y C. |
| g.-) | Altura máxima de edificación | 10.5 m. |
| h.-) | Antejardín mínimo | Según O.G de U. y C. |
| i.-) | Estacionamiento | De acuerdo al artículo 12 de la Ordenanza Local del PRC Vigente |
| j.-) | Cierros exteriores y perimetrales | Para ésta zona se contemplará los siguientes tipos: a) Zócalo de mampostería en piedra, altura mínima 50 cm., y un 50% de transparencia en todo su frente. Altura máxima 2 m.; b) Cierro vivo con 50% de transparencia y altura máxima de 2 m. |
| k.-) | Densidad poblacional máxima viviendas | 200 hab/Há. |

**Notas de esta zona:** es la única que usa la forma "Densidad poblacional máxima **viviendas**" (con la palabra "viviendas" incluida en la etiqueta); el resto de las zonas dice solo "Densidad poblacional máxima". También es la única que escribe "Para **ésta** zona" (con tilde, pronombre demostrativo — ortografía válida en 2002, previa a la norma de la RAE de 2010 que retiró la exigencia de tilde diacrítica en "esta/ésta"); las demás zonas usan "esta" sin tilde.

---

## 4. ZONA U3ACB-2 (páginas 4→5)

> **Descripción (texto literal):** "Corresponde a las zonas destinadas a vivienda de media densidad y equipamiento."

> **Usos de suelo (texto literal):** "Vivienda y equipamiento a escala vecinal y equipamiento de esparcimiento y turismo a escala comunal. Educación: Escuelas Básicas, Jardines Infantiles, Parvularios. Culto: Capillas. Cultura: Bibliotecas. Organización Comunitaria: Juntas de Vecinos, Centros Sociales. Areas Verdes: Plazas, Jardines, Juegos Infantiles. Deportes: Canchas. Esparcimiento y Turismo: Cines, Juegos Electrónicos, Bares, Fuentes de Soda. Servicios Profesionales: Oficinas en general. Esparcimiento y Turismo a escala comunal: Restaurantes, Hosterías, Moteles, Hospederías, Hoteles."

**Sin valor específico en la fuente** para "usos prohibidos" — no se enuncia un listado separado en el texto de esta zona.

### Intensidad de ocupación

| Letra (fuente) | Parámetro | Valor |
|---|---|---|
| a.-) | Superficie predial mínima | 400 m2 |
| b.-) | Frente predial mínimo | 20 m. |
| c.-) | Ocupación máxima de suelo | 50% |
| d.-) | Coeficiente máximo de constructibilidad | 1.5 |
| e.-) | Sistema de agrupamiento | Aislado |
| f.-) | Distanciamiento | según O.G de U.y C. |
| g.-) | Altura máxima de edificación | 10.5 m. o por rasante |
| h.-) | Antejardín mínimo | Según O.G de U. y C. |
| i.-) | Estacionamiento | De acuerdo al artículo 12 de la Ordenanza Local del PRC Vigente |
| j.-) | Cierros exteriores y perimetrales | Para esta zona se contemplará los siguientes tipos: a) Zócalo de mampostería en piedra, altura mínima 50 cm., y un 50% de transparencia en todo su frente. Altura máxima; 2 m.; b) Cierro vivo con 50% de transparencia y altura máxima de 2 m. |
| k.-) | Densidad poblacional máxima | 320 hab/Há. |

**`[sic]`:** en el ítem j, "Altura máxima; **2 m.;**" usa punto y coma donde correspondería dos puntos ("Altura máxima**:** 2 m."). Este mismo patrón se repite en varias zonas más (ver nota consolidada en §13).

---

## 5. ZONA U3ACB-3 (página 5)

> **Descripción (texto literal):** "Corresponde a las zonas destinadas equipamiento en un primer piso y a vivienda en densidad alta desde el segundo en adelante." `[sic]` — falta la preposición "a" antes de "equipamiento" ("destinadas **a** equipamiento").

> **Usos de suelo (texto literal):** "Vivienda y equipamiento a escala vecinal. Educación: Escuelas Básicas, Jardines Infantiles, Parvularios. Culto: Capillas. Cultura: Bibliotecas. Organización Comunitaria: Juntas de Vecinos, Centros Sociales. Areas Verdes: Plazas, Jardines, Juegos Infantiles. Deportes: Canchas. Esparcimiento y Turismo: Cines, Juegos Electrónicos, Bares, Fuentes de Soda. Servicios Profesionales: Oficinas en general. Comercio Minorista: Centros comerciales, Mercados, Supermercados, Ferias libres, Locales comerciales, Playas de estacionamiento."

**Sin valor específico en la fuente** para "usos prohibidos" — no se enuncia un listado separado en el texto de esta zona.

### Intensidad de ocupación

| Letra (fuente) | Parámetro | Valor |
|---|---|---|
| a.-) | Superficie predial mínima | 900 m2 |
| b.-) | Frente predial mínimo | 20 m. |
| c.-) | Ocupación máxima de suelo | 60% |
| d.-) | Coeficiente máximo de constructibilidad | 3 |
| e.-) | Sistema de agrupamiento | Aislado |
| f.-) | Distanciamiento | según O.G de U. y C. |
| g.-) | Altura máxima de edificación | 17.5 m o por rasante |
| h.-) | Antejardín mínimo | Según O.G de U. y C. |
| **I**.-) | Estacionamiento | De acuerdo al artículo 12 de la Ordenanza Local del PRC Vigente |
| j.-) | Cierros exteriores y perimetrales | Para esta zona se contemplará los siguientes tipos: a) Zócalo de mampostería en piedra, altura mínima 50 cm., y un 50% de transparencia en todo su frente. Altura máxima; 2 m.; b) Cierro vivo con 50% de transparencia y altura máxima de 2 m. |
| k.-) | Densidad poblacional máxima | 720 hab/Há. |

**Nota:** el ítem de Estacionamiento aparece con "**I**.-)" en mayúscula en la fuente (único caso junto con U3ACB-5/D), verificado visualmente contra la imagen — no es error de transcripción de este documento, es así en el original.

---

## 6. ZONA U3ACB-4 (páginas 5→6)

> **Descripción (texto literal):** "Corresponde a las zonas destinadas a equipamiento a toda escala" (sin punto final en la fuente, verificado en imagen).

> **Usos de suelo (texto literal):** "Equipamiento a escala regional Cultura: Museos, Salas de Concierto Teatros, Auditoriums. Areas Verdes: Santuarios de la Naturaleza. Deportes: Centros Deportivos, Canchas. Esparcimiento y Turismo: Cines, Clubes Sociales, Parques de entretenciones, Zonas de picnic, Hoteles, Moteles. Equipamiento a escala comunal Cultura: Bibliotecas, Salas de Concierto, Teatros, Casas de la Cultura. Areas Verdes: Parques. Esparcimiento y Turismo: Cines, Discotecas, Restaurantes, Hosterías, Hoteles, Hospederías, Residenciales, Moteles. Comercio Minorista: Centros comerciales, Mercados, Supermercados, Ferias libres, Locales comerciales, Playas de estacionamiento. Equipamiento a escala vecinal Cultura: Bibliotecas. Areas Verdes: Plazas, Jardines, Juegos infantiles. Esparcimiento y Turismo: Cines, Juegos electrónicos, Bares, Fuentes de Soda."

**Sin valor específico en la fuente** para "usos prohibidos" — no se enuncia un listado separado en el texto de esta zona.

### Intensidad de ocupación

| Letra (fuente) | Parámetro | Valor |
|---|---|---|
| a.-) | Superficie predial mínima | 2.000 m2 |
| b.-) | Frente predial mínimo | 40 m. |
| c.-) | Ocupación máxima de suelo | 100% |
| d.-) | Coeficiente máximo de constructibilidad | 2 |
| e.-) | Sistema de agrupamiento | Aislado |
| f.-) | Distanciamiento | 10 m a los medianeros |
| g.-) | Altura máxima de edificación | 14 m. |
| h.-) | Antejardín mínimo | No contempla |
| i.-) | Estacionamiento | De acuerdo al artículo 12 de la Ordenanza Local del PRC Vigente |
| j.-) | Cierros exteriores y perimetrales | Para esta zona se contemplará los siguientes tipos: a) Zócalo de mampostería en piedra, altura mínima 50 cm., y un 50% de transparencia en todo su frente. Altura máxima; 2 m.; b) Cierro vivo con 50% de transparencia y altura máxima de 2 m. |
| — | Densidad poblacional máxima | **Sin valor específico en la fuente** — la lista termina en el ítem j; no hay ítem k. Consistente con que es una zona de equipamiento puro (no residencial), donde no correspondería fijar densidad poblacional. |

**Nota:** es la única zona (junto con R21B-a, que no tiene esta cifra en absoluto) cuyo "Distanciamiento" trae un valor métrico propio y explícito ("10 m a los medianeros") en vez de remitir a la OGUC.

---

## 7. ZONA U3ACB-5 (página 6)

> **Descripción (texto literal):** "Corresponde a la zona adyacente a la ruta 5, que contemplan equipamiento y servicio a la ruta." `[sic]` — concordancia: sujeto singular "la zona" con verbo plural "contemplan" (correspondería "que contempla").

> **Usos de suelo (texto literal):** "Equipamiento a escala comunal tipo comercio: Comercio: Centros Comerciales, Mercados, Supermercados, Ferias, Libres, Locales Comerciales, Servicentros, Playas de Estacionamiento." `[sic]` — "Ferias, Libres" con coma espuria y "Libres" en mayúscula; en las demás zonas el término compuesto aparece correctamente como "Ferias libres" (p. ej., U3ACB-3, U3ACB-4).

**Sin valor específico en la fuente** para "usos prohibidos" — no se enuncia un listado separado en el texto de esta zona.

### Intensidad de ocupación

| Letra (fuente) | Parámetro | Valor |
|---|---|---|
| a.-) | Superficie predial mínima | 1.800 m2 |
| b.-) | Frente predial mínimo | 50 m. |
| c.-) | Ocupación máxima de suelo | 100% |
| **D**.-) | Coeficiente máximo de constructibilidad | 3 |
| e.-) | Sistema de agrupamiento | Continuo en el primer piso y aislado del segundo en adelante |
| f.-) | Distanciamiento | según O.G de U.y C., cuando corresponda |
| g.-) | Altura máxima de edificación | 10.5 o según rasantes (se aplica la más exigente) |
| h.-) | Antejardín mínimo | No contempla |
| i.-) | Estacionamiento | De acuerdo al artículo 12 de la Ordenanza Local del PRC Vigente |
| j.-) | Cierros exteriores | Zócalo de mampostería en piedra, altura mínima 50 cm. y un 50% de transparencia en todo su frente. Altura máxima: 2 m. |
| — | Densidad poblacional máxima | **Sin valor específico en la fuente** — la lista termina en j, sin ítem k. |

**Hallazgo específico de esta zona (verificado con cuidado contra la imagen):** el ítem j aquí se titula solo **"Cierros exteriores"** (sin "y perimetrales") y describe **un único tipo de cierro** (zócalo de mampostería, 50 cm, 50% transparencia, altura máx. 2 m.), **sin la opción alternativa "b) Cierro vivo..."** que sí aparece en todas las demás zonas U3ACB. No es un error de esta transcripción: se verificó directamente en la imagen `caldera_p4-9-06.png` que el párrafo termina en "Altura máxima: 2 m." sin continuar con una opción "b)". Es también la única zona del rango cuyo ítem de cierros usa correctamente dos puntos ("Altura máxima**:** 2 m.") en vez del punto y coma que aparece en el resto (ver §13).

---

## 8. ZONA U3ACB-6 (páginas 6→7)

> **Descripción (texto literal):** "Corresponde a las zonas destinadas a equipamiento a escala regional, comunal y vecinal."

> **Usos de suelo (texto literal):** "Esparcimiento y Turismo: Clubes Sociales, Parque de Entretenciones, Zonas de Camping, Moteles, Casinos. Comercio: Centros Comerciales, Supermercados. Equipamiento a escala comunal: Culto: Templos, Parroquias. Areas Verdes: Parques, Plazas. Deportes: Estadios, Canchas, Piscinas, Gimnasios, Centros Deportivos. Esparcimiento y Turismo, Teatros, Cines, Discotecas, Restaurantes, Hosterías, Moteles, Hospederías, Residenciales, Zonas de Picnic." `[sic]` — "Esparcimiento y Turismo**,**" usa coma donde el resto del documento usa dos puntos tras esta categoría (p. ej., "Esparcimiento y Turismo**:**" en todas las demás zonas).

**Sin valor específico en la fuente** para "usos prohibidos" — no se enuncia un listado separado en el texto de esta zona.

### Intensidad de ocupación

| Letra (fuente) | Parámetro | Valor |
|---|---|---|
| a.-) | Superficie predial mínima | 5.000 m2 |
| b.-) | Frente predial mínimo | 100 m |
| c.-) | Ocupación máxima de suelo | 80% |
| d.-) | Coeficiente máximo de constructibilidad | 1 |
| e.-) | Sistema de agrupamiento | Aislado |
| f.-) | Distanciamiento | 5 mt. en torno a su deslinde |
| g.-) | Altura máxima de edificación | 7 m. |
| h.-) | Antejardín mínimo | Según O.G de U. y C. |
| i.-) | Estacionamiento | De acuerdo al artículo 12 de la Ordenanza Local del PRC Vigente |
| j.-) | Cierros exteriores y perimetrales | Para esta zona se contemplará los siguientes tipos: a) Zócalo de mampostería en piedra, altura mínima 50 cm., y un 50% de transparencia en todo su frente. Altura máxima; 2 m.; b) Cierro vivo con 50% de transparencia y altura máxima de 2 m. |
| k.-) | Norma Especial | Los proyectos emplazados en esta franja, tendrán directa relación con la actividad turística, por lo tanto deberán mantener una concordancia en el diseño y materialidad con el entorno natural de la playa; tendiendo a la transparencia de los proyectos, tanto en los cierros como en los paramentos y muros, con el fin de no entorpecer la vista al mar. |

**Nota:** "Frente predial mínimo" (100 m) y en U3ACB-7 (50 m) son las dos únicas zonas del rango donde esta unidad se imprime **sin punto final** ("100 m", no "100 m."); en U3ACB-1 a U3ACB-5 siempre lleva punto ("15 m.", "20 m.", etc.). Preservado tal cual, sin normalizar.

---

## 9. ZONA U3ACB-7 (página 7)

> **Descripción (texto literal):** "Corresponde a las zonas destinadas a servicio hotelero a escala regional, comunal y vecinal."

> **Usos de suelo (texto literal):** "Esparcimiento y Turismo: Clubes Sociales, Parque de Entretenciones, Hoteles, Casinos. Areas Verdes: Parques, Plazas. Deportes: Estadios, Canchas, Piscinas, Gimnasios, Centros Deportivos. Esparcimiento y Turismo: Teatros, Cines, Discotecas, Restaurantes, Hosterias, Moteles, Hospederías." `[sic]` — "Hosteria**s**" sin tilde; en el resto del documento se escribe siempre "Hosterías" con tilde (p. ej., U3ACB-1, U3ACB-2, U3ACB-4, U3ACB-6).

**Sin valor específico en la fuente** para "usos prohibidos" — no se enuncia un listado separado en el texto de esta zona.

### Intensidad de ocupación

| Letra (fuente) | Parámetro | Valor |
|---|---|---|
| a.-) | Superficie predial mínima | 5.000 m2 |
| b.-) | Frente predial mínimo | 50 m |
| c.-) | Ocupación máxima de suelo | 80% |
| d.-) | Coeficiente máximo de constructibilidad | 1.3 |
| e.-) | Sistema de agrupamiento | Aislado |
| f.-) | Distanciamiento | 5 mts. |
| g.-) | Altura máxima de edificación | 10.5 m. |
| h.-) | Antejardín mínimo | Según O.G de U.y C. |
| i.-) | Estacionamiento | De acuerdo al artículo 12 de la Ordenanza Local del PRC Vigente |
| j.-) | Cierros exteriores y perimetrales | Para esta zona se contemplará los siguientes tipos: a) Zócalo de mampostería en piedra, altura mínima 50 cm., y un 50% de transparencia en todo su frente. Altura máxima; 2 m.; b) Cierro vivo con 50% de transparencia y altura máxima de 2 m. |
| k.-) | Norma Especial | Los proyectos emplazados en esta franja, tendrán directa relación con la actividad turística, por lo tanto deberán mantener una concordancia en el diseño y materialidad con el entorno natural de la playa; Así mismo la altura máxima de edificación estará condicionada por la altura del peñón, no pudiendo ser sobrepasada por ningún elemento del proyecto. |

**`[sic]`:** ítem h, "Antejardín mínimo**:,** Según O.G de U.y C." — coma espuria inmediatamente después de los dos puntos.

**Hallazgo importante — no confundir con U3ACB-6:** el ítem k ("Norma Especial") de U3ACB-7 **no es idéntico** al de U3ACB-6 pese a empezar igual. U3ACB-6 termina con la cláusula de "transparencia... para no entorpecer la vista al mar"; **U3ACB-7 en cambio termina con una restricción distinta y exclusiva de esta zona: la altura máxima de edificación queda condicionada por la altura del peñón (accidente rocoso) contiguo, sin que ningún elemento del proyecto pueda sobrepasarla.** Verificado en imagen para no arrastrar por error el texto de una zona a la otra, dado que ambos párrafos comparten la primera oración casi palabra por palabra.

También comparte con U3ACB-6 y U3ACB-5 el valor de Superficie predial mínima "5.000 m2" con U3ACB-6 — confirmado en imagen que ambas zonas efectivamente repiten ese mismo valor; no es error de esta transcripción.

---

## 10. ZONA R21B-a (páginas 8→9)

> **Descripción y régimen de usos (texto literal completo):** "Corresponde a playas de mar, márgenes rocosos naturales o artificiales, terrenos de playa y terrenos fiscales destinados al apoyo en tierra a actividades de pesca artesanal y acuicultura. Esta zona está especificada en el plano P-MOD-CAL-RAMADA. como R21B-a y corresponde a 2.1 há., está emplazada después de los 80 m. de la alta marea y posee un paso de servidumbre que le es común a todos los concesionarios, este paso de servidumbre esta destinado a actividades marítimas y en ningún caso podrá ser cercado o delimitado, resguardando el libre paso de peatones por la costa (zona ZP-2). Usos de suelo permitidos: arrastraderos, embarcaderos, rampas, huinches e instalaciones mínimas relacionadas a la pesca artesanal y cultivos de mar, especificadas en dictámenes de Contraloría Nº 014144 (mayo 1995) Nº 015452 (mayo 1997). No estarán permitidos los almacenamientos de grandes volúmenes de sustancias que pudieren contaminar el aire, las aguas o la tierra, tales como químicos, pinturas, combustibles, lubricantes o similares. La emisión de ruidos molestos, ocasionados o permanente, deberá quedar protegida de modo tal que no sea auditivamente percibida por el vecindario, para tal efecto se tendrá en cuenta lo indicado por el Ministerio de Salud y Código Sanitario. Quedará absolutamente prohibida toda actividad contaminante del medio ambiente, tanto en tierra como en retorno de aguas al mar. Los procesos de manejo de especies de cultivos marinos deberán consultar una completa y satisfactoria solución de ingeniería acuícola, que permita evitar la emisión de partículas contaminantes al aire, al suelo y al agua de mar. Las soluciones de aguas servidas deberán tener proyectos específicos aprobados por el servicio sanitario respectivo. Además toda actividad de Acuicultura deberá dar cumplimiento de las disposiciones legales vigentes sobre las condiciones que cautelen el deterioro ambiental, producto de la generación de residuos líquidos en el territorio del Plan, entre otras las siguientes:"

**`[sic]` en este párrafo:**
- "...plano P-MOD-CAL-RAMADA. como R21B-a..." — punto que corta indebidamente la oración antes de "como".
- "...este paso de servidumbre **esta** destinado..." — falta tilde en "está".
- "...ocasionados o **permanente**..." — falta concordancia de número (correspondería "permanentes").

**Superficie de la zona (dato descriptivo, no es parámetro de edificación):** 2.1 há., emplazada después de los 80 m. de la línea de alta marea.

**Usos prohibidos / restricciones explícitas (a diferencia de las zonas U3ACB, aquí sí hay una cláusula expresa):**
- Almacenamiento de grandes volúmenes de sustancias que pudieren contaminar aire, aguas o tierra (químicos, pinturas, combustibles, lubricantes o similares).
- Emisión de ruidos molestos perceptibles por el vecindario.
- Toda actividad contaminante del medio ambiente, en tierra o por retorno de aguas al mar.
- Cercado o delimitación del paso de servidumbre (debe mantenerse libre para el paso peatonal, zona ZP-2).

**Referencias legales citadas (texto literal, 6 ítems):**
1. El artículo 136º del D.S. Nº 430/91 Ministerio de Economía, Fomento y Reconstrucción, Ley General de Pesca y Acuicultura.
2. El D.S. Nº 1 (Defensa) de 1992, Reglamento para el Control de Contaminación Acuática.
3. Ley Nº 3.133/16 sobre vaciamiento de residuos industriales.
4. D.S. 351 (MOP) de 1992, Reglamento para la Neutralización y depuración de Residuos Líquidos Industriales.
5. Ley 19.300 de Bases Generales del Medio Ambiente y su Reglamento sobre el sistema de evaluación de impacto ambiental, aprobado por D.S. Nº 30 del Ministerio General Secretaría de la Presidencia de 1997.
6. El D.S. Nº 609 (MOP) de 1998, Norma de emisión de contaminantes asociados a descargas de residuos industriales líquidos a sistemas de alcantarillados.

*(Verificación externa de consistencia: los 6 números y años de estas normas corresponden a instrumentos legales chilenos reales y correctamente numerados — p. ej., Ley 19.300 es efectivamente la Ley de Bases Generales del Medio Ambiente y D.S. 609/1998 MOP es la norma real de emisión para residuos industriales líquidos a alcantarillado — lo que da confianza adicional de que no hay dígitos alterados por auto-corrección en esta lista.)*

### Intensidad de ocupación

| Letra (fuente) | Parámetro | Valor |
|---|---|---|
| — | Superficie predial mínima | **Sin valor específico en la fuente** — la lista de esta zona no incluye este parámetro; empieza directamente en "Ocupación máxima de suelo". Consistente con que la zona no es de subdivisión predial estándar, sino de playas fiscales y concesiones existentes. |
| — | Frente predial mínimo | **Sin valor específico en la fuente** — mismo motivo que el anterior. |
| a.-) | Ocupación máxima de suelo | 80% |
| b.-) | Coeficiente máximo de constructibilidad | 0.8 |
| c.-) | Sistema de agrupamiento | Aislado |
| d.-) | Distanciamiento | 5 m a medianeros, aún en muros sin vanos |
| e.-) | Altura máxima de edificación | 7m |
| f.-) | Antejardín mínimo | 5 m sin edificaciones ni instalaciones de ningún tipo |
| g.-) | Estacionamiento | De acuerdo al artículo 12 de la Ordenanza Local del PRC Vigente |
| h.-) | Cierros exteriores y perimetrales | Para esta zona se contemplarán los siguientes tipos: a) Zócalo de mampostería en piedra, altura mínima 50 cm., y un 50% de transparencia en todo su frente. Altura máxima; 2 m.; b) Cierro vivo con 50% de transparencia y altura máxima de 2 m. |
| i.-) | Materialidad de instalaciones | Zócalo de mampostería en piedra de 1m, como antepecho. Transparencia en los segundos pisos. Estos proyectos deberán ser aprobados por la Dirección de Obras de la I. Municipalidad de Caldera, entidad que deberán velar por que estos proyectos mantengan una concordancia en el diseño y la materialidad con el entorno natural. |
| j.-) | Normas Especiales | Los proyectos emplazados en esta franja, tendrán directa relación con la actividad turística, por lo tanto deberán mantener una concordancia en el diseño y materialidad con el entorno natural de la playa; tendiendo a la transparencia de los proyectos, tanto en los cierros como en los paramentos y muros, con el fin de no entorpecer la vista al mar. |

**Nota:** el ítem "i) Materialidad de instalaciones" es **exclusivo de esta zona** — ninguna de las 7 zonas U3ACB lo incluye. Es coherente con que R21B-a regula instalaciones de apoyo a pesca artesanal/acuicultura, un tipo de construcción distinto a vivienda/equipamiento.

---

## 11. Tabla comparativa resumen (lectura rápida — el detalle completo y autoritativo está en §3-10)

| Parámetro | U3ACB-1 | U3ACB-2 | U3ACB-3 | U3ACB-4 | U3ACB-5 | U3ACB-6 | U3ACB-7 | R21B-a |
|---|---|---|---|---|---|---|---|---|
| Superficie predial mínima | 300 m2 | 400 m2 | 900 m2 | 2.000 m2 | 1.800 m2 | 5.000 m2 | 5.000 m2 | Sin valor específico¹ |
| Frente predial mínimo | 15 m. | 20 m. | 20 m. | 40 m. | 50 m. | 100 m | 50 m | Sin valor específico¹ |
| Ocupación máxima de suelo | 50% | 50% | 60% | 100% | 100% | 80% | 80% | 80% |
| Coef. máx. constructibilidad | 1.5 | 1.5 | 3 | 2 | 3 | 1 | 1.3 | 0.8 |
| Sistema de agrupamiento | Aislado y pareado | Aislado | Aislado | Aislado | Continuo (1er piso) / Aislado (desde 2°) | Aislado | Aislado | Aislado |
| Altura máxima | 10.5 m. | 10.5 m. o por rasante | 17.5 m o por rasante | 14 m. | 10.5 o según rasantes (más exigente) | 7 m. | 10.5 m. (condicionada por altura del peñón) | 7m |
| Antejardín mínimo | Según OGUC² | Según OGUC² | Según OGUC² | No contempla | No contempla | Según OGUC² | Según OGUC² | 5 m sin edificaciones |
| Densidad poblacional máxima | 200 hab/Há. | 320 hab/Há. | 720 hab/Há. | Sin valor específico³ | Sin valor específico³ | Sin valor específico³ | Sin valor específico³ | Sin valor específico³ |

¹ Zona de playas fiscales/concesiones, no de subdivisión predial estándar — ver §10.
² "Según O.G de U. y C." / "Según O.G de U.y C." (la fuente varía la puntuación exacta entre zonas; ver tablas de detalle §3-10 para la cita literal de cada una).
³ Zonas de equipamiento, servicio a ruta, o pesca artesanal — no residenciales; la fuente no fija densidad poblacional para ellas.

---

## 12. Zonas de restricción sin cuadro numérico: ZP-1, ZP-2, R22a, A.V.

Verificación explícita solicitada: ¿estas 4 zonas realmente carecen de tabla numérica, o tienen algún parámetro cuantitativo que la nota de Fase 3 pasó por alto? Se revisó cada una individualmente contra la imagen. Resultado: **ninguna de las 4 tiene un cuadro "INTENSIDAD DE OCUPACION" con lista letrada** (se confirma la observación de Fase 3 en ese sentido exacto), **pero una de ellas (ZP-1) sí contiene valores cuantitativos concretos incrustados en el texto narrativo**, que no deben tratarse como "sin dato" — ver detalle zona por zona.

### ZONA ZP-1 (páginas 7→8)

> **Texto literal:** "Corresponde a la franja de terreno del borde litoral, destinada a proteger El RECURSO COSTERO, sobre todo aquellas PLAYAS ARENOSAS, característica natural propia y exclusiva de la región. También contempla sectores de borde rocoso.
> 1) Sectores de Playa Arenosa. Se deberá destinar una franja de 80 metros de ancho, medidos de la línea de más alta marea, para uso de actividades deportivas, recreativas y similares.
> 2) Sectores Rocosos. Las actividades productivas, económicas o turísticas que requieran de un contacto directo con el mar, podrán emplazarse en los cabezales de playas de arena o márgenes rocosos, respetando la franja de protección de 37 m de circulación."

`[sic]`: "proteger **El** RECURSO COSTERO" — mayúscula inicial anómala en "El" a mitad de frase.

**Hallazgo — parámetro cuantitativo que la nota de Fase 3 no menciona explícitamente:** esta zona **no tiene cuadro de intensidad de ocupación** (correcto, no hay COS/CC/altura/agrupamiento — es coherente con ser una franja de protección donde no se contempla edificación), **pero sí define dos anchos de franja cuantitativos y específicos en su propio cuerpo narrativo**:
- **80 metros** de ancho, medidos desde la línea de más alta marea, para sectores de playa arenosa (uso deportivo/recreativo).
- **37 metros** de franja de protección de circulación, para sectores rocosos.

Estos no son parámetros de edificación (no hay COS/CC/altura porque no se permite construir), pero sí son datos normativos cuantitativos de la zona (anchos de franja de restricción) y se documentan aquí explícitamente para no perderlos bajo una etiqueta genérica de "sin datos". Se usa **"Sin valor específico en la fuente"** únicamente para los campos de un cuadro de edificación que esta zona no tiene por diseño (COS, CC, altura, agrupamiento, antejardín, densidad) — no para los anchos de franja, que sí están explícitamente en la fuente.

### ZONA ZP-2 (página 8)

> **Texto literal:** "Corresponde a la franja de terreno del borde litoral, destinada a proteger LA CIRCULACION PEATONAL en todo la extensión del litoral, teniendo acceso a todas las playas como espacios de uso publico. En ella queda incorporada una franja de circulación peatonal, ciclística, vehicular de servicios y de área verde, como forma de proteger y resguardar al uso publico, el recurso costero.
> USOS DE SUELO PERMITIDOS: Equipamiento recreacional y deportivo abiertos sin edificaciones, cabinas para bañistas, kioskos de temporada y áreas verdes.
> \* Los proyectos turísticos que contemplen alojamiento masivo de personas y sus respectivos equipamientos, en los sectores de playas arenosas, deberán ubicarse detrás de la franja de protección."

`[sic]`: "en **todo** la extensión" (correspondería "toda", concordancia de género); "uso **publico**" (dos veces en el párrafo, sin tilde; correspondería "público").

**Verificación:** a diferencia de ZP-1, en ZP-2 **no se encontró ningún valor cuantitativo** en el texto (ni ancho de franja propio, ni porcentaje, ni metros). El propio ancho de la franja ZP-2 no está definido textualmente en este rango — puede estar definido gráficamente en el plano P-MOD-CAL-RAMADA (fuera del alcance de este documento, que cubre solo texto de páginas 4-9). Se usa **"Sin valor específico en la fuente"** para cualquier parámetro cuantitativo de esta zona: el texto es perfectamente legible, simplemente no contiene esas cifras (no es un problema de legibilidad, por lo que no corresponde "Dato no determinable").

### ZONA R22a (página 8)

> **Texto literal:** "Corresponde a áreas que por su valor ecológico es necesario conservar en su estado natural, para mantener el equilibrio y calidad del medio ambiente. Constituye una zona de protección de Campos Dunarios y al islote de la península de Ramada, no se permitirá edificación de ningún tipo con el fin de destinarlas a actividades recreativas y científicas. Restricciones para la preservación del medio natural. Usos de suelo permitidos: Áreas Verdes, miradores, senderos peatonales."

**Verificación:** ningún valor numérico en todo el párrafo. Coherente con el propio texto, que declara expresamente "**no se permitirá edificación de ningún tipo**" — por diseño no correspondería un cuadro COS/CC/altura, ya que la construcción está derechamente prohibida. **"Sin valor específico en la fuente"** para todos los parámetros de edificación, con esta explicación (prohibición expresa de construir, no ausencia de dato).

### ZONA A.V (página 8)

> **Texto literal:** "Corresponde a las zonas de Áreas Verdes identificadas en el Plano P-MOD-CAL-RAMADA como A.V y su materialización como tal será ejecutada por los propietarios que enfrentan a dicha zona de acuerdo al % de cesión, de cualquier manera será responsabilidad de la D.O.M de la I. Municipalidad de Caldera designar o señalar al propietario cual área deberá ejecutar, para resguardar el diseño de la totalidad del loteo."

**Verificación fina realizada:** el párrafo menciona literalmente el símbolo "**%**" (en "de acuerdo al % de cesión"), lo que en una primera lectura podría parecer un parámetro cuantitativo pasado por alto. **Al revisar con cuidado, no lo es**: el texto no fija un porcentaje numérico concreto para esta zona — remite de forma genérica "al % de cesión" como mecanismo legal ya existente (cesión gratuita de terrenos, definida en la normativa general de urbanismo, no en este párrafo), sin indicar aquí ninguna cifra propia. Por lo tanto se mantiene como **"Sin valor específico en la fuente"** para cualquier parámetro cuantitativo de esta zona — el símbolo "%" está presente en el texto, pero no acompaña ningún número; no corresponde registrarlo como un dato cuantitativo de la zona.

### Resumen de la verificación de las 4 zonas de restricción

| Zona | ¿Cuadro INTENSIDAD DE OCUPACION? | ¿Algún valor cuantitativo en el texto? | Tratamiento |
|---|---|---|---|
| ZP-1 | No | **Sí — 80 m (franja playa arenosa) y 37 m (franja protección/circulación borde rocoso)** | Valores documentados explícitamente en §12; "Sin valor específico en la fuente" solo para campos de edificación (que no existen por diseño) |
| ZP-2 | No | No (ningún metraje ni porcentaje en el texto) | "Sin valor específico en la fuente" para todo parámetro cuantitativo |
| R22a | No | No | "Sin valor específico en la fuente" — edificación expresamente prohibida |
| A.V | No | No (el "%" mencionado no trae cifra propia) | "Sin valor específico en la fuente" |

---

## 13. Verificación de cierre de la última tabla (p.9) y apertura del Capítulo IV Vialidad

Verificado con lectura directa (no solo cotejo de texto) de `caldera_p4-9-09.png`:

- El cuadro "INTENSIDAD DE OCUPACION" de la **ZONA R21B-a** cierra en el ítem **"j.-) Normas Especiales"**, cuyo párrafo termina en "...con el fin de no entorpecer la vista al mar." — oración completa, sin corte ni continuación visible.
- Inmediatamente después, sin más zonas intermedias, aparece:
  - **"CAPITULO IV"** (título, línea propia, sangría de artículo)
  - **"Vialidad"** (subtítulo)
  - **"Artículo 9:"** — sobre la Avenida Punta Ramadas proyectada (texto completo, oración cerrada).
  - **"Artículo 10:"** — sobre perfiles geométricos viales (texto completo, oración cerrada: "...serán definidos en los respectivos proyectos de loteos y en estudios según corresponda.").
- Después del Artículo 10 hay espacio en blanco y luego el pie de página estándar "...página 9 de 10" — **no hay ningún contenido adicional cortado a mitad de oración al final de la página 9** dentro del rango entregado.
- **Conclusión:** se confirma exactamente lo indicado por Fase 3 — la página 9 cierra la última tabla normativa por zona (R21B-a) y abre el Capítulo IV de Vialidad, y el Artículo 10 aparece gramaticalmente completo. No puedo confirmar si existe un Artículo 11 en la página 10 (fuera de mi rango y fuera del alcance de este encargo) — solo puedo verificar que, dentro de páginas 4-9, no queda ninguna oración inconclusa al cierre de la página 9.

---

## 14. Discrepancias y hallazgos respecto de la nota de Fase 3

1. **Formato "narrativo por zona en texto plano":** confirmado sin reservas — ver §0. No es tabla con bordes; es lista letrada dentro de texto corrido, que aquí se convierte a tabla Markdown preservando el contenido literal.
2. **8 zonas con cuadro completo (7 U3ACB + R21B-a):** confirmado. Las 8 tienen cuadro "INTENSIDAD DE OCUPACION" con lista letrada de parámetros. Ninguna zona adicional oculta dentro del rango 4-9 tiene este tipo de cuadro.
3. **"p3 termina en el encabezado sin tabla":** consistente con lo observado — dentro de mi rango (que empieza en p.4) no hay rastro de un "CAPITULO III" ni de un artículo introductorio de la lista de zonas; el primer contenido de p.4 es directamente el subtítulo "PLAYA RAMADA" seguido de "ZONA U3ACB-1". No puedo verificar directamente el contenido de p.3 (fuera de mi material), pero no hay contradicción con la nota de Fase 3.
4. **"p9 cierra la última tabla y abre Cap. IV Vialidad":** confirmado con verificación de zoom/lectura directa — ver §13.
5. **"p7-8: ZP-1, ZP-2, R22a, A.V. son de restricción sin cuadro numérico (no confundir con sin-tablas)":** confirmado en cuanto a que ninguna tiene un cuadro "INTENSIDAD DE OCUPACION" con lista letrada. **Hallazgo adicional que matiza la nota de Fase 3:** la zona **ZP-1 sí contiene dos valores cuantitativos explícitos en su texto narrativo (franjas de 80 m y 37 m)** que no deben tratarse como ausencia total de datos — ver §12. Este matiz no contradice a Fase 3 (que no afirmó que hubiera cero números, solo que no había "cuadro numérico" en el sentido de tabla de intensidad de ocupación — afirmación que sigue siendo correcta), pero se documenta para que una fase posterior no descarte por error los anchos de franja de ZP-1 al ver la zona etiquetada como "sin cuadro".
6. **"p10 = tabla de VIALIDAD, fuera del rango":** consistente con lo observado en el cierre de p.9 (Capítulo IV recién comienza con Art. 9 y 10 en prosa, no en tabla, dentro de mi rango); no tengo acceso a p.10 para confirmar el formato de esa tabla, pero no hay nada en p.9 que lo contradiga.
7. **Hallazgo no cubierto explícitamente por Fase 3 — tablas/listas partidas entre páginas:** Fase 3 no detalla cuáles zonas específicas tienen su lista "INTENSIDAD DE OCUPACION" partida entre dos páginas. Este documento identifica exactamente 3 casos (U3ACB-2, U3ACB-4, U3ACB-6 — ver §2) más la partición de la descripción narrativa de ZP-1 y de R21B-a (sin que el cuadro numérico de R21B-a en sí se parta).
8. **Hallazgo no cubierto por Fase 3 — variaciones tipográficas menores repetidas:** el patrón "Altura máxima**;** 2 m.;" (punto y coma en vez de dos puntos) se repite idéntico en los ítems de cierros de U3ACB-2, U3ACB-3, U3ACB-4, U3ACB-6, U3ACB-7 y R21B-a — es decir, en 6 de las 8 zonas con cuadro completo. Solo U3ACB-1 (con puntuación distinta, sin signo) y U3ACB-5 (con dos puntos correctos, y sin la opción "b" de cierro vivo) se apartan de este patrón. No es un hallazgo que cambie ninguna norma sustantiva, pero se documenta como verificación de que cada instancia fue efectivamente cotejada de forma individual contra la imagen y no copiada en bloque de una zona a otra.
9. **Hallazgo no cubierto por Fase 3 — U3ACB-7 tiene una cláusula de altura única (condicionada por el peñón):** ver §9. Es fácil confundir el ítem "k) Norma Especial" de U3ACB-6 y U3ACB-7 porque ambos empiezan con la misma oración; se verificó que difieren en la segunda mitad y se transcribió cada uno por separado.
10. **No se detectaron errores de auto-corrección de códigos de zona.** Se verificaron individualmente contra la imagen los 7 códigos U3ACB-1 a U3ACB-7 (aparecen en orden numérico estrictamente ascendente y sin repeticiones a través de las páginas 4-7, lo que además sirve de auto-validación cruzada) y los códigos R22a / R21B-a / ZP-1 / ZP-2 / A.V, confirmando que no se confundieron entre sí en ningún punto de este documento.
11. **No se usó "Dato no determinable" en ningún campo de este documento** — a diferencia de otros documentos de este proyecto (p. ej., San Antonio, con fuente escaneada e ilegibilidades reales), en este rango de Caldera el texto fuente es nativo, nítido y completo; todos los "sin dato" encontrados corresponden a campos que la propia zona no define por diseño, no a ilegibilidad.

---

## 15. Notas finales de verificación

**Método:** lectura directa de las 6 imágenes PNG a 250 dpi (`caldera_p4-9-04.png` a `-09.png`), cotejadas línea por línea contra el archivo de texto de apoyo (`caldera_p4-9.txt`). Se prestó atención especial, tal como pide el encargo, a (a) los 7 códigos de zona U3ACB-1 a U3ACB-7 —que difieren solo en el último dígito— verificando cada uno contra su imagen de origen y confirmando además su correlativo ascendente sin saltos ni repeticiones; y (b) a las cifras de cada ítem de "INTENSIDAD DE OCUPACION", cotejadas una por una.

**Resultado de la verificación imagen-vs-texto:** coincidencia exacta en las 6 páginas, sin ninguna discrepancia entre el render PNG y el `.txt` de apoyo. Esto es consistente con que la fuente es un PDF de texto nativo (no escaneado), según lo indicado en §0.

**Confianza por página/sección:**

| Página / sección | Confianza | Motivo |
|---|---|---|
| p.4 (U3ACB-1 completa, U3ACB-2 parcial) | **Alta** | Texto nítido, nativo, sin ambigüedad; coincide 100% con el .txt |
| p.5 (U3ACB-2 cont., U3ACB-3 completa, U3ACB-4 parcial) | **Alta** | Ídem |
| p.6 (U3ACB-4 cont., U3ACB-5 completa, U3ACB-6 parcial) | **Alta** | Ídem |
| p.7 (U3ACB-6 cont., U3ACB-7 completa, ZP-1 parcial) | **Alta** | Ídem |
| p.8 (ZP-1 cont., ZP-2, R22a, A.V completas, R21B-a parcial) | **Alta** | Ídem; incluye verificación fina del "%" de A.V. (§12) para descartar que fuera un dato cuantitativo real |
| p.9 (R21B-a cont. + cuadro completo, Cap. IV inicio) | **Alta** | Ídem; verificado el cierre limpio de la última tabla y la apertura de Vialidad (§13) |
| Zonas U3ACB-1 a U3ACB-7 (8 cuadros normativos, incluyendo R21B-a) | **Alta** | Las 8 zonas con cuadro "INTENSIDAD DE OCUPACION" completo fueron transcritas y verificadas parámetro por parámetro contra la imagen |
| Zonas ZP-1, ZP-2, R22a, A.V (restricción, sin cuadro) | **Alta** | Confirmado en las 4 que no hay cuadro de intensidad de ocupación; identificados con precisión los valores cuantitativos reales que sí existen en prosa (ZP-1: 80 m y 37 m) frente a los que no (ZP-2, R22a, A.V) |
| Correspondencia de páginas y continuidad de listas partidas | **Alta** | Verificado directamente contra las imágenes, no inferido solo del .txt |

**Nivel de confianza global: Alto.** No se identificó ningún valor ilegible ni ningún corte de página que dejara un dato numérico a medias. Las únicas incertidumbres genuinas están fuera del rango de este encargo por definición (contenido de p.3 y p.10, no entregados) y se señalan como tales, sin especular sobre su contenido.

**No se inventó ningún valor.** Todo campo sin dato se marcó como "Sin valor específico en la fuente" (con explicación del motivo de diseño) — no se usó "Dato no determinable" en ningún punto de este documento, porque no hubo ninguna ilegibilidad real en el material entregado.
