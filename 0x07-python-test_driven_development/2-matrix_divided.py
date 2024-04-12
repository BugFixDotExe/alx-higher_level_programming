#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This module contains a function who has
    the sole purpose of dividing a matrix
    by the given div and returning it back
    to it's caller
"""


def matrix_divided(matrix, div):
    """matrix_divided a function that divides a matrix by div
    Args:
        matrix (list): The first parameter, a list(any type)
        div (number): The second parameter, a number
    Return:
        Returns a new matrix
    """
    type_err_message = "matrix must be a matrix (list of lists) of integers/floats"
    if (len(matrix) == 0):
        raise IndexError("list index out of range")
    if not isinstance(matrix[0], list):
        raise TypeError(type_err_message)
    len_sub_matrix = len(matrix[0])

    cpy = list(map(list, matrix))
    for sub_list in range(len(cpy)):
        if not isinstance(cpy[sub_list], list):
            raise TypeError(type_err_message)
        if len(cpy[sub_list]) != len_sub_matrix:
            raise TypeError("Each row of the matrix must have the same size")
        for value in range(len(cpy[sub_list])):
            if not isinstance(cpy[sub_list][value], int) and not isinstance(cpy[sub_list][value], float):
                raise TypeError(type_err_message)
            if div == 0:
                raise ZeroDivisionError("division by zero")
            cpy[sub_list][value] = round((cpy[sub_list][value]) / div, 2)
    return (cpy)
