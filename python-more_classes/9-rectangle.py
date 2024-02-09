#!/usr/bin/python3
"""
Define a rectangle
"""


class Rectangle:
    """Define the rectangle attribute"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize a new reactangle instance

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrives the width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """Retrieves the height of the rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle

        Args:
            value (int): The width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle

        Args:
            value (int): The height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return the printable representation of the rectangle

        Represent the rectangle with the # character
        """
        if self.width == 0 or self.height == 0:
            return ""
        printed_rectangle = (str(self.print_symbol) * self.__width + '\n') \
            * (self.__height - 1) + (str(self.print_symbol) * self.__width)
        return printed_rectangle

    def __repr__(self):
        """Return the string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message for every deletion of a reclangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the grater area

        Args:
            rect_1 (Rectangle): The first rectangle
            rect_2 (Rectangle): The second rectangle
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new rectangle with width and height equal to size

            Args:
            size (int): The width and height of the new rectangle
        """
        return cls(size, size)
