#!/usr/bin/env python3
"""
Module to plot a scatter graph of men's height vs weight using simulated data.
"""

import numpy as np
import matplotlib.pyplot as plt


def scatter():
    """
    Generate and plot a scatter graph of men's height vs weight.

    - x-axis: Height (in)
    - y-axis: Weight (lbs)
    - Points are magenta
    - Title: Men's Height vs Weight

    The data is generated from a multivariate normal distribution
    and adjusted to simulate realistic weights.

    Args:
        None

    Returns:
        None: Displays the scatter plot using matplotlib.
    """
    # Mean height 69 inches, covariance 15
    mean = [69, 0]
    cov = [[15, 8], [8, 15]]

    # Set random seed for reproducibility
    np.random.seed(5)

    # Generate 2000 samples
    x, y = np.random.multivariate_normal(mean, cov, 2000).T

    # Shift weights to realistic values
    y += 180

    # Create figure with default size
    plt.figure(figsize=(6.4, 4.8))

    # Scatter plot with magenta points
    plt.scatter(x, y, color='m')

    # Label axes
    plt.xlabel("Height (in)")
    plt.ylabel("Weight (lbs)")

    # Set title
    plt.title("Men's Height vs Weight")

    # Display plot
    plt.show()
