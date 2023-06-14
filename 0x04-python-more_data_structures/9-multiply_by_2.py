#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ''' Return a new dictionary with all the values multiplied by 2

    >>> a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14,
    'Mike': 14, 'Molly': 16}
    >>> multiply_by_2(a_dictionary)
    >>> a_dictionary = {'John': 24, 'Alex': 16,
    'Bob': 28, 'Mike': 28, 'Molly': 32}

    '''

    new_dictionary = {}

    for key, value in a_dictionary.items():
        new_dictionary[key] = value * 2

    return new_dictionary
