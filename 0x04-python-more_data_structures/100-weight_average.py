#!/usr/bin/python3
def weight_average(my_list=[]):
    ''' Returns weighted average of the list of tuples '''

    tup_add = 0
    weight_add = 0

    if my_list is not None:
        for item in my_list:
            a, b, *_ = item + (0, 0)
            tup_add += (a * b)
            weight_add += b
        return tup_add / weight_add
    else:
        return 0
