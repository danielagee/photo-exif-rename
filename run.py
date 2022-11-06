# Day 46 - Extract list of all files in the root folder.
# This will be done by integrating the Day 5 code with code from the
# Backup Tool project.

import exifread
import os

# Import the glob function to get a list of image files.
import glob

root_path = 'C:\\Python\\pictures\\'

# Adds '**' to the user specified root directory so that Python will only
# search the root and subdirectories.
root_path += '*.*'

# Extracts the active and backup file lists from the user specified folders.
file_list = glob.glob(root_path, recursive=True)

# For loop to write a parsed list of all missing backup files to the text document.
for item in file_list:
    print(str(item))

""" #Temporarily commenting out unused code to test the extract code
# image_file = 'image1.jpg'

# "With" statement to cycle through the tags until we reach the one we want.
with open(path+image_file, 'rb') as image_tags:
    tags = exifread.process_file(image_tags, stop_tag="EXIF DateTimeOriginal")
    dateTaken = tags["EXIF DateTimeOriginal"]

year = str(dateTaken)[0:4]
month = str(dateTaken)[5:7]
day = str(dateTaken)[8:10]

# Concatenate the year, month, day, and existing file name to make the new file name.
new_name = f'{year}-{month}-{day} - {image_file}'
print(new_name)
os.rename(path+image_file, path+new_name)
print("File renamed.")
"""
