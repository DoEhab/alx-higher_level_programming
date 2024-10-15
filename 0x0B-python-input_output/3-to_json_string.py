#!/usr/bin/python3
"""convert string to json representation"""
import json


def to_json_string(my_obj):
    """
    convert to json rep
    Args:
        my_obj: string to be converted

    Returns:
        Json representation
    """
    return json.dumps(my_obj)
