# Importing necessary libraries
import os  # Library for interacting with the operating system (working with files and directories)
import shutil  # Library for high-level file operations like moving files

# Setting the directory that you want to organize (e.g., "Documents" folder in the user's home directory)
directory = r"C:\Users\karos\Documents"  # You can change this to another folder you want to organize

# A dictionary that maps file extensions to corresponding folder names
extensions = {
    ".jpg": "Images",  # .jpg files will be moved to the "Images" folder
    ".png": "Images",  # .png files will be moved to the "Images" folder
    ".gif": "Images",  # .gif files will be moved to the "Images" folder
    ".mp4": "Videos",  # .mp4 files will be moved to the "Videos" folder
    ".mov": "Videos",  # .mov files will be moved to the "Videos" folder
    ".doc": "Documents",  # .doc files will be moved to the "Documents" folder
    ".pdf": "Documents",  # .pdf files will be moved to the "Documents" folder
    ".txt": "Documents",  # .txt files will be moved to the "Documents" folder
    ".mp3": "Music",  # .mp3 files will be moved to the "Music" folder
    ".wav": "Music"  # .wav files will be moved to the "Music" folder
}

# Displaying which directory is being organized
print(f"Organizing files in: {directory}")

# Starting to loop through all files and directories in the specified directory
for filename in os.listdir(directory):
    # Creating the full path for the current file or directory
    file_path = os.path.join(directory, filename)

    # Checking if it's a file (not a directory)
    if os.path.isfile(file_path):
        # Extracting the file extension and converting it to lowercase
        extension = os.path.splitext(filename)[1].lower()

        # Logging: displaying the name of the file being processed
        print(f"Processing file: {filename}")

        # Checking if the file extension is in the defined extensions dictionary
        if extension in extensions:
            # Getting the folder name to which the file should be moved
            folder_name = extensions[extension]

            # Creating the full path for the folder (it will be created if it doesn't exist)
            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)  # exist_ok=True prevents error if the folder already exists

            # Creating the full destination path for where the file will be moved
            destination_path = os.path.join(folder_path, filename)

            # Moving the file to the appropriate folder
            shutil.move(file_path, destination_path)

            # Logging: displaying the move action for the file
            print(f"Moved {filename} to {folder_name} folder")
        else:
            # Logging: if the file extension is not recognized, we skip the file and log it
            print(f"Skipped {filename}. Unknown file extension.")
    else:
        # Logging: if the item is a directory, not a file, we skip it and log it
        print(f"Skipped {filename}. It's a directory.")

# After all files have been processed, we display a completion message
print("File organization completed.")
