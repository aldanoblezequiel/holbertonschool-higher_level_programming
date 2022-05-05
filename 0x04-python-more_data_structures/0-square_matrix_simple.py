#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    ret = []
    for n in matrix:
        re = map(lambda x: x * x, n)
        ret.append(list(re))
    return ret
