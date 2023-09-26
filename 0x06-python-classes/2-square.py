#!/usr/bin/python3
# 0-square.py by Hesham Orabi
"""A module that defines a square"""


class Square:
    """Class represents a square"""

    def __init__(self, size):
        """Initializing this square class
        Args:
			size - represnets the size of the square defined
		Raises:
			TypeError: if size is not integer
			ValueError: if size is less than zero
        """
		
		if not isinstance(size, int):
			raise TypeError('size must be an integer')
		if size < 0:
			raise ValueError('size must be >= 0')

        self.__size = size
