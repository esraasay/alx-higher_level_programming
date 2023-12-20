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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area of the object

        returns:
            the size of the object
        """
        return self.__size**2
