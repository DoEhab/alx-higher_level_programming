#!/usr/bin/python3
"""fun to read json from file"""
import json
from typing import TextIO


def load_from_json_file(filename):
    """
    read json from file
    Args:
        filename: the file name

    Returns:
        void

    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
