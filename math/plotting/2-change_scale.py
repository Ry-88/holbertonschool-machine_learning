#!/usr/bin/env python3
"""
Module to plot the exponential decay of C-14 over time
as a line graph with logarithmic y-axis.
"""

import numpy as np
import matplotlib.pyplot as plt


def line():
    """
    Plot the exponential decay of C-14 as a line graph.

    - x-axis: Time (years)
    - y-axis: Fraction Remaining (logarithmic scale)
    - Title: Exponential Decay of C-14
    - x-axis range: 0 to 28650
    - The decay is modeled as y = e^(-t / half_life), with half-life 5730 years

    Args:
        None

    Returns:
        None: Displays the plot using matplotlib.
    """
    # Half-life of C-14 in years
    half_life = 5730.0

    # Generate x values from 0 to 28650 years
    x = np.linspace(0, 28650, 1000)

    # Compute exponential decay: fraction remaining
    y = np.exp(-x / half_life)

    # Create figure with default size
    plt.figure(figsize=(6.4, 4.8))

    # Plot y vs x as a solid blue line
    plt.plot(x, y, color='b', linestyle='-')

    # Label x-axis
    plt.xlabel("Time (years)")

    # Label y-axis
    plt.ylabel("Fraction Remaining")

    # Set title of the plot
    plt.title("Exponential Decay of C-14")

    # Set y-axis to logarithmic scale
    plt.yscale("log")

    # Set x-axis limits from 0 to 28650
    plt.xlim(0, 28650)

    # Display the plot
    plt.show()
