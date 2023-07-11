#!/usr/bin/python3
''' This module implements a function that creates an object from
a JSON file '''


def load_from_json_file(filename):
    ''' Creates an object from a JSON file '''
    import json

    with open(filename, 'r', encoding='utf-8') as file:
        return json.loads(file.readline())
