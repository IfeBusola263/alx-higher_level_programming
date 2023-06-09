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

    def my_print(self):
        ''' This method prints the square with the character #'''
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
