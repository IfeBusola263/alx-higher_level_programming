#!/usr/bin/python3
from functools import reduce


def roman_to_int(roman_string):
    ''' Return the coversion of a roman numeral instance '''
    if type(roman_string) is str:
        rom = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        pattern = [rom.get(item) for item in roman_string]
        return reduce(lambda x, y: x if x > y else y - x, pattern)
    else:
        return 0
