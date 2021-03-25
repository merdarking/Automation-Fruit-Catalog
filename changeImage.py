#! /usr/bin/python3

import os
import sys
from PIL import Image

'''Get the images name list in the directory'''
def get_file_list():

    # Go into the path in the images
    path = os.path.join(os.path.dirname(sys.argv[0]),"supplier-data")
    os.chdir(path)

    # Get the file names in the images directory
    images = os.listdir("images")
    images = [image_file for image_file in images if '.tiff' in image_file]
    return tuple(images)

def process_image():
    # Obtain information about file name need to be processed
    images_list = get_file_list()

    # Create a new directory to save file
    if not os.path.isdir("edited"):
        os.mkdir("edited")
    
    # Process the image in the list
    for image in images_list:

        # The path of the images need to be processed
        image_path = os.path.join(".","images", image)
        # The path of the images to be saved
        save_path = os.path.join(".","edited", image)
        save_path = save_path.replace('.tiff','.jpeg')
        
        # Open the image file
        img = Image.open(image_path)

        # Resize the image
        new_img = img.resize((600,400))
        # Save the edited image
        new_img.convert('RGB').save(save_path,'jpeg')
    return 'Image Process to "edited" directory completed'

def main():
    files_name = process_image()
    print(files_name)

if __name__ == '__main__':
    main()