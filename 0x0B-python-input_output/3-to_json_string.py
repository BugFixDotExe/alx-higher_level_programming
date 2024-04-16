#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A module that returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """to_json_string function that returns the JSON
        representation of an object(string)
    Args:
        my_obj: a python object
    Returns:
        a string repersentation of my_obj
    """
    return json.dumps(my_obj)
