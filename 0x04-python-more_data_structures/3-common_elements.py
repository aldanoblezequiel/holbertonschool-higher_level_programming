#!/usr/bin/python3
def common_elements(set_1, set_2):
    ret = []
    for n in set_1:
        for i in set_2:
            if n == j:
                ret.append(i)
                break
    return ret
