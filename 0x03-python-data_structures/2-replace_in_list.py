#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    len_of_list = len(my_list) - 1
    if idx < 0 or idx > len_of_list:
        return (my_list)
    else:
        my_list[idx] = element
        return (my_list)
