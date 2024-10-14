#!/usr/bin/python3
#!/usr/bin/python3
"""define Rectangle class inherit from base geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):

        """
        fun to initialize rect class
        Args:
            width: rect width
            height: rect height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area function"""
        return self.__width * self.__height

    def __str__(self):
        """return updated string"""
        result = "[" + str(self.__class__.__name__) + "]"
        result += str(self.__width) + "/" + str(self.__height)
        return result
