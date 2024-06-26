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
            Raises:
                TypeError: when value is not an int
                ValueError: when value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
        if type(name) == None and type(value) == None:
            raise TypeError("integer_validator() missing 2 required positional arguments: 'name' and 'value'")
        if type(value) == None:
            raise TypeError("integer_validator() missing 1 required positional argument: 'value'")
        if type(name) == None:
            raise TypeError("integer_validator() missing 1 required positional argument: 'name'")
