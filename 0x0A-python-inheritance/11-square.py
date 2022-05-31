#!/usr/bin/python3
"""
Task 11 xd
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """validates if size is an int"""
    def __init__(self, size):
        """validates if is an int"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
        """Modifies mother class"""

    def __str__(self):
        """prints width or height"""
        return '[Square] {:d}/{:d}'.format(self.__size, self.__size)
