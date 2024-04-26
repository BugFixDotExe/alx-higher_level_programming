#!/usr/bin/python3
import json
class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        elif id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries)
    def save_to_file(cls, list_objs):
        if list_objs is None:
