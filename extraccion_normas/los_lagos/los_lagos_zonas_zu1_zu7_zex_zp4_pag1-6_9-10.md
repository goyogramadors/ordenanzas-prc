# Normas Urbanísticas — Ordenanza Local del Plan Regulador Comunal de Los Lagos (Resolución N°77/1996) + Decreto N°796/2007

**Fuente:** Diario Oficial de la República de Chile, N° 35.654, martes 31 de diciembre de 1996, páginas 13 a 18 — "APRUEBA PLAN REGULADOR COMUNAL DE LOS LAGOS" (Resolución/Res. Afecta N°77, Puerto Montt, 6 de septiembre de 1996, del Intendente Regional de la X Región de Los Lagos, que aprueba lo obrado por el Decreto Exento N°144 de 28/06/1995 de la I. Municipalidad de Los Lagos y contiene íntegro el texto de la Ordenanza Local del Plan Regulador Comunal de Los Lagos). Documento del PDF: `Ordenanzas ordenadas/OCR ok/los_lagos_na_plan_regulador__Plan_Regulador_Comunal.pdf` (12 páginas totales). Segunda parte de la fuente: Diario Oficial, publicación del 03/07/2008, "MUNICIPALIDAD DE LOS LAGOS — FIJA USOS DE SUELO Y NORMAS URBANÍSTICAS A ZONA ZEx-3... ASIMILÁNDOLAS A LA ZONA CONSOLIDADA ZU-4" (Decreto N°796 exento, Los Lagos, 28 de noviembre de 2007).

**Extracción:** páginas 1 a 6 del PDF (= páginas impresas 13 a 18 del Diario Oficial N°35.654; desfase constante página PDF = página impresa − 12) y páginas 9 a 10 del PDF (Decreto N°796/2007, páginas impresas propias del Diario Oficial de 2008, sin numeración correlativa con las páginas 1-6). Quedan fuera de este encargo las páginas 7-8 (Capítulo V Vialidad, cuadro de calles) y 11-12 (planos).

**Método:** TEXTO+VISUAL. Extracción de texto con `pdftotext -layout` para ambos rangos, más verificación visual con `pdftoppm` (150-200dpi) de las páginas 2, 5, 6, 9 y 10 completas, incluyendo recortes ampliados de las tablas de zonas ZEx-1/ZEx-4 en la página 5 para confirmar dígitos y la palabra "agrupamiento" (el texto OCR de `pdftotext` la deforma sistemáticamente como "agolpamiento" en varias zonas; confirmado visualmente que el original dice **"agrupamiento"**, no "agolpamiento" — se transcribe la forma correcta). Las páginas 9-10 (Decreto 796/2007) tienen capa de texto nativo limpia (no son imagen escaneada, a diferencia de lo que sugería la nota de Fase 3 sobre "verificado visual"); aun así se renderizaron y compararon visualmente palabra por palabra contra el texto extraído, sin discrepancias.

**Nota de precisión respecto de Fase 3:** la nota de Fase 3 llama a este bloque "Cap.5 Zonificación". En el documento real, la tabla de contenidos (página 1) y los encabezados de artículo muestran que la zonificación es el **Capítulo IV** ("Definición de Macroáreas Zonificación, Uso de Suelo y Normas Específicas", Art.21-23) y que el **Capítulo V es Vialidad** (Art.24 en adelante, páginas 6-8, excluido de este encargo). Se documenta como precisión, no como error de Fase 3 — el contenido y el rango de páginas que describe la nota son correctos.

