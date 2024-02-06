#!/usr/bin/python3
"""Define a square"""


class Square:
    """
    Initialize a new Square instance

    Parameters:
        size (int): The size of the square
    """
    def __init__(self, size=0):
        try:
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            print("size must be an integer")
