@echo off
setlocal
cd /d "%~dp0"
set PYTHONIOENCODING=utf-8

rem Windows suele tener un "python" que solo es un alias de la Microsoft
rem Store (no un interprete real). Usamos la instalacion real donde se
rem instalo Playwright; si no existe (otro equipo, reinstalo Python),
rem caemos de vuelta al "python" generico del PATH.
set "PY=%LOCALAPPDATA%\Python\pythoncore-3.14-64\python.exe"
if not exist "%PY%" set "PY=python"

"%PY%" -c "import playwright" >nul 2>nul
if errorlevel 1 (
    echo ================================================================
    echo  ERROR: no se encontro el paquete "playwright" para:
    echo    %PY%
    echo.
    echo  Instalalo con estos comandos y luego vuelve a hacer doble
    echo  clic en este archivo:
    echo    "%PY%" -m pip install playwright
    echo    "%PY%" -m playwright install chromium
    echo ================================================================
    pause
    exit /b 1
)

echo ================================================================
echo  Bot de descarga - Ordenanzas del Plan Regulador Comunal
echo  Lista: comunas_chile.txt (RM, luego Valparaiso, luego el resto)
echo  Procesa en lotes de 10, registrando el avance en:
echo    registro_progreso.csv
echo  Si se interrumpe (se cierra esta ventana, se corta la luz, etc.)
echo  puedes volver a hacer doble clic aqui: continua donde quedo.
echo ================================================================
echo.

"%PY%" descargar_prc.py --lista comunas_chile.txt

echo.
echo ================================================================
echo  Proceso terminado o pausado.
echo  Revisa registro_progreso.csv para ver el avance.
echo  Los PDF quedan en la carpeta "descargas".
echo ================================================================
pause
endlocal
