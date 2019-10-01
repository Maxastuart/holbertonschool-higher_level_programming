#!/usr/bin/python3
class Square:
    """Define a Square class"""

    def __init__(self, size=0):
        """Defines and initializes a square.
        size (int): the length of one side of the square.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
