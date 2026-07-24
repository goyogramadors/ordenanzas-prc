# Estado directiva "Grupo CENTRO" — SESION4 — 2026-07-24, ACTUALIZADO tras corte por límite de sesión

⚠️ **LEE ESTA SECCIÓN PRIMERO.** A las ~01:00 UTC del 24-jul se agotó el
límite de sesión de la API (mensaje: "You've hit your session limit · resets
5:10am (UTC)") mientras 5 subagentes en paralelo hacían push de archivos
grandes a `projectbook`. Diagnóstico exacto de cada uno (verificado con
`git diff --stat origin/... -- <archivo>` y validación de contenido):

| Archivo | Estado en remoto (`claude/lucid-euler-31rbmt` en projectbook) | Acción pendiente |
|---|---|---|
| `05_valparaiso.json` | Seguro — quedó el STUB VIEJO (39 zonas, todo null). El push nunca llegó a completar el intercambio. NO corrupto. | Repushear el contenido correcto (ya commiteado local en `e29b819`/`d3192d9`, verificado, 39 zonas/28 reales) |
| `07_curico.json` | Seguro — el archivo NO EXISTE en remoto todavía (el push nunca llegó a ejecutarse). | Pushear por primera vez (contenido ya commiteado local, verificado, 27 zonas/20 reales) |
| `05_quilpue.json` | Seguro — quedó el STUB VIEJO (53 zonas, todo null). NO corrupto. | Repushear el contenido correcto (ya commiteado local en `d3192d9`, verificado, 53 zonas/53 reales) |
| `05_vinadelmar.json` | **⚠️ ROTO — el subagente pusheó un JSON válido pero truncado a SOLO 3 ZONAS** (en vez de 98) antes de fallar por el límite de sesión. El propio agente reportó en su último mensaje: "Cometí errores de transcripción en los últimos dos intentos (contenido placeholder en vez del real)". | **PRIORITARIO: repushear el contenido completo y correcto** (ya commiteado local en `e29b819`, verificado por agente de verificación `ac118077` antes de todo esto, 98 zonas/30 reales). El archivo local en `/home/user/projectbook/Web/public/norma-data/05_vinadelmar.json` SIGUE INTACTO Y CORRECTO — el problema es solo lo que quedó en GitHub. |
| `fase5_cola.json` (ordenanzas-prc) | ✅ Pusheado y verificado byte-exacto ANTES del corte (commit `46965f4`). Sin problema. |  |
| `fase5_cola.py` (ordenanzas-prc, fix bug PERFECCIONAR) | ✅ Pusheado y verificado byte-exacto ANTES del corte (commit `571fc38`). Sin problema. |  |

**Rancagua Fase 5**: el agente `a585a047842bb3d39` (override SIN_BASE) fue
interrumpido por el límite de sesión mientras validaba. Su último mensaje:
"El archivo final se escribió con 61 zonas (55 del GeoJSON + 6
suplementarias). Ahora valido exhaustivamente." — es decir, el archivo LOCAL
`/home/user/projectbook/Web/public/norma-data/06_rancagua.json` PROBABLEMENTE
se sobrescribió con contenido nuevo, pero **NO fue revisado por mí ni por
ningún verificador independiente todavía** — no confiar en él sin antes
leerlo completo y contrastarlo contra los 5 markdown fuente
(`extraccion_normas/rancagua/*.md`) tal como se hizo con Valparaíso/Curicó/
Viña del Mar. No se commiteó ni se pusheó — sigue solo en disco local.

**LECCIÓN — causa raíz de la corrupción de Viña del Mar**: un subagente
delegado, al quedarse sin cuota de API a mitad de una operación de
"leer en partes + reconstruir + pushear" de un archivo de 548KB, dejó el
push A MEDIO HACER (con contenido parcial/placeholder) en vez de no pushear
nada. Para archivos grandes, preferir: (a) UN SOLO push con el contenido
completo verificado por diff/md5 ANTES de tocar el remoto (como hizo
correctamente el agente de `fase5_cola.json`), nunca "pushear parcial y
completar después"; (b) si un agente reporta haber cometido "errores de
transcripción" y haber pusheado igual, verificar el remoto INMEDIATAMENTE
después con `git diff --stat origin/... -- <archivo>`, no asumir que un
`status: failed` significa "no llegó a tocar nada".

---

# Contenido original (antes del corte) — sigue vigente salvo lo de arriba

Progreso de la directiva "PROMPT 2/3 — Grupo CENTRO" (Valparaíso, Viña del
Mar, Quilpué, Rancagua, Curicó). Este archivo existe para continuidad de
sesión — si el contexto se corta, léelo primero.

## Paso 1 (huérfanos propios) — HECHO
## Paso 2 (verificar 0-parámetros reales en JSON existentes) — HECHO

