#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A module with an empty class"""


class BaseGeometry:
    """BaseGeometry an empty class"""
    def area(self):
        """An emmpty public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """An public instance method that validates an int
            Args:
                name (string): a string value
                value (int): an int value
        """
        if isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
