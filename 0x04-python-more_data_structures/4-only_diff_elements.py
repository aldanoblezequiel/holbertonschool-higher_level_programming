#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    ret = []
    for n in set_1:
        if n not in set_2:
            ret.append(n)
    for j in set_2:
        if j not in set_1:
            ret.append(j)
    return ret
