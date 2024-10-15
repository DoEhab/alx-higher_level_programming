#!/usr/bin/python3
import json

"""convert string to json representation"""


def to_json_string(my_obj):
    """
    convert to json rep
    Args:
        my_obj: string to be converted

    Returns:
        Json representation
    """
    return json.dumps(my_obj)
