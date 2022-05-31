#!/usr/bin/python3
"""Class MyInt that inherited from int"""


class MyInt(int):
    """My int class xd"""

    def __eq__(self, value):
        """Myint is the same to"""
        return self.real != value

    def __ne__(self, value):
        """Myint is diferent from"""
        return self.real == value
