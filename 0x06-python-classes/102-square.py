#!/usr/bin/python3
class Square:
    """Define a Square class."""

    def __init__(self, size=0):
        """Define and initialize a square.
        size (int): the length of one side of the square
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def __int__(self):
        """Return the square as an int"""
        return self.area()

    def __eq__(self, other):
        """Return whether the square is equal to an other
        other (int): the number to compare to
        """
        return int(self) == other

    def __ne__(self, other):
        """Return whether the square is not equal to an other
        other (int): the number to compare to
        """
        return int(self) != other

    def __gt__(self, other):
        """Return whether the square is greater than an other
        other (int): the number to compare to
        """
        return int(self) > other

    def __lt__(self, other):
        """Return whether the square is less than an other
        other (int): the number to compare to
        """
        return int(self) < other

    def __ge__(self, other):
        """Return whether the square is greater than or equal to an other
        other (int): the number to compare to
        """
        return int(self) >= other

    def __le__(self, other):
        """Return whether the square is less than or equal to an other
        other (int): the number to compare to
        """
        return int(self) <= other

    def area(self):
        """Return the area of the Square."""
        return self.__size * self.__size

    @property
    def size(self):
        """Define size property."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the Square.
        value (int): the new length of one side of the square
        """
        self._Square__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
