#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        if x == 0:
            return 0
        for i in range(x):
            if my_list[i]:
                print("{:d}".format(my_list[i]), end="")
                i += 1
                continue
        print()
        return i
    except IndexError:
        print()
        return i
