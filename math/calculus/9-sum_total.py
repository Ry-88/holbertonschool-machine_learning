#!/usr/bin/env python3
"""
Module that provides a function to compute the sum of squares.
"""


def summation_i_squared(n):
    """
    Calculate the sum of squares from 1 to n.

    Args:
        n (int): Stopping condition.

    Returns:
        int: The integer value of the sum.
        None: If n is not a valid number.
    """
    if not isinstance(n, int) or n < 1:
        return None

    return n * (n + 1) * (2 * n + 1) // 6
