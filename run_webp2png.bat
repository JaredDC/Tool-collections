@echo off
REM %~dp0 batch file 's drive+path
REM %~d0  batch file 's drive
REM %0    batch file itself


cd %~dp0
::start python webp2png.py
python webp2png.py

rem delay 3s
ping -n 3 127.0.0.1 > nul
