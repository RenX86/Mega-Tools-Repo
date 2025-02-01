import os
from pathlib import Path
from typing import Optional, List
import sys

class FolderTreeVisualizer:
    """A class to handle the visualization of folder structures with interactive features."""
    
    def __init__(self):
        # Default exclusion lists that can be modified
        self.default_exclude_dirs = ['.git', '__pycache__', 'node_modules', '.idea', '.vscode']
        self.default_exclude_files = ['.pyc', '.pyo', '.pyd', '.DS_Store']
        
    def get_valid_path(self) -> str:
        """
        Interactively get a valid folder path from the user.
        Keeps asking until a valid path is provided or user chooses to exit.
        """
        while True:
            # Get the path from user with a clear prompt
            print("\nEnter the folder path to visualize (or 'exit' to quit):")
            path = input().strip()
            
            # Check for exit command
            if path.lower() == 'exit':
                print("Exiting program...")
                sys.exit(0)
            
            # Convert to absolute path if relative path is given
            path = os.path.abspath(path)
            
            # Validate the path
            if not os.path.exists(path):
                print(f"Error: Path '{path}' does not exist.")
                continue
                
            if not os.path.isdir(path):
                print(f"Error: '{path}' is not a directory.")
                continue
                
            try:
                # Test if we have read permissions
                os.listdir(path)
                return path
            except PermissionError:
                print(f"Error: No permission to access '{path}'.")
                continue
            except Exception as e:
                print(f"Error: {str(e)}")
                continue

    def get_max_depth(self) -> Optional[int]:
        """
        Interactively get the maximum depth from the user.
        Returns None for unlimited depth.
        """
        while True:
            print("\nEnter maximum depth to traverse (press Enter for unlimited):")
            depth_input = input().strip()
            
            if not depth_input:
                return None
                
            try:
                depth = int(depth_input)
                if depth < 1:
                    print("Depth must be a positive number.")
                    continue
                return depth
            except ValueError:
                print("Please enter a valid number.")

    def get_additional_exclusions(self) -> tuple[List[str], List[str]]:
        """
        Interactively get additional exclusions from the user.
        Returns tuple of (exclude_dirs, exclude_files).
        """
        print("\nWould you like to add custom exclusions? (y/n):")
        if input().strip().lower() != 'y':
            return [], []
            
        print("\nEnter additional directories to exclude (comma-separated, or press Enter to skip):")
        exclude_dirs = [d.strip() for d in input().split(',') if d.strip()]
        
        print("\nEnter additional file patterns to exclude (comma-separated, or press Enter to skip):")
        exclude_files = [f.strip() for f in input().split(',') if f.strip()]
        
        return exclude_dirs, exclude_files

    def draw_tree(
        self,
        root_path: str,
        exclude_dirs: Optional[List[str]] = None,
        exclude_files: Optional[List[str]] = None,
        max_depth: Optional[int] = None
    ) -> None:
        """
        Draws the tree structure of a folder.
        
        Args:
            root_path: The path to the root directory
            exclude_dirs: List of directory names to exclude
            exclude_files: List of file patterns to exclude
            max_depth: Maximum depth to traverse
        """
        # Combine default and custom exclusions
        exclude_dirs = list(set(self.default_exclude_dirs + (exclude_dirs or [])))
        exclude_files = list(set(self.default_exclude_files + (exclude_files or [])))
        
        def should_exclude(name: str, is_dir: bool) -> bool:
            """Helper function to check if an item should be excluded."""
            if is_dir:
                return name in exclude_dirs
            return any(name.endswith(ext) for ext in exclude_files)
        
        def print_tree(
            directory: Path,
            prefix: str = "",
            is_last: bool = True,
            depth: int = 0
        ) -> None:
            """Recursively prints the tree structure."""
            # Check max depth
            if max_depth is not None and depth > max_depth:
                return
                
            # Get the directory name for printing
            dir_name = directory.name or str(directory)
            
            # Create the appropriate prefix for this item
            if prefix == "":
                print(f"\nFolder structure for: {dir_name}")
                print("=" * (len(dir_name) + 20))
            else:
                connector = "└── " if is_last else "├── "
                print(f"{prefix}{connector}{dir_name}")
            
            # Prepare the prefix for children
            children_prefix = prefix + ("    " if is_last else "│   ")
            
            try:
                # Get all valid items in the directory
                items = [
                    item for item in sorted(directory.iterdir())
                    if not should_exclude(item.name, item.is_dir())
                ]
                
                # Print all items
                for index, item in enumerate(items):
                    is_last_item = index == len(items) - 1
                    if item.is_dir():
                        print_tree(item, children_prefix, is_last_item, depth + 1)
                    else:
                        connector = "└── " if is_last_item else "├── "
                        print(f"{children_prefix}{connector}{item.name}")
                        
            except PermissionError:
                print(f"{children_prefix}└── [Permission Denied]")
            except Exception as e:
                print(f"{children_prefix}└── [Error: {str(e)}]")

        # Start the tree visualization
        try:
            print_tree(Path(root_path))
        except Exception as e:
            print(f"Error while processing directory: {str(e)}")

def main():
    """Main function that handles the interactive flow."""
    visualizer = FolderTreeVisualizer()
    
    print("Welcome to the Folder Tree Visualizer!")
    print("This program will help you visualize the structure of a directory.")
    
    while True:
        # Get folder path
        path = visualizer.get_valid_path()
        
        # Get maximum depth
        max_depth = visualizer.get_max_depth()
        
        # Get custom exclusions
        exclude_dirs, exclude_files = visualizer.get_additional_exclusions()
        
        # Draw the tree
        visualizer.draw_tree(
            path,
            exclude_dirs=exclude_dirs,
            exclude_files=exclude_files,
            max_depth=max_depth
        )
        
        # Ask if user wants to visualize another directory
        print("\nWould you like to visualize another directory? (y/n):")
        if input().strip().lower() != 'y':
            print("Thank you for using Folder Tree Visualizer!")
            break

if __name__ == "__main__":
    main()