#!/usr/bin/python3
''' This module defines a locked class '''


class LockedClass:
    ''' Defines a locked class that can only be created, when the attribute
    is the string first_name '''
    def __new__(cls):
        ''' checks to see if an attribute has been referred to '''
        if hasattr(cls, first_name):
            return super()__new__(cls)