**Nota de cobertura — todas las zonas encontradas:** el Art.21 declara expresamente la lista completa de zonas del plan: "Áreas Consolidadas: ZU-1, ZU-2, ZU-3, ZU-4, ZU-5, ZU-6, ZU-7. Áreas Extensión urbana: ZEX-1, ZEX-2, ZEX-3, ZEX-4 y ZEX-5. Áreas de Restricción: ZP-1, ZP-2, ZP-3, ZP-4, ZP-5, ZP-6, ZP-7." Es decir, **19 zonas en total**, no solo las 9 que menciona a modo de ejemplo la nota de Fase 3 (ZU-1 a ZU-7, ZEx-3, ZP-4, ZEx-5). Las 19 están íntegramente presentes en las páginas 5-6 del PDF y se transcriben todas a continuación, incluyendo las zonas de restricción (ZP-1, ZP-2, ZP-4, ZP-5, ZP-7) que en la fuente **no tienen tabla numérica de normas específicas** — son zonas de protección descritas solo en prosa (se transcribe así, sin inventar valores).

**Nota de cruce con otro documento del corpus:** el mismo texto normativo de las 19 zonas (con idéntica redacción y los mismos valores) también fue transcrito, de forma independiente, en `extraccion_normas/los_lagos/los_lagos_144_ordenanza_original_19zonas_pag5-6.md` (documento `los_lagos_4ececfecdd`, sesión SESION1, HECHO el 2026-07-15), a partir de un PDF **distinto** (`los_lagos_144_...Ordenanza_Comunal_PRC_LOS_LAGOS.pdf`, el decreto municipal original de 1995, páginas 5-6 de ese archivo). No es una colisión de id (son documentos y rangos de páginas distintos dentro del pipeline, cada uno con su propio recibo JSON), pero se deja constancia porque ambas transcripciones se corroboran mutuamente valor por valor — coincidencia total salvo por la fidelidad tipográfica de detalle (p.ej. "agrupamiento" vs "agolpamiento", que aquí se corrige tras verificación visual). Este documento añade, además, lo que el otro no cubre: los Artículos 1-20 (definiciones, Art.7-20) con contexto de fuente Diario Oficial, y el Decreto N°796/2007 completo (páginas 9-10), ausente del otro documento.

---

## Definiciones de términos (Capítulo III, Artículo 7) — contexto para leer las tablas de zonas

| Término | Definición (transcripción literal) |
|---|---|
| Coeficiente de Ocupación de suelo (COS) | "Número que multiplicado por la Superficie total del predio, descontada de esta última las áreas declaradas de utilidad pública que pudieran afectarlas por disposiciones del presente Plan Regulador, fija el máximo de m2 posibles de construir en el nivel del piso terminado adyacente al terreno definitivo. Para tal efecto, la superficie edificada se determinará con la proyección del edificio sobre el terreno, descontando el 100% de la proyección de los aleros, balcones, cubiertas en voladizos." Las terrazas y pavimentos exteriores no se contabilizan; tampoco los cobertizos ni construcciones ligeras cubiertas y abiertas por dos o más lados que no excedan el 10% de la superficie del terreno (el exceso sobre ese porcentaje se contabiliza en un 50%). |
| Coeficiente de Constructibilidad | "Número que multiplicado por la superficie total del predio, descontada de esta última las áreas declaradas de utilidad pública, fija el máximo de m2 posibles de construir en él." |
| Edificación aislada | "Es la que se construye separada de los deslindes, emplazada por lo menos a las distancias resultantes de la aplicación de las normas sobre rasantes y distanciamientos que establece la Ordenanza General de Urbanismo y Construcciones (D.S. 47 V. y U. 1992; de D.O. 19.05.1992)." |
| Edificación pareada | "Es la que corresponde a dos edificaciones que se construyen simultáneamente, o diferidas en el tiempo, emplazadas a partir de un deslinde común, manteniendo una misma línea de fachada, altura y longitud de pareo. Las fachadas no pareadas deberán cumplir con las normas previstas para la edificación aislada." |
| Edificación continua | "Es la que se construye simultáneamente, o diferida en el tiempo, emplazada a partir de los deslindes laterales opuestos o concurrentes de un mismo predio y ocupando todo el frente de éste, manteniendo un mismo plano de fachada y con la altura que establece el presente Plan Regulador." |
| Densidad Bruta | "Es la relación entre número de viviendas por Hectáreas (medidas éstas a eje de vías, incluidos los espacios públicos y de equipamiento)." |
| Altura de Edificación | "Distancia vertical medida entre el suelo vertical y un plano paralelo al mismo que corresponderá al cielo del local habitable más elevado; si éste no fuera horizontal (mansarda) se trazará una línea imaginaria paralela al suelo natural por el punto más elevado del último recinto habitable la cual no podrá tener una altura inferior a 2 m." Suelo natural: "el estado que se encuentra en terreno al momento de proponer una construcción en él, no considerando excavaciones, rellenos u otras obras de carácter artificial." |
| Adosamientos (Art.9) | Se ajustan al artículo 2.6.2. de la OGUC; "se permitirán para cualquier forma de **agrupamiento**" (confirmado visualmente; no "agolpamiento"). |
| Rasantes y distanciamientos (Art.8) | Se rigen por el artículo 2.6.3. de la OGUC. Es la norma a la que remiten todas las tablas de zona bajo "Altura máxima de la edificación: respetando rasantes de acuerdo al artículo 8 de la presente Ordenanza". |
| Antejardines — regla general (Art.11) | Profundidad no inferior a 3 m para vías estructurantes y 2 m en calles locales y/o pasajes, salvo lo que fije cada zona en el Art.23. Si una zona no establece antejardín, se exige igualmente en costados de cuadra donde el 50% o más de su longitud ya disponga de ellos (misma profundidad mínima). En predios de esquina con destino vivienda unifamiliar, el antejardín se exige solo en el frente de acceso; el otro costado queda sujeto al 40% del ancho vigente en la vía — salvo que el predio enfrente 2 vías estructurantes (Art.26), caso en que esta regla no aplica. |

