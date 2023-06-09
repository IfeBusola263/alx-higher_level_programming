#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    ''' List -> List

    Returns a new list without mutating the argument list 'my_list'.
    Returns the list 'my_list if index idx is negative or out of range

    >>> new_in_list([1, 2, 3, 4, 5], 3, 9)
    [1, 2, 3, 9, 5]
    >>> new_in_list([1, 2, 3, 4, 5], -3, 9)
    [1, 2, 3, 4, 5]
    >>> new_in_list([1, 2, 3, 4, 5], 10, 9)
    [1, 2, 3, 4, 5]

    '''
    # get the highest index of the list
    highest_index = len(my_list) - 1

    # check if index is not negative or out of range
    if idx >= 0 and idx <= highest_index:

        # create an empty list
        new_list = []

        # fill new_list with content of my_list
        for item in my_list:
            if my_list.index(item) == idx:
                new_list.append(element)
                continue
            new_list.append(item)

        return new_list
    # return the list my_list if idx is negative or out of range
    else:
        return my_list
