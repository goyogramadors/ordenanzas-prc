# Estado directiva "Grupo CENTRO" — SESION4 — 2026-07-23/24

Progreso de la directiva "PROMPT 2/3 — Grupo CENTRO" (Valparaíso, Viña del
Mar, Quilpué, Rancagua, Curicó). Este archivo existe para continuidad de
sesión — si el contexto se corta, léelo primero.

## Paso 1 (huérfanos propios) — HECHO
Sin huérfanos propios al inicio.

## Paso 2 (verificar 0-parámetros reales en JSON existentes) — HECHO
Confirmado por grep exhaustivo (no muestreo): Valparaíso 39/39, Viña del Mar
90/90, Quilpué 53/53, Rancagua 55/55 zonas con TODOS los campos de
parámetros null. Curicó sin archivo previo.

## Paso 3 (Fase 4 — reclamar y transcribir documentos) — HECHO, todo pusheado y verificado byte-exacto
- **Valparaíso**: nada libre en cola — ya 100% completa (4/4 HECHO, sesiones previas).
- **Viña del Mar**: nada libre en cola — **BLOQUEADA**, no 100% completa: 2 ítems
  EN_PROCESO de SESION3 desde 2026-07-16 (7+ días, huérfanos casi seguros:
  `vina_del_mar_81ae67ab99` y `vina_del_mar_fb27c3b86e`). No los liberé
  (regla vigente: no tocar huérfanos ajenos). Bloquea que Viña del Mar llegue
  al 100% que exige `fase5_cola.py` para procesarla vía el flujo normal.
- **Quilpué**: reclamado `quilpue_17f18a5bc1` (único ítem de toda su cola).
  Transcrito: 53 zonas, Decreto 2732/2019. Pusheado y verificado byte-exacto
  (md + json). Quilpué ahora 100% completa (1/1).
- **Rancagua**: reclamados `rancagua_7ea02082d3` (12 zonas, Decreto 5415/2016)
  y `rancagua_308c1c986d` (60 zonas, Decretos 559+764/2023 — mucho más grande
  de lo anticipado por fase3). Ambos pusheados y verificados byte-exacto.
  Rancagua ahora 100% completa (5/5).
- **Curicó**: nada libre en cola — ya 100% completa (6/6 HECHO, sesiones previas).

## Paso 4 (Fase 5 — JSON + fix bug PERFECCIONAR) — EN CURSO

### Fix del bug PERFECCIONAR — HECHO, pusheado y verificado
`fase5_cola.py` en `ordenanzas-prc` (commit `571fc38`): un JSON "existente" en
`norma-data` ahora se ignora para el filtro EXISTENTE si TODAS sus zonas
tienen los campos numéricos en null (stub de ingesta GeoJSON) — ya no cae
directo a PERFECCIONAR (bucket que ni siquiera se escribe en
`fase5_cola.json`). Afecta a 22 comunas en todo el corpus, no solo estas 5.
Regenerar con: `cd /workspace/ordenanzas-prc && ARCHIBLOCKS_WEB_PUBLIC=/home/user/projectbook/Web/public python3 fase5_cola.py`

### Descubrimiento importante: checkout local de `extraccion_normas/` estaba stale
Muchos `.md` marcados HECHO en `fase4_registro/*.json` no existían en el
disco local (aunque SÍ en remoto) — afectaba a `valparaiso_418...md`,
`curico_93_2011...md`, y los 4 documentos de Viña del Mar. Reparado con
`git checkout origin/master -- extraccion_normas/` (sync completo, decenas
de archivos de otras comunas también recuperados). Si esto vuelve a pasar:
mismo comando.

### JSON Fase 5 generados y VERIFICADOS (subagente independiente comparó cada
uno contra el markdown fuente real y corrigió discrepancias):
- **Valparaíso** (`Web/public/norma-data/05_valparaiso.json`, projectbook):
  39 zonas (28 con parámetros reales). 3 discrepancias corregidas (ZM
  cos_notas, SZPP densidad 900→800, B1 predial 440→480).
- **Curicó** (`Web/public/norma-data/07_curico.json`, projectbook, archivo
  NUEVO): 27 zonas (20 con parámetros reales + 7 sin polígono GeoJSON propio).
  3 discrepancias corregidas (ZE-1 COS, ZE-3 tabla completa era de ZE-4 por
  error, ZE-5 coef.constructibilidad).
