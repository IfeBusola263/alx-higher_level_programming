#!/usr/bin/python3
''' This module implements a function that prints methods and attributes
available to a class'''


def lookup(obj):
    ''' returns a list of available attributes and methods of an
    object'''

    return dir(obj)
