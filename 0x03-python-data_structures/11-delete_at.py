#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    ret_list = []
    len_of_list = len(my_list) - 1
    if idx > len_of_list or idx < 0:
        return (my_list)
    for i in range(len(my_list)):
        if i == idx:
            del my_list[i]
    return (my_list)
