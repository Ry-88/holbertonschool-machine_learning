#!/usr/bin/env python3
"""Function that calculates the shape of a numpy.ndarray"""


def np_shape(matrix):
    """Return the shape of a numpy.ndarray"""
    if not hasattr(matrix, "shape"):
        return None
    return list(matrix.shape)
