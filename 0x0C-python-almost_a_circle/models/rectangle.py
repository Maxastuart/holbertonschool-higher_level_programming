#!/usr/bin/python3
from models.base import Base


""" Rectangle class module
"""


class Rectangle(Base):
    """ Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)

    @property
    def width(self):
        """Define width property."""
        return self.__width

    @property
    def height(self):
        """Define height property."""
        return self.__height

    @property
    def x(self):
        """Define x property."""
        return self.__x

    @property
    def y(self):
        """Define y property."""
        return self.__y

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.
        value (int): the new length of the width.
        """
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.
        value (int): the new length of the height.
        """
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    @x.setter
    def x(self, value):
        """Set x.
        value (int): the new x.
        """
        self.__x = value
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @y.setter
    def y(self, value):
        """Set y.
        value (int): the new y.
        """
        self.__y = value
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Prints the rectangle with #s."""
        for n in range(self.__y):
            print("")
        for row in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def update(self, *args, **kwargs):
        """Updates the attributes with the given values."""
        if args is not None and len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
