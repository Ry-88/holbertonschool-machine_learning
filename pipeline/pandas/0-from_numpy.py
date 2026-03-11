#!/usr/bin/env python3
"""Creates a pandas DataFrame from a NumPy ndarray"""

import pandas as pd


def from_numpy(array):
    """Create a pandas DataFrame from a NumPy ndarray.

    Args:
        array: numpy ndarray

    Returns:
        pandas DataFrame with alphabetically labeled columns
    """

    columns = []
    for i in range(array.shape[1]):
        columns.append(chr(65 + i))

    return pd.DataFrame(array, columns=columns)
