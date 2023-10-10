#!/usr/bin/python3
"""

    script that adds all arguments to a Python list, and then save them

"""
import sys
import os.path

args = sys.argv[1:]

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

lst = []
if os.path.exists("./add_item.json"):
    lst.extend(load_from_json_file("add_item.json"))

save_to_json_file(lst + args, "add_item.json")
