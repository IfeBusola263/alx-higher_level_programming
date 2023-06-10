#!/usr/bin/python3
def multiple_returns(sentence):
    ''' str -> tuple

    Return a tuple with the length of the string sentence
    and the first character, None if sentence is empty

    >>> multiple_returns("At school, I learnt C!")
    (22, 'A')
    >>> multiple_returns("Jesus is Lord!")
    (14, 'J')

    '''
    # Check if sentence is not empty
    if sentence != "":

        # Use tuple packing to create tuple
        new_tuple = len(sentence), sentence[0]

        # return the new tuple
        return new_tuple
    else:
        # return zero and None
        return 0, None
