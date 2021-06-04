@echo off
cd %~dp0

echo webp->png, png->ico
python webp2png.py

echo rename clip1...
python rename_clip1.py 


echo rename mr skin pic_files.
xcopy "mr_skin_renamer.py" "D:\jared\erotic\mr skin\mr_skin_renamer.py"  /y /q /d
cd "D:\jared\erotic\mr skin\"

python mr_skin_renamer.py

rem delay 4s
ping -n 4 127.0.0.1 > nul
