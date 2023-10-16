#!/usr/bin/python3
"""

    class will be the “base” of all other classes in this project.

"""
import json
import os.path as osp


class Base:
    """class will be the “base” of all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Intialzing"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return a str rep od list_dict"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """return list for json rep"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save object in a file """
        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dic)

        with open(filename, 'w') as f:
            f.write(lists)

    @classmethod
    def create(cls, **dictionary):
        """retern an instance of a class"""
        obj = cls(1, 1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        fpath = cls.__name__ + ".json"
        if osp.exists(fpath):
            with open(fpath, "r", encoding="utf-8") as f:
                dict_list = cls.from_json_string(f.read())
                return [cls.create(**dic) for dic in dict_list]
        return []
