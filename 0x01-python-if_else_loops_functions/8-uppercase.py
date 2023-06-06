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
# if the character is within the small letter ascii alphabets
        if ord(str[i]) >= 97 or ord(str[i]) <= 122:
# convert it to capital letter and print it
            print("{:c}".format(ord(str[i]) - 32), end='')
# if it is not print it as is
        else:
            print("{}".format(str[i]), end='')
# print a new line
    print()
