#!/usr/bin/python3
''' This module implements a class and it's methods '''


class Student:
    ''' This is a student class '''
    def __init__(self, first_name, last_name, age):
        ''' This init method initializes the fields of the class '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        ''' Retrives a dictionary representation of the class '''
        return self.__dict__
