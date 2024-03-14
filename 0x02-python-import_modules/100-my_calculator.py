#!/usr/bin/python3
import sys
if __name__ == "__main__":
    import calculator_1 as cal

    arg_len = len(sys.argv)
    # This checks for the len of args
    arg_len = arg_len - 1
    if (arg_len < 3 or arg_len != 3):
        print("Usage: {:s} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)

    # This checks for a valid operator
    op = sys.argv[2]
    if op == "+":
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        ret_add = cal.add(a, b)
        print("{:d} + {:d} = {:d}".format(a, b, ret_add))

    elif op == "-":
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        ret_sub = cal.sub(a, b)
        print("{:d} - {:d} = {:d}".format(a, b, ret_sub))

    elif op == "*":
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        ret_mul = cal.mul(a, b)
        print("{:d} * {:d} = {:d}".format(a, b, ret_mul))

    elif op == "/":
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        ret_div = cal.div(a, b)
        print("{:d} / {:d} = {:d}".format(a, b, ret_div))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
