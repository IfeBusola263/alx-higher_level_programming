#!/usr/bin/python3
''' The matrix division module '''


def matrix_divided(matrix, div):
    ''' Returns a new matrix with the elements list of lists matrix
    divided by div'''

    main_list = []
    if type(matrix) is not list or len(matrix)< 2:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if matrix == None or div == None:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for item in matrix:
        inner_list = []

        if type(item) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        for num in item:
            if type(num) in [int, float]:
                inner_list.append(round(num/div, 2))
            else:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        main_list.append(inner_list)

    return main_list
