#!/usr/bin/env python3
"""
Module that defines a function to compute the integral
of a polynomial represented as a list of coefficients.
"""


def poly_integral(poly, C=0):
    """
    Calculate the integral of a polynomial.

    Args:
        poly (list): List of coefficients where the index
                     represents the power of x.
        C (int): Integration constant.

    Returns:
        list: New list representing the integral.
        None: If poly or C are not valid.
    """
    # Validate poly
    if (not isinstance(poly, list) or len(poly) == 0 or
            not all(isinstance(coef, (int, float)) for coef in poly)):
        return None

    # Validate C
    if not isinstance(C, int):
        return None

    # If polynomial is zero
    if poly == [0]:
        return [C]

    integral = [C]

    # Compute integral
    for i, coef in enumerate(poly):
        value = coef / (i + 1)

        # Convert whole numbers to int
        if value.is_integer():
            value = int(value)

        integral.append(value)

    # Remove trailing zeros (make list as small as possible)
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral
