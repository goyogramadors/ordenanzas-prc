# Decreto Exento N°230 (2013) — Enmienda N°1 art. 4.1.3, Ordenanza Local PRC Curicó

Fuente: Diario Oficial (boletín), inserción del Decreto Exento N°0230, I. Municipalidad de Curicó, Secretaría Municipal, Curicó 25 de enero de 2013 (Acue011-2013). Vistos: Acuerdo N°160 (sesión 09/07/2012), Decreto Exento N°1865 de 23/07/2012, Acuerdo N°11 (sesión 15/01/2013). El Decreto aprueba en forma definitiva, en su punto PRIMERO, la modificación del Plan Regulador de Curicó vía Enmienda N°1, que cambia la Ordenanza Local del Plan Regulador Vigente — "ENMIENDA DEL ARTÍCULO 4.1.3 DE USOS DE SUELO Y NORMAS ESPECÍFICAS", Título 4 "Zonificación, Usos de Suelo y Normas Específicas", Artículo 4.1.3 "Usos de Suelo y Normas Específicas" — modificando las normas de condiciones de subdivisión y edificación de las zonas del Área Urbana indicadas en el Artículo 4.1.2 Zonificación de la Ordenanza Local.

**Nota de alcance — "Usos" por zona:** ninguna de las tablas de las páginas 3-6 trae un listado de usos de suelo permitidos/prohibidos por zona (eso vive en el Artículo 4.1.2, no incluido en este render). Las tablas solo presentan las normas de subdivisión y edificación **diferenciadas por 4 categorías de uso genéricas que actúan como columnas**: Residencial, Equipamiento, Actividades productivas e Infraestructura (algunas zonas traen solo un subconjunto de estas columnas). Por eso el campo "Usos" de cada zona más abajo se omite/marca "No especificado en esta tabla" tal como indica la plantilla.

**Nota de verificación de cobertura (Paso 2):** se enumeraron visualmente las 4 páginas antes de transcribir. Total de zonas encontradas: **14** — ZCC, ZU-1, ZU-2, ZU-3, ZU-4, ZU-5, ZU-6, ZU-7, ZU-8, ZU-9, ZU-10, ZU-11, ZI, ZE-2 — coincide exactamente con la lista esperada en el contexto del encargo. Distribución: pág. 3 trae ZCC y ZU-1 (esta última con tabla incompleta, ver nota); pág. 4 trae ZU-2, ZU-3, ZU-4, ZU-5; pág. 5 trae ZU-6, ZU-7, ZU-8, ZU-9; pág. 6 trae ZU-10, ZU-11, ZI, ZE-2, y cierra con el texto del decreto (SEGUNDO, firma).

**Nota de método (celdas combinadas):** las tablas están escaneadas como imagen (no hay texto seleccionable). Varias filas muestran menos valores que columnas porque el documento original combina celdas adyacentes cuando dos o más usos comparten el mismo valor normativo. Dado que a simple vista es fácil confundir el límite de una celda combinada (ej. "¿el valor aplica a Residencial+Equipamiento, o a Residencial+Equipamiento+Actividades productivas?"), cada tabla de zona con 3 o 4 columnas de uso fue verificada **midiendo programáticamente la posición de las líneas de grilla verticales** (análisis de píxeles sobre el render de cada página) para confirmar, fila por fila, qué usos comparten celda. Esto corrigió al menos dos lecturas iniciales a simple vista (agrupamiento/distanciamiento de ZU-5 y ZU-7, que se muestran combinados como "Residencial+Equipamiento" / "Actividades productivas+Infraestructura" y no como se asumió al inicio). Todos los valores numéricos en sí fueron legibles sin ambigüedad.

**Nota de convención propia:** en el original, la celda "-" (guion) se usa deliberadamente para indicar que la norma **no aplica** a ese uso (ej. densidad máxima no aplica a Equipamiento/Actividades productivas/Infraestructura). Se transcribe como "No aplica" para distinguirlo de valores realmente ilegibles o de filas que no existen en una tabla (esas se marcan "No especificado").

