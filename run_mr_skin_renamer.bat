@echo off
xcopy "mr_skin_renamer.py" "D:\jared\erotic\mr skin\mr_skin_renamer.py"  /y /q /d
cd "D:\jared\erotic\mr skin\"
echo Start to rename mr skin pic_files.
python mr_skin_renamer.py

rem delay 4s
ping -n 4 127.0.0.1 > nul
