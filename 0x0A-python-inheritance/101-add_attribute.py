#!/usr/bin/python3
"""
Adds atribute to object
"""


def add_attribute(obj, atr, value):
    """raise error if not args passed
    """
    if type(obj) is int:
        raise TypeError("can`t add new attribute")

    return atr, value
