#!/usr/bin/python3
def common_elements(set_1, set_2):
    ''' Returns a set of common elements in set 'set_1' and 'set_2'

    >>> set_1 = { "Python", "C", "Javascript" }
    >>> set_2 = { "Bash", "C", "Ruby", "Perl" }
    >>> common_elements(set_1, set_2)
    {'C'}

    '''

    return set_1 & set_2
