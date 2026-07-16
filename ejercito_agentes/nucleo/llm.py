"""
Punto ÚNICO de acceso al LLM para los 50 agentes.

Los agentes NO importan directamente desde el orquestador externo: importan
desde aquí. Así, si el nombre real del módulo o de la función cambia, se edita
un solo archivo y no cincuenta.

La ruta de la función se resuelve de forma perezosa (solo en la primera llamada
real) para que importar un agente nunca falle por un módulo aún no disponible.

Configuración por variable de entorno:
    RUTA_PROCESAR_CON_LLM="paquete.modulo:nombre_de_la_funcion"
Valor por defecto: "orquestador:procesar_con_llm"
"""

from __future__ import annotations

import importlib
import os
from typing import Any, Callable

RUTA_POR_DEFECTO = "orquestador:procesar_con_llm"

# Caché de la función ya resuelta.
_funcion_resuelta: Callable[..., Any] | None = None


def _resolver_funcion() -> Callable[..., Any]:
    """Importa y devuelve la función `procesar_con_llm` provista por el entorno."""
    ruta = os.environ.get("RUTA_PROCESAR_CON_LLM", RUTA_POR_DEFECTO)
    nombre_modulo, separador, nombre_funcion = ruta.partition(":")

    if not separador:
        raise ValueError(
            f"RUTA_PROCESAR_CON_LLM mal formada: '{ruta}'. "
            "Formato esperado: 'modulo:funcion'."
        )

    try:
        modulo = importlib.import_module(nombre_modulo)
    except ImportError as error:
        raise ImportError(
            f"No se pudo importar el módulo '{nombre_modulo}' declarado en "
            f"RUTA_PROCESAR_CON_LLM. Ajusta esa variable de entorno al módulo "
            f"real que expone la función del orquestador."
        ) from error

    funcion = getattr(modulo, nombre_funcion, None)
    if funcion is None:
        raise AttributeError(
            f"El módulo '{nombre_modulo}' no expone la función '{nombre_funcion}'."
        )

    return funcion


async def procesar_con_llm(prompt: str) -> str:
    """
    Envoltorio asíncrono sobre la función real del orquestador.

    Se limita a delegar: no captura errores. Cualquier fallo sube hasta el
    agente y de ahí al orquestador, que es el único responsable de registrar
    el texto "Ha Fallado".
    """
    global _funcion_resuelta

    if _funcion_resuelta is None:
        _funcion_resuelta = _resolver_funcion()

    return await _funcion_resuelta(prompt)
