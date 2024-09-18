#!/usr/bin/python3
"""Creating a base class"""

import json


class Base:
    """Defining class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing class Base"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = idi

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returning json string representation of list of dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
