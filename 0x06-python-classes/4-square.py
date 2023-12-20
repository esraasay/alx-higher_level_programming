#!/usr/bin/python3
"""sqare module"""


class Square:
    """define a square"""

    def __init__(self, size=0):
        """constractor.

        args:
                        size: size of the square
        raisees:
            typeerror: type of the square
            valueerror: value of the square
        """

        self.size = size

    @property
    def size(self):
        """property for size of the square

        raises:
            typeerror: type of the square
            valueerror: value of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area of the object

        returns:
            the size of the object
        """
        return self.__size**2
