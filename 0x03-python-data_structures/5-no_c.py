#!/usr/bin/python3
def no_c(my_string):
    ''' str -> str

    Returns a new string with every 'c' and 'C' characters deleted
    from the new string

    >>> no_c("Best School")
    Best Shool
    >>> no_c("Chicago")
    hiago
    >>> no_c("C is fun!")
     is fun!

    '''

    # create an empty string
    new_str = ""

    # loop through the string
    for i in my_string:

        # check if any of the character is 'cC'
        if i not in 'cC':

            # if it's not concatenate with new_str
            new_str += i

    # return the new string
    return new_str
