#!/usr/bin/python3
''' This module implements a class Base '''


class Base:
    ''' This class base class of all other class '''

    __nb_objects = 0

    def __init__(self, id=None):
        ''' Magic method which is called after every instance of the
        class is created '''

        if isinstance(id, int) and id < 0:
            raise ValueError("id cannot be negative")

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
