#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A module that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """load_from_json_file a function that creates an obj
        from  a JSON file
        Args:
            filename (string): a filename
        Returns:
            Returns a python obj
    """
    if len(filename) == 0:
        return None
    with open(filename, encoding="UTF-8") as a_file:
        return json.loads(a_file.read())
