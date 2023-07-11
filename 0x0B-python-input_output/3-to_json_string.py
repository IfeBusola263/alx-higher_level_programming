#!/usr/bin/python3
''' This module implements a function that returns a JSON
representation of an object'''


def to_json_string(my_obj):
    ''' return JSON representation of the object '''

    import json

    return json.dumps(my_obj)
