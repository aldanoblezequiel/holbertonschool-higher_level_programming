#!/usr/bin/python3
"""
Prints a sized square
"""


def print_square(size):
    """Prints a square with size"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for n in range(size):
        for i in range(size):
            print("#", end="")
        print("")
