#!/usr/bin/python3
"""
This module demonstrates how to
- declare a class Square
- with an attribute named size and some validations about it
- calculate the area of the square
"""


class Square:
    """
    A square class definition

    Attributes:
        size (:obj:`int`, optional): The size of the square
    """

    def __init__(self, size=0) -> None:
        """
        Size attribute initialization. The default value is zero,
        and it will throw error if the given value is
        not an integer or less than zero

        Args:
            size (:obj:`int`, optional): The size of the square,
            default value is zero
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculate the area of the square

        Args: None
        Returns:
            The area of the square
        """
        return (self.__size ** 2)