## Clasificación de áreas y zonas (Artículo 21)

> "El presente Plan Regulador contempla las siguientes áreas: Área Consolidada... Área de Extensión Urbana... Área Restricción... Áreas Especiales... Las áreas anteriormente mencionadas se dividen en las siguientes zonas: **Áreas Consolidadas: ZU-1, ZU-2, ZU-3, ZU-4, ZU-5, ZU-6, ZU-7. Áreas Extensión urbana: ZEX-1, ZEX-2; ZEX-3; ZEX-4 y ZEX-5. Áreas de Restricción: ZP-1, ZP-2, ZP-3, ZP-4, ZP-5, ZP-6, ZP-7.**"

(La fuente usa indistintamente "ZEX-1"/"ZEx1"/"ZEx-2" — mayúsculas y guion inconsistentes según el punto del documento; en los encabezados de cada zona (páginas 5-6) aparece literalmente "Zona ZEx1" sin guion para la primera y "Zona ZEx-2" a "Zona ZEx-5" con guion para las siguientes. Se estandariza aquí a "ZEx-1"..."ZEx-5" para consistencia, dejando esta nota como registro de la variante tipográfica original.)

---

## Zonas Urbanas (Área Consolidada)

### Zona ZU-1

**a) Usos de suelo permitidos:** Vivienda; Equipamiento de escalas comunal y vecinal de todo tipo; Actividades complementarias a la vialidad y el transporte sólo del tipo señalado en letra a) del artículo 16 de la presente Ordenanza.
**b) Usos de suelo prohibidos:** Todos los usos de suelo no mencionados precedentemente.

**c) Normas Específicas**

| Parámetro | Valor |
|---|---|
| Superficie predial mínima | 300 m² |
| Frente predial mínimo | 10 m |
| Coeficiente de ocupación de suelo | 80% |
| Densidad Bruta | No se consulta |
| Sistema de agrupamiento | Aislado, pareado y continuo |
| Altura máxima de la edificación | Aislado o pareado, respetando rasantes. Continuo 12 m. Sobre la altura máxima de la edificación continua se permite construcción aislada, respetando rasantes de acuerdo al Art. 8 de la presente Ordenanza |
| Profundidad máxima de la edificación continua | 50% del deslinde común |
| Antejardín mínimo | No se consultan, excepto lo dispuesto en el inciso segundo del artículo 11 de la presente Ordenanza |

