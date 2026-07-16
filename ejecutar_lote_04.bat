@echo off
setlocal
cd /d "%~dp0"
set PYTHONIOENCODING=utf-8

set "PY=%LOCALAPPDATA%\Python\pythoncore-3.14-64\python.exe"
if not exist "%PY%" set "PY=python"

title Bot 04 - PRC
echo ================================================================
echo  BOT 04 de descarga PRC (en paralelo)
echo  Lista:    comunas_lote_04.txt
echo  Registro: registro_04.csv
echo  Puedes cerrar esta ventana y volver a abrir este .bat: continua
echo  donde quedo (segun su propio registro).
echo ================================================================
echo.

"%PY%" descargar_prc.py --lista comunas_lote_04.txt --registro registro_04.csv

echo.
echo BOT 04 termino o se pauso. Revisa registro_04.csv.
pause
endlocal
