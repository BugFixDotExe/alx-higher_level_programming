#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        i = 0;
        type_int = 0
        if x == 0:
            return type_int
        for i in range(x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                type_int += 1
            else:
                continue
        print()
        return type_int
    except IndexError:
        return type_int
