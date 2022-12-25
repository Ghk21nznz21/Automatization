@ECHO OFF
cd ./changer_download
call venv/Scripts/activate.bat
python move_files.py