**Nota — posible solape con otro extracto de esta misma carpeta:** existe también el archivo `curico_decreto230_enmienda1_extracto_pag1-4.md`, que transcribe el mismo Decreto Exento N°230/2013 (mismas 14 zonas) a partir de un PDF distinto (copia suelta del decreto, no el Diario Oficial). Es la misma norma publicada por dos vías — evitar doble conteo en Fase 5. Ese extracto coincide con esta transcripción en prácticamente todos los valores, con una diferencia puntual detectada: para "Altura de cierros" en varias zonas (ej. ZU-2, ZU-3) ese otro archivo agrupa "Residencial/Equipamiento/Actividades productivas" vs. "Infraestructura", mientras que la medición de píxeles hecha aquí confirma que el límite real de la celda combinada en el render es "Residencial/Equipamiento" vs. "Actividades productivas/Infraestructura". Se prioriza la medición de píxeles de este documento.

---

## Zona ZCC (Zona Centro Cívico)
**Usos:** No especificado en esta tabla (ver nota general).
**Condiciones:**
- Superficie predial mínima: Residencial 560 m²; Equipamiento 420 m².
- Coeficiente de ocupación de suelo (COS): 1 en ambos usos.
- Coeficiente de constructibilidad: 3,25 en ambos usos.
- Sistema de agrupamiento: Continuo (ambos usos).
- Distanciamiento: No especificado (esta tabla no trae esa fila).
- Altura máxima de edificación: 17 m en ambos usos.
- Antejardín: No especificado (esta tabla no trae esa fila; en su lugar usa "Retranqueo de fachada Nivel +3", ver abajo).
- Densidad máxima: Residencial 480 hab/ha; Equipamiento No aplica.
- Altura de cierros: No aplica en ambos usos (celda "-").
- Retranqueo de fachada Nivel +3: 3 m (ambos usos).

## Zona ZU-1 (Zona Urbana Central 1)
**Usos:** No especificado en esta tabla (ver nota general).
**Condiciones:**
- Superficie predial mínima: Residencial 420 m²; Equipamiento 280 m²; Actividades productivas 210 m².
- Coeficiente de ocupación de suelo (COS): 1 en los tres usos.
- Coeficiente de constructibilidad: 7,28 (valor único para los tres usos).
- Sistema de agrupamiento: Continuo (los tres usos).
- Distanciamiento: No especificado (esta tabla no trae esa fila).
- Altura máxima de edificación: No especificado (esta tabla no trae esa fila; confirmado con zoom, no es error de lectura — la fila simplemente no existe en esta tabla).
- Antejardín: No especificado (esta tabla no trae esa fila; en su lugar usa "Retranqueo Nivel +3", ver abajo).
- Densidad máxima: Residencial 960 hab/ha; Equipamiento y Actividades productivas No aplica.
- Altura de cierros: No aplica (valor único "-", los tres usos).
- Retranqueo Nivel +3: 3 m (los tres usos).

## Zona ZU-2 (Zona Urbana Pericentral 2)
**Usos:** No especificado en esta tabla (ver nota general).
**Condiciones:**
- Superficie predial mínima: Residencial 280 m²; Equipamiento 280 m²; Actividades productivas 140 m²; Infraestructura 1050 m².
- Coeficiente de ocupación de suelo (COS): Residencial 0,78; Equipamiento y Actividades productivas 1; Infraestructura 0,52.
- Coeficiente de constructibilidad: 8,125 (valor único para los cuatro usos).
- Sistema de agrupamiento: Aislado, pareado, continuo (Residencial/Equipamiento/Actividades productivas); Aislado (Infraestructura).
- Distanciamiento: OGUC (Residencial/Equipamiento/Actividades productivas); 5 m (Infraestructura).
- Altura máxima de edificación: Residencial y Equipamiento 57,6 m; Actividades productivas 16,8 m; Infraestructura 10,8 m.
- Antejardín: Vía troncal 7 m - Otra Jerarquía 5 m - Pasajes OGUC (Residencial/Equipamiento); 7 m (Actividades productivas/Infraestructura).
- Densidad máxima: Residencial 768 hab/ha; resto No aplica.
- Altura de cierros: 2,0 m (Residencial/Equipamiento); 2,5 m (Actividades productivas/Infraestructura).
- Retranqueo Nivel +4: 4 m (los cuatro usos).

