@echo off
git pull origin main 
pip install -r requirements.txt 
python hello.py
python qrgen.py
pause
