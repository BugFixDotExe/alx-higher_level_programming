#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as cal
    a = 10
    b = 5
    ret_add = cal.add(a, b)
    ret_sub = cal.sub(a, b)
    ret_mul = cal.mul(a, b)
    ret_div = cal.div(a, b)

    print("{:s} + {:s} = {:s}".format(str(a), str(b), str(ret_add)))
    print("{:s} - {:s} = {:s}".format(str(a),str(b), str(ret_sub)))
    print("{:s} * {:s} = {:s}".format(str(a), str(b), str(ret_mul)))
    print("{:s} / {:s} = {:s}".format(str(a), str(b), str(ret_div)))
