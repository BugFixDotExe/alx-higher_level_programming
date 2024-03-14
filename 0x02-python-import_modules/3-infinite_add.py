#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sum = 0
    arg_len = len(sys.argv)
    arg_len = arg_len - 1
    if arg_len == 0:
        print(arg_len)
    elif arg_len == 1:
        print("{:d}".format(int(sys.argv[1])))
    elif arg_len > 1:
        for i in range(1, len(sys.argv)):
            sum += int(sys.argv[i])
        print("{:d}".format(sum))
