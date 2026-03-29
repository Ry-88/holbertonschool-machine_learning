#!/usr/bin/env python3
"""
Module that plots a histogram of student grades for Project A.
"""
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """
    Plots a histogram of student scores with bins of width 10,
    labeled axes, and outlined bars.
    """
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    plt.hist(student_grades, bins=np.arange(0, 110, 10), edgecolor='black')
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')
    plt.xlim(0, 100)
    plt.xticks(range(0, 110, 10))
    plt.ylim(0, 30)
    plt.yticks(range(0, 31, 5))

    plt.show()
