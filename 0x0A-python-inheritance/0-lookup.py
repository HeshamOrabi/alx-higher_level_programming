#!/usr/bin/python3
"""

    function returns the list of available attributes and methods of obj

"""


def lookup(obj):
    """returns the list of available attributes"""
    return dir(obj)
