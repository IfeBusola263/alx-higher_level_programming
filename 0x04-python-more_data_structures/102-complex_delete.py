#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    ''' Delete key in dictionary 'a_dictionary' with the value 'value' '''

    list_keys = []
    for key, val in a_dictionary.items():
        if val == value:
            list_keys.append(key)
    for items in list_keys:
        del a_dictionary[items]
    return a_dictionary
