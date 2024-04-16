#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A module that returns the object representation of JSON"""
import json


def from_json_string(my_str):
    """from_json_string function that returns a string
        representation into aof a JSON reper.
    Args:
        my_str (string): a python string of JSON
    Returns:
        a JSON repersentation of my_str
    """
    return json.loads(my_str)
