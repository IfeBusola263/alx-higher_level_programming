#!/usr/bin/python3
''' This module defines a Rectangle class and the atrributes '''


class Rectangle:
    ''' A rectangle class that defines width and height attributes '''

    def __init__(self, width=0, height=0):
        ''' The init method is a class method that initializes
        once an instance of the class is created '''
        self.width = width
        self.height = height

    @property
    def width(self):
        ''' The width method with the property decorator
        is a setter to protect the attribute of the fields of the class'''
        return self.__width

    @width.setter
    def width(self, value):
        ''' The width method with the decorator width.setter is an attribute
        setter for the class rectangle '''

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        ''' The width method with the property decorator
        is a setter to protect the attribute of the fields of the class'''
        return self.__height

    @height.setter
    def height(self, value):
        ''' The width method with the decorator width.setter is an attribute
        setter for the class rectangle '''

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
