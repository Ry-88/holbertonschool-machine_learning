#!/usr/bin/env python3
"""Module that defines an Exponential distribution."""


class Exponential:
    """Represents an exponential distribution."""

    def __init__(self, data=None, lambtha=1.):
        """Initialize an Exponential distribution.

        Args:
            data (list): List of data to estimate lambtha
            lambtha (float): Expected number of occurrences

        Raises:
            TypeError: If data is not a list
            ValueError: If data has fewer than two values
            ValueError: If lambtha is not positive
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

            mean = sum(data) / len(data)
            self.lambtha = float(1 / mean)

    def pdf(self, x):
        """Calculates the value of the PDF for a given time period."""
        if x < 0:
            return 0

        return self.lambtha * (2.7182818285 ** (-self.lambtha * x))

    def cdf(self, x):
        """Calculates the value of the CDF for a given time period."""
        if x < 0:
            return 0

        return 1 - (2.7182818285 ** (-self.lambtha * x))
