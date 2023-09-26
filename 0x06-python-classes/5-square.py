#!/usr/bin/python3
# 0-square.py by Hesham Orabi
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

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
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

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def my_print(self):
        """
        function to print square size to stdout with #
        """

        if self.__size == 0:
            print()

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
