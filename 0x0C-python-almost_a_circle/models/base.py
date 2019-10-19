#!/usr/bin/python3
import json


""" Base class module
"""


class Base:
    """ Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.
        list_dictionaries: a list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.
        list_objs: a list of instances who inherits of Base.
        """
        with open(cls.__name__ + ".json", 'w', encoding="UTF-8") as myfile:
            mylist = []
            for obj in list_objs:
                mylist.append(obj.to_dictionary())
            myfile.write(cls.to_json_string(mylist))
