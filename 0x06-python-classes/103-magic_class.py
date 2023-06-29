#!/usr/bin/python3
''' Magic class module for area and circumference '''

import math


class MagicClass:
    ''' This class defines the attribute radius and methods for
    area anf circumference of a circle'''

    def __init__(self, radius):
        ''' The init method initiates once an instance is created '''
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        if radius is None:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        ''' Returns the area of a circle (Magic Calculation) '''
        return self.__radius ** 2 * math.pi

    def circumference(self):
        ''' Returns the circumference of a circle(Magic calculation)'''
        return 2 * math.pi * self.__radius
