::set PYTHON_DIR=where python
::for /F %%i in ('git rev-parse --short HEAD') do ( set commitid=%%i)
@echo off
::for /F %%i in ('where python') do (set commitid=%%i)
::echo commitid=%commitid%
python rename_clip1.py 
pause
