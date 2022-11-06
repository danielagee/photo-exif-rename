# Day 46 - Extract list of all files in the root folder and loop to rename.
# This will be done by integrating the Day 45 code with code from the
# Backup Tool project.

import exifread
import os
import glob

root_path = 'C:\\Python\\pictures\\'
root_path_original = root_path

# Adds '**' to the user specified root directory so that Python will only
# search the root and subdirectories.
root_path += '*.*'

# Extracts the active and backup file lists from the user specified folders.
file_list = glob.glob(root_path, recursive=True)

# For loop to write a parsed list of all missing backup files to the text document.
for item in file_list:
    # "With" statement to cycle through the tags until we reach the one we want.
    with open(item, 'rb') as image_tags:
        tags = exifread.process_file(image_tags, stop_tag="EXIF DateTimeOriginal")
        dateTaken = tags["EXIF DateTimeOriginal"]

    year = str(dateTaken)[0:4]
    month = str(dateTaken)[5:7]
    day = str(dateTaken)[8:10]

    # variable 'item' contains the full path name. Short code to trim that out...
    original_file_name = item.replace(root_path_original, '')
    # Concatenate the year, month, day, and existing file name to make the new file name.
    new_name = f'{year}-{month}-{day} - {original_file_name}'
    os.rename(item, root_path_original+new_name)
print("Files renamed.")