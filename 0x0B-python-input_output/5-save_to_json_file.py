#!/usr/bin/python3
"""write json to file"""
import json


def save_to_json_file(my_obj, filename):
    """
    write json
    Args:
        my_obj: json to be written on file
        filename: file to create or write text

    Returns:
        void

    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
