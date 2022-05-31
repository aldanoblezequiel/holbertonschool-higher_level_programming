#!/usr/bin/python3
"""
Calculate widht, height, etc
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """create Rectangle from BaseGeometry"""
    def __init__(self, width, height):
        """
        width and height private
        """
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """rec area"""
        return self.__width * self.__height

    def __str__(self):
        """print width or height"""
        return '[Rectangle] ' + str(self.__width) + "/" + str(self.__height)
