#!/usr/bin/env bash
set -e

VENV_NAME=venv
cd $(dirname "$0")
cd ..
# Windows venv activation
# In cmd.exe
#$VENV_NAME\Scripts\activate.bat
# In PowerShell
#$VENV_NAME\Scripts\Activate.ps1
# Linux and MacOS venv activation
source $VENV_NAME/bin/activate
python main.py
