@echo off
setlocal
cd /d "%~dp0"
set PYTHONIOENCODING=utf-8

set "PY=%LOCALAPPDATA%\Python\pythoncore-3.14-64\python.exe"
if not exist "%PY%" set "PY=python"

title Bot 09 - PRC
echo ================================================================
echo  BOT 09 de descarga PRC (en paralelo)
echo  Lista:    comunas_lote_09.txt
echo  Registro: registro_09.csv
echo  Puedes cerrar esta ventana y volver a abrir este .bat: continua
echo  donde quedo (segun su propio registro).
echo ================================================================
echo.

"%PY%" descargar_prc.py --lista comunas_lote_09.txt --registro registro_09.csv

echo.
echo BOT 09 termino o se pauso. Revisa registro_09.csv.
pause
endlocal