- **Viña del Mar** (`Web/public/norma-data/05_vinadelmar.json`, projectbook,
  PARCIAL a propósito): 98 zonas (30 con parámetros reales de 4 de 6
  decretos — faltan los 2 bloqueados por los huérfanos de SESION3). 17 campos
  en 9 zonas corregidos — el hallazgo más grave: **E-12 tenía TODO el bloque
  de edificación contaminado con los valores de E-13** (predial, CC, COS,
  altura, antejardín — todos mal), ya corregido.

### Estado del PUSH de estos 3 JSON a projectbook — EN CURSO AHORA MISMO
Commiteados localmente en projectbook (commit `e29b819` en
`claude/lucid-euler-31rbmt`), pero `git push` está bloqueado en este entorno.
Delegué el push a 3 subagentes en paralelo (usan `mcp__github__push_files` +
verificación byte-exacta + loop de corrección si hace falta):
- Valparaíso: agente `a2d794485f280a884`
- Curicó: agente `a28e2ae4a7209a7e1`
- Viña del Mar (548KB, el más grande, con instrucciones de partir en trozos
  si hace falta): agente `ae9b924ae33c2b2f9`

**SI EL CONTEXTO SE CORTA ANTES DE QUE ESTOS TERMINEN:** revisar si el commit
`e29b819` (o su contenido) ya llegó a
`origin/claude/lucid-euler-31rbmt` en projectbook con:
```
git fetch origin claude/lucid-euler-31rbmt
git diff origin/claude/lucid-euler-31rbmt -- Web/public/norma-data/05_valparaiso.json Web/public/norma-data/07_curico.json Web/public/norma-data/05_vinadelmar.json
```
Si el diff no está vacío para alguno, falta pushear ese archivo (el commit
local ya tiene el contenido correcto, solo falta subirlo).

### Pendiente — NO iniciado todavía
1. **Rancagua Fase 5**: no se ha generado JSON. Situación real: SIN_BASE
   genuino (los 5 documentos de Fase 4 son todos modificaciones sectoriales,
   ninguno es una ordenanza base completa) — no es un falso negativo de
   categoría como Valparaíso/Curicó. Requiere override manual + nota
   transparente explicando que es ficha parcial construida solo de
   modificaciones (~79 zona-menciones entre los 5 documentos, con
   solapamiento entre decretos 5415/2016 y 559-764/2023 sobre las mismas
   zonas — aplicar "gana el más reciente" al consolidar). Reemplazaría el
   stub existente `06_rancagua.json` (55 zonas, hoy 100% null).
2. **Quilpué Fase 5**: no se ha generado JSON. Ahora que Fase 4 está 100%
   completa (1/1) y su documento es categoría ORDENANZA_PRC (caso limpio,
   sin necesidad de override), debería fluir por el flujo normal de
   `fase5_cola.py`/`fase5_registro.py` una vez regenerada la cola.
3. **Regenerar `fase5_cola.json` una vez más** (tras Rancagua y Quilpué) para
   snapshot final del estado de estas 5 comunas — y pushearlo también a
   `ordenanzas-prc` (no se ha pusheado ninguna versión todavía).
4. **Registrar en `fase5_registro/`** (crear manualmente el reclamo si el
   flujo normal de `tomar` no las ofrece por las razones de override) y
   correr `completar` para que quede el reporte de cobertura GeoJSON oficial.
5. **Informe final al usuario** — no entregar hasta que 1-4 estén hechos
   (instrucción explícita: "trabaja en silencio... informe final con el
   estado real, no solo 'existe archivo'").

## Disciplina a mantener
- Byte-exact verify después de CADA push (fetch + show + diff).
- Si hay mismatch: NUNCA reconstruir de memoria — releer el archivo local
  fresco con Read y copiar exacto (lección aprendida esta sesión: un mismatch
  en `rancagua_308c1c986d.json` fue por reconstruir de memoria en vez de
  copiar el archivo recién generado por `completar`).
- Archivos grandes (>100KB): delegar el push a un subagente fresco en vez de
  reintentarlo yo mismo (riesgo de cortar por límite de tokens de salida).
