#!/usr/bin/python3
def best_score(a_dictionary):
    ''' Returns the key with the highest value in a dictionary

    >>> a_dictionary = {'John': 12, 'Bob': 14,
    'Mike': 14, 'Molly': 16, 'Adam': 10}
    >>> best_score(a_dictionary)
    >>> Molly
    >>>
    >>> best_score(None)

    '''

    # if the dictionary is an empty dictionary
    # otherwise find the maximum value
    if a_dictionary is not None:
        val_list = a_dictionary.values()
        max_val = max(val_list)

        # loop the dictionary to match the value with max_val to return key
        for key, value in a_dictionary.items():
            if value == max_val:
                return key
    else:
        return None
