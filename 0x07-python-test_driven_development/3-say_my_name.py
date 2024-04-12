#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A moudle that has a function
   say_my_name that prints the name entered
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name a function that prints My name is <first name> <last name>
    Args:
        first_name (string): The first parameter
        last_name (string): The first parameter
    Returns: nothing
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if len(first_name) == 0 and len(last_name) == 0:
        raise ValueError("first_name must be " +
                         "a string and last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
