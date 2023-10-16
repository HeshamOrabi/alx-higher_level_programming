#!/usr/bin/python3
"""

    class Square that inherits from Rectangle:

"""
from .rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Intializing"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """print a str representation"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - "
                f"{self.size}")

    def to_dictionary(self):
        """return a dic rep"""
        return ({'x': self.x, 'y': self.y, 'id': self.id,
                'size': self.size})

    def update(self, *args, **kwargs):
        """set args"""
        if args:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.size = args[1]
            if len(args) == 3:
                self.x = args[2]
            if len(args) == 4:
                self.y = args[3]
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    @property
    def size(self):
        """Get size"""
        return self.width

    @size.setter
    def size(self, size):
        """Set size"""
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size
