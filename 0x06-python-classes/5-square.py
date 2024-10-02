#!/usr/bin/python3
""" Defines a square. """


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes square class
        Args:
            size: represents size of square
        Raises:
            TypeError: if size is'nt a integer
            ValueError: is size is less than zeri
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """Gets size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Area of square
        Return: square of size
        """

        return (self.__size ** 2)

    def my_print(self):
        """prints square in # """

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
