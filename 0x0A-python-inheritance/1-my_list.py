#!/usr/bin/python3
''' This module implements a class that inherits from the List class'''


class MyList(list):
    ''' This class inherits from the list class '''

    def __init__(self):
        ''' initializes when an instance of the class is created '''
        list.__init__(self)

    def print_sorted(self):
        ''' prints the list, sorted in ascending order '''
        new_list = sorted(self)

        print(new_list)
