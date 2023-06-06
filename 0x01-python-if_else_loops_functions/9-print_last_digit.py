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
        last_digi = number % 10
        print("{}".format(last_digi), end='')
        return last_digi
    else:
        last_digi = number % 10
        print("{}".format(last_digi), end='')
        return last_digi