### Zona ZU-2

**a) Usos de suelo permitidos:** Vivienda; Equipamiento de escala vecinal de todo tipo; Industria, almacenamiento y talleres inofensivos; Actividades complementarias a la vialidad y el transporte de acuerdo a lo establecido en el artículo 16 de la presente Ordenanza.
**b) Usos de suelo prohibidos:** "Todos los usos de suelo no mencionados como prohibidos" — así consta textualmente en la fuente (verificado visualmente); nótese que esta redacción es inversa a la fórmula usada en el resto de las zonas ("no mencionados precedentemente" = prohibido lo no listado como permitido). Se transcribe literal, sin corregir, por ser posible particularidad o errata del texto original publicado.

**c) Normas Específicas**

| Parámetro | Valor |
|---|---|
| Superficie predial mínima | Vivienda y equipamiento: 200 m². Otros usos permitidos: 400 m² |
| Frente predial mínimo | 10 m |
| Coeficiente máximo de ocupación de suelo | Vivienda y equipamiento: 60% |
| Densidad Bruta | No se consulta |
| Sistema de agrupamiento | Aislado o pareado |
| Altura máxima de la edificación | Respetando rasantes de acuerdo a artículo 8 de la presente Ordenanza |
| Antejardín mínimo | De acuerdo a lo establecido en el artículo 11 de la presente Ordenanza Local |

### Zona ZU-3

**a) Usos de suelo permitidos:** Vivienda; Equipamiento de escala vecinal de todo tipo; Almacenamiento y Talleres inofensivos; Actividades complementarias a la vialidad y el transporte sólo del tipo señalado en letra a) del artículo 16 de la presente Ordenanza.
**b) Usos de suelo prohibidos:** Todos los usos de suelo no mencionados precedentemente.

**c) Normas Específicas**

| Parámetro | Valor |
|---|---|
| Superficie predial mínima | 160 m² |
| Frente predial mínimo | 8 m |
| Coeficiente de ocupación de suelo | 60% |
| Densidad Bruta | No se consulta |
| Sistema de agrupamiento | Aislado o pareado |
| Altura máxima de la edificación | Respetando rasantes, de acuerdo al Art. 8 de la presente Ordenanza |
| Antejardín mínimo | De acuerdo a lo establecido en el artículo 11 de la presente Ordenanza Local |

### Zona ZU-4

**a) Usos de suelo permitidos:** Vivienda; Equipamiento de escala vecinal de todo tipo; Talleres inofensivos.
**b) Usos de suelo prohibidos:** Todos los usos de suelo no mencionados precedentemente.

**c) Normas Específicas**

| Parámetro | Valor |
|---|---|
| Superficie predial mínima | 160 m² |
| Frente predial mínimo | 8 m |
| Coeficiente de ocupación de suelo | 60% |
| Densidad Bruta | No se consulta |
| Sistema de agrupamiento | Aislado o pareado |
| Altura máxima de la edificación | Respetando rasantes, de acuerdo al artículo 8 de la presente Ordenanza |
| Antejardín mínimo | De acuerdo a lo establecido en la artículo 11 de la presente Ordenanza Local |

### Zona ZU-5 (Zona Microindustrial)

**a) Usos de suelo permitido:** Industrias, almacenamiento y talleres inofensivos; Vivienda, sólo cuidador.
**b) Uso de suelo prohibido:** Todos los usos de suelo no mencionados precedentemente.

**c) Normas Específicas**

| Parámetro | Valor |
|---|---|
| Superficie predial mínima | 5.000 m² |
| Frente predial mínimo | 40 m |
| Coeficiente de ocupación de suelo | 30% |
| Densidad Bruta | No se consulta |
| Sistema de agrupamiento | Aislado, prohibido adosamiento |
| Altura máxima de la edificación | Respetando rasantes de acuerdo al artículo 8 de la presente Ordenanza |
| Antejardín mínimo | No se consulta, excepto lo dispuesto en el inciso 2° del artículo 11 de la presente Ordenanza |

