#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = 0
    b = 0
    c = 0
    d = 0

    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if len_a < 2 or len_b < 2:
        if len_a == 0:
            a, b = 0, 0
        if len_b == 0:
            c, d = 0, 0

        if len_a == 1:
            a, b = tuple_a[0], 0
        if len_b == 1:
            c, d = tuple_b[0], 0

    if len_a > 2 or len_b > 2:
        if len_a > 2:
            a, b = tuple_a[0], tuple_a[1]
        if len_b > 2:
            c, d = tuple_b[0], tuple_b[1]

    if len_a == 2 or len_b == 2:
        if len_a == 2:
            a, b = tuple_a[0], tuple_a[1]
        if len_b == 2:
            c, d = tuple_b[0], tuple_b[1]
    a = a + c
    b = b + d
    sum_of_tup = a, b
    return (sum_of_tup)
