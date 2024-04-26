#!/bin/usr/python3
from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args is not None and len(args) > 0:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.size = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            if len(args) >= 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
        if kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
    def to_dictionary(self):
        return self.__dict__

    def __str__(self):
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(self.__class__.__name__, self.id, self.x, self.y, self.size)
