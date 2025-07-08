@echo off
git pull origin main #repo updating in terminal
pip install -r requirements.txt #installing modules
python hello.py
python qrgen.py
pause
