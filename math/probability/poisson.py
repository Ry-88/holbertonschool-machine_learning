#!/usr/bin/env python3
"""Module that defines a Poisson distribution."""


class Poisson:
    """Represents a Poisson distribution."""

    def __init__(self, data=None, lambtha=1.0):
        """Initialize a Poisson distribution.

        Args:
            data (list): List of data to estimate lambtha.
            lambtha (float): Expected number of occurrences.

        Raises:
            TypeError: If data is not a list.
            ValueError: If data has less than two values.
            ValueError: If lambtha is not positive.
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")

            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """Calculates the value of the PMF for a given number of successes.

        Args:
            k (int or float): Number of successes.

        Returns:
            float: PMF value for k.
        """
        # Convert k to integer
        k = int(k)

        # If k is negative, PMF is 0
        if k < 0:
            return 0

        # PMF formula: P(X=k) = (e^-lambtha * lambtha^k) / k!
        # Using math.exp and math.factorial
        from math import exp, factorial
        return (exp(-self.lambtha) * self.lambtha**k) / factorial(k)
