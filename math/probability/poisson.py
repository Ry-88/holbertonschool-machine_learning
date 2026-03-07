#!/usr/bin/env python3
"""Create a class Poisson that represents
a Poisson distribution.
"""

import math


class Poisson:
    """
    Represents a Poisson distribution.

    Attributes:
    -----------
    lambtha : float
        The expected number of occurrences in a given time frame.
    """

    def __init__(self, data=None, lambtha=1.0):
        """
        Initialize a Poisson distribution instance.

        Parameters:
        -----------
        data : list, optional
            A list of data to estimate the distribution's lambtha.
            If provided, lambtha is calculated as the mean of the data.
        lambtha : float, optional
            The expected number of occurrences (default is 1.0).
            Used only if data is None.

        Raises:
        -------
        TypeError:
            If data is not a list.
        ValueError:
            If lambtha <= 0.
            If data contains fewer than 2 values.
        """
        if data is None:
            # Case when data is not provided: use lambtha directly
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            # Case when data is provided: estimate lambtha from data
            if not isinstance(data, list):
                raise TypeError("data must be a list")

            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            # Calculate lambtha as the mean of the data
            self.lambtha = float(sum(data) / len(data))
