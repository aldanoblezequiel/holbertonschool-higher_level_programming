#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ret = {}
    for n, v in a_dictionary.items():
        ret[n] = v * 2
    return ret
