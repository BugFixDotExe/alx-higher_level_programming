#!/usr/bin/python3
def element_at(my_list, idx):
    len_of_list = len(my_list) - 1
    if idx < 0 or idx > len_of_list:
        return (None)
    else:
        val_at_idx = my_list[idx]
        return (val_at_idx)
