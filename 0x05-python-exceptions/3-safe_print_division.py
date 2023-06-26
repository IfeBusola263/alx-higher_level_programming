#!/usr/bin/python3
def safe_print_division(a, b):
    ''' Returns the division of two integers.

    >>> safe_print_division(12,2)
    6.0
    >>> safe_print_division(12,0)
    None

    '''
    try:
        res = a / b
        return res
    except Exception:
        res = None
    finally:
        print("Inside result:", res)
