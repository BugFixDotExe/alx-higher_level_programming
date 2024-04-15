#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A class Rectangle that inherits from BaseGeometry"""

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """__init__ a constructor"""
        """
        Args:
            width (integers): first arg
            height (integers): second arg
        """
        self.__width = width
        self.__height = height

