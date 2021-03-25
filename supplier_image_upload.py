#! /usr/bin/python3

import os
import sys
import requests

'''Get the images name list in the directory'''
def get_file_list():

    # Go into the path in the images
    path = os.path.join(os.path.dirname(sys.argv[0]),"supplier-data")
    os.chdir(path)

    # Get the file names in the images directory
    images = os.listdir("edited")
    images = [image_file for image_file in images if '.jpeg' in image_file]
    return tuple(images)

'''Uploading the image'''
def upload_image(ip_address, file_path):
    url = "http://{}/upload/".format(ip_address)
    with open(file_path, 'rb') as opened:
        r = requests.post(url,files={'file': opened})
        r.close()
    return r.status_code

def main():
    # Get images list
    images = get_file_list()
    # Instance IP address
    ip_address = '0.0.0.0'
    # Upload the image
    for image in images:
        path = os.path.join(os.path.join(sys.argv[0]),'supplier-data','edited', image)
        print(upload_image(ip_address, path))

if __name__ == '__main__':
    main()