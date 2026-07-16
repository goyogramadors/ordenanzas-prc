@echo off
setlocal
cd /d "%~dp0"
set PYTHONIOENCODING=utf-8

set "PY=%LOCALAPPDATA%\Python\pythoncore-3.14-64\python.exe"
if not exist "%PY%" set "PY=python"

title Bot 06 - PRC
echo ================================================================
echo  BOT 06 de descarga PRC (en paralelo)
echo  Lista:    comunas_lote_06.txt
echo  Registro: registro_06.csv
echo  Puedes cerrar esta ventana y volver a abrir este .bat: continua
echo  donde quedo (segun su propio registro).
echo ================================================================
echo.

"%PY%" descargar_prc.py --lista comunas_lote_06.txt --registro registro_06.csv

echo.
echo BOT 06 termino o se pauso. Revisa registro_06.csv.
pause
endlocal
