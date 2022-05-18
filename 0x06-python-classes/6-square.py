#!/usr/bin/python3

"""Square class module"""


class Square:

    """Class square"""

    def checker(self, x, y):
        """check if can init"""
        try:
            if type(y[0]) is not int or type(y[1]) is not int:
                raise TypeError("position must be a tuple \
                                of 2 positive integers")
            if type(y) is not tuple:
                raise TypeError("position must be a tuple of \
                                2 positive integers")
            if len(y) != 2:
                raise TypeError("position must be a tuple of \
                                2 positive integers")
            if y[0] < 0 or y[1] < 0:
                raise TypeError("position must be a tuple of 2 \
                                positive integers")
            if type(x) is not int:
                raise TypeError("size must be an integer")
            elif x < 0:
                raise ValueError("size must be >= 0")
        except Exception:
            raise TypeError("position must be a tuple of 2 positive integers")

    def __init__(self, size=0, position=(0, 0)):
        """init var"""
        self.checker(size, position)
        self.__position = position
        self.__size = size

    @property
    def size(self):
        """value of size"""
        return self.__size

    @size.setter
    def size(self, n):
        """size"""
        self.checker(n, None)

    @property
    def position(self):
        """value of pos"""
        return self.__position

    @position.setter
    def position(self, x):
        """get the position"""
        self.checker(None, x)

    def area(self):
        """area"""
        return self.__size * self.__size

    def my_print(self):
        """print a square"""
        if (self.size == 0):
            print()
        else:
            if self.__position[1] > 0:
                for i in range(0, self.__position[1]):
                    print()
            for i in range(0, self.__size):
                if self.__position[0] > 0:
                    for k in range(0, self.__position[0]):
                        print(" ", end='')
                for j in range(0, self.__size):
                    print("#", end='')
                print()
