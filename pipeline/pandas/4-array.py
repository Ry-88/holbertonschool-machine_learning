#!/usr/bin/env python3
"""
Module that converts selected DataFrame values to a numpy array.
"""

import pandas as pd


def array(df):
    """
    Select the last 10 rows of the High and Close columns
    and convert them into a numpy.ndarray.

    Args:
        df (pd.DataFrame): DataFrame containing High and Close columns.

    Returns:
        numpy.ndarray: Array containing the selected values.
    """
    # Select last 10 rows of High and Close
    selected = df[["High", "Close"]].tail(10)

    # Convert to numpy array
    return selected.values
