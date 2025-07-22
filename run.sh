#!/bin/bash

# Detect platform
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "Running on Windows CMD"
    cmd.exe /c run.bat
else
    echo "Running on Linux/Termux"
    # Replace this with your actual Unix commands
    chmod +x script.sh
    ./script.sh
fi
