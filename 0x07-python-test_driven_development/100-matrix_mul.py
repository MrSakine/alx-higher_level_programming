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
    not_a_list_check = not_a_list(m_a, m_b)
    if (isinstance(not_a_list_check, str)):
        raise TypeError(not_a_list_check)

    not_a_list_of_lists_check = not_a_list_of_lists(m_a, m_b)
    if (isinstance(not_a_list_of_lists_check, str)):
        raise TypeError(not_a_list_of_lists_check)

    empty_check = empty(m_a, m_b)
    if (isinstance(empty_check, str)):
        raise ValueError(empty_check)

    not_a_int_or_float_check = not_int_or_float(m_a, m_b)
    if (isinstance(not_a_int_or_float_check, str)):
        raise TypeError(not_a_int_or_float_check)

    not_a_rectangle_check = not_a_rectangle(m_a, m_b)
    if (isinstance(not_a_rectangle_check, str)):
        raise TypeError(not_a_rectangle_check)
    elif (len(m_a[0]) != len(m_b)):
        raise ValueError("m_a and m_b can't be multiplied")
    else:
        result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

        for i in range(len(m_a)):
            for j in range(len(m_b[0])):
                for k in range(len(m_b)):
                    result[i][j] += m_a[i][k] * m_b[k][j]

        return (result)


def not_a_list(m_a, m_b, text="%1$ must be a list") -> str | None:
    """
    Check is the m_a or m_b are a list

    Attributes:
        m_a (any): first matrix
        m_b (any): second matrix
        text (:obj:`str`, optional): error text

    Returns:
        - None if they are lists
        - Otherwise, the error message
    """
    if (not isinstance(m_a, list)):
        return (text.replace("%1$", "m_a"))
    elif (not isinstance(m_b, list)):
        return (text.replace("%1$", "m_b"))
    else:
        return (None)


def not_a_list_of_lists(
    m_a,
    m_b,
    text="%1$ must be a list of lists"
) -> str | None:
    """
    Check is the m_a or m_b are a list of lists

    Attributes:
        m_a (any): first matrix
        m_b (any): second matrix
        text (:obj:`str`, optional): error text

    Returns:
        - None if they are list of lists
        - Otherwise, the error message
    """
    if (not all([isinstance(row, list) for row in m_a])):
        return (text.replace("%1$", "m_a"))
    elif (not all([isinstance(row, list) for row in m_b])):
        return (text.replace("%1$", "m_b"))
    else:
        return (None)


def empty(m_a, m_b, text="%1$ can't be empty") -> str | None:
    """
    Check is the m_a or m_b are empty

    Attributes:
        m_a (any): first matrix
        m_b (any): second matrix
        text (:obj:`str`, optional): error text

    Returns:
        - None if they are not empty
        - Otherwise, the error message
    """
    if (len(m_a) == 0 or all([len(row) == 0 for row in m_a])):
        return (text.replace("%1$", "m_a"))
    elif (len(m_b) == 0 or all([len(row) == 0 for row in m_b])):
        return (text.replace("%1$", "m_b"))
    else:
        return (None)


def not_int_or_float(
    m_a,
    m_b,
    text="%1$ should contain only integers or floats"
) -> str | None:
    """
    Check is the m_a or m_b elements are integers or floats

    Attributes:
        m_a (any): first matrix
        m_b (any): second matrix
        text (:obj:`str`, optional): error text

    Returns:
        - None if their elements are integers or floats
        - Otherwise, the error message
    """
    if (
        not all(
            [
                isinstance(el, int) or isinstance(el, float)
                for row in m_a
                for el in row
            ]
        )
    ):
        return (text.replace("%1$", "m_a"))
    elif (
        not all(
            [
                isinstance(el, int) or isinstance(el, float)
                for row in m_b
                for el in row
            ]
        )
    ):
        return (text.replace("%1$", "m_b"))
    else:
        return (None)


def not_a_rectangle(
    m_a,
    m_b,
    text="each row of %1$ must be of the same size"
) -> str | None:
    """
    Check is the m_a or m_b have the same row size

    Attributes:
        m_a (any): first matrix
        m_b (any): second matrix
        text (:obj:`str`, optional): error text

    Returns:
        - None if they have the same row size
        - Otherwise, the error message
    """
    if (
        not all(
            [len(m_a[i]) == len(m_a[i + 1])
             for i in range(len(m_a) - 1)]
        )
    ):
        return (text.replace("%1$", "m_a"))
    elif (
        not all(
            [len(m_b[i]) == len(m_b[i + 1])
             for i in range(len(m_b) - 1)]
        )
    ):
        return (text.replace("%1$", "m_b"))
    else:
        return (None)
