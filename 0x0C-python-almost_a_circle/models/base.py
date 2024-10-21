#!/usr/bin/python3
""" Base Class """
import json


class Base:
    """define base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init method
        Args:
            id: obj count
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json rep
        Args:
            list_dictionaries: list of dict
        """

        if list_dictionaries is None or list_dictionaries == []:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save list of objects to a file in json format
        Args:
            list_objs: list of dict
        """

        f_name = cls.__name__ + ".json"
        with open(f_name, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                for obj in list_objs:
                    f.write(Base.to_json_string(obj.to_dictionary()))

    @staticmethod
    def from_json_string(json_string):
        """takes json string as input and return json list
        Args:
            json_string: list of json string
        """

        if json_string is None or json_string == "[]":
            return []
        for i in json_string:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create instance of class
        Args:
            dictionary: kargs, list of keys and values
        """
        if dictionary != {}:
            if cls.__name__ == "Rectangle":
                cls_obj = cls(2, 3)
            elif cls.__name__ == "Square":
                cls_obj = cls(2)
            cls_obj.update(dictionary)
            return cls_obj

    @classmethod
    def load_from_file(cls):
        f_name = cls.__name__ + ".json"
        try:
            with open(f_name, "r") as f:
                js_str = f.read()
                instance_list = []
                my_list = Base.from_json_string(js_str)
                for my_dict in my_list:
                    instance_list.__add__(cls.create(cls, **my_dict))
                return instance_list
        except FileNotFoundError:
            return []

