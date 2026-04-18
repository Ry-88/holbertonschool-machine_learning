#!/usr/bin/env python3
"""Module for performing K-means clustering"""

import numpy as np


def kmeans(X, k, iterations=1000):
    """
    Performs K-means clustering on a dataset

    Parameters:
    X (numpy.ndarray): shape (n, d) containing the dataset
        n is the number of data points
        d is the number of dimensions for each data point
    k (int): number of clusters
    iterations (int): maximum number of iterations

    Returns:
    tuple:
        centroids (numpy.ndarray): shape (k, d) containing the
        centroid means for each cluster
        clss (numpy.ndarray): shape (n,) containing the index of
        the cluster each data point belongs to
    Returns (None, None) on failure
    """
    if type(k) is not int or k <= 0:
        return None, None
    if type(X) is not np.ndarray or len(X.shape) != 2:
        return None, None
    if type(iterations) is not int or iterations <= 0:
        return None, None

    n, d = X.shape

    centroids = np.random.uniform(
        np.min(X, axis=0),
        np.max(X, axis=0),
        size=(k, d)
    )

    for i in range(iterations):
        copy = centroids.copy()

        D = np.sqrt(((X - centroids[:, np.newaxis]) ** 2).sum(axis=2))
        clss = np.argmin(D, axis=0)

        for j in range(k):
            if len(X[clss == j]) == 0:
                centroids[j] = np.random.uniform(
                    np.min(X, axis=0),
                    np.max(X, axis=0),
                    size=(1, d)
                )
            else:
                centroids[j] = (X[clss == j]).mean(axis=0)

        D = np.sqrt(((X - centroids[:, np.newaxis]) ** 2).sum(axis=2))
        clss = np.argmin(D, axis=0)

        if np.all(copy == centroids):
            return centroids, clss

    return centroids, clss
