#!/usr/bin/env python3
"""Module that performs matrix multiplication using numpy."""

import numpy as np


def np_matmul(mat1, mat2):
    """
    Performs matrix multiplication between two numpy.ndarrays.

    Args:
        mat1 (numpy.ndarray): First matrix.
        mat2 (numpy.ndarray): Second matrix.

    Returns:
        numpy.ndarray: The product of mat1 and mat2.
    """
    return np.matmul(mat1, mat2)
