#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A module for the Square like the previous"""


class Square:
    """A class for find the square of a number"""
    def __init__(self, size=0):
        """The __init__ method for constructing the obj
        Args:
            size (int): instance varaibles
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """An accessor of the instance variable __size"""
        return self.__size

    @size.setter
    def size(self, size):
        """A mutator of the instance varibale __size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """An instance method for getting the square of the instance
            variable x
        """
        return self.__size ** 2
