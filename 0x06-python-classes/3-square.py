#!/usr/bin/python3
# File: 3-square.py
"""Define Square Python Class."""


class Square:
    def __init__(self, size=0):
        """
        new square
        Args:
            size: square size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
