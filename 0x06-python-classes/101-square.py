#!/usr/bin/python3
''' This module contains a class, with field size '''


class Square:
    ''' This class instantiates the field '''

    def __init__(self, size=0, position=(0, 0)):
        ''' Initializes the field attribute '''
        self.size = size
        self.position = position

    @property
    def size(self):
        ''' This is a pythonic way to protect to variable size'''
        return self.__size

    @size.setter
    def size(self, value):
        ''' Sets the value if any wrong input(integer) is given by user '''
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        ''' This is a pythonic way to protect to variable position'''
        return self.__position

    @position.setter
    def position(self, value):
        ''' Sets the value if any wrong input(tuple) is given by user '''
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        first, second = value

        if type(first) is not int or type(second) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")

        if (first < 0 or second < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        ''' Returns the area of the square.'''
        return self.__size ** 2

    def my_print(self):
        ''' This method prints the square with the character #'''
        if self.__size == 0:
            print()
        else:
            # print the square and fill with spaces
            if self.__position[1] > 0:
                for i in range(self.__position[1]):
                    print()
            for i in range(self.__size - 1):
                # fill with spaces here
                print(" " * self.__position[0], end='')

                for j in range(self.__size):
                    print('#', end='')
                print()
            print(" " * self.__position[0], end='')
            return '#' * self.__size

    def __str__(self):
        '''Prints a nicely outputed object of type string of the
        instance of a class'''
        return self.my_print()
