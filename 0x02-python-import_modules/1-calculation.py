#!/usr/bin/python3
import calculator_1 as cal

if __name__ == "__main__":
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, cal.add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, cal_1.sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, cal_1.mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, cal_1.div(a, b)))