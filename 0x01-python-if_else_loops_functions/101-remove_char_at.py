#!/usr/bin/python3
def remove_char_at(str, n):
    ''' Return a list characters with the nth item removed

    >>> remove_char_at("Best School", 3)
    Bes School
    >>> remove_char_at("Chicago", 2)
    Chcago
    >>> remove_char_at("C is fun!", 0)
     is fun!
    >>> remove_char_at("Python", -2)
    Python
    '''
    ret = ''
# check if n is negative index and concatenate each char to the empty string
    if n < 0:
        for i in range(len(str)):
            ret += str[i]
        return ret
# if n is not negative concatenate with empty string, excluding index n
    else:
        for i in range(len(str)):
            if i != n:
                ret += str[i]
        return ret
