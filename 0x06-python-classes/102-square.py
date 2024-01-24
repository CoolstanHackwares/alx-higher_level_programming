#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def __lt__(self, other):
        """Less than comparison."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparison."""
        return self.area() <= other.area()

    def __eq__(self, other):
        """Equal comparison."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equal comparison."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparison."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparison."""
        return self.area() >= other.area()
