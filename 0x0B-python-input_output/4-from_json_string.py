#!/usr/bin/python3
"""

    function that returns the JSON representation of an object (string)

"""
import json


def from_json_string(my_str):
    """function that returns the JSON representation of an object (string)"""
    return json.loads(my_str)
