#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    ''' Executes the  function fct safely with the arguments
    args
    '''
    # unpack arguments
    a, b = args

    try:
        # pass the arguments into the function
        result = fct(a, b)
        return result

    # return None if an error occurs and print error to
    # standard error
    except Exception as err:
        print("Exception:", err, file=sys.stderr)
        return None
