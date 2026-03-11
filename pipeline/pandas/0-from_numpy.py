#!/usr/bin/env python3
"""Creates a pandas DataFrame from a NumPy ndarray"""

import numpy as np
import pandas as pd


def from_numpy(array):
    """Create a pandas DataFrame from a NumPy ndarray.

    Args:
        array (np.ndarray): numpy array used to create the DataFrame

    Returns:
        pd.DataFrame: DataFrame with alphabetical capitalized columns
    """

    cols = [chr(65 + i) for i in range(array.shape[1])]
    return pd.DataFrame(array, columns=cols)
