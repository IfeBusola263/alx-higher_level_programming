#!/usr/bin/python3
def print_list_integer(my_list=[]):
    ''' list -> int

    Prints the content of the string.

    >>> print_list_integer([1, 2, 3, 4, 5])
    1
    2
    3
    4
    5
    '''
    for item in my_list:
        print("{:d}".format(item))
