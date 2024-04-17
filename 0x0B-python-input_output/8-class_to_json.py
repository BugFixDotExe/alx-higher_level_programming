#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A that returns the dictionary
description with simple data structure
"""


def class_to_json(obj):
    """a function that returns the dictionary
    description with simple data structure
    Args:
        obj: a python object
    Returns:
        dictionary description with simple data structure
    """
    return obj.__dict__
