@echo off

REM randompy.bat

if "%~1"=="" (
    echo Usage: js ^<filename.js^>
    exit /b 1
)

python main.py %1