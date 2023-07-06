#!/usr/bin/python3
''' Module for string operations '''


def say_my_name(first_name, last_name=""):
    ''' Prints the first name(first_name) and the last name
    (last_name), if last name is provided. If last name is
    is not provided only first name is printed '''

    if first_name in [None, ""]:
        raise TypeError("first_name must be a string")

    if type(first_name) is not str or first_name.isdigit() is True:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str or last_name.isdigit() is True:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