### Zona ZU-6

**a) Usos de suelo permitidos:** Vivienda; Equipamiento de escala comunal de todo tipo; Equipamiento ferroviario; Almacenamiento inofensivos, sólo frente a calle Brasil; Actividades complementarias a la vialidad y el transporte sólo del tipo señalado en letra a) del artículo 16 de la presente Ordenanza.
**b) Usos de suelo prohibidos:** Todos los usos de suelo no mencionados precedentemente.

**c) Normas Específicas**

| Parámetro | Valor |
|---|---|
| Superficie predial mínima | 500 m² |
| Frente predial mínimo | 15 m |
| Coeficiente de ocupación de suelo | 40% |
| Densidad Bruta | 100 hab/há |
| Sistema de agrupamiento | Aislado |
| Altura máxima de la edificación | Respetando rasantes de acuerdo al artículo 8 de la presente Ordenanza |
| Antejardín mínimo | 5 m |

### Zona ZU-7

**a) Usos de suelo permitidos:** Equipamiento de escala comunal de áreas verdes, deportes, esparcimiento y turismo; vivienda sólo de propietario y cuidador.
**b) Usos de suelo prohibidos:** Todos los usos de suelo no mencionados precedentemente.

**c) Normas Específicas**

| Parámetro | Valor |
|---|---|
| Superficie predial mínima | 2000 m² |
| Frente predial mínimo | 25 m |
| Coeficiente de ocupación de suelo | 30% |
| Densidad Bruta | No se consulta |
| Sistema de agrupamiento | Aislado |
| Altura máxima de la edificación | Respetando rasantes de acuerdo al artículo 8 de la presente Ordenanza |
| Antejardín mínimo | 5 m |

---

## Zonas de Extensión Urbana

### Zona ZEx-1

*(En el encabezado original de la fuente aparece como "Zona ZEx1", sin guion — ver nota de tipografía arriba.)*

**a) Usos de suelo permitidos:** Vivienda; Equipamiento de escala vecinal de todo tipo; Talleres inofensivos.
**b) Usos de suelo prohibidos:** "Todos los usos de suelo no mencionados precedemente" — así consta textualmente en la fuente (confirmado visualmente con recorte ampliado); es la única zona donde la fórmula habitual "precedentemente" aparece impresa como "precedemente" (falta "nt"), aparente errata tipográfica del Diario Oficial. Se transcribe [sic], sentido no afectado.

**c) Normas Específicas**

| Parámetro | Valor |
|---|---|
| Superficie predial mínima | 160 m² |
| Frente predial mínimo | 8 m |
| Coeficiente de ocupación de suelo | 50% |
| Densidad Bruta | Se consulta una densidad bruta de 225 hab/há |
| Sistema de agrupamiento | Aislado o pareado |
| Altura máxima de la edificación | Respetando rasantes de acuerdo a artículo 8 de la presente Ordenanza |
| Antejardín mínimo | 3 m |

### Zona ZEx-2

**a) Usos de suelo permitidos:** Viviendas; Equipamiento de escala vecinal de todo tipo, excepción esparcimiento y turismo según artículo 14 de la presente Ordenanza.
**b) Usos de suelo prohibidos:** Todos los usos de suelo no mencionados precedentemente.

**c) Normas Específicas**

| Parámetro | Valor |
|---|---|
| Superficie predial mínima | Vivienda 300 m². Equipamiento 500 m² |
| Frente predial mínimo | Vivienda 10 m. Equipamiento 60 m |
| Coeficiente de ocupación de suelo | Vivienda 40%. Equipamiento 60% |
| Densidad Bruta máxima | 100 hab/há |
| Sistema de agrupamiento | Aislado o pareado |
| Altura máxima de la edificación | Respetando rasantes de acuerdo a artículo 8 de la presente Ordenanza |
| Antejardín mínimo | 3 m |

### Zona ZEx-3 (Zona Industrial) — valores originales de 1996

