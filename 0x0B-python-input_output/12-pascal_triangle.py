#!/usr/bin/python3
"""

    Representing the Pascal’s triangle of n

"""


def pascal_triangle(n):
    """Representing the Pascal’s triangle of n"""
    if n <= 0:
        return []

    lst = []
    for i in range(n):
        row_lst = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row_lst.append(1)
            else:
                row_lst.append(lst[i - 1][j] + lst[i - 1][j - 1])
        lst.append(row_lst)
    return lst
