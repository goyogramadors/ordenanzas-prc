@echo off
setlocal
cd /d "%~dp0"

echo ================================================================
echo  Lanzando 10 bots en PARALELO (una ventana por bot).
echo  OJO: son 10 navegadores headless a la vez; usa harta CPU/RAM.
echo  Si el equipo se pone lento, cierra algunas ventanas: cada bot
echo  guarda su avance y puede reanudarse solo.
echo ================================================================
echo.
pause

start "Bot 01" cmd /c ejecutar_lote_01.bat
start "Bot 02" cmd /c ejecutar_lote_02.bat
start "Bot 03" cmd /c ejecutar_lote_03.bat
start "Bot 04" cmd /c ejecutar_lote_04.bat
start "Bot 05" cmd /c ejecutar_lote_05.bat
start "Bot 06" cmd /c ejecutar_lote_06.bat
start "Bot 07" cmd /c ejecutar_lote_07.bat
start "Bot 08" cmd /c ejecutar_lote_08.bat
start "Bot 09" cmd /c ejecutar_lote_09.bat
start "Bot 10" cmd /c ejecutar_lote_10.bat

echo Se abrieron las ventanas de los bots. Puedes cerrar ESTA ventana.
endlocal
