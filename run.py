import exifread
import os
import glob

# Ask for top node folder, a.k.a. the directory to work in.
root_path = input('What is the path directory to work with?\n'
                         'Example format: c:\\MyPictures\\RenameThese\\ \n')

while True:
    check = input('\nIs this the correct directory? ' + root_path + '\nY/N ')

    if check.lower().startswith('y'):
        # Extracts the file list.
        file_list = glob.glob(root_path+'*.*', recursive=True)
        print("Reading and renaming files.")

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
        exit()
    elif check.lower().startswith('n'):
        print("Exiting program.")
        exit()
