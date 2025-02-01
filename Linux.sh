#!/bin/bash

# Change to the script's directory
cd "$(dirname "$0")"

# Virtual environment setup
VENV_DIR="venv"

# Create virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
    echo "Virtual environment created."
fi

# Activate virtual environment
source "$VENV_DIR/bin/activate"

# Install dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies..."
    python -m pip install --no-cache-dir --no-input --disable-pip-version-check -r requirements.txt
fi

# Find Python scripts inside subfolders, excluding venv
scripts=()
while IFS= read -r -d '' script; do
    scripts+=("$script")
done < <(find . -mindepth 2 -type f -name "*.py" ! -path "./$VENV_DIR/*" -print0)

# Check if scripts exist
if [ ${#scripts[@]} -eq 0 ]; then
    echo "No Python scripts found!"
    deactivate
    exit 1
fi

# Display script options
echo "Select a Python script to run:"
for i in "${!scripts[@]}"; do
    echo "$((i+1)). ${scripts[$i]#./}"
done

# Get user choice
read -p "Enter number: " choice
if [[ "$choice" =~ ^[0-9]+$ ]] && (( choice > 0 && choice <= ${#scripts[@]} )); then
    script="${scripts[$((choice-1))]}"
    script_dir="$(dirname "$script")"
    script_name="$(basename "$script")"

    # Run the script inside its folder
    echo "Running: $script_name in $script_dir"
    (cd "$script_dir" && python "$script_name")
else
    echo "Invalid choice!"
    deactivate
    exit 1
fi

# Deactivate virtual environment
deactivate
