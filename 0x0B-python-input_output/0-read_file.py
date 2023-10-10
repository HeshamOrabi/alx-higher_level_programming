#!/usr/bin/python3
"""

    function that reads a text file (UTF8) and prints it to stdout

"""


def read_file(filename=""):
    """function that reads a text file"""
    with open("my_file_0.txt", "r", encoding="utf-8") as f:

        file_text = f.read()

        print(file_text, end="")
