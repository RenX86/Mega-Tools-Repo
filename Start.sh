#!/bin/bash

GREEN="\e[32m"
RESET="\e[0m"

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

    case $choice in
        1)
            cd "$(dirname "$0")/Downloaders" 2>/dev/null
            python Gallery-dl.py
            read -p "Press any key to continue..."
            ;;
        2)
            cd "$(dirname "$0")/Downloaders" 2>/dev/null
            python Yt-dlp.py
            read -p "Press any key to continue..."
            ;;

        3)
            cd "$(dirname "$0")/Encryption" 2>/dev/null
            python PyGuardian-V1.py
            read -p "Press any key to continue..."
            ;;
        4)
            cd "$(dirname "$0")/Encryption" 2>/dev/null
            python PyGuardian-V2.py
            read -p "Press any key to continue..."
            ;;
        
        5)
            cd "$(dirname "$0")/Encryption" 2>/dev/null
            python PyGuardian-V2.1.py
            read -p "Press any key to continue..."
            ;;

        6)
            cd "$(dirname "$0")/Encryption" 2>/dev/null
            python PyGuardian-V3.py
            read -p "Press any key to continue..."
            ;;

        7)
            cd "$(dirname "$0")/File-Tree" 2>/dev/null
            python Tree.py
            read -p "Press any key to continue..."
            ;;

        8)
            cd "$(dirname "$0")/FileOpsManager" 2>/dev/null
            python FileOpsManger.py
            read -p "Press any key to continue..."
            ;;

        9)
            cd "$(dirname "$0")/Image-Converter" 2>/dev/null
            python Image-Converter.py
            read -p "Press any key to continue..."
            ;;

        10)
            cd "$(dirname "$0")/PDF-Utils" 2>/dev/null
            python X-PDF-Script.py
            read -p "Press any key to continue..."
            ;;

        11)
            exit 0
            ;;
        *)
            echo "${GREEN}Invalid choice. Please enter 1, 2, or 3.${RESET}"
            read -p "Press any key to continue..."
            ;;
    esac
done