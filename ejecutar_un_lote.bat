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
echo  Bot de descarga - UN SOLO LOTE (10 comunas) y se detiene.
echo  Util si prefieres avanzar de a poco y revisar entre lotes.
echo  Vuelve a hacer doble clic para procesar el siguiente lote.
echo ================================================================
echo.

"%PY%" descargar_prc.py --lista comunas_chile.txt --lotes 1

echo.
pause
endlocal
