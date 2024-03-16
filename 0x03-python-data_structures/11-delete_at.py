#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    len_of_list = len(my_list) - 1
    if idx > len_of_list or idx < 0:
        return (my_list)
    for i in range(len(my_list)):
        if i == idx:
            my_list[idx] = my_list[idx+1]
        my_list[i] = my_list[i+1]

    return (my_list)
