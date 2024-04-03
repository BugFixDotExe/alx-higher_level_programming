#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""The module is another iteration of the Square module from previous."""


class Square:
    """The class Square to be used in construction of a Square type"""
    def __init__(self, size=0):
        """
        The __init__ method used for construction of obj
        Args:
            size (int): the input value to be attached to the obj
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """A getter method for the instance variable of the obj.
            Calculate the area of the private variable(instance variable)
           Returns:
                int: The area of the square.
        """
        return self.__size ** 2