*Nota: esta zona fue posteriormente reasignada en parte por el Decreto N°796/2007 — ver sección aparte al final de este documento.*

**a) Usos de suelo permitidos:** Industria, almacenamiento y talleres inofensivos y molestos; Viviendas, sólo cuidador; Actividades complementarias a la vialidad y el transporte sólo del tipo señalado en la letra a) del artículo 16 de la presente Ordenanza.
**b) Usos de suelo prohibidos:** Todos los usos de suelo no mencionados precedentemente.

**c) Normas Específicas**

| Parámetro | Valor |
|---|---|
| Superficie predial mínima | Equipamiento: 2.500 m². Industria, almacenamiento y talleres: 5.000 m² |
| Frente predial mínimo | Equipamiento: 35 m. Industria, almacenamiento y talleres: 50 m |
| Coeficiente de ocupación de suelo | 30% |
| Densidad Bruta | No se consulta |
| Sistema de agrupamiento | Aislado |
| Altura máxima de la edificación | Respetando rasantes de acuerdo al artículo 8 de la presente Ordenanza |
| Antejardín mínimo | 10 m |

### Zona ZEx-4

**a) Usos de suelo permitidos:** Vivienda; Equipamiento de deportes y áreas verdes de escala comunal; Actividades agrícolas.
**b) Usos de suelo prohibidos:** Todos los usos de suelo no mencionados precedentemente.

**c) Normas Específicas**

| Parámetro | Valor |
|---|---|
| Superficie predial mínima | 20.000 m² |
| Frente predial mínimo | 100 m |
| Coeficiente de ocupación de suelo | 0,2% |
| Densidad Bruta | 5 hab/Há |
| Sistema de agrupamiento | Aislado |
| Altura máxima de la edificación | Respetando rasantes de acuerdo al artículo 8 de la presente Ordenanza |
| Antejardín mínimo | 10 m |

*(El valor de COS de 0,2% se verificó visualmente con recorte ampliado por ser un valor atípicamente bajo frente al resto de las zonas — confirmado que así consta en el original; es consistente con el resto del perfil de la zona: predio mínimo 20.000 m², densidad 5 hab/Há, uso agrícola permitido, es decir, una zona de borde/expansión de muy baja ocupación.)*

### Zona ZEx-5

**a) Usos de suelo permitidos:** Equipamiento de salud de escala comunal y comercio de escala vecinal; Actividades complementarias a la vialidad y el transporte de acuerdo a lo establecido en el artículo 16 de la presente Ordenanza.
**b) Usos de suelo prohibidos:** Todos los usos de suelo no mencionados precedentemente.

**c) Normas Específicas**

| Parámetro | Valor |
|---|---|
| Superficie predial mínima | 500 m² |
| Frente predial mínimo | 15 m |
| Coeficiente de ocupación de suelo | 60% |
| Densidad Bruta | 60 hab/há |
| Sistema de agrupamiento | Aislado |
| Altura máxima de la edificación | Respetando rasantes de acuerdo al artículo 8 de la presente Ordenanza |
| Antejardín mínimo | 5 m |

---

## Zonas de Restricción

### Zona ZP-1 — Faja de Línea Férrea

Zona especial de protección del trazado de la vía férrea, de 20 m de ancho. **La fuente no incluye tabla de usos de suelo ni de normas específicas para esta zona** — es descripción de sola prosa, zona no edificable por definición. No se inventan valores.

### Zona ZP-2 — Zona Protección Ruta 5 Sur

Zona especial no edificable, de protección de la carretera, de 35 m a ambos costados del derecho a vía de 40 m de la Ruta 5 Sur. **Sin tabla de usos de suelo ni normas específicas en la fuente.**

### Zona ZP-3

Corresponde a zona no edificable expuesta a riesgo de inundación, ubicada en ambas riberas del río Collilelfu, en la ribera sur del río Calle Calle y ribera norte del estero Huiña-Huiño. El ancho de estas fajas es variable según se grafica en plano PRC LAG-01a. El ancho mínimo es 30 m.

