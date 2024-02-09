#!/usr/bin/python3
"""Define a square class"""


class Square:
    """Define a square"""
    def __init__(self, size=0):
        """
        Initialize a new Square instance

        Args:
            size (int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """Retrives the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size

        Args:
            value (int): The value of the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for y in range(self.size):
                for x in range(self.size):
                    print("#", end='')
                print()
