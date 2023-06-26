#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ''' Returns the number of elements printed from my_list
    prints the content of my_list

    >>> safe_print_list([1, 2, 3, 4, 5], 2)
    2
    12
    >>> safe_print_list([1, 2, 3, 4, 5], 5)
    5
    12345
    >>> safe_print_list([1, 2, 3, 4, 5], 4)
    4
    1234
    >>> safe_print_list([1, 2, 3, 4, 5], 8)
    5
    12345

    '''
    count = 0

    try:
        for i in range(x):
            print("{}".format(my_list[i]), end='')
            count += 1
        print()
        return x
    except Exception as err:
        print()
        return count
