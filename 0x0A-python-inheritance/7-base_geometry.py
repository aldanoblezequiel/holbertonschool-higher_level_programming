#!/usr/bin/python3
"""
Create empty basgeoemtry
"""


class BaseGeometry:
    """
    add intval
    """
    def area(self):
        """raise XXception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks errors"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")

        if value <= 0:
            raise ValueError(name + " must be greater than 0")
