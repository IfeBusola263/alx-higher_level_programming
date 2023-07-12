#!/usr/bin/python3
''' This module implements a Base Geometry class'''


# class BaseGeometry(object):
#     ''' This is an empty class '''

#     def area(self):
#         ''' raises an exception when called '''
#         raise Exception("area() is not implemented")

#     def integer_validator(self, name, value):
#         ''' validates the type of object value and name '''

#         if type(value) is not int:
#             raise TypeError(f"{name} must be an integer")

#         if value <= 0:
#             raise ValueError(f'{name} must be greater than 0')

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' A class that inherits from BaseGeometry '''

    def __init__(self, width, height):
        ''' the init magic method is initiated when an
        instance of the class is created'''

        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
