import os
import shutil
import logging
from pathlib import Path

# Configure logging to record operations into a log file.
logging.basicConfig(
    filename='file_organizer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Define file categories and associated file extensions.
FILE_CATEGORIES = {
    'Images':    ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff','.heic'],
    'Documents': ['.pdf', '.doc', '.docx', '.pages','.txt', '.xls', '.xlsx', '.numbers','.ppt', '.pptx'],
    'Audio':     ['.mp3', '.m4a', '.wav', '.aac', '.ogg', '.flac'],
    'Videos':    ['.mp4', '.avi', '.mov', '.mkv', '.wmv','.mov'],
    'Archives':  ['.zip', '.tar', '.gz', '.rar', '.7z']
}

def organize_files(directory):
    """
    Organize files in the given directory into folders based on file extension.
    
    Parameters:
        directory (str): The path to the directory to organize.
    """
    dir_path = Path(directory)
    if not dir_path.exists():
        print(f"Error: The directory '{directory}' does not exist.")
        return

    # Iterate over each item in the directory.
    for item in dir_path.iterdir():
        if item.is_file():  # Process only files
            file_ext = item.suffix.lower()  # Get the file extension in lower case.
            destination_folder = None

            # Determine which category folder the file belongs to.
            for category, extensions in FILE_CATEGORIES.items():
                if file_ext in extensions:
                    destination_folder = category
                    break

            # If no matching category is found, assign the file to 'Others'
            if destination_folder is None:
                destination_folder = 'Others'
            
            destination_path = dir_path / destination_folder

            # Create the destination folder if it doesn't exist.
            if not destination_path.exists():
                try:
                    destination_path.mkdir()
                    logging.info(f"Created folder: {destination_path}")
                except Exception as e:
                    logging.error(f"Could not create folder {destination_path}: {e}")
                    print(f"Error creating folder {destination_path}: {e}")
                    continue

            # Move the file to the destination folder.
            try:
                shutil.move(str(item), str(destination_path / item.name))
                logging.info(f"Moved file: {item.name} to {destination_folder}")
                print(f"Moved: {item.name} -> {destination_folder}")
            except Exception as e:
                logging.error(f"Error moving file {item.name}: {e}")
                print(f"Error moving file {item.name}: {e}")

if __name__ == '__main__':
    # Ask the user to input the directory path.
    target_directory = input("Enter the full path of the directory to organize: ").strip()
    organize_files(target_directory)
