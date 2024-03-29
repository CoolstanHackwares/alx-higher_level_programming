#!/usr/bin/python3
"""
Module 11-square
Creates a Square class.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square.
    Inherits from Rectangle.
    """

    def __init__(self, size):
        """Initializes a square instance.

        Args:
            - size: size of the square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Computes the area of the Square instance.
        Overwrites the area() method from Rectangle.
        """

        return self.__size ** 2

    def __str__(self):
        """Returns a formatted string for printing."""

        return str("[Square] {}/{}".format(self.__size, self.__size))
