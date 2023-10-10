#!/usr/bin/python3
"""

    improved BaseGeometry

"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size):
        """Intializing..."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
