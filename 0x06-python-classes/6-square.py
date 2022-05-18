#!/usr/bin/python3
"""
Square class
"""


class Square:
    """
    Class Square
    """

    def __init__(self, size=0, position=(0, 0)):
        """init"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """pos value"""
        return self.__position

    @position.setter
    def position(self, value):
        """pos value"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """square area"""
        return self.__size * self.__size

    def my_print(self):
        """prints the square in stdout"""
        if self.__position[1] <= 0:
            print("", end="")
        else:
            for z in range(self.__position[1]):
                print("")

        if self.__size == 0:
            print("")
        else:
            for n in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for i in range(self.__size):
                    print("#", end="")
                print("")