**a) Usos de suelo permitidos:** Equipamiento de áreas verdes y deportes de escala vecinal, sólo canchas.
**b) Usos de suelo prohibidos:** Todos los usos de suelo no mencionados precedentemente.

**c) Normas Específicas**

| Parámetro | Valor |
|---|---|
| Superficie predial mínima | 5.000 m² |
| Frente predial mínimo | 50 m |

*(La fuente solo entrega estos dos parámetros para ZP-3; no hay COS, densidad, agrupamiento, altura ni antejardín — consistente con ser zona de protección no edificable. No se inventan los campos faltantes.)*

### Zona ZP-4 — Recinto ESSAL

Zona especial de protección de instalaciones de la Empresa de Servicios Sanitarios Los Lagos. **La fuente no incluye tabla de usos de suelo ni de normas específicas para esta zona** — es descripción de sola prosa. No se inventan valores.

### Zona ZP-5 — Recinto ENDESA

Zona especial de protección de subestación eléctrica. **Sin tabla de usos de suelo ni normas específicas en la fuente.**

### Zona ZP-6 — Zona de Equipamiento de Cementerio

**Usos de suelo permitidos:** Cementerio.
**Usos de suelo prohibidos:** Todos los usos de suelo no mencionados precedentemente.
**Norma general:** "Esta zona está acogida a las disposiciones contenidas en el DS. N° 357/70 del Ministerio de Salud, Reglamento General de Cementerios."

*(No hay tabla numérica de superficie predial/frente/COS/densidad/agrupamiento/altura/antejardín para esta zona en la fuente — se rige por remisión al DS 357/70, no se inventan valores.)*

### Zona ZP-7 — Zona de Pendientes

Zona especial de protección de sectores con fuertes pendientes. Queda prohibido todo tipo de obras, como asimismo la extracción de materiales y el despojo de su capa vegetal. **Sin tabla de usos de suelo ni normas específicas en la fuente** (la prohibición total reemplaza cualquier norma de edificación).

---

## Decreto N°796/2007 (publicado en el Diario Oficial el 03/07/2008) — Zona ZEx-3 asimilada a la Zona Consolidada ZU-4

**Título:** "Municipalidad de Los Lagos — Fija Usos de Suelo y Normas Urbanísticas a Zona ZEx-3 (Zona Industrial Lotes N°3 y N°4) del Plan Regulador Comunal de Los Lagos Asimilándolas a la Zona Consolidada ZU-4."

**Núm. 796 exento, Los Lagos, 28 de noviembre de 2007.** Decreto que, a solicitud del propietario Empresas Martabid Ltda. (solicitud de 30/03/2007, para permitir un loteo habitacional de 177 viviendas), reclasifica parte de la zona industrial ZEx-3 a un régimen normativo idéntico al de la Zona ZU-4, mediante un seccional específico. Fundamentos citados: informes de la Dirección de Obras Municipales (23/04/2007 y 21/06/2007), acuerdo del Concejo Municipal N°777 (21/06/2007) para iniciar el cambio de uso de suelo, presentación del diseño de loteo (recibida 05/11/2007, N°256), Art.2.1.14 inciso 2° de la OGUC, y memoria explicativa de la DOM (13/05/2008). Aprobado por acuerdo del Concejo Municipal N°892 (03/06/2008), sesión ordinaria N°126 (15/05/2008). Firma: Simón Mansilla Roa, Alcalde; Veruska Ivanoff R., Secretaria Municipal (S).

**Zona resultante: "ZU-4 (Seccional 'La Rotonda')".**
**Área afectada:** Lotes 3 y 4 de una superficie aproximada de 46.325 m², de propiedad de Empresas Martabid Ltda., confinado entre Calle Quinchilca y Lote N°2 del Sr. Jorge Klocker y Calle de Acceso Sur a Los Lagos con Carretera 5 Sur.

