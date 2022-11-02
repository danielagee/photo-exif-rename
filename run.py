# Day 41 - Install and test exifread package.

# The exifread package seems to have quite a bit of functionality. Recommend to read through the details!
# https://github.com/ianare/exif-py/blob/develop/README.rst
# https://pypi.org/project/ExifRead/

# An extensive list of exif tags can be found here: https://exiftool.org/TagNames/EXIF.html

# Import the ExifRead package. This has the functionality we need to extract the metadata from the photos.
# Painful lesson learned here... PyCharm does not automatically import PIP installed packages. You have to
# manually import them to the project using File > Settings > Project > Project Interpreter, Press the + button
# Type "exifread" in the top search box, Press Install Package

import exifread

# Open image file for reading (must be in binary mode)
image_file = open('C:\\Python\\image1.jpg', 'rb')

# Return Exif tags
tags = exifread.process_file(image_file)
print(tags)
