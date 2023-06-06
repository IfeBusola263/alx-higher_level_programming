#!/usr/bin/python3
def print_last_digit(number):
    ''' Return the value of last digit of number number.

    >>> print_last_digit(2000)
    0
    >>> print_last_digit(-5087)
    7
    >>> print_last_digit(698736)
    6
    '''

    if number < 0:
        number = number * -1
        return number % 10
    else:
        return number % 10
