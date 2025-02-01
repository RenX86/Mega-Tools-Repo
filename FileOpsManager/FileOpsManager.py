import subprocess
import os
import argparse

def hide_folder(folder_name):
    if not os.path.exists(folder_name):
        print(f"Error: The folder '{folder_name}' does not exist.")
        return
    command = f'attrib +h +s +r "{folder_name}"'
    run_command(command, "hidden", folder_name)

def show_folder(folder_name):
    if not os.path.exists(folder_name):
        print(f"Error: The folder '{folder_name}' does not exist.")
        return
    command = f'attrib -h -s -r "{folder_name}"'
    run_command(command, "revealed", folder_name)

def blend_files(image_file, zip_file, output_file=None):
    if not (os.path.isfile(image_file) and os.path.isfile(zip_file)):
        print("Error: Both files must exist.")
        return
    output_file = output_file or image_file  # Default output name is the image file
    command = f'copy /b "{image_file}"+"{zip_file}" "{output_file}"'
    run_command(command, "blended", f"{image_file} and {zip_file}")

def run_command(command, action, target):
    try:
        result = subprocess.run(command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"Successfully {action}: {target}")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error while trying to {action} {target}")
        print(f"Error message: {e.stderr}")

def interactive_mode():
    print("Welcome to the File Manipulator!")
    print("This script can hide/show folders and blend files.")
    print("Type 'q' to exit the program.")

    while True:
        alias = input("Enter the command ('h', 's', 'b', or 'q' to exit): ").strip("\\'").lower()
        if alias == 'q':
            print("Exiting the program. Goodbye!")
            break
        elif alias == 'h':
            folder_name = input("Enter the folder name or path to hide: ").strip("\\'")
            hide_folder(folder_name)
        elif alias == 's':
            folder_name = input("Enter the folder name or path to show: ").strip("\\'")
            show_folder(folder_name)
        elif alias == 'b':
            image_file = input("Enter the path of the image file: ").strip("\\'")
            zip_file = input("Enter the path of the zip file: ").strip("\\'")
            output_file = input("Enter the output file name (or press Enter to overwrite the image file): ").strip("\\'") or None
            blend_files(image_file, zip_file, output_file)
        else:
            print(f"'{alias}' is not recognized. Please use 'h', 's', or 'b'.")

def main():
    parser = argparse.ArgumentParser(description="File Manipulation Tool")
    parser.add_argument('--hide', help='Hide a folder', type=str)
    parser.add_argument('--show', help='Show a folder', type=str)
    parser.add_argument('--blend', help='Blend an image file and a zip file', nargs=2)
    parser.add_argument('--output', help='Output file name for blended files', type=str)

    args = parser.parse_args()

    # If no arguments are passed, enter interactive mode
    if args.hide:
        hide_folder(args.hide)
    elif args.show:
        show_folder(args.show)
    elif args.blend:
        blend_files(args.blend[0], args.blend[1], args.output)
    else:
        interactive_mode()

if __name__ == "__main__":
    main()
