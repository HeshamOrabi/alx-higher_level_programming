#!/usr/bin/python3
"""

    Function that divides all elements of a matrix.

"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix

    Args:
        matrix: matrix to be divided
        div: the divider

    Return: resulting matrix
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(err)
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    fls = []
    for lst in matrix:
        if not isinstance(lst, list):
            raise TypeError(err)
        row_size = len(matrix[0])
        if len(lst) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        res_list = []
        for i in lst:
            if not isinstance(i, (float, int)):
                raise TypeError(err)
            res = round(i / div, 2)
            res_list.append(res)
        fls.append(res_list)
    return fls
