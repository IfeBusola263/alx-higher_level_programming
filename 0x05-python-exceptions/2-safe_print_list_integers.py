#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ''' Prints the integers in the list 'my_list' and quietly
    skips other data types. any out of range index is raised.

    >>> safe_print_list_integers([1, 2, 3, 4, 5], 2)
    12

    >>> safe_print_list_integers([1, 2, 3, 4, 5], 5)
    12345

    >>> safe_print_list_integers([1, 2, 3, 4, 5], 8)
    12345Traceback (most recent call last):
    File "./2-main.py", line 14, in <module>
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
    File "/0x05/2-safe_print_list_integers.py", line 7,
    in safe_print_list_integers
    print("{:d}".format(my_list[i]), end="")
    IndexError: list index out of range
    '''
    count = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end='')
                count += 1
        print()
        return count
    except Exception:
        raise
