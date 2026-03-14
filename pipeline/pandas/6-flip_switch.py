#!/usr/bin/env python3
"""
Module that sorts a DataFrame in reverse chronological order
and then transposes it.
"""


def flip_switch(df):
    """
    Sort the DataFrame in reverse chronological order
    and transpose it.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: Transformed DataFrame.
    """
    df = df.sort_index(ascending=False)
    return df.transpose()
