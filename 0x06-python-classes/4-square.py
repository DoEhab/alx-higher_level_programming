#!/usr/bin/python3
# File: 4-square.py
"""Define Square Python Class."""


class Square:
    """" square init function"""

    def __init__(self, size=0):
        """
        new square
        Args:
            size: square size
        """
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        set size
        Args:
            value: square size
                """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