## Zona ZU-3 (Zona Urbana Mixta 3)
**Usos:** No especificado en esta tabla (ver nota general).
**Condiciones:**
- Superficie predial mínima: Residencial 210 m²; Equipamiento 420 m²; Actividades productivas 280 m²; Infraestructura 700 m².
- Coeficiente de ocupación de suelo (COS): 0,78 (Residencial/Equipamiento/Actividades productivas); 0,52 (Infraestructura).
- Coeficiente de constructibilidad: 3,9 (Residencial/Equipamiento/Actividades productivas); 0,52 (Infraestructura).
- Sistema de agrupamiento: Aislado, pareado, continuo (Residencial/Equipamiento/Actividades productivas); Aislado (Infraestructura).
- Distanciamiento: OGUC (Residencial/Equipamiento/Actividades productivas); 5 m (Infraestructura).
- Altura máxima de edificación: Residencial y Equipamiento 57,6 m; Actividades productivas 16,8 m; Infraestructura 10,8 m.
- Antejardín: Vía troncal 7 m - Otra Jerarquía 5 m - Pasajes OGUC (Residencial/Equipamiento); 7 m (Actividades productivas/Infraestructura).
- Densidad máxima: Residencial 576 hab/ha; resto No aplica.
- Altura de cierros: 2,0 m (Residencial/Equipamiento); 2,5 m (Actividades productivas/Infraestructura).

## Zona ZU-4 (Zona Urbana Mixta 4)
**Usos:** No especificado en esta tabla (ver nota general).
**Condiciones:**
- Superficie predial mínima: Residencial 210 m²; Equipamiento 420 m²; Actividades productivas 210 m²; Infraestructura 700 m².
- Coeficiente de ocupación de suelo (COS): 0,78 (Residencial/Equipamiento/Actividades productivas); 0,52 (Infraestructura).
- Coeficiente de constructibilidad: Residencial y Equipamiento — edificación continua o pareada 1,95, edificación aislada 3,90; Actividades productivas e Infraestructura 0,52.
- Sistema de agrupamiento: Aislado, pareado, continuo (Residencial/Equipamiento/Actividades productivas); Aislado (Infraestructura).
- Distanciamiento: OGUC (Residencial/Equipamiento/Actividades productivas); 5 m (Infraestructura).
- Altura máxima de edificación: 25,2 m (Residencial/Equipamiento); 13,2 m (Actividades productivas/Infraestructura).
- Antejardín: Vía troncal 7 m - Otra Jerarquía 5 m - Pasajes OGUC (Residencial/Equipamiento); 7 m (Actividades productivas/Infraestructura).
- Densidad máxima: Residencial 768 hab/ha; resto No aplica.
- Altura de cierros: 2,0 m (Residencial/Equipamiento); 2,5 m (Actividades productivas/Infraestructura).

## Zona ZU-5 (Zona Urbana Mixta 5)
**Usos:** No especificado en esta tabla (ver nota general).
**Condiciones:**
- Superficie predial mínima: Residencial 210 m²; Equipamiento 350 m²; Actividades productivas 140 m²; Infraestructura 700 m².
- Coeficiente de ocupación de suelo (COS): Residencial 0,78; Equipamiento y Actividades productivas 1; Infraestructura 0,52.
- Coeficiente de constructibilidad: Residencial y Equipamiento — edificación continua o pareada 1,95, edificación aislada 3,90; Actividades productivas e Infraestructura 0,52.
- Sistema de agrupamiento: Aislado, pareado, continuo (Residencial/Equipamiento); Aislado (Actividades productivas/Infraestructura).
- Distanciamiento: OGUC (Residencial/Equipamiento); 5 m (Actividades productivas/Infraestructura).
- Altura máxima de edificación: 8,4 m (valor único, los cuatro usos).
- Antejardín: Vía troncal 5 m - Otra Jerarquía 3 m - Pasajes OGUC (Residencial/Equipamiento); 7 m (Actividades productivas/Infraestructura).
- Densidad máxima: Residencial 144 hab/ha; resto No aplica.
- Altura de cierros: 2,0 m (Residencial/Equipamiento); 2,5 m (Actividades productivas/Infraestructura).

