#!/usr/bin/python3
"""
Square class
"""


class Square():
    """
    class Square
    """
    def __init__(self, size=0):
        """init"""
        self.size = size

    @property
    def size(self):
        """size square"""
        return self.__size

    def area(self):
        """quare area"""
        return self.size * self.size

    @size.setter
    def size(self, value):
        """set size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
