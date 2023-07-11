#!/usr/bin/python3
''' This module implements a function thats writes to a
file using JSON string '''


def save_to_json_file(my_obj, filename):
    ''' Writes an object 'my_obj' to a file 'filename'
    using JSON string '''

    import json

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
