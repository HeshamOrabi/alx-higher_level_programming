#!/usr/bin/python3
"""

    Function that prints a square with the character #.

"""


def print_square(size):
    """prints a square with the character #
    Args:
        size (int): the size of square
    Raise:
        TypeError: if size is not int
        ValueError: is size < 0
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
