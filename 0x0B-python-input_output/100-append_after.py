#!/usr/bin/python3
''' This module implements a function that adds a line of text
to an existing file '''


def append_after(filename="", search_string="", new_string=""):
    ''' appends text 'new_string' to file 'filename' when string
    search string is found in any line in file 'filename' '''

    # open the file
    with open(filename, 'r', encoding='utf-8') as file:

        # loop through each line in the file
        lines = file.readlines()

    # re-open the file for comparison
    with open(filename, 'w', encoding='utf-8') as file:

        # loop through the list of lines from readlines
        for line in lines:

            file.write(line)
            # check if the string is in the line
            if search_string in line:

                # if it is found append the new string
                file.write(new_string)
