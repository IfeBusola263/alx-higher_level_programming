#!/usr/bin/python3
''' This module implements a function that checks for the
relationship between and object and parent classes of it's parent class'''


def inherits_from(obj, a_class):
    ''' Returns True if obj inherits from a class it's parent class
    inherits from'''

    if type(obj) is a_class:
        return False

    return issubclass(type(obj), a_class)
