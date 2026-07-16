"""
manager_orchestrator.py
=======================
Orquestador del ejército de 50 agentes trabajadores.

Responsabilidades:
  1. Leer `tasks.json`.
  2. Cargar dinámicamente los 50 agentes de la carpeta `agents/`.
  3. Lanzarlos de forma concurrente con un límite explícito de concurrencia.
  4. Aislar los fallos: si un agente cae, se registra "Ha Fallado" y la
     ejecución global CONTINÚA.
  5. Persistir cada resultado en `outputs/` a medida que se completa.

Nota de arquitectura:
    Los archivos de agente se llaman `@agente1sonnet.py`. El carácter `@` NO es
    válido en un identificador de Python, por lo que `import @agente1sonnet` es
    imposible. La carga se hace con `importlib.util.spec_from_file_location`,
    que permite desacoplar el NOMBRE del módulo de la RUTA del archivo.

Uso:
    python manager_orchestrator.py
    python manager_orchestrator.py --concurrencia 20 --reintentos 3
"""

from __future__ import annotations

import argparse
import asyncio
import importlib.util
import json
import logging
import re
import sys
import time
from pathlib import Path
from types import ModuleType
from typing import Any

# ---------------------------------------------------------------------------
# Constantes y rutas
# ---------------------------------------------------------------------------

RAIZ = Path(__file__).resolve().parent
CARPETA_AGENTES = RAIZ / "agents"
CARPETA_SALIDAS = RAIZ / "outputs"
ARCHIVO_TAREAS = RAIZ / "tasks.json"
ARCHIVO_REGISTRO = RAIZ / "orquestador.log"

# Texto EXACTO exigido para cualquier fallo. No modificar.
TEXTO_FALLO = "Ha Fallado"

CONCURRENCIA_POR_DEFECTO = 10
REINTENTOS_POR_DEFECTO = 2
TIEMPO_MAXIMO_POR_TAREA = 120  # segundos
ESPERA_BASE_REINTENTO = 1.5    # segundos (retroceso exponencial)

# Patrón que reconoce los nombres de archivo de los agentes.
PATRON_AGENTE = re.compile(r"^@agente(\d+)sonnet\.py$")

# La raíz debe estar en sys.path para que los agentes puedan hacer
# `from nucleo.llm import procesar_con_llm`.
if str(RAIZ) not in sys.path:
    sys.path.insert(0, str(RAIZ))

registrador = logging.getLogger("orquestador")


# ---------------------------------------------------------------------------
# Configuración de logging
# ---------------------------------------------------------------------------

def configurar_registro(nivel: int = logging.INFO) -> None:
    """Deja los logs en consola y en archivo, ambos en español."""
    formato = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)-18s | %(message)s",
        datefmt="%H:%M:%S",
    )

    consola = logging.StreamHandler(sys.stdout)
    consola.setFormatter(formato)

    archivo = logging.FileHandler(ARCHIVO_REGISTRO, mode="w", encoding="utf-8")
    archivo.setFormatter(formato)

    raiz_log = logging.getLogger()
    raiz_log.setLevel(nivel)
    raiz_log.handlers.clear()
    raiz_log.addHandler(consola)
    raiz_log.addHandler(archivo)


# ---------------------------------------------------------------------------
# Carga de tareas
# ---------------------------------------------------------------------------

def cargar_tareas() -> list[dict[str, Any]]:
    """Lee y valida `tasks.json`."""
    if not ARCHIVO_TAREAS.is_file():
        raise FileNotFoundError(f"No se encontró el archivo de tareas: {ARCHIVO_TAREAS}")

    with ARCHIVO_TAREAS.open(encoding="utf-8") as manejador:
        tareas = json.load(manejador)

    if not isinstance(tareas, list):
        raise ValueError("`tasks.json` debe contener un array de tareas en su raíz.")

    for posicion, tarea in enumerate(tareas):
        if not isinstance(tarea, dict):
            raise ValueError(f"La tarea en la posición {posicion} no es un objeto.")
        for campo in ("id", "agente", "instruccion"):
            if campo not in tarea:
                raise ValueError(
                    f"La tarea en la posición {posicion} carece del campo obligatorio '{campo}'."
                )

    registrador.info("Se cargaron %d tareas desde %s", len(tareas), ARCHIVO_TAREAS.name)
    return tareas


# ---------------------------------------------------------------------------
# Carga dinámica de los agentes
# ---------------------------------------------------------------------------

