#!/usr/bin/python3
''' This module implements a class rebel int '''


class MyInt(int):
    ''' The class MyInt inherits from int '''

    def __init__(self, num):
        ''' initialization of the object '''
        self.num = num

    def __eq__(self, other):
        ''' returns false if self is equal to other '''
        return self.num != other

    def __ne__(self, other):
        ''' returns false if self is not equal to other '''
        return self.num == other
