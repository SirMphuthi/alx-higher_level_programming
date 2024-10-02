#!/usr/bin/python3
"""square module"""


class Square:
    """defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Creates a square
        Args:
            size (int): size of square
            position (int, int): square coordinates
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """Property of size
        Raises:
            TypeError: if size is not integer.
            ValueError: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """"Property of coordinates
        Raises:
            TypeError: if value is not tuple of 2 integers < 0
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ sets square positon
        Args: value as tuple of two positive integers
        Raises:
            TypeError: if value is not tuple on in < 0
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Gets area of square
        Returns: size of square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """print square position"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
