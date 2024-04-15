#!/usr/bin/pyton3
# -*- coding: utf-8 -*-
"""a module for printing attr and method of an obj"""


def lookup(obj):
    """a function that returns the list of available
    attributes and methods of an object
    Args:
        obj: The first parameter
    Returns:
        list: A list of methods and objects
    """
    return dir(obj)
