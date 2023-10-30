#!/usr/bin/python3
"""
This module solves the N queens problem
"""
import sys


class NQueenPuzzle():
    """
    NQueenPuzzle class definition
    """

    def __init__(self, number=None) -> None:
        """
        Initializes class instances attributes
        Throw errors if number isn't integer or less than 4

        Attributes:
            number (any): The number of queens

        Returns: None
        """
        temp = int(number)
        if (temp < 4):
            print("N must be at least 4")
            exit(1)
        self.__number = temp

    @property
    def number(self):
        """Returns the number of queens"""
        return (self.__number)

    @number.setter
    def number(self, value):
        """Set a new number of queens"""
        self.__init__(value)

    def possible_solutions(self):
        """Returns the possible solutions"""
        pass


"""
Todo:
    - throw errors if number isn't an integer, otherwise
    - get the number through sys module
    - create a new instance of the class NQueenPuzzle
    - print every possible solutions
"""
try:
    puzzle = NQueenPuzzle(sys.argv[1])
    print(puzzle.possible_solutions())
except IndexError:
    print("Usage: nqueens N")
    exit(1)
except ValueError:
    print("N must be a number")
    exit(1)
