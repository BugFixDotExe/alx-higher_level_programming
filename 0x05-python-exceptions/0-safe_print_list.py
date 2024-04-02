#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        if x == 0:
            return 0
        for i in range(x):
            if my_list[i]:
                i += 1
                continue
        return i
    except IndexError:
        return i
