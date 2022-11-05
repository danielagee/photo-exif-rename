# Day 45 - Concatenate and append date into original file name

# Import the ExifRead package.
import exifread

# First, we need to pull out the path and image file name as separate variables
# to use the file name in the end result.
path = 'C:\\Python\\'
image_file = 'image1.jpg'

# "With" statement to cycle through the tags until we reach the one we want.
# Replacing the hard coded file name with the variables gives the below.
with open(path+image_file, 'rb') as image_tags:
    tags = exifread.process_file(image_tags, stop_tag="EXIF DateTimeOriginal")
    dateTaken = tags["EXIF DateTimeOriginal"]

year = str(dateTaken)[0:4]
print(year)
month = str(dateTaken)[5:7]
print(month)
day = str(dateTaken)[8:10]
print(day)

# There are multiple ways to achieve the concatenation but f-string seems to be
# the preferred, and most elegant, way to do so.
# https://peps.python.org/pep-0498/
new_name = f'{year}-{month}-{day} - {image_file}'
# new_name = "%s-%s-%s - %s" % (year, month, day, image_file)
# new_name = year+'-'+month+'-'+day+' - '+str(image_file)
print(new_name)
