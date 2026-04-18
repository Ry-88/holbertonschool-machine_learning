#!/usr/bin/env python3
"""
Module for performing K-means clustering.
"""
import numpy as np


def kmeans(X, k, iterations=1000):
    """
    Performs K-means clustering on a dataset.

    Args:
        X (numpy.ndarray): Array of shape (n, d) containing the dataset.
        k (int): Positive integer containing the number of clusters.
        iterations (int): Positive integer containing the max iterations.

    Returns:
        C (numpy.ndarray): Shape (k, d) containing the centroid means,
                           or None on failure.
        clss (numpy.ndarray): Shape (n,) containing the index of the cluster
                              that each data point belongs to, or None on fail.
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None, None
    if type(k) is not int or k <= 0:
        return None, None
    if type(iterations) is not int or iterations <= 0:
        return None, None

    # Get bounds for initialization
    low = np.min(X, axis=0)
    high = np.max(X, axis=0)

    # 1. Initialize the cluster centroids using multivariate uniform distribution
    C = np.random.uniform(low, high, size=(k, X.shape[1]))

    # Loop 1: Iterations over the dataset
    for _ in range(iterations):
        C_copy = np.copy(C)

        # Calculate distances from each point to each centroid using broadcasting
        # X[:, np.newaxis] broadcasts to (n, 1, d) and C broadcasts to (k, d)
        # Resulting differences are (n, k, d), taking the norm across axis 2 yields (n, k)
        distances = np.linalg.norm(X[:, np.newaxis] - C, axis=2)
        
        # Get cluster assignments based on minimum distance
        clss = np.argmin(distances, axis=1)

        # Loop 2: Update centroids based on assigned points
        for j in range(k):
            cluster_points = X[clss == j]
            
            # Reinitialize empty clusters
            if cluster_points.shape[0] == 0:
                # 2. Second exact use of numpy.random.uniform
                C[j] = np.random.uniform(low, high, size=(1, X.shape[1]))
            else:
                C[j] = np.mean(cluster_points, axis=0)

        # Check for convergence: no change in centroids between iterations.
        if np.all(C_copy == C):
            break

    return C, clss
