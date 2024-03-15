#!/usr/bin/python3
def no_c(my_string):
    for c in my_string:
        if c == 'c' or c == 'C':
            new_str = my_string.replace(c, "")
    return (new_str)
