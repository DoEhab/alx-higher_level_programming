#!/usr/bin/python3
# File: 2-is_same_class.py
"""define fun is same class"""


def is_same_class(obj, a_class):
    """return true if obj is instance of class

    Args:
        obj: object to be type checked
        a_class: the class type
    """
    if type(obj) == a_class:
        return True
    return False
