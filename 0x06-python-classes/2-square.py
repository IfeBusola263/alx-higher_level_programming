#!/usr/bin/python3
''' This module contains a class, with field size '''


class Square:
    ''' This class instantiates the field '''

    def __init__(self, size=0):
        ''' Initializes the file attribute '''
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
