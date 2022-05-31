#!/usr/bin/python3
"""
Checks if the object is an instance
"""


def inherits_from(obj, a_class):
    """
    Check if is instamce of specificed class
    """
    if isinstance(obj, a_class):
        if issubclass(a_class, obj.__class__) is not True:
            return True
    return False
