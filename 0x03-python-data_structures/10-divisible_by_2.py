#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    demo = my_list.copy()
    for i in range(len(demo)):
        if demo[i] % 2 == 0:
            demo[i] = True
        else:
            demo[i] = False
    return (demo)
