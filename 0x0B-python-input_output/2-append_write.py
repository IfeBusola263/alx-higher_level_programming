#!/usr/bin/python3
''' This module implements a funtion that appends text to a file '''


def append_write(filename="", text=""):
    ''' Appends text 'text' to file 'filename' and returns
    the number of characters appended '''

    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
