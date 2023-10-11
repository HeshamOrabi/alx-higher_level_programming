#!/usr/bin/python3
"""

    class Student

"""


class Student:
    """A class to define student"""
    def __init__(self, first_name, last_name, age):
        """Intializing..."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dict representation"""
        if type(attrs) is list:
            dic = {}
            for attr in attrs:
                if attr in dir(self):   # we could have used hasattr()
                    dic[attr] = getattr(self, attr)
                else:
                    continue
            return dic
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """reconstruct an instanceof of a dict"""
        for k, v in json.items():
            setattr(self, k, v)
