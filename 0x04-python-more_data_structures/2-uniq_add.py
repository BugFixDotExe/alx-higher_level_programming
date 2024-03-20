#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return
    sum_of_item = 0
    my_list = set(my_list)
    my_list = list(my_list)
    for i in my_list:
        sum_of_item += i
    return (sum_of_item)
