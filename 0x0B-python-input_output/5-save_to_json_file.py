#!/usr/bin/python3
"""

    Write a function that writes an Object to a text file, using a JSON

"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file, using a JSON"""
    with open(filename, "w", encoding="UTF-8") as f:
        f.write(json.dumps(my_obj))
