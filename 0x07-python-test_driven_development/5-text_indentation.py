#!/usr/bin/python3
''' This module houses functions functions that manipulates strings '''


def text_indentation(text):
    ''' Prints the portion of string with '.', '?' and ':'
    as delimeters in the sentence and also ensure that each line
    is striped of whitespaces, both at the beginning and ending
    of the text '''

    if type(text) is not str:
        raise TypeError("text must be a string")

    # create an empty string
    line = ""

    # loop through the string checking each character
    for word in text.strip():

        # check for delimeter
        if word in ['.', '?', ':']:

            # once delimiter is found strip white space and print
            line = line + word
            print(line.strip())
            print()

            # reset line to empty string
            line = ""

        # When delimiter is not found keep concatenating
        else:
            line = line + word

    # display the last line if no delimeter was found
    print(line.strip(), end='')
