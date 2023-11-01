#!/usr/bin/python3
"""
This module is about to multiply 2 matrix
through numpy module
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplication of 2 matrix through numpy.dot() function

    Attributes:
        m_a (any): first matrix
        m_b (any): second matrix

    Returns: The result of the multiplication
    """
    return (np.matmul(m_a, m_b))
