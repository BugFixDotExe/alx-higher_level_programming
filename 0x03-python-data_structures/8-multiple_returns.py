#!/usr/bin/python3
def multiple_returns(sentence):
    len_of_sen = len(sentence)
    if len_of_sen == 0:
        sentence[0] = None
    multi_ret = len_of_sen, sentence[0]
    return (multi_ret)
