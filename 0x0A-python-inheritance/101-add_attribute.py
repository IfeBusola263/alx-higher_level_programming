#!/usr/bin/python3
''' This module implements a function that added attributes to a
class'''


def add_attribute(*args):
    ''' Tries to add attributes to a function'''

    # use sequence unpacking to store the class name
    # attribute name and the attribute value

    obj, attr, value, *_ = args

    if not isinstance(obj, str) or not hasattr(obj, attr):
        return setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
