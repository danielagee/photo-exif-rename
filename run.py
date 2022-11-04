# Day 43 - Slice the string to extract year, month, day.

# Import the ExifRead package.
import exifread

# A "with" statement allows us to cycle through the tags until we reach the one we want
# https://www.geeksforgeeks.org/with-statement-in-python/
# https://docs.python.org/3/reference/compound_stmts.html#the-with-statement
with open('C:\\Python\\image1.jpg', 'rb') as image_file:
    tags = exifread.process_file(image_file, stop_tag="EXIF DateTimeOriginal")
    dateTaken = tags["EXIF DateTimeOriginal"]

year = str(dateTaken)[0:4]
print(year)
month = str(dateTaken)[5:7]
print(month)
day = str(dateTaken)[8:10]
print(day)
