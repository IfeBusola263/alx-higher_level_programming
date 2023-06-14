#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    ''' Replace or adds (as necessary) the key/ value in a dictioanary

    >>> a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
    >>> update_dictionary(a_dictionary, 'language', "Python")
    >>> a_dictonary
    { 'language': "C", 'number': 89, 'track': "Low level", language', "Python"}

    '''

    a_dictionary[key] = value
    return a_dictionary
