#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return
    mul_of_two = a_dictionary.copy()
    for key, value in mul_of_two.items():
        mul_of_two[key] *= 2
    return (mul_of_two)