def cargar_agentes() -> dict[int, ModuleType]:
    """
    Carga por ruta los módulos `agents/@agenteNsonnet.py`.

    Devuelve un diccionario {numero_de_agente: modulo}, ordenado numéricamente
    (no lexicográficamente: el agente 2 va antes que el 10).
    """
    if not CARPETA_AGENTES.is_dir():
        raise FileNotFoundError(
            f"No existe la carpeta de agentes: {CARPETA_AGENTES}. "
            "Ejecuta primero `python generar_agentes.py`."
        )

    agentes: dict[int, ModuleType] = {}

    for ruta in CARPETA_AGENTES.iterdir():
        coincidencia = PATRON_AGENTE.match(ruta.name)
        if coincidencia is None:
            continue

        numero = int(coincidencia.group(1))
        # El nombre del módulo debe ser un identificador válido: se descarta la '@'.
        nombre_modulo = f"agente{numero}sonnet"

        especificacion = importlib.util.spec_from_file_location(nombre_modulo, ruta)
        if especificacion is None or especificacion.loader is None:
            registrador.error("No se pudo preparar la carga de %s", ruta.name)
            continue

        modulo = importlib.util.module_from_spec(especificacion)
        sys.modules[nombre_modulo] = modulo

        try:
            especificacion.loader.exec_module(modulo)
        except Exception as error:  # noqa: BLE001 - un agente roto no debe tumbar la carga
            registrador.error("Fallo al importar %s: %s", ruta.name, error)
            sys.modules.pop(nombre_modulo, None)
            continue

        if not hasattr(modulo, "ejecutar"):
            registrador.error("%s no expone la corrutina `ejecutar`. Se omite.", ruta.name)
            continue

        agentes[numero] = modulo

    agentes_ordenados = dict(sorted(agentes.items()))
    registrador.info("Se cargaron %d agentes desde %s/", len(agentes_ordenados), CARPETA_AGENTES.name)
    return agentes_ordenados


# ---------------------------------------------------------------------------
# Ejecución de una tarea individual
# ---------------------------------------------------------------------------

async def ejecutar_tarea(
    tarea: dict[str, Any],
    agentes: dict[int, ModuleType],
    semaforo: asyncio.Semaphore,
    reintentos: int,
) -> dict[str, Any]:
    """
    Ejecuta UNA tarea con SU agente, bajo el semáforo de concurrencia.

    Esta función NUNCA propaga excepciones hacia arriba: es la frontera de
    aislamiento del sistema. Ante cualquier error devuelve un registro con
    resultado == "Ha Fallado", y el orquestador sigue con el resto.
    """
    id_tarea = tarea["id"]
    numero_agente = tarea["agente"]
    nombre_agente = f"@agente{numero_agente}sonnet"

    registro: dict[str, Any] = {
        "id_tarea": id_tarea,
        "agente": nombre_agente,
        "estado": "PENDIENTE",
        "resultado": None,
        "intentos": 0,
        "error": None,
        "duracion_segundos": 0.0,
    }

    inicio = time.perf_counter()

    async with semaforo:
        modulo = agentes.get(numero_agente)

        # Caso 1: el agente asignado ni siquiera existe.
        if modulo is None:
            registrador.error(
                "Tarea %s: el agente %s no está disponible.", id_tarea, nombre_agente
            )
            registro.update(
                estado="FALLIDO",
                resultado=TEXTO_FALLO,
                error=f"Agente {nombre_agente} no encontrado en la carpeta agents/",
                duracion_segundos=round(time.perf_counter() - inicio, 3),
            )
            return registro

        # Caso 2: el agente existe. Se intenta ejecutar, con reintentos.
        for intento in range(1, reintentos + 1):
            registro["intentos"] = intento
            try:
                registrador.info(
                    "Tarea %s -> %s (intento %d/%d)", id_tarea, nombre_agente, intento, reintentos
                )

                resultado = await asyncio.wait_for(
                    modulo.ejecutar(tarea), timeout=TIEMPO_MAXIMO_POR_TAREA
                )

                registro.update(
                    estado="EXITOSO",
                    resultado=resultado,
                    error=None,
                    duracion_segundos=round(time.perf_counter() - inicio, 3),
                )
                registrador.info(
                    "Tarea %s completada por %s en %.2fs",
                    id_tarea, nombre_agente, registro["duracion_segundos"],
                )
                return registro

            except asyncio.CancelledError:
                # La cancelación es cooperativa: se respeta y se propaga.
                raise

            except asyncio.TimeoutError:
                mensaje = f"Tiempo de espera agotado ({TIEMPO_MAXIMO_POR_TAREA}s)"
                registrador.warning(
                    "Tarea %s: %s en el intento %d.", id_tarea, mensaje, intento
                )
                registro["error"] = mensaje

            except Exception as error:  # noqa: BLE001 - captura deliberadamente amplia
                mensaje = f"{type(error).__name__}: {error}"
                registrador.warning(
                    "Tarea %s: error en el intento %d -> %s", id_tarea, intento, mensaje
                )
                registro["error"] = mensaje

            # Aún quedan intentos: se espera con retroceso exponencial.
            if intento < reintentos:
                espera = ESPERA_BASE_REINTENTO * (2 ** (intento - 1))
                await asyncio.sleep(espera)

    # Agotados todos los intentos.
    registro.update(
        estado="FALLIDO",
        resultado=TEXTO_FALLO,
        duracion_segundos=round(time.perf_counter() - inicio, 3),
    )
    registrador.error(
        "Tarea %s: %s tras %d intentos. Se registra '%s' y se continúa.",
        id_tarea, nombre_agente, registro["intentos"], TEXTO_FALLO,
    )
    return registro


