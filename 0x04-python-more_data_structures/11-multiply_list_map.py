#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    ''' Return a list 'my_list' with all the elements nultiplied by 'number'

    >>> my_list = [1, 2, 3, 4, 6]
    >>> multiply_list_map(my_list, 4)
    [4, 8, 12, 16, 24]

    '''
    new_list = list(map(lambda x : x * number, my_list))

    return new_list
