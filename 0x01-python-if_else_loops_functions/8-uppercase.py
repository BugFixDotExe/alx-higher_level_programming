#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            str_ret = chr(ord(str[i]) - 32)
        else:
            str_ret = str[i]
        print("{:s}".format(str_ret), end="")
    print("{:s}".format(""))
