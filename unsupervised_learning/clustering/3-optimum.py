#!/usr/bin/env python3
"""Module for determining the optimum number of clusters."""

import numpy as np

kmeans = __import__('1-kmeans').kmeans
variance = __import__('2-variance').variance


def optimum_k(X, kmin=1, kmax=None, iterations=1000):
    """
    Tests for the optimum number of clusters using variance

    Performs K-means clustering for different values of k and
    evaluates the improvement in variance compared to kmin.

    Parameters:
    X (numpy.ndarray): shape (n, d) containing the dataset
        n is the number of data points
        d is the number of dimensions for each data point
    kmin (int): minimum number of clusters to test
    kmax (int): maximum number of clusters to test
        if None, kmax is set to n (number of data points)
    iterations (int): maximum number of iterations for K-means

    Returns:
    tuple:
        results (list): list containing tuples of (C, clss) for each k
            C is a numpy.ndarray of shape (k, d) with centroid means
            clss is a numpy.ndarray of shape (n,) with cluster indices
        d_vars (list): list of variance differences from kmin
    Returns (None, None) on failure
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None, None

    if not isinstance(kmin, int) or kmin <= 0:
        return None, None

    if kmax is not None and (not isinstance(kmax, int) or kmax < kmin):
        return None, None

    if not isinstance(iterations, int) or iterations <= 0:
        return None, None

    if isinstance(kmax, int) and kmax <= kmin:
        return None, None

    if kmax is None:
        max_cluster = X.shape[0]
    else:
        max_cluster = kmax

    results = []
    d_vars = []

    # Compute baseline clustering (k = kmin)
    C, clss = kmeans(X, kmin, iterations)
    results.append((C, clss))

    base_var = variance(X, C)
    d_vars = [0.0]

    k = kmin + 1

    # Test increasing number of clusters
    while k < max_cluster + 1:
        C, clss = kmeans(X, k, iterations)
        current_var = variance(X, C)

        results.append((C, clss))
        d_vars.append(base_var - current_var)

        k += 1

    return results, d_vars
