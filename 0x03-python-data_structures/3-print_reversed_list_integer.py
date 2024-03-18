#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        print("{:d}".format(len(my_list)))
    elif len(my_list) == 1:
        print("{:d}".format(my_list[0]))
    else:
        len_of_list = len(my_list)-1
        while len_of_list >= 0:
            print("{:d}".format(my_list[len_of_list]))
            len_of_list -= 1
