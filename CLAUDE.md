# CLAUDE.md — ordenanzas-prc-chile

> **Idioma:** responde en español de Chile (tú, no vos/vosotros).

## Qué es este repo

Material de trabajo/respaldo para producir las fichas normativas (`NormativaPRC`)
del geolocalizador de Archibots. **No es la app** — la app y el resultado final
(JSON en `Web/public/norma-data`) viven en el repo `projectbook`
(`https://github.com/goyogramadors/projectbook`).

Lee primero **README.md** (alcance completo y requisito de workspace).

## Workspace requerido

Este repo debe convivir como carpeta **hermana** de tu clon de `projectbook`
(mismo directorio padre):

```
tu-carpeta-de-trabajo/
├── projectbook/           <- Web/public/norma-data, Web/public/geo-data
└── ordenanzas-prc-chile/  <- este repo (PDFs, extraccion_normas, scripts)
```

Si tu clon de `projectbook` tiene otro nombre o ruta, exporta `ARCHIBLOCKS_WEB_PUBLIC`
apuntando a su `Web/public` antes de correr los scripts de Fase 5 (ver README.md).

## Cómo continuar el trabajo

- **Fase 4** (transcribir tablas de norma PDF → Markdown en `extraccion_normas/`):
  abre `PROMPT_FASE4_SESION.md` y sigue las instrucciones tal cual — trae su
  propio sistema de coordinación (`fase4_registro.py` / `fase4_cola.json`).
- **Fase 5** (generar el JSON `NormativaPRC` final por comuna): abre
  `PROMPT_FASE5_SESION.md`. **Primer paso obligatorio de esa fase:** invoca la
  skill `ordenanza-a-json` (ya está en `.claude/skills/` de este repo) — es la
  autoridad sobre el esquema, los enums y las reglas de normalización.
- Ambas fases usan colas compartidas (`fase*_cola.json` + carpeta
  `fase*_registro/`) para que varias sesiones trabajen en paralelo sin pisarse.
  Reemplaza `<SESION>` por tu identificador tal como indica cada prompt.

## Convenciones

- Ambos `PROMPT_FASE*_SESION.md` piden **trabajar en silencio**: solo reportas
  resultados (línea de arranque, línea por comuna terminada, informe final),
  nunca narras el proceso ni vuelcas el contenido de las fichas en el chat.
- No inventes valores de norma ni de enum: si el dato no está en el Markdown/PDF
  fuente, va `null` con una nota explicando por qué.
