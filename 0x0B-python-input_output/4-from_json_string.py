#!/usr/bin/python3
''' This module implements a function that converts a JSON
string to a python value'''


def from_json_string(my_str):
    ''' Returns the python value of the JSON string my_str '''

    import json

    return json.loads(my_str)
