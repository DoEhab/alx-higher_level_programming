#!/usr/bin/python3
"""fun to read a file"""


def read_file(filename=""):
    """
    read and print file
    Args:
        filename: the file name

    Returns:
        print file content

    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
