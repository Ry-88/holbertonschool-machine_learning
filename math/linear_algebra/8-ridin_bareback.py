#!/usr/bin/env python3
"""Write a function that performs matrix multiplication"""


def mat_mul(mat1, mat2):
    """Performs matrix multiplication"""
    if type(mat1) is not list or type(mat2) is not list:
        return None
    if len(mat1) == 0 or len(mat2) == 0:
        return None
    if type(mat1[0]) is not list or type(mat2[0]) is not list:
        return None
    if len(mat1[0]) != len(mat2):
        return None
    return [[sum(mat1[i][k] * mat2[k][j] for k in range(len(mat2)))
             for j in range(len(mat2[0]))] for i in range(len(mat1))]
