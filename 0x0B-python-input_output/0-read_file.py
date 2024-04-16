#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A module that reads a file in UTF-8 encoding"""


def read_file(filename=""):
    """read_file a function for reading a file given a path
        Args:
            filename (string): a filepath
    """
    if len(filename == 0):
        return
    with open(filename, encoding='UTF-8') as a_file:
        print(a_file.read())
