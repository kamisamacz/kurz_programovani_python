@echo off
SET PYTHON_PATH=C:\Users\kamisamacz\AppData\Local\Programs\Python\Python312\python.exe
SET SCRIPT_PATH=%~dp0main.py

start cmd /k "%PYTHON_PATH% %SCRIPT_PATH%"
start position_script.ahk
