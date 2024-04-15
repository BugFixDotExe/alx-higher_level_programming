#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A module that returns True or False"""


def is_same_class(obj, a_class):
    """is_same_class
        A method that returns True if obj is
        instance of a_class,False otherwise
        Args:
            obj: a python object
            a_class: a python class
        Returns:
            True: if obj is instance of a_class
            False: if obj is not instance of a_class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
