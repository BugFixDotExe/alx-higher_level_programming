#!/usr/bin/python3
def max_integer(my_list=[]):
    len_of_list = len(my_list)
    if len_of_list == 0:
        return (None)
    else:
        current_largest = my_list[0]
        for val in my_list:
            if val >= current_largest:
                current_largest = val
        return (current_largest)
