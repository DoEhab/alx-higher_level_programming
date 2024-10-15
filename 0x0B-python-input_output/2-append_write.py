#!/usr/bin/python3
"""append text to file"""


def append_write(filename="", text=""):
    """
    write text
    Args:
        filename: file to create or append text to
        text: text to be appended on file

    Returns:
        number of chars written

    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