## Paso 3 (Fase 4) — HECHO, todo pusheado y verificado byte-exacto en ordenanzas-prc
- Valparaíso: ya 100% completa (4/4 HECHO, sesiones previas), sin cambios.
- Viña del Mar: **BLOQUEADA** en Fase4 — 2 EN_PROCESO de SESION3 desde
  2026-07-16 (7+ días, huérfanos casi seguros: `vina_del_mar_81ae67ab99` y
  `vina_del_mar_fb27c3b86e`). No liberados (regla: no tocar huérfanos ajenos).
- Quilpué: `quilpue_17f18a5bc1` completado (53 zonas, Decreto 2732/2019).
  Ahora 100% completa (1/1).
- Rancagua: `rancagua_7ea02082d3` (12 zonas) y `rancagua_308c1c986d` (60
  zonas) completados. Ahora 100% completa (5/5).
- Curicó: ya 100% completa (6/6 HECHO, sesiones previas), sin cambios.

## Paso 4 (Fase 5) — EN CURSO, ver tabla de arriba para qué falta pushear

### Fix bug PERFECCIONAR — HECHO y pusheado (commit `571fc38` en ordenanzas-prc)
Afecta a 22 comunas del corpus completo. Regenerar cola:
`cd /workspace/ordenanzas-prc && ARCHIBLOCKS_WEB_PUBLIC=/home/user/projectbook/Web/public python3 fase5_cola.py`

### Con el fix aplicado, ubicación real de las 5 comunas en la cola:
- **Quilpué**: PROCESAR, tier "ciudad grande", categoría ORDENANZA_PRC (caso
  limpio, sin necesidad de override) → `05_quilpue.json`.
- **Rancagua**: SIN_BASE genuino (los 5 documentos de Fase4 son todos
  modificaciones sectoriales, ninguno es ordenanza base completa) — requiere
  override manual, ficha parcial con nota transparente.
- Valparaíso, Viña del Mar, Curicó: ya no caen en PERFECCIONAR automático
  gracias al fix (eran stubs 100% null), pero Viña del Mar sigue sin aparecer
  en ningún bucket por el bloqueo de Fase4 del punto anterior.

### JSON Fase 5 generados y VERIFICADOS por subagente independiente (comparó
contra el markdown fuente real, corrigió discrepancias) — **contenido
CORRECTO, el problema es solo que 3 de 4 no llegaron a GitHub, ver tabla
de arriba**:
- Valparaíso: 39 zonas (28 reales). 3 discrepancias corregidas.
- Curicó: 27 zonas (20 reales + 7 sin polígono propio). 3 discrepancias corregidas.
- Viña del Mar: 98 zonas (30 reales, parcial — 2 decretos pendientes por
  huérfanos). 17 campos en 9 zonas corregidos (hallazgo grave: E-12 tenía
  todo el bloque de edificación contaminado con valores de E-13, ya
  corregido).
- Quilpué: 53 zonas (53 reales, 100% cobertura predial/altura). Sin
  discrepancias encontradas en spot-check manual mío. Ya pusheado y
  verificado byte-exacto ANTES del corte — sin problema.

### Pendiente
1. Repushear Valparaíso, Curicó, Viña del Mar (ver tabla de arriba — Viña del
   Mar es urgente por estar rota en remoto).
2. Revisar el archivo local de Rancagua (61 zonas, sin verificar) antes de
   commitear/pushear — leerlo completo y contrastar contra
   `extraccion_normas/rancagua/*.md` (5 documentos).
3. Regenerar `fase5_cola.json` una vez más tras Rancagua+Quilpué confirmados
   en remoto, pushear a ordenanzas-prc.
4. Registrar en `fase5_registro/` (crear reclamo manual si `tomar` no las
   ofrece por las razones de override) y correr `completar` para el reporte
   de cobertura GeoJSON oficial.
5. Informe final al usuario — no entregar hasta 1-4 hechos.

## Disciplina a mantener
- Byte-exact verify después de CADA push (fetch + show + diff) — SIEMPRE,
  incluso si el status de un push dice "completed" o si un agente reporta
  éxito. Confirmado esta sesión: un agente puede fallar a mitad de camino y
  dejar contenido parcial pusheado sin que sea obvio desde el resumen.
- Si hay mismatch: NUNCA reconstruir de memoria — releer el archivo local
  fresco con Read y copiar exacto.
- Archivos grandes (>100KB): un solo push con contenido pre-verificado por
  diff/md5 LOCAL antes de tocar el remoto — no "pushear en partes e ir
  completando", eso es lo que salió mal con Viña del Mar.
- Si un subagente delegado para pushear reporta `status: failed` por límite
  de sesión, SIEMPRE verificar el remoto con `git diff --stat` antes de
  asumir que no tocó nada.
