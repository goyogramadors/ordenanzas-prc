@echo off
setlocal
cd /d "%~dp0"
set PYTHONIOENCODING=utf-8
set "PY=%LOCALAPPDATA%\Python\pythoncore-3.14-64\python.exe"
if not exist "%PY%" set "PY=python"

echo ================================================================
echo  Limpiador: elimina PDFs de "Certificado de Informes/Informaciones
echo  Previas" (CIP) que se hayan colado en la carpeta descargas.
echo  Primero muestra que borraria; luego pregunta antes de eliminar.
echo ================================================================
echo.
echo --- Vista previa (no borra nada todavia) ---
"%PY%" limpiar_certificados.py --dry-run
echo.
set /p RESP="Escribe SI para eliminarlos de verdad, o cierra esta ventana: "
if /I "%RESP%"=="SI" (
    "%PY%" limpiar_certificados.py
) else (
    echo No se borro nada.
)
echo.
pause
endlocal
