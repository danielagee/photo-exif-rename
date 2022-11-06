# Day 47 - Testing on a bigger data set
# Running on the full data set immediately raises failures. Missing tags, wrong file types, etc.
# Fixes used:
# 1) Swap dateTaken = tags["EXIF DateTimeOriginal"] with dateTaken = tags.get("EXIF DateTimeOriginal")
#       a) The original code fails if the tag is missing. The new code returns None which I can then
#           skip with an "if date_taken != None:" statement
# 2) added "if item.endswith(('.jpg', '.JPG')):" to skip non-jpg files.
# 3) added "if dateTaken is not None:" to skip files without exif date tags

import exifread
import os
import glob

root_path = 'C:\\Python\\pictures\\'

# Extracts the file list.
# The root path is needed later, but *.* is only needed once.
# Consolidated here and removed the root_path_original variable.
file_list = glob.glob(root_path+'*.*', recursive=True)
print("Reading and renaming files.")

# For loop to write a parsed list of all missing backup files to the text document.
for item in file_list:
    # if statement filters for only jpg or JPG files
    if item.endswith(('.jpg', '.JPG')):
        # with statement allows us to cycle through the tags
        with open(item, 'rb') as image_tags:
            tags = exifread.process_file(image_tags, stop_tag="EXIF DateTimeOriginal")
            dateTaken = tags.get("EXIF DateTimeOriginal")

        # if statement filters out files with no date tags
        if dateTaken is not None:
            year = str(dateTaken)[0:4]
            month = str(dateTaken)[5:7]
            day = str(dateTaken)[8:10]
            new_name = f'{year}-{month}-{day} - {item.replace(root_path, "")}'
            os.rename(item, root_path+new_name)
print("Files renamed.")
