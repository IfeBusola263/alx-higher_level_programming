#!/usr/bin/python3
''' This module implements a class Base '''

import json


class Base:
    ''' This class base class of all other class '''

    __nb_objects = 0

    def __init__(self, id=None):
        ''' Magic method which is called after every instance of the
        class is created '''

        if isinstance(id, int) and id < 0:
            raise ValueError

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' The method converts python objects to JSON
        string for parsing '''

        if list_dictionaries is None:
            return '[]'
        if isinstance(list_dictionaries, list) and len(list_dictionaries) < 1:
            return '[]'

        return json.dumps(list_dictionaries, sort_keys=True)
