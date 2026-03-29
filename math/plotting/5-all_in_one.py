#!/usr/bin/env python3
"""
Module that plots all previous graphs in one figure.
"""
import numpy as np
import matplotlib.pyplot as plt


def all_in_one():
    """
    Plots 5 graphs in a 3x2 grid with the last plot spanning
    two columns and all text in x-small font size.
    """
    y0 = np.arange(0, 11) ** 3

    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
    y1 += 180

    x2 = np.arange(0, 28651, 5730)
    r2 = np.log(0.5)
    t2 = 5730
    y2 = np.exp((r2 / t2) * x2)

    x3 = np.arange(0, 21000, 1000)
    r3 = np.log(0.5)
    t31 = 5730
    t32 = 1600
    y31 = np.exp((r3 / t31) * x3)
    y32 = np.exp((r3 / t32) * x3)

    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)

    # Create figure
    plt.figure(figsize=(6.4, 4.8))
    plt.suptitle("All in One")

    # Plot 1 (top-left)
    plt.subplot(3, 2, 1)
    plt.plot(y0, 'r-')
    plt.title("y = x^3", fontsize='x-small')

    # Plot 2 (top-right)
    plt.subplot(3, 2, 2)
    plt.scatter(x1, y1, s=10)
    plt.title("Men's Height vs Weight", fontsize='x-small')
    plt.xlabel("Height (in)", fontsize='x-small')
    plt.ylabel("Weight (lbs)", fontsize='x-small')

    # Plot 3 (middle-left)
    plt.subplot(3, 2, 3)
    plt.plot(x2, y2)
    plt.yscale('log')
    plt.title("Exponential Decay of C-14", fontsize='x-small')
    plt.xlabel("Time (years)", fontsize='x-small')
    plt.ylabel("Fraction Remaining", fontsize='x-small')

    # Plot 4 (middle-right)
    plt.subplot(3, 2, 4)
    plt.plot(x3, y31, 'r--', label='C-14')
    plt.plot(x3, y32, 'g-', label='Ra-226')
    plt.title("Exponential Decay of Radioactive Elements",
              fontsize='x-small')
    plt.xlabel("Time (years)", fontsize='x-small')
    plt.ylabel("Fraction Remaining", fontsize='x-small')
    plt.legend(fontsize='x-small')

    # Plot 5 (bottom, spans 2 columns)
    plt.subplot(3, 1, 3)
    plt.hist(student_grades,
             bins=np.arange(0, 110, 10),
             edgecolor='black')
    plt.title("Project A", fontsize='x-small')
    plt.xlabel("Grades", fontsize='x-small')
    plt.ylabel("Number of Students", fontsize='x-small')

    # Adjust layout to prevent overlap
    plt.tight_layout()
    plt.show()
