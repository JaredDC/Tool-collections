::set PYTHON_DIR=where python
::for /F %%i in ('git rev-parse --short HEAD') do ( set commitid=%%i)
@echo off
::for /F %%i in ('where python') do (set commitid=%%i)
::echo commitid=%commitid%
python rename_clip1.py 
rem delay 3s
ping -n 3 127.0.0.1 > nul