#!/usr/bin/python3
def weight_average(my_list=[]):
    ''' Returns weighted average of the list of tuples '''

    tup_add = 0
    weight_add = 0

    if len(my_list) > 0:
        for item in my_list:
            a, b = item
            tup_add += (a * b)
            weight_add += b
        return float(tup_add / weight_add)
    else:
        return 0
