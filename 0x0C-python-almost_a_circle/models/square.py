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
        if args is not None and len(args) != 0:
            ls = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if ls[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, ls[i], args[i])
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    if k == 'size':
                        setattr(self, 'width', v)
                        setattr(self, 'height', v)
                    else:
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
