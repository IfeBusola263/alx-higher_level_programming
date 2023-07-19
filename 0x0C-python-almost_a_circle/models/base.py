#!/usr/bin/python3
''' This module implements a class Base '''

import json
import os


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

    @classmethod
    def save_to_file(cls, list_objs):
        ''' The saves the json representation of a python object
        in a file '''

        # get the name of the class calling the method
        # create file name
        filename = cls.__name__ + ".json"
        # insts = ["Rectangle", "Square"]

        if list_objs is not None and len(list_objs) > 0:

            # get dictionary representation of model
            js_dict = []
            for cls in list_objs:
                js_dict.append(cls.to_dictionary())

                # for inst in insts:

                # check the class to work with
                # if inst in str(type(list_objs[0])):

                # j_file = "./" + inst + ".json"
                # oj_file = inst + ".json"
                # check if the file exists

            if os.path.exists("./" + filename):
                # open the file for writing
                with open(filename, "w", encoding="utf-8") as file:
                    file.write(Base.to_json_string(js_dict))

            # If the file does not exist
            else:
                with open(filename, "w", encoding="utf-8") as file:
                    file.write(Base.to_json_string(js_dict))

        else:
            with open(filename, "w", encoding="utf-8") as file:
                file.write('[]')

    @staticmethod
    def from_json_string(json_string):
        ''' Returns the list of a json string, after converting
        the json string '''

        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        ''' Returns an instance of the class calling the method '''

        obj = cls(2, 3, 5, 6)

        obj.update(**dictionary)

        return obj
