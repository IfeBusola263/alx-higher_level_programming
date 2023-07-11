#!/usr/bin/python3
''' This module implements a class and it's methods '''


class Student:
    ''' This is a student class '''
    def __init__(self, first_name, last_name, age):
        ''' This init method initializes the fields of the class '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' Retrives a dictionary representation of the class '''
        list_dict = {}

        # check if the attr is a list
        if isinstance(attrs, list):

            # loop through the list
            for item in attrs:

                # compare the item to the key
                for key, value in self.__dict__.items():

                    # if they are thesame add to the empty dictionary
                    if item is key:
                        list_dict[key] = value

            # After compilation return the list
            return list_dict

        # if the attrs is not a list just return the dictionary
        return self.__dict__
