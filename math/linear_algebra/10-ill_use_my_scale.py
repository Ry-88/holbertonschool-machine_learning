#!/usr/bin/env python3
"""Write a function that calculates
the shape of a numpy.ndarray"""


import numpy as np

def np_shape(matrix):
    """Calculates the shape of a numpy.ndarray"""
    if type(matrix) is not np.ndarray:
        return None
    return list(matrix.shape)
