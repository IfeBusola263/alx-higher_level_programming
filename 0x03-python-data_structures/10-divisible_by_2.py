#!/usr/bin/python
def divisible_by_2(my_list=[]):
    ''' List -> list of (bool)

    Returns a list of boolean values 'True' of 'False' corresponding to the
    integer, provided the integer at the index is divisible by 2 or a multiple
    of integer 2

    >>> divisible_by_2([0, 1, 2, 3])
    ['True', 'False', 'True', 'False']
    >>> divisible_by_2([-1, -10, -5, 0])
    ['False', 'True', 'False', 'True']

    '''
    # Create an empty list to store new item
    new_list = []

    # loop through list using modulo
    for item in my_list:

        # Handle negative item
        if item < 0:
            new_var = abs(item)
            if new_var % 2 == 0:
                new_list.append(True)
            else:
                new_list.append(False)

        # For positive integars
        else:
            if item % 2 == 0:
                new_list.append(True)
            else:
                new_list.append(False)

    return new_list
