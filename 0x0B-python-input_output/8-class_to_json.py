#!/usr/bin/python3
'''This is module implements a function that
returns the dictionary description of an object'''


def class_to_json(obj):
    ''' Returns the dictionary description of the object obj '''

    # if type(obj) in [list, dict, str, int, bool]:
    return obj.__dict__
