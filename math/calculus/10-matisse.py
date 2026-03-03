#!/usr/bin/env python3
"""
Module that defines a function to compute the derivative
of a polynomial represented as a list of coefficients.
"""


def poly_derivative(poly):
    """
    Calculate the derivative of a polynomial.

    Args:
        poly (list): List of coefficients where the index
                     represents the power of x.

    Returns:
        list: New list representing the derivative.
        None: If poly is not valid.
    """
    # Validate input
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    # Check that all elements are numbers (int or float)
    for coef in poly:
        if not isinstance(coef, (int, float)):
            return None

    # If polynomial is constant
    if len(poly) == 1:
        return [0]

    # Compute derivative
    derivative = []
    for i in range(1, len(poly)):
        derivative.append(poly[i] * i)

    # If derivative is zero polynomial
    if all(coef == 0 for coef in derivative):
        return [0]

    return derivative
