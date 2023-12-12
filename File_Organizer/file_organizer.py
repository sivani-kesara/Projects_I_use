# Import necessary libraries/modules
import os  # Module for interacting with the operating system
import shutil  # Module for high-level file operations
# Define a function to organize files in a given folder
def organize_files(folder_path):
    # Dictionary to store folder names based on file extensions
    extensions_folders = {}
    # Iterate through files in the specified folder
    for filename in os.listdir(folder_path):
        # Check if the item is a file
        if os.path.isfile(os.path.join(folder_path, filename)):
            # Extract the file extension and convert to lowercase
            file_extension = filename.split('.')[-1].lower()
            # Check if the extension exists in the dictionary; if not, create a folder for it
            if file_extension not in extensions_folders:
                extensions_folders[file_extension] = f"{file_extension}_files"
    # Create folders for each unique file extension
    for folder in extensions_folders.values():
        folder_path_extension = os.path.join(folder_path, folder)
        os.makedirs(folder_path_extension, exist_ok=True)
    # Move files to their respective folders based on their extensions
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_extension = filename.split('.')[-1].lower()
            dest_folder = extensions_folders[file_extension]
            src = os.path.join(folder_path, filename)
            dest = os.path.join(folder_path, dest_folder, filename)
            # Move the file to the destination folder
            shutil.move(src, dest)
            # Print a message indicating the file movement
            print(f"Moved {filename} to {dest_folder} folder.")
# Specify the path of the folder to organize
folder_path = "folder path"
# Call the function to organize the files in the specified folder
organize_files(folder_path)