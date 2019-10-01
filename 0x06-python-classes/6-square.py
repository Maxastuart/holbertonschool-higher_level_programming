#!/usr/bin/python3
class Square:
    """Define a Square class."""

    def __init__(self, size=0, position=(0, 0)):
        """Define and initialize a square.
        size (int): optional, the length of one side of the square
        position (int, int): optional, a tuple of integers of the Square's
        position offset (x horizontal, y vertical).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Define position property."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position offset of the square.
        value (int, int): a tuple of integers of the Square's position offset
        (x horizontal, y vertical).
        """
        self.__position = value
        if type(self.__position) is not tuple or \
           len(self.__position) is not 2 or \
           not all(isinstance(i, int) for i in self.__position) or \
           not all(i >= 0 for i in self.__position):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the Square.

        Prints the square to stdout with '#'s,
        vertical offset of newlines, and
        horizontal offset spaces.
        """
        if self.__size is 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print("{}".format(' ' * self.__position[0] + '#' * self.__size))
