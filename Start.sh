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
    echo "3. Exit"
    echo -e "${GREEN}==================================${RESET}"
    read -p "${GREEN}Enter your choice (1-3): ${RESET}" choice

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
            exit 0
            ;;
        *)
            echo "${GREEN}Invalid choice. Please enter 1, 2, or 3.${RESET}"
            read -p "Press any key to continue..."
            ;;
    esac
done