#!/usr/bin/python3
def multiple_returns(sentence):
    str_list = []
    len_of_sen = len(sentence)
    for val in sentence:
        str_list.append(val)
    if len_of_sen == 0:
        str_list.append(None)
    multi_ret = len_of_sen, str_list[0]
    return (multi_ret)
