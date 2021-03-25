#! /usr/bin/python3

import os
import sys
import datetime # NEW
import reports # NEW

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
        image_name = desc.replace('.jpeg','.txt')
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

# START HERE IS NEW
'''Combine name and weight on each individual item'''
def process_body(items):
    text = "name: {}<br/>weight: {} lbs".format(items['name'], str(items['weight']))
    return text

def main():
    decription_data = get_file_data()

    # START HERE IS NEW
    '''Content of the pdf file'''
    date = datetime.datetime.today().strftime('%B %e, %Y')
    attachment = os.path.join("..","processed.pdf")
    title = "Processed Updated on {}".format(date)
    
    '''Process the body'''
    overall_body = []
    for item in decription_data:
        item_body = process_body(item)
        overall_body.append(item_body)
    paragraph = '<br/><br/>'.join(overall_body)
    print(reports.generate_report(attachment, title, paragraph))
    
if __name__ == '__main__':
    main()