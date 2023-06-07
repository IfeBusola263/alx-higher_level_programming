#!/usr/bin/python3
def uppercase(str):
    ''' Return uppercase format of each character in the string.

    >>> uppercase("best")
    BEST
    >>> uppercase("Best School 98 Battery street")
    BEST SCHOOL 98 BATTERY STREET
    '''
# Loop through each character
    for i in range(len(str)):
        check = ord(str[i]) >= 97 or ord(str[i]) <= 122
        print("{:c}".format(ord(str[i] - 1) if check else str[i]), end='')
    print()
