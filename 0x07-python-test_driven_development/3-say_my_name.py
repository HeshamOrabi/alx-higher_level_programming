#!/usr/bin/python3
"""

    Function that prints My name is <first name> <last name>

"""


def say_my_name(first_name, last_name=""):
    """prints My name
    Args:
        first_name (str): Your first name
        last_name (str): Your last name
    Raise:
        TypeError : if first_name or last_name is not string
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print(f"My name is {first_name} {last_name}")
