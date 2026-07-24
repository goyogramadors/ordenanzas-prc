# Grupo SUR — estado de avance (AMIGO1)

Última actualización: 2026-07-24T00:35Z aprox. Escrito porque el límite de sesión
ya se agotó una vez en este encargo (reset previo 18:30 UTC, luego 00:10 UTC) y
mató agentes en background a mitad de tarea sin guardar nada en disco.

## Ya CERRADO y empujado a git (no requiere repetir)

- **Temuco**: QA hecha. Única zona nula es "AV" (área verde), correctamente
  documentada sin cuadro de edificación en la fuente. Comuna OK, no tocar más.
- **Concepción**: revisado el corpus (`ordenanzas-prc`) — NO existe la ordenanza
  base con las tablas Z-1.x a Z-8.x que cubrirían las 19 zonas "estimadas" del
  JSON actual (`08_concepcion.json`). Solo hay decretos de enmienda menores
  (135, 192, 548) + un ítem huérfano de SESION1 (`concepcion_317e72b863`,
  zonas H1/H3/HE3/etc., no relacionado). No se puede cerrar esta sesión, no hay
  fuente. No reintentar salvo que aparezca nueva fuente en el corpus.
- **Chillán**: Fase 4 avanzada (chillan_71e3392d7a HECHO, 23 zonas, p21-33,
  confianza ALTA) + chillan_b7607186b4 marcado FALLIDO (duplicado exacto).
  PERO Chillán sigue BLOQUEADA para Fase 5 automática: quedan 2 ítems
  EN_PROCESO huérfanos de SESION1 desde 2026-07-16 (`chillan_23f38c9556`,
  `chillan_86dbeb6043`) que nunca se resolvieron — regla de convivencia dice
  no liberarlos yo. Reportar al usuario, no tocar salvo autorización explícita.
  Queda también libre sin reclamar `chillan_bde732cfe9` (PRICH intercomunal
  2005, 25p, no crítico).
- **Talca (Fase 4)**: HECHO. `talca_dfa074e060` (30 zonas, ordenanza base 2011,
  p7-65, confianza ALTA) + 6 documentos de enmienda/modificación ya existían.
  Comuna 100% resuelta en Fase 4 (incluye fix aplicado a `fase5_cola.py` para
  que FALLIDO no bloquee para siempre — ya pusheado a master).
- **Puerto Montt (Fase 4)**: HECHO. `puerto_montt_598c7b39dd` (60 zonas,
  ordenanza refundida 2016, p38-114, confianza ALTA) + `puerto_montt_29f76e45a2`
  marcado FALLIDO (superseded, era la versión 2008 obsoleta) + varios
  documentos de enmienda ya existían. Comuna 100% resuelta en Fase 4.

Todo lo anterior ya está commiteado y pusheado a `origin/master` y
`origin/claude/fase4-transcripcion-amigo1` en el repo `goyogramadors/ordenanzas-prc`.
Verificable con `git log --oneline` desde `/workspace/ordenanzas-prc`.

## EN PROGRESO — esto es lo que se puede perder si se corta la sesión

Reclamadas en Fase 5 (`fase5_registro/puerto_montt.json` y
`fase5_registro/talca.json`, estado EN_PROCESO, sesión AMIGO1, ya pusheadas a
`ordenanzas-prc` master) pero el JSON `NormativaPRC` en sí (que se guarda en
`projectbook/Web/public/norma-data/10_puertomontt.json` y `07_talca.json`)
**todavía NO existe en disco** — dos agentes en background lo están generando.
Si mueren SIN haber escrito el archivo, no se pierde nada salvo tiempo: hay
que volver a lanzar el mismo encargo.

### Cómo relanzar si hace falta (comandos exactos)

```bash
cd /workspace/ordenanzas-prc
export ARCHIBLOCKS_WEB_PUBLIC=/home/user/projectbook/Web/public
python3 fase5_registro.py estado --sesion AMIGO1   # confirmar que siguen EN_PROCESO bajo AMIGO1
ls /home/user/projectbook/Web/public/norma-data/10_puertomontt.json  # si existe, ya está, solo falta completar+push
ls /home/user/projectbook/Web/public/norma-data/07_talca.json
```

Los markdowns fuente de cada comuna (con id, categoría, orden de aplicación
base→enmienda) ya están completos en `fase5_registro/puerto_montt.json` y
`fase5_registro/talca.json` en `ordenanzas-prc` — no hace falta re-derivarlos,
solo releer esos dos JSON de reclamo para tener la lista exacta de markdowns
a fusionar y sus rutas.

Si hay que rehacer el JSON desde cero: usar la skill `ordenanza-a-json`,
cruzar contra `Web/public/geo-data/10_PRC_Puerto_Montt.json` /
`07_PRC_Talca.json`, guardar en `norma-data/`, correr
`fase5_registro.py completar <comuna> --confianza X --nota "..."`, y pushear
el `.json` de `norma-data` a `goyogramadors/projectbook` rama
`claude/geolocalizador-workspace-setup-5u203d` (git push directo o
`mcp__github__push_files` si falla por permisos), y el `fase5_registro/<comuna>.json`
actualizado a `goyogramadors/ordenanzas-prc` (push_files, ambas ramas).

## Pendiente tras cerrar Puerto Montt/Talca Fase 5

- Informe final del Grupo SUR (formato silencioso, ver PROMPT en el mensaje
  original del usuario): Temuco (QA), Concepción (sin fuente), Chillán/Talca/
  Puerto Montt con su estado real.
- Mencionar el bloqueo de Chillán por huérfanos de SESION1 como hallazgo.
- NO correr `consolidar` de fase5 (regla: solo si 0 EN_PROCESO en TODAS las
  sesiones, no verificado).

## Borrar este archivo

Este archivo es solo una nota de trabajo temporal de esta sesión (AMIGO1). Una
vez que el informe final del Grupo SUR quede entregado y Puerto Montt/Talca
queden HECHO en Fase 5, se puede borrar sin problema (no forma parte del
sistema de coordinación real, que vive en fase4_registro/ y fase5_registro/).
