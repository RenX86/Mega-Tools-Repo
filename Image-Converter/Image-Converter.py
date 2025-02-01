import subprocess
import os
from pathlib import Path
from typing import Tuple, Optional

SUPPORTED_FORMATS = ['png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff','webp']
DEFAULT_QUALITY = 100  # Default quality setting

def convert_image(input_path: Path, output_format: str, quality: int = DEFAULT_QUALITY, output_dir: Optional[Path] = None) -> Optional[Path]:
    """
    Converts an image to the specified format using ImageMagick CLI.
    
    :param input_path: Path to the input image file.
    :param output_format: The desired output image format (e.g., 'png', 'jpg').
    :param quality: Image quality (0-100, default 85). Only applies to lossy formats like JPEG.
    :param output_dir: Optional directory for the output file. If None, uses the input file's directory.
    :return: The path to the converted image, or None if conversion failed.
    """
    if not input_path.is_file():
        raise FileNotFoundError(f"The file {input_path} does not exist.")
    
    if output_format not in SUPPORTED_FORMATS:
        raise ValueError(f"Unsupported format: {output_format}. Supported formats are: {', '.join(SUPPORTED_FORMATS)}")

    if not 0 <= quality <= 100:
        raise ValueError("Quality must be between 0 and 100.")

    output_dir = output_dir or input_path.parent
    output_path = output_dir / f"{input_path.stem}.{output_format}"

    # Add quality parameter to the command
    convert_cmd = ["magick", str(input_path), "-quality", str(quality), str(output_path)]

    try:
        subprocess.run(convert_cmd, check=True, capture_output=True, text=True)
        print(f"Image converted successfully: {output_path}")
        return output_path
    except subprocess.CalledProcessError as e:
        print(f"Error converting image: {e}")
        print(f"Command output: {e.output}")
        return None

def get_user_input() -> Tuple[Optional[Path], Optional[str], Optional[int], Optional[Path]]:
    """
    Prompts the user for the image path, output format, quality, and optional output directory.
    
    :return: A tuple containing the image path, desired output format, quality, and output directory (if specified).
    """
    input_path = Path(input("Enter the path to the image file: ").strip("\"'")).resolve()
    if not input_path.is_file():
        print(f"Error: File {input_path} does not exist.")
        return None, None, None, None
    
    output_format = input(f"Enter the desired output format {SUPPORTED_FORMATS}: ").strip().lower()
    if output_format not in SUPPORTED_FORMATS:
        print(f"Error: Unsupported format. Please choose from {SUPPORTED_FORMATS}")
        return None, None, None, None
    
    quality = input(f"Enter the desired quality (0-100, default is {DEFAULT_QUALITY}): ").strip()
    if quality:
        try:
            quality = int(quality)
            if not 0 <= quality <= 100:
                raise ValueError
        except ValueError:
            print("Error: Quality must be an integer between 0 and 100.")
            return None, None, None, None
    else:
        quality = DEFAULT_QUALITY
    
    output_dir = input("Enter the output directory (optional, press Enter to use the same directory): ").strip("\"'")
    output_dir = Path(output_dir).resolve() if output_dir else None
    if output_dir and not output_dir.is_dir():
        print(f"Error: The specified output directory {output_dir} does not exist.")
        return None, None, None, None
    
    return input_path, output_format, quality, output_dir

def main():
    print("Welcome to the Image Converter!")
    while True:
        try:
            input_image, output_format, quality, output_dir = get_user_input()
            if input_image and output_format:
                convert_image(input_image, output_format, quality, output_dir)
            
            another = input("Do you want to convert another image? (y/n): ").lower()
            if another != 'y':
                print("Thank you for using the Image Converter. Goodbye!")
                break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()