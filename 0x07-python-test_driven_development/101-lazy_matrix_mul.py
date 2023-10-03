#!/usr/bin/python3

"""

This module contains a function that multiplies two matrices

"""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.
    Args:
        m_a: The first matrix.
        m_b: The second matrix.
    """

    return (numpy.matmul(m_a, m_b))
