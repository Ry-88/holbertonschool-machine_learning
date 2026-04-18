#!/usr/bin/env python3
"""Module for performing K-means clustering"""

import numpy as np


def initialize(X, k):
    """
    Initializes cluster centroids for K-means

    Parameters:
    X (numpy.ndarray): shape (n, d) dataset
    k (int): number of clusters

    Returns:
    numpy.ndarray of shape (k, d) or None
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


def kmeans(X, k, iterations=1000):
    """
    Performs K-means clustering

    Parameters:
    X (numpy.ndarray): shape (n, d) dataset
    k (int): number of clusters
    iterations (int): max number of iterations

    Returns:
    C, clss or None, None on failure
    C: centroid means (k, d)
    clss: cluster indices (n,)
    """
    if (not isinstance(X, np.ndarray) or X.ndim != 2 or
            not isinstance(k, int) or k <= 0 or
            not isinstance(iterations, int) or iterations <= 0):
        return None, None

    n, d = X.shape
    if k > n:
        return None, None

    C = initialize(X, k)
    if C is None:
        return None, None

    for _ in range(iterations):  # loop 1
        # Compute distances (vectorized)
        distances = np.linalg.norm(X[:, None] - C, axis=2)

        # Assign clusters
        clss = np.argmin(distances, axis=1)

        new_C = np.copy(C)

        for i in range(k):  # loop 2
            points = X[clss == i]

            if points.size == 0:
                # Reinitialize centroid (second uniform call)
                min_vals = np.min(X, axis=0)
                max_vals = np.max(X, axis=0)
                new_C[i] = np.random.uniform(min_vals, max_vals)
            else:
                new_C[i] = np.mean(points, axis=0)

        # Check convergence
        if np.allclose(C, new_C):
            return C, clss

        C = new_C

    return C, clss
