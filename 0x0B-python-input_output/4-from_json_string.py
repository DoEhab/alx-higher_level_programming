#!/usr/bin/python3
"""convert obj from json representation"""
import json


def from_json_string(my_str):
    """
    obj from json
    Args:
        my_obj: string to be converted

    Returns:
        obj represented by json
    """
    return json.loads(my_str)
