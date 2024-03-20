#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = []
    if matrix is None:
        return
    for sub_list in matrix:
        squared.append(list(map(lambda val: val * val, sub_list)))
    return (squared)
