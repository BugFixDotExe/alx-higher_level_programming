#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A module that writes to a file in UTF-8 encoding"""


def write_file(filename="", text=""):
    """read_file a function for reading a file given a path
        Args:
            filename (string): a filepath
            text (string): the text to be written
        Returns:
            number of characters written (int)
    """
    if len(text) == 0:
        return (0)
    with open(filename, mode="w", encoding="UTF-8") as a_file:

