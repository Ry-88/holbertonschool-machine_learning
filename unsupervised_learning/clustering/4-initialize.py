#!/usr/bin/env python3
"""Module for initializing a Gaussian Mixture Model."""

import numpy as np

kmeans = __import__('1-kmeans').kmeans


def initialize(X, k):
    """
    Initializes the parameters for a Gaussian Mixture Model (GMM)

    Parameters:
    X (numpy.ndarray): shape (n, d) containing the dataset
        n is the number of data points
        d is the number of dimensions for each data point
    k (int): number of clusters (Gaussian components)

    Returns:
    tuple:
        pi (numpy.ndarray): shape (k,) containing the priors
            for each cluster
        m (numpy.ndarray): shape (k, d) containing the centroid
            means for each cluster
        S (numpy.ndarray): shape (k, d, d) containing the covariance
            matrices for each cluster
    Returns (None, None, None) on failure
    """
    # --------- Validation ----------
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None, None, None
    if not isinstance(k, int) or k <= 0:
        return None, None, None

    n, d = X.shape
    if k > n:
        return None, None, None

    # --------- Initialize priors ----------
    # Equal probability for each cluster
    pi = np.full(k, 1 / k)

    # --------- Initialize means using K-means ----------
    m, _ = kmeans(X, k)
    if m is None:
        return None, None, None

    # --------- Initialize covariance matrices ----------
    # Identity matrix for each cluster (shape: k, d, d)
    S = np.tile(np.eye(d), (k, 1, 1))

    return pi, m, S
