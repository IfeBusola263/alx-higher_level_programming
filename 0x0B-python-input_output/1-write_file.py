#!/usr/bin/python3
''' This module implements a function that writes to a file '''


def write_file(filename="", text=""):
    ''' Returns number of text written to file filename '''

    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
