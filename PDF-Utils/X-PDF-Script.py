import subprocess
import os
import sys
from shutil import which
import re

# Configuration
REQUIRED_TOOLS = ['pdftotext', 'pdfimages', 'pdftops', 'pdftopng']
PDF_EXTENSION = '.pdf'
TXT_EXTENSION = '.txt'
PS_EXTENSION = '.ps'

def normalize_path(path):
    """Normalize the input path so it handles slashes correctly on any system."""
    return os.path.abspath(os.path.normpath(path))

def is_tool_installed(tool_name):
    """Check if the external tool is installed."""
    return which(tool_name) is not None

def check_tool_availability():
    """Ensure all required tools are available, or notify the user."""
    missing_tools = [tool for tool in REQUIRED_TOOLS if not is_tool_installed(tool)]
    if missing_tools:
        print(f"Error: The following tools are not installed or not found in PATH: {', '.join(missing_tools)}")
        print("Please install these tools and add them to your PATH before running this script.")
        return False
    return True

def validate_file_path(file_path, expected_extension):
    """Validate that the file path exists and has the correct extension."""
    normalized_path = normalize_path(file_path)
    if not os.path.exists(normalized_path):
        raise FileNotFoundError(f"The file '{normalized_path}' does not exist.")
    if not normalized_path.lower().endswith(expected_extension.lower()):
        raise ValueError(f"The file '{normalized_path}' does not have the expected {expected_extension} extension.")
    return normalized_path

def validate_output_folder(folder_path):
    """Validate and create the output folder if it doesn't exist."""
    normalized_path = normalize_path(folder_path)
    os.makedirs(normalized_path, exist_ok=True)
    return normalized_path

def sanitize_filename(filename):
    """Sanitize the filename to prevent command injection."""
    return re.sub(r'[^a-zA-Z0-9_.-]', '_', filename)

def run_subprocess(command):
    """Run a subprocess command and handle errors."""
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {' '.join(command)}")
        print(f"Error output: {e.stderr}")
        raise

def extract_text(pdf_file, output_txt_file):
    """Extract text from a PDF using Xpdf's 'pdftotext' tool."""
    pdf_file = validate_file_path(pdf_file, PDF_EXTENSION)
    output_txt_file = normalize_path(output_txt_file)
    
    command = ['pdftotext', pdf_file, output_txt_file]
    run_subprocess(command)
    print(f"Text extracted and saved to {output_txt_file}")

def extract_images(pdf_file, output_folder):
    """Extract images from a PDF using Xpdf's 'pdfimages' tool."""
    pdf_file = validate_file_path(pdf_file, PDF_EXTENSION)
    output_folder = validate_output_folder(output_folder)
    
    command = ['pdfimages', '-j', pdf_file, os.path.join(output_folder, 'image')]
    run_subprocess(command)
    print(f"Images extracted and saved to {output_folder}")

def convert_to_ps(pdf_file, output_ps_file):
    """Convert a PDF to PostScript format using Xpdf's 'pdftops' tool."""
    pdf_file = validate_file_path(pdf_file, PDF_EXTENSION)
    output_ps_file = normalize_path(output_ps_file)
    
    command = ['pdftops', pdf_file, output_ps_file]
    run_subprocess(command)
    print(f"PDF converted to PostScript and saved to {output_ps_file}")

def convert_to_png(pdf_file, output_folder):
    """Convert a PDF to PNG using Xpdf's 'pdftopng' tool."""
    pdf_file = validate_file_path(pdf_file, PDF_EXTENSION)
    output_folder = validate_output_folder(output_folder)
    
    output_prefix = os.path.join(output_folder, 'page')
    command = ['pdftopng', pdf_file, output_prefix]
    run_subprocess(command)
    print(f"PDF pages converted to PNG images and saved to {output_folder}")

def get_input(prompt, validator=None):
    """Get user input with optional validation."""
    while True:
        user_input = input(prompt).strip()
        if validator:
            try:
                return validator(user_input)
            except (ValueError, FileNotFoundError) as e:
                print(f"Invalid input: {e}")
        else:
            return user_input

def display_menu():
    """Displays a menu to the user and returns their choice."""
    print("\nPDF Utility Menu:")
    print("1. Extract Text")
    print("2. Extract Images")
    print("3. Convert to PostScript")
    print("4. Convert PDF to PNG")
    print("5. Exit")
    
    return get_input("Enter the number corresponding to the operation you want to perform: ",
                     lambda x: int(x) if 1 <= int(x) <= 5 else ValueError("Please enter a number between 1 and 5."))

def main():
    if not check_tool_availability():
        sys.exit(1)

    while True:
        try:
            choice = display_menu()

            if choice == 1:
                pdf_file = get_input("Enter the path to the PDF file: ", lambda x: validate_file_path(x, PDF_EXTENSION))
                output_txt_file = get_input("Enter the path to save the extracted text file: ", lambda x: normalize_path(x))
                extract_text(pdf_file, output_txt_file)

            elif choice == 2:
                pdf_file = get_input("Enter the path to the PDF file: ", lambda x: validate_file_path(x, PDF_EXTENSION))
                output_folder = get_input("Enter the folder to save extracted images: ", lambda x: validate_output_folder(x))
                extract_images(pdf_file, output_folder)

            elif choice == 3:
                pdf_file = get_input("Enter the path to the PDF file: ", lambda x: validate_file_path(x, PDF_EXTENSION))
                output_ps_file = get_input("Enter the path to save the PostScript file: ", lambda x: normalize_path(x))
                convert_to_ps(pdf_file, output_ps_file)

            elif choice == 4:
                pdf_file = get_input("Enter the path to the PDF file: ", lambda x: validate_file_path(x, PDF_EXTENSION))
                output_folder = get_input("Enter the folder to save PNG files: ", lambda x: validate_output_folder(x))
                convert_to_png(pdf_file, output_folder)

            elif choice == 5:
                print("Exiting the program.")
                break

            input("Press Enter to return to the main menu...")

        except Exception as e:
            print(f"An error occurred: {e}")
            input("Press Enter to return to the main menu...")

if __name__ == '__main__':
    main()