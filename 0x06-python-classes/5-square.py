#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A module for the Square like the previous"""


class Square:
    """A class for finding the quare of a number"""
    size = 0
    print(size)
    def __init__(self, size=0):
        """The __init__ method for obj construction
        Args:
            size (int): the args to be binded to the obj
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    @property
    def size(self):
        """An accessor for __size"""
        return self.__size

    @size.getter
    def size(self, size):
        """ A mutator for __size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """An instance method for accessing __size ** 2"""
        return self.__size ** 2

    def my_print(self):
        """An instance method that prints # given size"""
        for i in range(size):
            for j in range(size):
                print("#",end="")
