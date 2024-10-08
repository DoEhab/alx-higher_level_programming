#!/usr/bin/python3
"""define add_integer function"""
def add_integer(a, b=98):
    """ sum two numbers

    Args:
        a: first int
        b: second int
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
