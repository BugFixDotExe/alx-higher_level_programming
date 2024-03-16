#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = 0
    len_of_list = len(my_list) - 1
    while len_of_list >= i:
        print("{:d}".format(my_list[len_of_list]))
        len_of_list -= 1
