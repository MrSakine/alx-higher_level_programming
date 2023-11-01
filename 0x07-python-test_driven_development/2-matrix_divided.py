#!/usr/bin/python3
"""
This module is about dividing matrix members by an integer
Use this to run
matrix_divided = __import__('2-matrix_divided').matrix_divided
matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """
    Divide matrix members by div, throw errors when
    - matrix isn't a list or a list of list
    - matrix list elements aren't integers and floats
    - matrix lists size aren't the same
    - div isn't an integer or a float or is zero

    Attributes:
        matrix (any): the matrix of integers or floats
        div (any): the number to use for division

    Returns:
        A new matrix with the members of old ones divided by div argument
    """
    if (
        not isinstance(matrix, list) or matrix == [] or
        not all([isinstance(row, list) for row in matrix]) or
        all(row == [] for row in matrix)
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    elif (
        not all(
            [
                isinstance(el, int) or isinstance(el, float)
                for row in matrix
                for el in row
            ]
        )
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    elif (
        not all(
            [len(matrix[i]) == len(matrix[i + 1])
             for i in range(len(matrix) - 1)]
        )
    ):
        raise TypeError("Each row of the matrix must have the same size")
    elif (
        not isinstance(div, int) and
        not isinstance(div, float)
    ):
        raise TypeError("div must be a number")
    elif (div == 0):
        raise ZeroDivisionError("division by zero")
    else:
        result = []
        for i in matrix:
            temp = []
            for j in i:
                n = round((j / div), 2)
                temp.append(n)
            result.append(temp)
        return (result)
