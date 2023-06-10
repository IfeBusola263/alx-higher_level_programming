#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    ''' List -> None

    Print item of the list 'my_list' in reverse order.

    >>> print_reversed_list_integer([1, 2, 3, 4, 5])
    5
    4
    3
    2
    1

    '''
    # confirm it is not an empty list
    if my_list is not None:

        # Reverse the list
        my_list.reverse()

        # loop through the list to display each item
        for item in my_list:
            print("{:d}".format(item))
