#!/usr/bin/python3
"""Defines a base geometry class."""


class BaseGeometry:
    """base geometry class"""

    def area(self):
        """area fun"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate int param.

        Args:
            name (str): The name for param.
            value (int): int value.
        Raises:
            TypeError: If value is not int.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
