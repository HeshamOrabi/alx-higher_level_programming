#!/usr/bin/python3
"""

    returns True if the object is exactly an instance of the specified class

"""


def is_kind_of_class(obj, a_class):
    """returns True or false"""
    if isinstance(obj, a_class):
        return True
    return False
