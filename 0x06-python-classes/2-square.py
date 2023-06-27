#!/usr/bin/python3
''' This module contains a class, with field size '''


class Square:
    ''' This class instantiates the field '''

    def __init__(self, size=0):
        ''' Initializes the file attribute '''
        self.__size = size

        try:
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            print("size must be an integer")
