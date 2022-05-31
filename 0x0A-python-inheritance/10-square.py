#!/usr/bin/python3
"""
Validates Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """size validation"""
    def __init__(self, size):
        """validates int"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
        """modifies fahter class"""
