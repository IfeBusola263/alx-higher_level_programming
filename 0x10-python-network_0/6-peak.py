#!/usr/bin/python3
"""
This module implements a function to find the peak of a list

"""

def find_peak(list_of_integers):
    '''
    The function finds the peak of a list
    '''

    if list_of_integers is not None and len(list_of_integers) != 0:
        if len(list_of_integers) % 2 == 0:
            return max(max(list_of_integers[:2]), max(list_of_integers[-2:-1]))
        else:
            return max(list_of_integers[-2:-1])

    else:
        return None
