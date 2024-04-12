#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A module that adds two integers and returns the sum
    Using the doctest in  interactive mode we perform
    a test on this module
"""


def add_integer(a, b=98):
    """add_integer a function that adds two ints
        there's also a float to int taking place
    Args:
        a: The first parameter
        b: The second parameter, with default
    Returns:
        int: The return is the sum of a + b
    """
    if a is None or type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if b is None or type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        if isinstance(a, float):
            a = int(a)
        if isinstance(b, float):
            b = int(b)
        return a + b
