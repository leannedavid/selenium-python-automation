import os
from pathlib import Path
# Match file type to their directory
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

# Loops through dictionary's items and returns the category where the suffix exists.
def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category;
    
    # returns a "MISC" folder if the file's extension doesn't belong in the dictionary 
    return 'MISC'

print(pickDirectory('.pdf'))

# scandir will grab every object in our folder
def organizeDirectory():
    for item in os.scandir():

        # if the file is a directory/folder, skip it
        if item.is_dir():
            continue

        filePath = Path(item)
        fileType = filePath.suffix.lower() # .suffix grabs the file extension of our object
        directory = pickDirectory(fileType) # directory now equals the appropriate category the object's extension should belong to
        directoryPath = Path(directory) # grabs the path of the directory

        # If the directory path does not already exist, make a directory with that name
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        
        # Moves a file into the directory by changing the file path to join with the directory's path
        filePath.rename(directoryPath.joinpath(filePath))

# Runs our program
organizeDirectory()