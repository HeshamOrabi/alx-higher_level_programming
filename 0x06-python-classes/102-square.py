#!/usr/bin/python3
"""A module that defines a square """


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """
        Initializing this square class
        Args:
            size: represnets the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, (int, float)):
            raise TypeError('size must be a number')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        function to get area
        Returns: The square of the size
        """

        return self.__size ** 2

    @property
    def size(self):
        """
        function to get size
        Returns: The size
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        function to set size
        """

        if not isinstance(value, (int, float)):
            raise TypeError('size must be a number')
        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def __eq__(self, other):
        """Magic func for op"""
        return self.size == other.size

    def __lt__(self, other):
        """Magic func for op"""
        return self.size < other.size

    def __gt__(self, other):
        """Magic func for op"""
        return self.size > other.size

    def __ge__(self, other):
        """Magic func for op"""
        return self.size >= other.size

    def __le__(self, other):
        """Magic func for op"""
        return self.size <= other.size

    def __ne__(self, other):
        """Magic func for op"""
        return self.size != other.size
