#!/usr/bin/env python3

def matrix_shape(matrix):
    """Calculates the shape of a matrix"""
    if type(matrix) is not list or len(matrix) == 0:
        return []
    if type(matrix[0]) is not list:
        return [len(matrix)]
    return [len(matrix)] + matrix_shape(matrix[0])
