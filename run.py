# Day 45 - Rename the file

# Import the ExifRead package.
import exifread

# Import the OS package to use the os.rename module.
import os

path = 'C:\\Python\\'
image_file = 'image1.jpg'

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

# Use os.rename method to rename the file.
# https://docs.python.org/3/library/os.html#:~:text=os.rename(,src%20and%20dst.
os.rename(path+image_file, path+new_name)
print("File renamed.")
