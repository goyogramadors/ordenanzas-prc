"""
@agente10sonnet
=======================
Agente trabajador autónomo del ejército. Generado por `generar_agentes.py`.
NO editar a mano: los cambios se pierden al regenerar.

Especialidad: redacción técnica

Contrato con el orquestador:
  - Expone la corrutina `ejecutar(tarea) -> str`.
  - Devuelve el texto producido por el LLM.
  - Ante cualquier problema LANZA la excepción. NO la captura ni devuelve
    "Ha Fallado": ese registro es responsabilidad exclusiva del orquestador,
    que además decide los reintentos.
"""

from __future__ import annotations

import logging
from typing import Any

from nucleo.llm import procesar_con_llm

NUMERO_AGENTE = 10
NOMBRE_AGENTE = "@agente10sonnet"
ESPECIALIDAD = "redacción técnica"

registrador = logging.getLogger(NOMBRE_AGENTE)


def construir_prompt(tarea: dict[str, Any]) -> str:
    """Arma el prompt final que se enviará al LLM a partir de la tarea."""
    instruccion = str(tarea.get("instruccion", "")).strip()
    contenido = str(tarea.get("contenido", "")).strip()

    if not instruccion:
        raise ValueError(
            f"{NOMBRE_AGENTE}: la tarea {tarea.get('id')} no trae instrucción."
        )

    partes = [
        f"Eres {NOMBRE_AGENTE}, un agente especializado en {ESPECIALIDAD}.",
        "Responde siempre en español, de forma directa y sin preámbulos.",
        "",
        f"INSTRUCCIÓN: {instruccion}",
    ]

    if contenido:
        partes += ["", "CONTENIDO:", contenido]

    return "\n".join(partes)


async def ejecutar(tarea: dict[str, Any]) -> str:
    """Punto de entrada que invoca el orquestador."""
    id_tarea = tarea.get("id")
    registrador.debug("%s recibió la tarea %s", NOMBRE_AGENTE, id_tarea)

    prompt = construir_prompt(tarea)
    respuesta = await procesar_con_llm(prompt)

    # Una respuesta vacía se considera un fallo: se lanza para que el
    # orquestador reintente y, si insiste, registre "Ha Fallado".
    if respuesta is None or not str(respuesta).strip():
        raise ValueError(
            f"{NOMBRE_AGENTE}: el LLM devolvió una respuesta vacía "
            f"para la tarea {id_tarea}."
        )

    registrador.debug("%s completó la tarea %s", NOMBRE_AGENTE, id_tarea)
    return str(respuesta).strip()
