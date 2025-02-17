#!/bin/bash

GREEN="\e[32m"
RED="\e[31m"
RESET="\e[0m"

# Handle Ctrl+C (SIGINT) gracefully
trap "echo -e '\n${GREEN}Goodbye!${RESET}'; exit 0" SIGINT

VENV_DIR=".venv"

# Create virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
    echo "Virtual environment created."
fi

# Activate virtual environment
if [ -n "$ZSH_VERSION" ]; then
    source "$VENV_DIR/bin/activate"
elif [ -n "$BASH_VERSION" ]; then
    source "$VENV_DIR/bin/activate"
else
    echo -e "${RED}Unsupported shell. Activate the virtual environment manually.${RESET}"
fi

# Install dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies..."
    python -m pip install --no-cache-dir --disable-pip-version-check -r requirements.txt
fi

while true; do
    clear
    echo -e "${GREEN}==================================${RESET}"
    echo -e "${GREEN}Python Scripts Menu${RESET}"
    echo -e "${GREEN}==================================${RESET}"
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
    echo -e "${GREEN}========================${RESET}"
    echo -ne "${GREEN}Enter your choice (1-11): ${RESET}"
    read choice

    run_script() {
        local script_path="$1"
        if [ -f "$script_path" ]; then
            python3 "$script_path"
        else
            echo -e "${GREEN}Error: $script_path not found!${RESET}"
        fi
        read -p "Press any key to continue..."
    }

    case $choice in
        1) run_script "$(dirname "$0")/Downloaders/Gallery-dl.py" ;;
        2) run_script "$(dirname "$0")/Downloaders/Yt-dlp.py" ;;
        3) run_script "$(dirname "$0")/Encryption/PyGuardian-V1.py" ;;
        4) run_script "$(dirname "$0")/Encryption/PyGuardian-V2.py" ;;
        5) run_script "$(dirname "$0")/Encryption/PyGuardian-V2.1.py" ;;
        6) run_script "$(dirname "$0")/Encryption/PyGuardian-V3.py" ;;
        7) run_script "$(dirname "$0")/File-Tree/Tree.py" ;;
        8) run_script "$(dirname "$0")/FileOpsManager/FileOpsManager.py" ;;  # Fixed typo
        9) run_script "$(dirname "$0")/Image-Converter/Image-Converter.py" ;;
        10) run_script "$(dirname "$0")/PDF-Utils/X-PDF-Script.py" ;;
        11) echo -e "${GREEN}Goodbye!${RESET}"; exit 0 ;;
        *) echo -e "${GREEN}Invalid choice. Please enter a number between 1 and 11.${RESET}" ;;
    esac
done
