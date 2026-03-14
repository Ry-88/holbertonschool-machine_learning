#!/usr/bin/env python3
"""
Module that removes rows with NaN values in the Close column.
"""


def prune(df):
    """
    Remove any rows where the Close column has NaN values.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: DataFrame with NaN rows removed.
    """
    return df.dropna(subset=["Close"])
