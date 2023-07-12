#!/usr/bin/python3
''' This module implements a function that adds a line of text
to an existing file '''


def append_after(filename="", search_string="", new_string=""):
    ''' appends text 'new_string' to file 'filename' when string
    search string is found in any line in file 'filename' '''

    # open the file
    with open(filename, 'a+', encoding='utf-8') as mine:

        # loop through each line in the file
        for line in mine:

            line = mine.read()

            # loop through each word in the line and compare with search_string
            if line.find(search_string) >= 0:

                # if it is found append the new string
                mine.write(new_string)
