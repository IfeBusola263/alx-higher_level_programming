#!/usr/bin/python3
''' This module implements a Base Geometry class'''


class BaseGeometry:
    ''' This is an empty class '''

    def __init__(self):
        ''' initiatized when an instance of the class is created '''
        pass

    def area(self):
        ''' raises an exception when called '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' validates the type of object value and name '''

        if type(value) is not int:
            raise TypeError("<name> must be an integer")

        if value <= 0:
            raise ValueError("<name> must be greater than 0")
