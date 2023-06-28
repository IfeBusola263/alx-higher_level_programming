#!/usr/bin/python3
''' This module contains a class, with field size '''


class Square:
    ''' This class instantiates the field '''

    def __init__(self, size=0):
        ''' Initializes the file attribute '''
        self.size = size

    @property
    def size(self):
        ''' This is a pythonic way to protect to variable size'''
        return self.__size

    @size.setter
    def size(self, value):
        ''' Sets the value if any wrong input is given by user '''
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        ''' Returns the area of the square. '''
        return self.__size ** 2

    def __lt__(self, other):
        '''Return a boolean value 'True' if self is less than other,
        and False otherwise'''
        return self.area() < other.area()

    def __le__(self, other):
        '''Return a boolean value 'True' if self is less than
        or equal to other, and False otherwise'''
        return self.area() <= other.area()

    def __gt__(self, other):
        '''Return a boolean value 'True' if self is greater than
        other, and False otherwise'''
        return self.area() > other.area()

    def __ge__(self, other):
        '''Return a boolean value 'True' if self is greater than
        or equal to other, and False otherwise'''
        return self.area() >= other.area()

    def __eq__(self, other):
        '''Return a boolean value 'True' if self is
        equal to other, and False otherwise'''
        return self.area() == other.area()

    def __ne__(self, other):
        '''Return a boolean value 'True' if self is
        not equal to other, and False otherwise'''
        return self.area() != other.area()
