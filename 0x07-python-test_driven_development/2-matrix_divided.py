#!/usr/bin/python3
"""
Divide Matrix module
"""


def matrix_divided(matrix, div):
    """Divides elements of the matrix"""
    new_matrix = []
    exception1 = "matrix must be a matrix (list of lists) of integers/floats"
    div_req(div)
    if type(matrix) is not list:
        raise TypeError(exception1)

    for elem in matrix:
        new_elem = []
        if type(elem) is not list:
            raise TypeError(exception1)
        if len(elem) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for sub_elem in elem:
            if type(sub_elem) is not int and type(sub_elem) is not float:
                raise TypeError(exception1)
            new_elem.append(round(sub_elem / div, 2))
        new_matrix.append(new_elem)
    return new_matrix


def div_req(div):
    """Division function"""
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
