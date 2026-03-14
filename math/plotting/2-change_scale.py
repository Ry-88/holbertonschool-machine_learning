#!/usr/bin/env python3
"""
Module to plot the exponential decay of C-14 over time.
The plot shows a line graph with logarithmic y-axis.
"""

import numpy as np
import matplotlib.pyplot as plt


def line():
    """
    Plot the exponential decay of C-14 as a line graph.

    - x-axis: Time (years)
    - y-axis: Fraction Remaining (log scale)
    - Title: Exponential Decay of C-14
    - x-axis range: 0 to 28650 years
    - The decay is modeled using the formula y = exp(-t / half_life)

    Args:
        None

    Returns:
        None: The function displays the plot using matplotlib.
    """
    # Half-life of C-14 in years
    half_life = 5730.0

    # Generate x values from 0 to 28650
    x = np.linspace(0, 28650, 1000)

    # Compute fraction remaining
    y = np.exp(-x / half_life)

    # Create figure
    plt.figure(figsize=(6.4, 4.8))

    # Plot line in solid blue
    plt.plot(x, y, color='b', linestyle='-')

    # Set axis labels
    plt.xlabel("Time (years)")
    plt.ylabel("Fraction Remaining")

    # Set plot title
    plt.title("Exponential Decay of C-14")

    # Logarithmic scale for y-axis
    plt.yscale("log")

    # Set x-axis exactly from 0 to 28650
    plt.xlim(0, 28650)

    # Display plot
    plt.show()
