#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ''' Prints the elements(key/value) of a dictionary in sorted order

    >>> a_dictionary = { 'language': "C", 'Number': 89,
    'track': "Low level", 'ids': [1, 2, 3] }
    >>> print_sorted_dictionary(a_dictionary)
    Number: 89
    ids: [1, 2, 3]
    language: C
    track: Low level

    '''
    # sort the keys of the dictionary
    key_list = sorted(a_dictionary)

    # loop to print the key values
    for item in key_list:
        print("{}: {}".format(item, a_dictionary.get(item)))
