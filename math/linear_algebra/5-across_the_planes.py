#!/usr/bin/env python3
""" a function that adds two matrices element-wise
"""


def add_matrices2D(mat1, mat2):
    """Adds two matrices element-wise"""
    if type(mat1) is not list or type(mat2) is not list:
        return None
    if len(mat1) != len(mat2):
        return None
    for i in range(len(mat1)):
        if type(mat1[i]) is not list or type(mat2[i]) is not list:
            return None
        if len(mat1[i]) != len(mat2[i]):
            return None
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))]
            for i in range(len(mat1))]
