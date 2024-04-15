#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A module that returns a boolean given a class"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class
        A function that returns True
        or Flase, given an obj and a class
        Args:
            obj: the object
            a_class: the class
        Returns:
            True: if obj is instance
            False if obj is not instance
    """
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
