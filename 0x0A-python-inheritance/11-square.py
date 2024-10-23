#!/usr/bin/python3
"""Defines class Base."""


Rectangle = __import__('9-rectangle').Rectangle


"""Defines a Square class"""


class Square(Rectangle):
    """Represents a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Intializes a new square.

        Args:
            size (int): The size of the square's sides.
        """
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """Return the print() and str() representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
