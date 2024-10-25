#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines class Square that inherits from Rect"""

    def __init__(self, size, width, height, x=0, y=0, id=None):
        """initializes class object
            Args:
                  size: square size
                  x: x
                  y: y
                  id: id
        """
        super().__init__(width, height, x, y, id)

    @property
    def size(self):
        """return size value"""

        return self.width

    @size.setter
    def size(self, value):
        """set width and height to size
        Args:
            value: size value
        """

        self.width = value
        self.height = value

    def __str__(self):
        """overwrite __str__ for square class"""

        return "[Square] ({}) <{}>/<{}> - <{}>".format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """updates the square instances
        Args:
            args: list of arguments
            kwargs: list of key, vals
        """

        if len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
                i += 1
        elif len(kwargs) != 0:
            for key, val in kwargs:
                if key == "id":
                    self.id = val
                if key == "size":
                    self.size = val
                if key == "x":
                    self.x = val
                if key == "y":
                    self.y = val

    def to_dictionary(self):
        """return dict representation"""

        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
