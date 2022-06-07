#!/usr/bin/python3
"""Module Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update Square"""
        atr_list = ['id', 'size', 'x', 'y']
        if (args and (len(args) < 5 and len(args) > 0)):
            for idx in range(len(args)):
                setattr(self, atr_list[idx], args[idx])
            return

        for key in kwargs:
            if key in atr_list:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Returns a dictionary of the Square"""
        res = {
                'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y
                }
        return res

    # Built in functions

    def __init__(self, size, x=0, y=0, id=None):
        """Init of Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        txt = f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
        return txt
