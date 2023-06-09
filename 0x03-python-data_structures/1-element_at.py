#!/usr/bin/python3
def element_at(my_list, idx):
    ''' list -> Any(int, float,str)

    Returns an element of a list my_list at index idx, if index idx
    is negative, return none, same as out of range index

    >>> element_at([1, 2, 3, 4, 5], 3)
    4
    >>> element_at([1, 2, 3, 4, 5], -2)
    None
    >>> element_at([1, 2, 3, 4, 5], 7)
    None

    '''
    # store highest index
    highest_index = len(my_list) - 1

    # check for negative index and out of range
    # if found return 'None'
    if idx < 0 or idx > highest_index:
        return

    # return item at valid index
    else:
        return my_list[idx]
