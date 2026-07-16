"""
generar_agentes.py
==================
Genera automáticamente la carpeta `agents/` con los 50 archivos de agente
(`@agente1sonnet.py` ... `@agente50sonnet.py`), inyectando en cada uno la
lógica base del trabajador.

También crea el paquete `nucleo/` (punto único de acceso al LLM) si no existe,
de modo que un solo comando deja el proyecto listo para ejecutarse.

Uso:
    python generar_agentes.py                 # crea los que falten
    python generar_agentes.py --forzar        # sobrescribe los existentes
    python generar_agentes.py --cantidad 100  # otro tamaño de ejército
"""

from __future__ import annotations

import argparse
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
CARPETA_AGENTES = RAIZ / "agents"
CARPETA_NUCLEO = RAIZ / "nucleo"

CANTIDAD_POR_DEFECTO = 50

# Especialidad rotativa: da carácter propio a cada agente sin duplicar código.
ESPECIALIDADES = [
    "análisis documental",
    "extracción de datos estructurados",
    "síntesis y resumen",
    "clasificación y etiquetado",
    "redacción técnica",
]

# ---------------------------------------------------------------------------
# Plantilla del trabajador
# ---------------------------------------------------------------------------
# Se usa `str.replace` (no `str.format` ni f-strings) para no tener que escapar
# las llaves de las anotaciones de tipo del propio código generado.

PLANTILLA_AGENTE = '''"""
@agente__NUMERO__sonnet
=======================
Agente trabajador autónomo del ejército. Generado por `generar_agentes.py`.
NO editar a mano: los cambios se pierden al regenerar.

Especialidad: __ESPECIALIDAD__

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

NUMERO_AGENTE = __NUMERO__
NOMBRE_AGENTE = "@agente__NUMERO__sonnet"
ESPECIALIDAD = "__ESPECIALIDAD__"

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

    return "\\n".join(partes)


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
'''


# ---------------------------------------------------------------------------
# Generación
# ---------------------------------------------------------------------------

def generar_agente(numero: int, forzar: bool) -> str:
    """Escribe un archivo de agente. Devuelve el estado: 'creado' u 'omitido'."""
    ruta = CARPETA_AGENTES / f"@agente{numero}sonnet.py"

    if ruta.exists() and not forzar:
        return "omitido"

    especialidad = ESPECIALIDADES[(numero - 1) % len(ESPECIALIDADES)]

    codigo = (
        PLANTILLA_AGENTE
        .replace("__NUMERO__", str(numero))
        .replace("__ESPECIALIDAD__", especialidad)
    )

    ruta.write_text(codigo, encoding="utf-8")
    return "creado"


def asegurar_nucleo() -> None:
    """Crea `nucleo/` con el acceso único al LLM si todavía no existe."""
    CARPETA_NUCLEO.mkdir(exist_ok=True)

    archivo_init = CARPETA_NUCLEO / "__init__.py"
    if not archivo_init.exists():
        archivo_init.write_text(
            '"""Núcleo compartido por los agentes trabajadores."""\n',
            encoding="utf-8",
        )

    archivo_llm = CARPETA_NUCLEO / "llm.py"
    if archivo_llm.exists():
        return

    archivo_llm.write_text(
        '"""Punto único de acceso al LLM para todos los agentes."""\n'
        "\n"
        "from __future__ import annotations\n"
        "\n"
        "import importlib\n"
        "import os\n"
        "from typing import Any, Callable\n"
        "\n"
        'RUTA_POR_DEFECTO = "orquestador:procesar_con_llm"\n'
        "\n"
        "_funcion_resuelta: Callable[..., Any] | None = None\n"
        "\n"
        "\n"
        "def _resolver_funcion() -> Callable[..., Any]:\n"
        '    ruta = os.environ.get("RUTA_PROCESAR_CON_LLM", RUTA_POR_DEFECTO)\n'
        '    nombre_modulo, separador, nombre_funcion = ruta.partition(":")\n'
        "    if not separador:\n"
        '        raise ValueError(f"RUTA_PROCESAR_CON_LLM mal formada: {ruta!r}")\n'
        "    modulo = importlib.import_module(nombre_modulo)\n"
        "    funcion = getattr(modulo, nombre_funcion, None)\n"
        "    if funcion is None:\n"
        "        raise AttributeError(\n"
        '            f"El módulo {nombre_modulo!r} no expone {nombre_funcion!r}."\n'
        "        )\n"
        "    return funcion\n"
        "\n"
        "\n"
        "async def procesar_con_llm(prompt: str) -> str:\n"
        '    """Delega en la función real del orquestador. No captura errores."""\n'
        "    global _funcion_resuelta\n"
        "    if _funcion_resuelta is None:\n"
        "        _funcion_resuelta = _resolver_funcion()\n"
        "    return await _funcion_resuelta(prompt)\n",
        encoding="utf-8",
    )


def analizar_argumentos() -> argparse.Namespace:
    analizador = argparse.ArgumentParser(
        description="Genera los archivos de los agentes trabajadores."
    )
    analizador.add_argument(
        "--cantidad", type=int, default=CANTIDAD_POR_DEFECTO,
        help=f"Número de agentes a generar (por defecto: {CANTIDAD_POR_DEFECTO}).",
    )
    analizador.add_argument(
        "--forzar", action="store_true",
        help="Sobrescribe los archivos de agente que ya existan.",
    )
    return analizador.parse_args()


def main() -> None:
    argumentos = analizar_argumentos()

    if argumentos.cantidad < 1:
        raise SystemExit("La cantidad de agentes debe ser al menos 1.")

    CARPETA_AGENTES.mkdir(exist_ok=True)
    asegurar_nucleo()

    creados = 0
    omitidos = 0

    for numero in range(1, argumentos.cantidad + 1):
        if generar_agente(numero, argumentos.forzar) == "creado":
            creados += 1
        else:
            omitidos += 1

    print(f"Carpeta de agentes: {CARPETA_AGENTES}")
    print(f"Agentes creados:  {creados}")
    print(f"Agentes omitidos: {omitidos} (ya existían; usa --forzar para sobrescribir)")
    print("\nListo. Ahora ejecuta: python manager_orchestrator.py")


if __name__ == "__main__":
    main()