# ---------------------------------------------------------------------------
# Persistencia de resultados
# ---------------------------------------------------------------------------

def guardar_resultado(registro: dict[str, Any]) -> None:
    """Escribe el resultado de una tarea en `outputs/` apenas termina."""
    CARPETA_SALIDAS.mkdir(exist_ok=True)
    ruta = CARPETA_SALIDAS / f"tarea_{registro['id_tarea']:03d}.json"
    ruta.write_text(
        json.dumps(registro, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def guardar_resumen(registros: list[dict[str, Any]], duracion_total: float) -> dict[str, Any]:
    """Escribe `outputs/_resumen.json` con la estadística global de la corrida."""
    exitosos = [r for r in registros if r["estado"] == "EXITOSO"]
    fallidos = [r for r in registros if r["estado"] == "FALLIDO"]

    resumen = {
        "total_tareas": len(registros),
        "exitosas": len(exitosos),
        "fallidas": len(fallidos),
        "duracion_total_segundos": round(duracion_total, 3),
        "ids_fallidos": [r["id_tarea"] for r in fallidos],
    }

    CARPETA_SALIDAS.mkdir(exist_ok=True)
    (CARPETA_SALIDAS / "_resumen.json").write_text(
        json.dumps(resumen, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return resumen


# ---------------------------------------------------------------------------
# Bucle principal
# ---------------------------------------------------------------------------

async def orquestar(concurrencia: int, reintentos: int) -> dict[str, Any]:
    """Lanza todas las tareas en paralelo, con el límite de concurrencia dado."""
    tareas = cargar_tareas()
    agentes = cargar_agentes()

    if not agentes:
        raise RuntimeError("No se cargó ningún agente. Ejecuta `python generar_agentes.py`.")

    semaforo = asyncio.Semaphore(concurrencia)
    registrador.info(
        "Iniciando orquestación | tareas=%d | agentes=%d | concurrencia=%d | reintentos=%d",
        len(tareas), len(agentes), concurrencia, reintentos,
    )

    inicio = time.perf_counter()

    corrutinas = [
        ejecutar_tarea(tarea, agentes, semaforo, reintentos) for tarea in tareas
    ]

    # `return_exceptions=True` es la segunda red de seguridad: aunque
    # `ejecutar_tarea` ya captura todo, una excepción inesperada aquí tampoco
    # detendría al resto del ejército.
    resultados = await asyncio.gather(*corrutinas, return_exceptions=True)

    registros: list[dict[str, Any]] = []

    for tarea, resultado in zip(tareas, resultados):
        if isinstance(resultado, BaseException):
            registrador.error(
                "Excepción no controlada en la tarea %s: %s", tarea["id"], resultado
            )
            registro = {
                "id_tarea": tarea["id"],
                "agente": f"@agente{tarea['agente']}sonnet",
                "estado": "FALLIDO",
                "resultado": TEXTO_FALLO,
                "intentos": 0,
                "error": f"{type(resultado).__name__}: {resultado}",
                "duracion_segundos": 0.0,
            }
        else:
            registro = resultado

        guardar_resultado(registro)
        registros.append(registro)

    duracion_total = time.perf_counter() - inicio
    resumen = guardar_resumen(registros, duracion_total)

    registrador.info(
        "Orquestación finalizada | exitosas=%d | fallidas=%d | tiempo=%.2fs",
        resumen["exitosas"], resumen["fallidas"], resumen["duracion_total_segundos"],
    )
    if resumen["ids_fallidos"]:
        registrador.warning("Tareas con '%s': %s", TEXTO_FALLO, resumen["ids_fallidos"])

    return resumen


def analizar_argumentos() -> argparse.Namespace:
    analizador = argparse.ArgumentParser(
        description="Orquestador del ejército de 50 agentes."
    )
    analizador.add_argument(
        "--concurrencia", type=int, default=CONCURRENCIA_POR_DEFECTO,
        help=f"Agentes trabajando en paralelo (por defecto: {CONCURRENCIA_POR_DEFECTO}).",
    )
    analizador.add_argument(
        "--reintentos", type=int, default=REINTENTOS_POR_DEFECTO,
        help=f"Intentos por tarea antes de darla por fallida (por defecto: {REINTENTOS_POR_DEFECTO}).",
    )
    return analizador.parse_args()


def main() -> int:
    configurar_registro()
    argumentos = analizar_argumentos()

    if argumentos.concurrencia < 1 or argumentos.reintentos < 1:
        registrador.error("`--concurrencia` y `--reintentos` deben ser mayores o iguales a 1.")
        return 2

    try:
        resumen = asyncio.run(
            orquestar(argumentos.concurrencia, argumentos.reintentos)
        )
    except KeyboardInterrupt:
        registrador.warning("Ejecución interrumpida por el usuario.")
        return 130
    except Exception as error:  # noqa: BLE001
        registrador.critical("Fallo fatal del orquestador: %s", error)
        return 1

    # Código de salida distinto de cero si hubo fallos, útil en CI.
    return 0 if resumen["fallidas"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
