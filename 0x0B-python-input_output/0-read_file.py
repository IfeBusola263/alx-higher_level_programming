#!/usr/bin/python3
''' This module implements a function that reads text '''


def read_file(filename=""):
    ''' Prints read text to standard output '''

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
