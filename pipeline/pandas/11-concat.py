#!/usr/bin/env python3
"""
Module that concatenates two DataFrames (bitstamp and coinbase)
with Timestamp as index and labeled keys.
"""


def concat(df1, df2):
    """
    Concatenate selected rows from df2 (bitstamp) on top of df1 (coinbase)
    with keys labeling the source, using Timestamp as index.

    Args:
        df1 (pd.DataFrame): Coinbase DataFrame.
        df2 (pd.DataFrame): Bitstamp DataFrame.

    Returns:
        pd.DataFrame: Concatenated DataFrame with keys.
    """
    # Import index function from 10-index.py
    index = __import__('10-index').index

    # Set Timestamp as index for both DataFrames
    df1_indexed = index(df1)
    df2_indexed = index(df2)

    # Select rows from df2 up to and including timestamp 1417411920
    df2_selected = df2_indexed[df2_indexed.index <= 1417411920]

    # Concatenate df2 on top of df1 with keys
    concatenated = __import__('pandas').concat(
        [df2_selected, df1_indexed], keys=['bitstamp', 'coinbase']
    )

    return concatenated
