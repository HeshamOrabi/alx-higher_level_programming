#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matix = []
    new_matix = [[i**2 for i in row]for row in matrix]
    return new_matix
