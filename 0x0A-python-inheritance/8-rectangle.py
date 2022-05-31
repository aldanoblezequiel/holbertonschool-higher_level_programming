#!/usr/bin/python3
"""
Creates Rectangle inherited from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """creates subclass Rectangle"""
    def __init__(self, width, height):
        """
        width and height priv
        """
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)
