#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is a modue called rectangle that aims to define a rectangle"""


class Rectangle:
    """A class that defines a Rectangle"""

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            """
            The __init__ method constructs an obj
            Args:
                width (int): first parameter
                height (int): second parameter
            """
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must bean integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        per = 0
        if self.__width == 0 or self.__height == 0:
            return per
        per = 2 * (self.__width + self.__height)
        return per

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print()
        return ""
