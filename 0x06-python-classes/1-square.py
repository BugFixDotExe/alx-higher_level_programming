#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
The module has the sole purpose of defining a square given an input
"""


class Square:
    """A Class that defines a square given an input"""
    def __init__(self, size):
        """
        The __init__ method for construction or binding the obj with attributes
        Args:
            size (int): input size for defining a square
        """
        self.__size = size
