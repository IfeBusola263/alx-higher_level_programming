#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    ''' Returns the symmetric difference of the sets 'set_1' and 'set_2'

    >>> set_1 = { "Python", "C", "Javascript" }
    >>> set_2 = { "Bash", "C", "Ruby", "Perl" }
    >>> only_diff_elements(set_1, set_2)
    {'Bash', 'Javascript', 'Perl', 'Python', 'Ruby'}

    '''
    return set_1 ^ set_2
