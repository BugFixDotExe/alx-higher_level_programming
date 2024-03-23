#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return
    a_sorted_dict = dict(sorted(a_dictionary.items(), key=lambda x: x[1]))
    print(a_sorted_dict)
    a_sorted_dict = list(a_sorted_dict)
    end_item = len(a_sorted_dict) - 1
    return (a_sorted_dict[end_item])
