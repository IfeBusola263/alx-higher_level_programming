#!/usr/bin/python3

def roman_to_int(roman_string):
    ''' Return the coversion of a roman numeral instance '''

    ret = 0
    if type(roman_string) is str:
        rom = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        pattern = [rom.get(item) for item in roman_string]
        for item in range(1, len(pattern)):
            if pattern[item - 1] < pattern[item]:
                pattern[item] = pattern[item] - pattern[item - 1]
                pattern[item - 1] = 0
        return sum(pattern)
    else:
        return 0
