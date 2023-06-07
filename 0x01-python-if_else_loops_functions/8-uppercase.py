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
        # check if the character is a small letter ascii alphabet
        check = ord(str[i]) >= 97 and ord(str[i]) <= 122

        # if small letter convert, if not, just print the character
        print("{:c}".format(ord(str[i]) - 32) if check else str[i], end='')

    # display the new line after words, since i have ceased the newlne with end
    print()
