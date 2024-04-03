#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A module that bulds on the last square module"""


class Square:
    """A class that defines a Square obj
    The __init__ method used for construction an obj
    Args:
        size (int): used for instance variable instantiation
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
