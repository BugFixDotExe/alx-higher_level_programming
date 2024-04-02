#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value + "a":
            return False
    except TypeError:
        print("{:d}".format(value))
        return True
