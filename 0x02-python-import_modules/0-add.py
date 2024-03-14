#!/usr/bin/python3
if __name__ == "__main__":
    import add_0 as _add
    a = 1
    b = 2
    ret_sum = _add.add(a, b)
    print("{:s} + {:s} = {:s}".format(str(a), str(b), str(ret_sum)))
