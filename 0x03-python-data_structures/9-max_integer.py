#!/usr/bin/python3
def max_integer(my_list=[]):
    ''' List -> (int)

    Return the biggest integer in the list 'my_list'. if the list is
    empty, return None

    >>> max_integer([1, 90, 2, 13, 34, 5, -13, 3])
    90
    >>> max_integer([])
    None
    '''

    if my_list != []:
        new_list = sorted(my_list)
        return new_list[-1]
    else:
        return
