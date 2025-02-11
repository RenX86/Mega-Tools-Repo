@echo off
color 0A
:menu
cls
echo ==================================
echo Python Scripts Downloader Menu
echo ==================================
echo "1. Run Gallery-dl (Image Downloader)"
echo "2. Run Yt-dlp (Video Downloader)"
echo "3. Run PyGuardian-V1 (Encryption)"
echo "4. Run PyGuardian-V2 (Encryption)"
echo "5. Run PyGuardian-V2.1 (Encryption)"
echo "6. Run PyGuardian-V3 (Encryption)"
echo "7. Run Tree (File Tree)"
echo "8. Run FileOpsManager (File Operations Manager)"
echo "9. Run Image-Converter (Image Converter)"
echo "10. Run X-PDF-Script (PDF Utils)"
echo "11. Exit"
echo ==================================
set /p choice=Enter your choice (1-11): 

if "%choice%" == "1" (
    cd /d "%~dp0Downloaders"
    python Gallery-dl.py
    pause
    goto :menu
)

if "%choice%" == "2" (
    cd /d "%~dp0Downloaders"
    python Yt-dlp.py
    pause
    goto :menu
)

if "%choice%" == "3" (
    cd /d "%~dp0Encryption"
    python PyGuardian-V1.py
    pause
    goto :menu
)

if "%choice%" == "4" (
    cd /d "%~dp0Encryption"
    python PyGuardian-V2.py
    pause
    goto :menu
)
if "%choice%" == "5" (
    cd /d "%~dp0Encryption"
    python PyGuardian-V2.1.py
    pause
    goto :menu
)

if "%choice%" == "6" (
    cd /d "%~dp0Encryption"
    python PyGuardian-V3.py
    pause
    goto :menu
)

if "%choice%" == "7" (
    cd /d "%~dp0File-Tree"
    python Tree.py
    pause
    goto :menu
)

if "%choice%" == "8" (
    cd /d "%~dp0FileOpsManager"
    python Image-Converter.py
    pause
    goto :menu
)

if "%choice%" == "9" (
    cd /d "%~dp0Image-Converter"
    python Image-Converter.py
    pause
    goto :menu
)

if "%choice%" == "10" (
    cd /d "%~dp0PDF-Utils"
    python X-PDF-Script.py
    pause
    goto :menu
)

if "%choice%" == "11" (
    exit /b
)

goto :menu