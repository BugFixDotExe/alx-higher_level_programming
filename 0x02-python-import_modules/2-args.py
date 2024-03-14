#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_len = len(sys.argv)
    arg_len = arg_len - 1
    if arg_len == 0:
        print("{:d} arguments.".format(0))
    elif arg_len == 1:
        print("{:d} argument:\n{:d}: {:s}".format(
            arg_len, arg_len, sys.argv[1]))
    elif arg_len > 1:
        print("{:d} arguments:".format(arg_len))
        for i in range(1, len(sys.argv)):
            print("{:d}: {:s}".format(i, sys.argv[i]))
