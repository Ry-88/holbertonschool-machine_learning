#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def scatter():
    """
    Plot a scatter graph of men's height vs weight.

    - x-axis: Height (in)
    - y-axis: Weight (lbs)
    - Points are magenta
    - Title: Men's Height vs Weight
    """
    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x, y = np.random.multivariate_normal(mean, cov, 2000).T
    y += 180
    plt.figure(figsize=(6.4, 4.8))

    # Scatter plot of x vs y with magenta points
    plt.scatter(x, y, color='m')

    # Set axis labels
    plt.xlabel("Height (in)")
    plt.ylabel("Weight (lbs)")

    # Set plot title
    plt.title("Men's Height vs Weight")

    # Display the plot
    plt.show()
