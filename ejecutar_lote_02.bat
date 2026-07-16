@echo off
setlocal
cd /d "%~dp0"
set PYTHONIOENCODING=utf-8

set "PY=%LOCALAPPDATA%\Python\pythoncore-3.14-64\python.exe"
if not exist "%PY%" set "PY=python"

title Bot 02 - PRC
echo ================================================================
echo  BOT 02 de descarga PRC (en paralelo)
echo  Lista:    comunas_lote_02.txt
echo  Registro: registro_02.csv
echo  Puedes cerrar esta ventana y volver a abrir este .bat: continua
echo  donde quedo (segun su propio registro).
echo ================================================================
echo.

"%PY%" descargar_prc.py --lista comunas_lote_02.txt --registro registro_02.csv

echo.
echo BOT 02 termino o se pauso. Revisa registro_02.csv.
pause
endlocal
