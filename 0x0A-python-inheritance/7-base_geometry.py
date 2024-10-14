#!/usr/bin/python3
"""define base geometry class"""


class BaseGeometry:
    """Geometry Class"""

    def area(self):
        """area function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates an integer
            Args:
                name: var name
                value: var value to be checked
        """
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
