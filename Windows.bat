@echo off
setlocal enabledelayedexpansion

echo ==============================================
echo           Available Tools Menu
echo ==============================================

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed or not in the system PATH.
    echo Please install Python and add it to your system PATH.
    echo You can download Python at https://www.python.org/downloads/
    pause
    exit /b
)

:: Change to the script's directory
cd /d "%~dp0"

:: Virtual environment setup
set VENV_DIR=.venv

:: Check if virtual environment exists
if not exist "%VENV_DIR%" (
    echo Creating virtual environment...
    python -m venv "%VENV_DIR%"
    echo Virtual environment created.
)

:: Activate virtual environment
call "%VENV_DIR%\Scripts\activate.bat"

:: Install dependencies if requirements.txt exists
if exist "requirements.txt" (
    echo Installing dependencies wait it takes time...
    python -m pip install --no-cache-dir --no-input --disable-pip-version-check -r requirements.txt > install.log 2>&1
)

:: Get list of Python scripts (excluding venv)
set count=0
for /r %%f in (*.py) do (
    echo %%f | findstr /V /C:"%VENV_DIR%" >nul && (
        set /a count+=1
        set "script!count!=%%~nxf"
        set "script_path!count!=%%~dpf"
        echo !count!. %%~nxf
    )
)

:: Check if scripts exist
if %count%==0 (
    echo No Python scripts found!
    call "%VENV_DIR%\Scripts\deactivate.bat"
    pause
    exit /b
)

:: Ask user to choose a script
set /p choice=Enter number: 
if not defined script%choice% (
    echo Invalid choice!
    call "%VENV_DIR%\Scripts\deactivate.bat"
    pause
    exit /b
)

:: Get selected script and its path
set "selected=!script%choice%!"
set "selected_path=!script_path%choice%!"

:: Run the script in its corresponding folder
echo Running: %selected% in %selected_path%
cd /d "%selected_path%"
python "%selected%"

:: Deactivate virtual environment
call "%~dp0%VENV_DIR%\Scripts\deactivate.bat"

pause
