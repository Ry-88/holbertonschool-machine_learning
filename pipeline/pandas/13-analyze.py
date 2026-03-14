#!/usr/bin/env python3
"""
Module that computes descriptive statistics for a DataFrame
excluding the Timestamp column.
"""

import pandas as pd


def analyze(df):
    """
    Compute descriptive statistics for all columns except Timestamp.

    Args:
        df (pd.DataFrame): Input DataFrame containing a Timestamp column.

    Returns:
        pd.DataFrame: Descriptive statistics for numeric columns.
    """
    # Exclude Timestamp column if it exists
    df_numeric = df.drop(columns=["Timestamp"], errors="ignore")

    # Compute descriptive statistics
    stats = df_numeric.describe()

    return stats
