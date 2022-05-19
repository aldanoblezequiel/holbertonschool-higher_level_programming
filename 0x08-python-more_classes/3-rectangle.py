#!/usr/bin/python3
"""
    Rectangle
"""


class Rectangle:
    """
    Rectangle class
    """

    def __init__(self, width=0, height=0):
        """
           Class Rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Retrive width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrive height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Rectangles area"""
        return self.__height * self.__width

    def perimeter(self):
        """Rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """Returns rectangle with char"""
        out = ""
        if self.__width == 0 or self.__height == 0:
            return out
        else:
            i = self.__height
            while i:
                out += "#" * self.__width
                if i != 1:
                    out += "\n"
                i += -1
            return out
