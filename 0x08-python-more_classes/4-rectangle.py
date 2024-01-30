#!/usr/bin/python3
"""Defines a Rectangle class representing a rectangle geometry."""


class Rectangle:
    """Rectangle class representing a geometric rectangle with
    width and height.
    """

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance with default
        width=0 and height=0.
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Return an informal string representation of the Rectangle."""
        if self.__height == 0 or self.__width == 0:
            return ''

        rect_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rect_str += '#'
            rect_str += '\n'
        return rect_str[:-1]

    def __repr__(self):
        """Return a string representation able to recreate a Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    @property
    def width(self):
        """Get or set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__height == 0 or self.__width == 0:
            return 0

        return 2 * (self.__width + self.__height)
