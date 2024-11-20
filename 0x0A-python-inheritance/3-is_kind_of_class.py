#!/usr/bin/python3
"""define fun is kind of class"""


def is_kind_of_class(obj, a_class):
    """
    function check if obj is instance of class
    Args:
        obj: the object to be checked
        a_class: class to check if the obj is instance of

    Returns:
        if instance - True
        otherwise - False
    """
    return (isinstance(obj, a_class))
