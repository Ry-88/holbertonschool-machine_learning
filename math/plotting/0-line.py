#!/usr/bin/env python3
"""
Module to plot a cubic line graph from 0 to 10 with a red solid line.
"""

import numpy as np
import matplotlib.pyplot as plt


def line():
    """
    Plot a cubic line graph y = x^3 for x in the range 0 to 10.

    - The line is solid red.
    - The x-axis is set from 0 to 10.
    - The plot displays the cubic relationship between x and y.

    Args:
        None

    Returns:
        None: The function displays the plot using matplotlib.
    """
    # Generate x values from 0 to 10
    x = np.arange(0, 11)

    # Compute cubic y values
    y = x ** 3

    # Create a figure with default size
    plt.figure(figsize=(6.4, 4.8))

    # Plot y versus x as a solid red line
    plt.plot(x, y, color='red', linestyle='-')

    # Set x-axis limits exactly from 0 to 10
    plt.xlim(0, 10)

    # Display the plot
    plt.show()