## Zona ZU-6 (Zona Residencial 6)
**Usos:** No especificado en esta tabla (ver nota general).
**Condiciones:**
- Superficie predial mínima: Residencial 140 m²; Equipamiento 112 m²; Actividades productivas 140 m²; Infraestructura 700 m².
- Coeficiente de ocupación de suelo (COS): Residencial y Equipamiento 0,78; Actividades productivas 1; Infraestructura 0,52.
- Coeficiente de constructibilidad: Residencial y Equipamiento — edificación continua o pareada 1,95, edificación aislada 3,90; Actividades productivas e Infraestructura 0,52.
- Sistema de agrupamiento: Aislado, pareado, continuo (Residencial/Equipamiento); Aislado (Actividades productivas/Infraestructura).
- Distanciamiento: OGUC (Residencial/Equipamiento); 5 m (Actividades productivas/Infraestructura).
- Altura máxima de edificación: 25,2 m (Residencial/Equipamiento); 13,2 m (Actividades productivas/Infraestructura).
- Antejardín: Vía troncal o colectora 5 m - Otra Jerarquía 3 m - Pasajes OGUC (Residencial/Equipamiento); 7 m (Actividades productivas/Infraestructura).
- Densidad máxima: Residencial 780 hab/ha; resto No aplica.
- Altura de cierros: 2,0 m (Residencial/Equipamiento); 2,5 m (Actividades productivas/Infraestructura).

## Zona ZU-7 (Zona Residencial 7)
**Usos:** No especificado en esta tabla (ver nota general).
**Condiciones:**
- Superficie predial mínima: Residencial 175 m²; Equipamiento 210 m²; Actividades productivas 210 m²; Infraestructura 1050 m².
- Coeficiente de ocupación de suelo (COS): 0,78 (Residencial/Equipamiento); 0,52 (Actividades productivas/Infraestructura).
- Coeficiente de constructibilidad: 1,95 (Residencial/Equipamiento); 0,52 (Actividades productivas/Infraestructura).
- Sistema de agrupamiento: Aislado, pareado, continuo (Residencial/Equipamiento); Aislado (Actividades productivas/Infraestructura).
- Distanciamiento: OGUC (Residencial/Equipamiento); 5 m (Actividades productivas/Infraestructura).
- Altura máxima de edificación: 8,4 m (Residencial/Equipamiento); 13,2 m (Actividades productivas/Infraestructura).
- Antejardín: Vía troncal o colectora 5 m - Otra Jerarquía 3 m - Pasajes OGUC (Residencial/Equipamiento); 7 m (Actividades productivas/Infraestructura).
- Densidad máxima: Residencial 384 hab/ha; resto No aplica.
- Altura de cierros: 2,0 m (Residencial/Equipamiento); 2,5 m (Actividades productivas/Infraestructura).

