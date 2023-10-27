#!/usr/bin/python3
"""
This module is about to multiply 2 matrix
through numpy module
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Print the result of multiplication of 2 matrix

    Attributes:
        m_a (any): first matrix
        m_b (any): second matrix

    Returns: The result of the multiplication
    """
    return (np.dot(m_a, m_b))
