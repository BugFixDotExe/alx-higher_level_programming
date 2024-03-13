#!/usr/bin/python3
def remove_char_at(str, n):
    temp = list(str[0:len(str)])
    if n > len(str) or n < 0:
        return str
    temp[n] = ""
    temp = ''.join(temp)
    return (temp)
