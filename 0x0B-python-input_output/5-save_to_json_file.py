#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A module that writes an Obj to a text file, using a JSON repr"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file a function that saves a JSON reper to a file
    Args:
        my_obj: fitst args
        filename (string): name of the file
    """
    if type(my_obj) == set:
        raise TypeError("Object of type set is not JSON serializable")
    with open(filename, mode="w", encoding="UTF-8") as a_file:
        a_file.write(json.dumps(my_obj))
