#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    ''' List of Lists -> List of List

    Return the list of lists in form of a matrix

    >>> matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

    1 2 3
    4 5 6
    7 8 9

    '''

    for item in matrix:
        for items in item:
            if items == item[-1]:
                print("{}".format(items), end='')
            else:
                print("{}".format(items), end=' ')
        print()
