#!/usr/bin/env python3
"""
Module for visualising the exponential decay of Carbon-14 (C-14).

C-14 decays at a constant rate described by the equation:
    N(t) = N0 * exp((ln(0.5) / t_half) * t)

where t_half is the half-life of C-14 (~5730 years).  The plot uses a
logarithmic y-axis so that the exponential decay appears as a straight line,
making the half-life intervals easy to read off the chart.
"""

import numpy as np
import matplotlib.pyplot as plt


def change_scale():
    """
    Plot the exponential decay of C-14 over five half-life intervals.

    Computes the fraction of C-14 remaining at each half-life step from
    t = 0 to t = 28650 years (five half-lives), then renders a line graph
    with a logarithmic y-axis.

    The decay fraction at time t is given by:
        y = exp((ln(0.5) / t_half) * t)

    Axes:
        x -- Time in years, ranging from 0 to 28 650.
        y -- Fraction of C-14 remaining (logarithmic scale).

    Returns:
        None
    """
    # Build an array of time points at each half-life interval (years).
    x = np.arange(0, 28651, 5730)

    # Decay constant: ln(0.5) ensures the fraction halves every t_half years.
    r = np.log(0.5)

    # Half-life of C-14 in years.
    t = 5730

    # Fraction remaining at each time point.
    y = np.exp((r / t) * x)

    # Initialise the figure with a standard 6.4 × 4.8 inch canvas.
    plt.figure(figsize=(6.4, 4.8))

    # Draw the decay curve.
    plt.plot(x, y)

    # Label the axes.
    plt.xlabel("Time (years)")
    plt.ylabel("Fraction Remaining")

    # Add a descriptive title.
    plt.title("Exponential Decay of C-14")

    # Switch to a logarithmic y-axis so the decay plots as a straight line.
    plt.yscale("log")

    # Constrain the x-axis to exactly the simulated range.
    plt.xlim(0, 28650)

    # Adjust layout to prevent labels from being clipped.
    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    change_scale()
