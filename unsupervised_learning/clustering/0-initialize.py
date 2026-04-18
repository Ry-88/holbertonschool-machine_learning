#!/usr/bin/env python3
"""Module for initializing K-means centroids"""

import numpy as np


def initialize(X, k):
    """
    Initializes cluster centroids for K-means clustering

    Parameters:
    X (numpy.ndarray): shape (n, d) dataset
        n: number of data points
        d: number of dimensions
    k (int): number of clusters

    Returns:
    numpy.ndarray of shape (k, d) containing the initialized
    centroids, or None on failure
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None

    if not isinstance(k, int) or k <= 0:
        return None

    n, d = X.shape

    if k > n:
        return None

    min_vals = np.min(X, axis=0)
    max_vals = np.max(X, axis=0)

    return np.random.uniform(min_vals, max_vals, (k, d))
