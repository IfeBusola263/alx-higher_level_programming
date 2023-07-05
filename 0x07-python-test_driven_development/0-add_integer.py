#!/usr/bin/python3
''' This module houses a function that adds an integer '''


def add_integer(a, b=98):
    ''' Returns the addition of two integers a and b '''

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")

    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

if __name__ == '__main__':
    import doctest
    doctest.testfile()
