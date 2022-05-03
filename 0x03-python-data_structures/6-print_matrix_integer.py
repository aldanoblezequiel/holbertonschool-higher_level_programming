#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    length = len(matrix) - 1
    if not matrix:
        print()
    for row in matrix:
        counter = 0
        for i in row:
            if counter != 0:
                print(' ', end='')
            print("{:d}".format(i), end='')
            counter += 1
        print()
