#!/usr/bin/env python3
"""Write a function that calculates
the shape of a numpy.ndarray"""


def np_shape(matrix):
    """Calculates the shape of a numpy.ndarray"""
    # Check if it has shape attribute (duck typing for numpy arrays)
    if not hasattr(matrix, 'shape'):
        return None
    return list(matrix.shape)
