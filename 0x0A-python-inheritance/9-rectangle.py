#!/usr/bin/python3
"""

    improved BaseGeometry

"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rect class"""
    def __init__(self, width, height):
        """Initilize rectangle method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """get area"""
        return self.__width * self.__height

    def __str__(self):
        """print"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
