#!/usr/bin/python3
def search_replace(my_list, search, replace):
    ret = []
    for n in my_list:
        if n == search:
            ret.append(replace)
        else:
            ret.append(n)
    return ret
