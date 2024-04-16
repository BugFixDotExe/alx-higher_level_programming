#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A module that appends to a file in UTF-8 encoding"""


def append_write(filename="", text=""):
    """append_write a function for reading a file given a path
        Args:
            filename (string): a filepath
            text (string): the text to be written
        Returns:
            number of characters appended (int)
    """
    if len(text) == 0:
        return (0)
    with open(filename, mode="a", encoding="UTF-8") as a_file:
        return a_file.write(text)
