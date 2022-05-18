#!/usr/bin/python3
"""
Square class
"""


class Square:
    """Class square"""
    def __init__(self, size=0):
        """
        init
        """
        self.size = size

    @property
    def size(self):
        """size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """size value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """square area"""
        return self.__size * self.__size

    def my_print(self):
        """prints square in stdout"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for n in range(self.__size):
                    print("#", end="")
                print("")
                """sets value"""
