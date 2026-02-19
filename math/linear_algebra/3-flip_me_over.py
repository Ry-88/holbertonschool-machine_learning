#!/usr/bin/env python3
""" Write a function that
returns the transpose of a 2D matrix
"""


def matrix_transpose(matrix):
    """Calculates the transpose of a matrix"""
    if type(matrix) is not list or len(matrix) == 0:
        return []
    if type(matrix[0]) is not list:
        return [[i] for i in matrix]
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