## Zona ZU-8 (Zona Residencial 8)
**Usos:** No especificado en esta tabla (ver nota general).
**Condiciones:**
- Superficie predial mínima: Residencial 700 m²; Equipamiento y Actividades productivas 1750 m²; Infraestructura 1050 m².
- Coeficiente de ocupación de suelo (COS): 0,26 (Residencial/Equipamiento/Actividades productivas); 0,52 (Infraestructura).
- Coeficiente de constructibilidad: 0,325 (Residencial/Equipamiento); 0,52 (Actividades productivas/Infraestructura).
- Sistema de agrupamiento: Aislado (los cuatro usos).
- Distanciamiento: OGUC (Residencial/Equipamiento/Actividades productivas); 5 m (Infraestructura).
- Altura máxima de edificación: 13,2 m (Residencial/Equipamiento/Actividades productivas); 8,4 m (Infraestructura).
- Antejardín: Vía troncal o colectora 15 m - Otra Jerarquía 10 m (Residencial/Equipamiento/Actividades productivas); 15 m (Infraestructura).
- Densidad máxima: Residencial 48 hab/ha; resto No aplica.
- Altura de cierros: 2,0 m (Residencial/Equipamiento/Actividades productivas); 2,5 m (Infraestructura).

## Zona ZU-9 (Zona Residencial 9)
**Usos:** No especificado en esta tabla (ver nota general).
**Condiciones:**
- Superficie predial mínima: Residencial 1400 m²; Equipamiento, Actividades productivas e Infraestructura 1750 m² (sin diferenciar entre sí — sin línea de grilla que las separe en el render).
- Coeficiente de ocupación de suelo (COS): 0,26 (valor único, los cuatro usos, incluida Infraestructura).
- Coeficiente de constructibilidad: 0,52 (valor único, los cuatro usos, incluida Infraestructura).
- Sistema de agrupamiento: Aislado (los cuatro usos).
- Distanciamiento: OGUC (Residencial/Equipamiento/Actividades productivas); 5 m (Infraestructura).
- Altura máxima de edificación: 13,2 m (Residencial/Equipamiento/Actividades productivas); 8,4 m (Infraestructura).
- Antejardín: Vía troncal o colectora 15 m - Otra Jerarquía 10 m (Residencial/Equipamiento/Actividades productivas); 15 m (Infraestructura).
- Densidad máxima: Residencial 24 hab/ha; resto No aplica.
- Altura de cierros: 2,0 m (Residencial/Equipamiento/Actividades productivas); 2,5 m (Infraestructura).

## Zona ZU-10 (Zona Residencial 10)
**Usos:** No especificado en esta tabla (ver nota general).
**Condiciones:**
- Superficie predial mínima: Residencial 140 m²; Equipamiento y Actividades productivas 1750 m²; Infraestructura 1050 m².
- Coeficiente de ocupación de suelo (COS): 0,26 (Residencial/Equipamiento/Actividades productivas); 0,52 (Infraestructura).
- Coeficiente de constructibilidad: 0,325 (Residencial/Equipamiento); 0,52 (Actividades productivas/Infraestructura).
- Sistema de agrupamiento: Aislado (los cuatro usos).
- Distanciamiento: OGUC (Residencial/Equipamiento/Actividades productivas); 5 m (Infraestructura).
- Altura máxima de edificación: 13,2 m (Residencial/Equipamiento/Actividades productivas); 8,4 m (Infraestructura).
- Antejardín: Vía troncal o colectora 15 m - Otra Jerarquía 10 m (Residencial/Equipamiento/Actividades productivas); 15 m (Infraestructura).
- Densidad máxima: Residencial 120 hab/ha; resto No aplica.
- Altura de cierros: 2,0 m (Residencial/Equipamiento/Actividades productivas); 2,5 m (Infraestructura).

**Nota:** esta ZU-10 (base, Decreto 230/2013) es distinta de eventuales variantes "ZU-10a"/"ZU-10b" creadas por enmiendas posteriores (ya extraídas por separado en esta misma carpeta, si aplica) — no se fusionan en este documento.

