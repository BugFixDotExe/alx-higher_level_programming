#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_of_tup_a = len(tuple_a)
    len_of_tup_b = len(tuple_b)

    if len_of_tup_a < 2:
        if len_of_tup_a == 0:
            index_zero_a = 0
            index_one_a = 0
        elif len_of_tup_a == 1:
            index_zero_a = tuple_a[0]
            index_one_one_a = 0
    elif len_of_tup_b < 2:
        if len_of_tup_a == 0:
            index_zero_b = 0
            index_one_b = 0
        elif len_of_tup_b == 1:
            index_zero_b = tuple_b[0]
            index_one_b = 0
    elif len_of_tup_a >= 2:
        index_zero_a = tuple_a[0]
        index_one_a = tuple_a[1]
    elif len_of_tup_b >= 2:
        index_zero_b = tuple_b[0]
        index_one_b = tuple_b[1]
    print(index_zero_b)
