#!/usr/bin/python3
"""
This module demonstrates how to declare a class Square
with an attribute named size
"""


class Square:
    """
    A square class definition

    Attributes:
        size (any): The size of the square, can be any type
    """

    def __init__(self, size) -> None:
        """
        Size attribute initialization

        Args:
            size (any): The size of the square, can be any type
        """
        self.__size = size