**a) Usos de suelos permitidos:** Vivienda; Equipamiento de escala vecinal de todo tipo; Talleres inofensivos.
**b) Usos de suelos prohibidos:** Todos los usos de suelos no mencionados precedentemente.

**c) Normas específicas**

| Parámetro | Valor |
|---|---|
| Superficie predial mínima | 160 m² |
| Frente predial mínimo | 8 m |
| Coeficiente de ocupación de suelo | 60% |
| Densidad bruta | No se consulta |
| Sistema de agrupamiento | Aislado y pareado |
| Altura máxima de la edificación | Respetando rasante de acuerdo al artículo 8 de la Ordenanza Local del Plan Regulador Comunal |
| Antejardín | De acuerdo a lo establecido en el artículo 11 de la Ordenanza Local del Plan Regulador Comunal |

**Nota importante — esto es una MODIFICACIÓN POSTERIOR, no la norma original de 1996:** estos valores (superficie 160 m², frente 8 m, COS 60%, sin densidad, agrupamiento "aislado y pareado") **coinciden exactamente** con los de la Zona ZU-4 original transcrita arriba (que ya tenía esos mismos siete valores desde 1996). Lo que hace el Decreto 796/2007 no es cambiar cifras, sino **reclasificar el uso de suelo** de un predio específico (Lotes 3 y 4 de ZEx-3, industrial/molesto con vivienda solo de cuidador) al régimen normativo de ZU-4 (residencial/equipamiento vecinal), habilitando así el loteo habitacional de 177 viviendas solicitado. La zona ZEx-3 en el resto de su superficie (fuera de los Lotes 3 y 4) no consta modificada por este decreto y mantiene, según la fuente disponible, los valores originales de 1996 transcritos en la sección "Zona ZEx-3" de este documento.

---

## Metodología y confianza

- **Cobertura:** 19 zonas del Capítulo IV de la Ordenanza Local de 1996 (7 urbanas ZU-1 a ZU-7, 5 de extensión urbana ZEx-1 a ZEx-5, 7 de restricción ZP-1 a ZP-7) transcritas en su totalidad, más 1 zona adicional del Decreto N°796/2007 (reclasificación ZEx-3→ZU-4, Seccional "La Rotonda") — 20 entradas en total. De las 19 zonas de 1996, 5 (ZP-1, ZP-2, ZP-4, ZP-5, ZP-7) no tienen tabla numérica de normas específicas en la fuente — se documenta explícitamente esa ausencia en vez de inventar valores; 1 (ZP-3) solo tiene 2 de los 7 parámetros habituales (superficie y frente) — también documentado sin rellenar los faltantes; 1 (ZP-6) se rige por remisión a un reglamento externo (DS 357/70) sin tabla propia.
- **Verificación visual:** confirmada la lectura de "agrupamiento" (no "agolpamiento", error sistemático de la extracción de texto plano) en múltiples puntos del documento; confirmado el valor atípico COS=0,2% de ZEx-4; confirmada la errata "precedemente" (por "precedentemente") específica de la Zona ZEx-1; confirmado el contenido íntegro del Decreto 796/2007 (páginas 9-10) letra por letra contra su capa de texto nativo.
- **Definiciones de apoyo:** se incluyen las definiciones de COS, coeficiente de constructibilidad, edificación aislada/pareada/continua, densidad bruta y altura de edificación (Art.7, página 2 del PDF) como contexto de lectura de las tablas — no son zonas, se marcan aparte.
- **Nada fue inventado:** todo valor ausente en la fuente para una zona se declara explícitamente como ausente ("sin tabla de normas específicas en la fuente", "no hay X en la fuente"), nunca se completó por analogía con otra zona.
- **Confianza: ALTA.** Método TEXTO+VISUAL con doble verificación (texto plano + render de imagen con recortes ampliados en los puntos dudosos) y triangulación adicional con una transcripción independiente del mismo texto normativo hecha por otra sesión a partir de un PDF distinto (`los_lagos_4ececfecdd`, ver nota de cruce arriba), que coincide en el 100% de los valores numéricos.
