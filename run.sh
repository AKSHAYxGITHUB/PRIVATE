#!/usr/bin/env bash

# Detect platform
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "Running on Windows CMD"
    cmd.exe /c run.bat
else
    echo "Running on Termux/Linux"
    git pull origin main
    pip install -r requirements.txt
    python main.py
fi

