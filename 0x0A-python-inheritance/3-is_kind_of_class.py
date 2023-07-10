#!/usr/bin/python3
''' This module implements a function that checks for the class
and parent class of an object'''


def is_kind_of_class(obj, a_class):
    ''' Returns true is obj is of class a_class or base class of a_class '''
    return isinstance(obj, a_class)
