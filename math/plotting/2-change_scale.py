#!/usr/bin/env python3
"""
Module to plot the exponential decay of C-14 over time.
"""

import numpy as np
import matplotlib.pyplot as plt


def change_scale():
    """
    Plot the exponential decay of C-14 as a line graph.

    - x-axis: Time (years)
    - y-axis: Fraction Remaining (log scale)
    - Title: Exponential Decay of C-14
    - x-axis range: 0 to 28650
    """
    half_life = 5730.0
    x = np.linspace(0, 28650, 1000)
    y = np.exp(-x / half_life)

    plt.figure(figsize=(6.4, 4.8))
    plt.plot(x, y, 'b', linestyle='-')
    plt.xlabel("Time (years)")
    plt.ylabel("Fraction Remaining")
    plt.title("Exponential Decay of C-14")
    plt.yscale("log")
    plt.xlim(0, 28650)
    plt.show()
