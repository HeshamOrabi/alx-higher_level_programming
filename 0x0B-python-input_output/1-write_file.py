#!/usr/bin/python3
"""

    function that writes a string to a text file

"""


def write_file(filename="", text=""):
    """function that writes a string to a text file"""
    with open(filename, "w", encoding="utf-8") as f:

        num = f.write(text)

        return num
