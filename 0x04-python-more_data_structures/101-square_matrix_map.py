#!/usr/bin/python3
def square_matrix_map(matrix=[]):  # NC is my passion
    return list(map(lambda x: list(map(lambda y: y * y, x)), matrix.copy()))
