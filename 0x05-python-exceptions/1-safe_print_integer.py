#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        if len(value) >= 1:
            if isinstance(value[0], int):
                print("{:d}".format(value[0]))
                return True
    except TypeError:
        return False
