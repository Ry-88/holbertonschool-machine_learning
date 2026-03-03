#!/usr/bin/env python3
"""Module that concatenates two numpy arrays along a given axis."""

import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    Concatenates two numpy.ndarrays along a specified axis.

    Args:
        mat1 (numpy.ndarray): First matrix.
        mat2 (numpy.ndarray): Second matrix.
        axis (int): Axis along which to concatenate.

    Returns:
        numpy.ndarray: The concatenated matrix.
    """
    return np.concatenate((mat1, mat2), axis=axis)
