#!/usr/bin/python3
def no_c(my_string):
    sub_str = []
    for i in range(len(my_string)):
        if my_string[i] == "c" or my_string[i] == "C":
            continue
        else:
            sub_str.append(my_string[i])
    _str = ''.join(str(char) for char in sub_str)
    return (_str)
