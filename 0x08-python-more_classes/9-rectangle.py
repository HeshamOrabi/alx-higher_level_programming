#!/usr/bin/python3
""" Rectangle class representation """


class Rectangle:
    """this represents a rectangle

    Args:
        number_of_instances (int) : the number of obj
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializing a Rectangle object with width and height attributes.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the biggest rectangle based on the area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() == rect_2.area():
            return rect_1
        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ returns a new Rectangle instanc """
        return cls(size, size)

    def __str__(self):
        """ string reprisintation of obj """
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for i in range(self.height):
            for j in range(self.width):
                string += str(self.print_symbol)
            if not i == self.height - 1:
                string += '\n'
        return string

    def __repr__(self):
        """ string reprisintation of obj """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """ Intialize at deletion """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ returns the rectangle area """
        return self.width * self.height

    def perimeter(self):
        """ returns the rectangle perimeter """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
