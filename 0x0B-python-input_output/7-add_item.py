#!/usr/bin/python3
''' This is a script that adds all arguments to a python list
and save them in a file '''

import sys
import os

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

# set up command line input
new_items = sys.argv[1:]

# if file exists
if os.path.exists("./add_item.json"):

    # load the data from the json file
    string = load_from_json_file("add_item.json")

    # extend the list by the new contnet from the comand line
    string.extend(new_items)

    # save it into the JSON file
    save_to_json_file(string, "add_item.json")

# if the file does exist, create it and load the data from the command line
else:
    with open("add_item.json", 'w', encoding='utf-8') as file:
        file.write('')
        save_to_json_file(new_items, "add_item.json")
