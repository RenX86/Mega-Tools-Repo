#!/bin/bash

GREEN="\e[32m"
RESET="\e[0m"

# Handle Ctrl+C (SIGINT) gracefully
trap "echo -e '\n${GREEN}Exiting...${RESET}'; exit 0" SIGINT

while true; do
    clear
    echo -e "${GREEN}==================================${RESET}"
    echo -e "${GREEN}Python Scripts Downloader Menu${RESET}"
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
    echo -e "${GREEN}==================================${RESET}"
    read -p "${GREEN}Enter your choice (1-11): ${RESET}" choice

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
