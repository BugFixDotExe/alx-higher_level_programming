#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1 is None and set_2 is not None:
        return (set_2)
    if set_2 is None and set_1 is not None:
        return (set_1)
    if set_1 is None and set_2 is None:
        return
    else:
        c = set_1 & set_2
        return (c)
