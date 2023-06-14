#!/usr/bin/python3
def uniq_add(my_list=[]):
    ''' Returns the addition the unique elements of a list

    >>> my_list = [1, 2, 3, 1, 4, 2, 5]
    >>> uniq_add(my_list)
    15

    '''

    new_set = set(my_list)

    return sum(new_set)
