#!/usr/bin/python3
"""
This module is about to multiply 2 matrix
Use this to run
matrix_mul = __import__('100-matrix_mul').matrix_mul
matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
"""


def matrix_mul(m_a, m_b):
    """
    Multiple two matrix,
    throw errors when
    - m_a or m_b is not a list
    - m_a or m_b is not a list of lists
    - m_a or m_b is empty (it means: = [] or = [[]])
    - one element of m_a or m_b is not an integer or a float
    - m_a or m_b is not a rectangle (all rows should be of the same size)
    - m_a and m_b can't be multiplied

    Attributes:
        m_a (any): first matrix
        m_b (any): second matrix

    Returns: None
    """
    text = "%1$ must be a list"
    if (not isinstance(m_a, list)):
        raise TypeError(text.replace("%1$", "m_a"))
    if (not isinstance(m_b, list)):
        raise TypeError(text.replace("%1$", "m_b"))

    text = "%1$ must be a list of lists"
    if (not all([isinstance(row, list) for row in m_a])):
        raise TypeError(text.replace("%1$", "m_a"))
    if (not all([isinstance(row, list) for row in m_b])):
        raise TypeError(text.replace("%1$", "m_b"))

    text = "%1$ can't be empty"
    if (len(m_a) == 0 or all([len(row) == 0 for row in m_a])):
        raise ValueError(text.replace("%1$", "m_a"))
    if (len(m_b) == 0 or all([len(row) == 0 for row in m_b])):
        raise ValueError(text.replace("%1$", "m_b"))

    text = "%1$ should contain only integers or floats"
    if (
        not all(
            [
                isinstance(el, int) or isinstance(el, float)
                for row in m_a
                for el in row
            ]
        )
    ):
        raise TypeError(text.replace("%1$", "m_a"))
    if (
        not all(
            [
                isinstance(el, int) or isinstance(el, float)
                for row in m_b
                for el in row
            ]
        )
    ):
        raise TypeError(text.replace("%1$", "m_b"))

    text = "each row of %1$ must be of the same size"
    if (
        not all([len(m_a[i]) == len(m_a[i + 1]) for i in range(len(m_a) - 1)])
    ):
        raise TypeError(text.replace("%1$", "m_a"))
    if (
        not all([len(m_b[i]) == len(m_b[i + 1]) for i in range(len(m_b) - 1)])
    ):
        raise TypeError(text.replace("%1$", "m_b"))
    if (len(m_a[0]) != len(m_b)):
        raise ValueError("m_a and m_b can't be multiplied")
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return (result)
