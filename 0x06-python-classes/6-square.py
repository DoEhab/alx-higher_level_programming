#!/usr/bin/python3
# File: 6-square.py
"""Define Square Python Class."""


class Square:
    """" square init function"""

    def __init__(self, size=0, position=(0, 0)):
        """
        new square
        Args:
            size: square size
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        set position
        Args:
            value: position value
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__position[1]):
                print("")
            for i in range(0, self.__size):
                for k in range(0, self.__position[0]):
                    print("_", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print("")