## Zona ZU-11 (Zona Residencial 11)
**Usos:** No especificado en esta tabla (ver nota general).
**Condiciones:**
- Superficie predial mínima: Residencial 700 m²; Equipamiento, Actividades productivas e Infraestructura 1750 m² (sin diferenciar entre sí — sin línea de grilla que las separe en el render).
- Coeficiente de ocupación de suelo (COS): 0,26 (valor único, los cuatro usos, incluida Infraestructura).
- Coeficiente de constructibilidad: 0,52 (valor único, los cuatro usos, incluida Infraestructura).
- Sistema de agrupamiento: Aislado (los cuatro usos).
- Distanciamiento: OGUC (Residencial/Equipamiento/Actividades productivas); 5 m (Infraestructura).
- Altura máxima de edificación: 13,2 m (Residencial/Equipamiento/Actividades productivas); 8,4 m (Infraestructura).
- Antejardín: Vía troncal o colectora 15 m - Otra Jerarquía 10 m (Residencial/Equipamiento/Actividades productivas); 15 m (Infraestructura).
- Densidad máxima: Residencial 60 hab/ha; resto No aplica.
- Altura de cierros: 2,0 m (Residencial/Equipamiento/Actividades productivas); 2,5 m (Infraestructura).

## Zona ZI (Zona Industrial)
**Usos:** No especificado en esta tabla (ver nota general). Nota adicional: esta tabla no trae columna "Residencial" — zona sin uso residencial normado.
**Condiciones:**
- Superficie predial mínima: Equipamiento y Actividades productivas 700 m²; Infraestructura 1750 m².
- Coeficiente de ocupación de suelo (COS): 0,26 (Equipamiento/Actividades productivas); 0,3 (Infraestructura).
- Coeficiente de constructibilidad: 1,3 (Equipamiento); 0,39 (Actividades productivas/Infraestructura).
- Sistema de agrupamiento: Aislado (los tres usos).
- Distanciamiento: 10 m (Equipamiento); 15 m (Actividades productivas/Infraestructura).
- Altura máxima de edificación: 14,4 m (Equipamiento); 13,2 m (Actividades productivas/Infraestructura).
- Antejardín: Vía troncal o colectora 15 m, Vía de Jerarquía inferior 10 m (Equipamiento); 15 m (Actividades productivas/Infraestructura).
- Densidad máxima: No aplica (zona sin uso residencial; la tabla no incluye esta fila).
- Altura de cierros: 2,0 m (Equipamiento); 2,5 m (Actividades productivas/Infraestructura).

## Zona ZE-2 (Zona Especial 2, Equipamiento Comercial)
**Usos:** Equipamiento Comercial (según nombre de la zona en el título de la tabla; esta tabla no trae desglose por Residencial/Equipamiento/Actividades productivas/Infraestructura — valores únicos, sin columnas de uso).
**Condiciones:**
- Superficie predial mínima: 1000 m² (valor único).
- Coeficiente de ocupación de suelo (COS): 0,8.
- Coeficiente de ocupación de suelo 2° nivel: 0,65 (campo adicional propio de esta zona, no presente en las demás).
- Coeficiente de constructibilidad: 2,6.
- Sistema de agrupamiento: Aislado.
- Distanciamiento: No especificado (esta tabla no trae esa fila).
- Altura máxima de edificación: 13,2 m.
- Antejardín: 10 m.
- Densidad máxima: No especificado (esta tabla no trae esa fila).
- Altura de cierros: No especificado (esta tabla no trae esa fila).

---

## Cierre del decreto (pág. 6)

**SEGUNDO:** Procédase a través de la Dirección de Obras Municipales, realizar todos los trámites administrativos pertinentes, con la finalidad que dichas modificaciones entren en vigencia a la brevedad posible.

ANÓTESE, COMUNÍQUESE Y PUBLÍQUESE

Firman: **Carlos Figueroa Vega**, Secretario Municipal (S) — **Javier Muñoz Riquelme**, Alcalde de Curicó. (Ambas firmas manuscritas sobre timbre de la I. Municipalidad de Curicó, ilegibles más allá del nombre impreso bajo cada una).

Distribución: Dirección Control Interno, Dirección Obras Municipales, Transparencia, Archivo Correlativo / Secpla, Depto. Relaciones Públicas, Oficina de Concejales, Archivo Ordenanzas.
