#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    ''' List -> None

    Modifies a list 'my_list' at the given index 'idx' with item 'element'.
    if index 'idx' is negative returns my_list, same as out of range index.

    >>> new = replace_in_list([1, 2, 3, 4, 5], 3, 9)
    >>> new
    [1, 2, 3, 9, 5]
    >>> new = replace_in_list([1, 2, 3, 4, 5], -3, 9)
    >>> new
    [1, 2, 3, 9, 5]
    >>> new = replace_in_list([1, 2, 3, 4, 5], 8, 9)
    >>> new
    [1, 2, 3, 9, 5]

    '''

    # find the highest index of list
    highest_index = len(my_list) - 1

    # set condition to run if index is not negative or out of range
    if idx >= 0 and idx <= highest_index:
        my_list[idx] = element
        return my_list

    # return list if out of range or index is negative
    else:
        return my_list
