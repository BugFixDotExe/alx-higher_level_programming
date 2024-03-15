#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    len_of_list = len(my_list) - 1
    cpy_list = my_list.copy()
    if idx < 0 or idx > len_of_list:
        return (cpy_list)
    else:
        cpy_list[idx] = element
        return (cpy_list)
