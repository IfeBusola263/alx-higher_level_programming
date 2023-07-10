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
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')


class Rectangle(BaseGeometry):
    ''' A class that inherirs from BaseGeometry '''

    def __init__(self, width, height):
        ''' the init magic method is initiated when an
        instance of the class is created'''

        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)

        self.__width = width
        self.__height = height

    def area(self):
        ''' Returns the area of the rectangle '''
        return self.__width * self.__height

    def __str__(self):
        ''' Returns the string representation of the area, formatted '''
        return "[Rectangle]" + " " + f"{self.__width}/{self.__height}"


class Square(Rectangle):
    ''' The class square is a subclass of the rectangle class '''

    def __init__(self, size):
        ''' The init method initialized the fields and other starting
        instructions when the instance of the class is created '''

        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        ''' Returns the area of the square object '''
        return self.__size ** 2

    def __str__(self):
        ''' Returns the string representation of the area, formatted '''
        return "[Square]" + " " + f"{self.__size}/{self.__size}"
