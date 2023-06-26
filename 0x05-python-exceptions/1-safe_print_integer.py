#!/usr/bin/python3
def safe_print_integer(value):
    ''' Return True if an integer has been correctly printed
    and false otherwise

    >>> safe_print_integer(89)
    89
    >>> safe_print_integer(-89)
    -89
    >>> safe_print_integer("school")
    False

    '''
    try:
        print("{:d}".format(value))
        return True

    except Exception as err:
        return False
