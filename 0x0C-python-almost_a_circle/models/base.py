#!/usr/bin/python3
''' This module implements a class Base '''

import json
import os
import csv


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

        if cls.__name__ == "Rectangle":
            obj = cls(2, 3)
        else:
            obj = cls(2)

        obj.update(**dictionary)

        return obj

    @classmethod
    def load_from_file(cls):
        ''' Returns a list of instances created from a json file '''

        # open the json file to access dictionary of attributes for an instance
        # first check if the file exists

        list_of_instance = []
        filename = cls.__name__ + ".json"

        if "Rectangle" in filename or "Square" in filename:

            if os.path.exists("./" + filename):
                with open(filename, "r", encoding="utf-8") as file:
                    content_in_json = file.read().strip()
                    content = cls.from_json_string(content_in_json)

                # loop through the list creating instances
                for attr in content:

                    # append the instances into a new list
                    list_of_instance.append(cls.create(**attr))

                # return the list of instances
                return list_of_instance
            else:
                return list_of_instance

    @classmethod
    def save_to_file_csv(cls, list_objs):
        ''' saves the content of list_objects into a CSV file'''
        new_list = []

        # get file name
        if cls.__name__ in ("Rectangle", "Square"):
            filename = cls.__name__ + ".csv"

            # check if list_object is not empty and not None
            if list_objs is not None and len(list_objs) > 0:

                for item in list_objs:
                    new_list.append(item.to_dictionary())

                rect_attr = ["id", "width", "height", "x", "y"]
                sqr_attr = ["id", "size", "x", "y"]

                # open file for writing
                with open(filename, 'w', encoding="utf-8") as file:
                    if cls.__name__ == "Rectangle":

                        csv_rep = csv.DictWriter(file, fieldnames=rect_attr)
                        csv_rep.writeheader()
                        csv_rep.writerows(new_list)
                    else:
                        csv_rep = csv.DictWriter(file, fieldnames=sqr_attr)
                        csv_rep.writeheader()
                        csv_rep.writerows(new_list)
            else:
                with open("filename", 'w', encoding="utf-8") as file:
                    csv_rep = csv.writer(file)
                    csv_rep.writerow(new_list)

    @classmethod
    def load_from_file_csv(cls):
        ''' returns a list of instances created from a CSV file '''

        list_of_instance = []

        filename = cls.__name__ + ".csv"
        if "Rectangle" in filename or "Square" in filename:

            if os.path.exists("./" + filename):
                with open(filename, "r", encoding="utf-8") as file:
                    csv_rep = csv.DictReader(file)

                    for model in csv_rep:
                        for key, value in model.items():
                            model[key] = int(value)
                        list_of_instance.append(cls.create(**model))

                    return list_of_instance
            return list_of_instance
