#!/usr/bin/python3
def uniq_add(my_list=[]):
    ret = set(my_list)
    r = 0
    for n in ret:
        r += n
    return r
