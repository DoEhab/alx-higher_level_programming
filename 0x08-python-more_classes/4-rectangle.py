#!/usr/bin/python3
# File: 3-rectangle.py
"""New Rect class"""


class Rectangle:
    """rect class"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return (0)
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""

        result = []
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                result.append('#')
            result.append('\n')
        return "".join(result)

    def __repr__(self):
        return "Rectangle({0}, {1})".format(self.__width, self.__height)
