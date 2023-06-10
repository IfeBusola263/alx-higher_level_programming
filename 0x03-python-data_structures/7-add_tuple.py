#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ''' Tuple + Tuple -> Tuple

    Return the concatenation of Tuples

    >>> add_tuple((1, 89), (88, 11))
    (89, 100)
    >>> add_tuple((1, 89), (1, ))
    (2, 89)
    >>> add_tuple((1, 89), ())
    (1, 89)

    '''
    len_tupa = len(tuple_a)
    len_tupb = len(tuple_b)

    if len_tupa >= 2:
        first1, second1 = tuple_a[0], tuple_a[1]
    else:
        if len_tupa == 1:
            first1, second1 = tuple_a[0], 0
        else:
            first1, second1 = 0, 0

    if len_tupb >= 2:
        first2, second2 = tuple_b[0], tuple_b[1]
    else:
        if len_tupb == 1:
            first2, second2 = tuple_b[0], 0
        else:
            first2, second2 = 0, 0

    new_tup = first1 + first2, second1 + second2
    return new_tup
