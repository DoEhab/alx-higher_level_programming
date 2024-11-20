#!/usr/bin/python3
"""define fun is kind of class"""


def inherits_from(obj, a_class):
    """
    check if obj inherit from class
    Args:
        obj: obj to be checked
        a_class: the class to check the obj with

    Returns:
        True if instance
        False otherwise
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)