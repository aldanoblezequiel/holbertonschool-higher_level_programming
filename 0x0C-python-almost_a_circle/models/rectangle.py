#!/usr/bin/python3
"""This is module Rectangle"""
from models.base import Base


class Rectangle(Base):
    """This is the Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of Rectangle object"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, width):
        if (type(width) is not int):
            raise TypeError("width must be an integer")
        if (width <= 0):
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, height):
        if (type(height) is not int):
            raise TypeError("height must be an integer")
        if (height <= 0):
            raise ValueError("height must be > 0")

        self.__height = height

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, x):
        if (type(x) is not int):
            raise TypeError("x must be an integer")
        if (x < 0):
            raise ValueError("x must be >= 0")

        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) is not int):
            raise TypeError("y must be an integer")
        if (y < 0):
            raise ValueError("y must be >= 0")

        self.__y = y

    # Built in functions
    def __str__(self):
        txt = f"[Rectangle] ({self.id}) {self.x}/{self.y} -"
        txt += f" {self.width}/{self.height}"
        return (txt)

    # Rectangle Functionality
    def area(self):
        """Returns the area"""
        return (self.__height * self.__width)

    def display(self):
        """Displays the rectangle"""
        print("\n"*self.y, end='')
        for line in range(self.__height):
            print(" "*self.x, end='')
            print('#'*self.__width)

    def update(self, *args, **kwargs):
        """Updates the arguments"""
        atr_list = ['id', 'width', 'height', 'x', 'y']
        if args is not None:
            if len(args) < 6 and len(args) > 0:
                for i in range(len(args)):
                    setattr(self, atr_list[i], args[i])
                return

        for key in kwargs:
            if key in atr_list:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Returns the dictionary"""
        res = {
                'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width
                }
        return res
