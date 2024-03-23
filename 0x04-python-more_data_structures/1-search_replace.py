#!/usr/bin/python3
def search_replace(my_list, search, replace):
    flag = 0
    if my_list is None:
        return
    cpy_list = my_list.copy()
    for idx in range(len(cpy_list)):
        if cpy_list[idx] == search:
            flag = 1
            cpy_list[idx] = replace
    if flag == 1:
        return (cpy_list)
    else:
        return (my_list)
