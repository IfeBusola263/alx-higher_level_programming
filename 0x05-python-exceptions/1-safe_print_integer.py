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
        if isinstance(value, int) and int(value):
            print("{:d}".format(int(value)))
            return True

    except Exception as err:
        return False
