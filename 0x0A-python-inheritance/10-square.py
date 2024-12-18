#!/usr/bin/python3
"""define Square class inherit from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """init new class square"""

    def __init__(self, size):
        """
        init square
        Args:
            size: square size
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
