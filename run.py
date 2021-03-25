#! /usr/bin/python3

import os
import sys
import requests
import json

'''Get the description file name list in the directory'''
def get_file_list():

    # Go into the path in the descriptions
    path = os.path.join(os.path.dirname(sys.argv[0]),"supplier-data")
    os.chdir(path)

    # Get the file names in the descriptions directory
    descriptions = os.listdir("descriptions")
    descriptions = [desc_file for desc_file in descriptions if '.txt' in desc_file]
    return tuple(descriptions)

'''Obtain and save it into the dictionary to be dumped into JSON'''
def get_file_data():

    # Get the file name
    descriptions = get_file_list()
    key = ('name', 'weight', 'description', 'image_name')

    desc_data = []

    # Get the file data information to be processed locally
    for desc in descriptions:
        image_name = desc.replace('.txt','.jpeg')
        path = os.path.join(os.path.dirname(sys.argv[0]),"supplier-data","descriptions",desc)
        tmp_dict = {}
        
        # Open the data
        with open(path,'r') as opened:
            item = [content.strip() for content in opened]
            # Remove any empty line
            if '' in item:
                item.remove('')
            opened.close()
        
        # Throw away the lbs
        item[1] = int(item[1].strip(' lbs'))
        # Convert into dictionary
        tmp_dict[key[0]], tmp_dict[key[1]], tmp_dict[key[2]], tmp_dict[key[3]] = item[0], item[1], item[2], image_name

        desc_data.append(tmp_dict)
    
    return desc_data


'''Dump into json file'''
'''
def save_data(items):
    path = os.path.join("..","descriptions.json")
    with open(path,'w') as desc_json:
        json.dump(items, desc_json, indent=2)
    return 'Data succesfully dumped into json format as "descriptions.json"'
'''

'''Post the data into website'''
def upload_description(ip_address, item):
    url = 'http://{}/fruits/'.format(ip_address)

    # Post the data into the server
    r= requests.post(url, data=item)
    return r.status_code

def main():
    decription_data = get_file_data()
    #print(save_data(decription_data))
    ip_address = '0.0.0.0'
    for item in decription_data:
       print(upload_description(ip_address, item))

if __name__ == '__main__':
    main()