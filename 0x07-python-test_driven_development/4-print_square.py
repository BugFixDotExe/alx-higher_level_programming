#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A module that prints square's given the size"""


def print_square(size):
    """print_square function, takes size and prints a #
        Args:
            size (int): number of # to be printed
    """
    if size is None:
        raise TypeError("print_square() " +
                        "missing 1 required positional argument: 'size'")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    else:
        for i in range(size):
            for i in range(size):
                print("#", end="")
            print()
