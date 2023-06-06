#!/usr/bin/python3

def islower(c):
    """ Returns True if character c is lower and false otherwise.

    >>> islower("a")
    'True'
    >>> islower("A")
    'False'
    >>> islower(90)
    'False'
    """
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
