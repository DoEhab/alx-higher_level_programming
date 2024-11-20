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

    def to_json(self):
        return self.__dict__
