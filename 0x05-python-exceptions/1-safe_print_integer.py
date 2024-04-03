#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        elif isinstance(value, list):
            print("{:d}".format(value[0]))
            return True
        elif isinstance(value, tuple):
            print("{:d}".format(value[0]))
            return True
    except TypeError:
        return False
