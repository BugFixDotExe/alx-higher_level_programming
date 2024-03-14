#!/usr/bin/python3
import calculator_1 as cal

if __name__ == "__main__":
    a = 10
    b = 5
    ret_add = cal.add(a, b)
    ret_sub = cal.sub(a, b)
    ret_mul = cal.mul(a, b)
    ret_div = cal.div(a, b)

    print("{:d} + {:d} = {:d}".format(a, b, ret_add))
    print("{:d} - {:d} = {:d}".format(a, b, ret_sub))
    print("{:d} * {:d} = {:d}".format(a, b, ret_mul))
    print("{:d} / {:d} = {:d}".format(a, b, ret_div))
