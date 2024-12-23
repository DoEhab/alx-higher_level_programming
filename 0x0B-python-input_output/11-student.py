#!/usr/bin/python3
""" class Student
"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        init function
        Args:
            first_name: student first name
            last_name: student last name
            age: student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            for x in attrs:
                if isinstance(x, str):
                    return {name: getattr(self, name) for name in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        for key, val in json.items():
            setattr(self, key, val)
