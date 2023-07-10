#!/usr/bin/python3
''' This module implements a function to checks if an object
is an instance of a specified class'''


def is_same_class(obj, a_class):
    ''' Returns True if obj is an instance of the class a_class'''

    if a_class is object:
        return False

    return isinstance(obj, a_class)
