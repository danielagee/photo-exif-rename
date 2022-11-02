# Import the ExifRead package. This has the functionality we need to extract the meta data from the photos.
import exifread
with open('C:\\Python\\image1.jpg', 'rb') as fh:
    tags = exifread.process_file(fh, stop_tag="EXIF DateTimeOriginal")
    dateTaken = tags["EXIF DateTimeOriginal"]

print(dateTaken)
