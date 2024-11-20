#!/usr/bin/python3
"""write text to file"""


def write_file(filename="", text=""):
    """
    write text
    Args:
        filename: file to create or write text
        text: text to be written on file

    Returns:
        number of chars written

    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
