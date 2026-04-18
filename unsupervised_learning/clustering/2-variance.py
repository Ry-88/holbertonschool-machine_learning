#!/usr/bin/env python3
"""Module for computing total intra-cluster variance."""

import numpy as np


def variance(X, C):
    """
    Calculates the total intra-cluster variance for a dataset

    Parameters:
    X (numpy.ndarray): shape (n, d) containing the dataset
        n is the number of data points
        d is the number of dimensions for each data point
    C (numpy.ndarray): shape (k, d) containing the centroid means
        k is the number of clusters

    Returns:
    float: total intra-cluster variance
    Returns None on failure
    """
    # Validate inputs
    if (
        not isinstance(X, np.ndarray)
        or X.ndim != 2
        or not isinstance(C, np.ndarray)
        or C.ndim != 2
        or X.shape[1] != C.shape[1]
        or C.shape[0] == 0
    ):
        return None

    # Compute differences using broadcasting → shape (n, k, d)
    diff = X[:, None, :] - C[None, :, :]

    # Squared distances → shape (n, k)
    dist_sq = (diff ** 2).sum(axis=2)

    # Minimum squared distance per point → shape (n,)
    min_dist_sq = np.min(dist_sq, axis=1)

    # Total intra-cluster variance (scalar)
    return np.sum(min_dist_sq)
