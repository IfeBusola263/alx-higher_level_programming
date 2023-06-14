#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    ''' Returns the squares of the individual elements of the matrix
    without mutating the given nested list.

    >>> square_matrix_simple([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
    [[1, 4, 9], [16, 25, 36], [49, 64, 81]]

    '''

    # create new list, the outer list
    new_matrix = []

    # loop through the nested list to access each list
    for row in matrix:
        inner_list = []

        # loop through the inner list and perform operations
        # then populate the new inner list
        for item in row:
            inner_list.append(item * item)

        # populate the new list after each operation on each inner list
        new_matrix.append(inner_list)

    return new_matrix
