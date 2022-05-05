#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    key_list = list(a_dictionary.keys())
    val_list = list(a_dictionary.values())
    n = 0
    for i in val_list:
        if i > n:
            n = i
    r = key_list[val_list.index(n)]
    return r
