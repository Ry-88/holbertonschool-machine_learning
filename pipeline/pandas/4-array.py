#!/usr/bin/env python3
"""
Module that converts the last 10 rows of High and Close columns
into a numpy array.
"""


def array(df):
    """
    Select the last 10 rows of High and Close columns and convert
    them into a numpy.ndarray.

    Args:
        df (pd.DataFrame): DataFrame containing High and Close columns.

    Returns:
        numpy.ndarray: Array of the selected values.
    """
    return df[["High", "Close"]].tail(10).values
