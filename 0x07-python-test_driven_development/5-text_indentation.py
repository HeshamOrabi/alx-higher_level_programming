#!/usr/bin/python3
"""

    function that prints a text with 2 new lines

"""


def text_indentation(text):
    """prints a text with 2 new lines
    Args:
        text (str): string to be edited
    Raise:
        TypeError: if textis not str
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    count = 0
    while count < len(text) and text[count] == " ":
        count = count + 1

    while count < len(text):
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count = count + 1
            while count < len(text) and text[count] == " ":
                count = count + 1
            continue
        count = count + 1
