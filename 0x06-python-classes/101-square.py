#!/usr/bin/python3
"""
This module demonstrates how to
- declare a class Square
- with an attribute named size and some validations about it
- set getter and setter on the size attribute
- calculate the area of the square
- print the square with the character #
- using positions to show spaces
- string representation of the class Square
"""


class Square:
    """
    A square class definition

    Attributes:
        size (:obj:`int`, optional): The size of the square
        position (:obj:`tuple` of :obj:`int`, optional) The
            position of the lines
    """

    def __init__(self, size=0, position=(0, 0)) -> None:
        """
        Size attribute initialization. The default value is zero,
        and it will throw error if the given value (size) is
        not an integer or less than zero or given value (position)
        is not a tuple of 2 positive integers

        Args:
            size (:obj:`int`, optional): The size of the square
            position (:obj:`tuple` of :obj:`int`, optional) The
                position of the lines
        """
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        elif (
            isinstance(position, tuple) and len(tuple(position)) != 2 or
            not isinstance(position, tuple)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not all(isinstance(p, int) and p >= 0 for p in tuple(position))):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

    @property
    def size(self):
        """Return the size of the square"""
        return (self.__size)

    @property
    def position(self):
        """Return the positions of the square"""
        return (self.__position)

    @size.setter
    def size(self, value):
        """Set a new size for the size of the square"""
        self.__init__(value, self.__position)

    @position.setter
    def position(self, value):
        """Set a new tuple of positions of the square"""
        self.__init__(self.__size, value)

    def area(self):
        """
        Calculate the area of the square

        Args: None
        Returns:
            The area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        If size is zero print an empty line else prints in
        stdout the square with the character #.
        Positions to use to fill spaces.
        Don't fill lines by spaces when position[1] > 0.

        Args: None
        Returns: None
        """
        if (self.size == 0):
            print("")
        else:
            if (self.position[1] > 0):
                print("")
            for _ in range(self.size):
                for _ in range(self.position[0]):
                    print(" ", end="")
                for _ in range(self.size):
                    print("#", end="")
                print("")

    def __repr__(self) -> str:
        """
        String representation of the Square class instance

        Args: None
        Returns: a new string that represents a square
        """
        output = ""
        if (self.size == 0):
            return (output)
        else:
            remain = self.position[1]
            if (remain > 0):
                output += "\n"
                remain -= 1
            for _ in range(self.size):
                for _ in range(self.position[0]):
                    output += " "
                for _ in range(self.size):
                    output += "#"
                output += "\n"
            while (remain > 0):
                output += "\n"
                remain -= 1
            output = output[:len(output) - 1]
            return (output)
