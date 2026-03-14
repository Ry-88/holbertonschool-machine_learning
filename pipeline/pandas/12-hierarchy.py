#!/usr/bin/env python3
"""
Module that concatenates bitstamp and coinbase DataFrames with
MultiIndex rearranged and timestamp range selection.
"""

import pandas as pd
index = __import__('10-index').index


def hierarchy(df1, df2):
    """
    Rearrange MultiIndex to have Timestamp first, select a specific
    timestamp range from df2 and df1, concatenate with keys,
    and display in chronological order.

    Args:
        df1 (pd.DataFrame): Coinbase DataFrame.
        df2 (pd.DataFrame): Bitstamp DataFrame.

    Returns:
        pd.DataFrame: Concatenated DataFrame with Timestamp as first level.
    """
    # Set Timestamp as index for both DataFrames
    df1_indexed = index(df1)
    df2_indexed = index(df2)

    # Select rows from df2 and df1 in the timestamp range
    df1_selected = df1_indexed[
        (df1_indexed.index >= 1417411980) & (df1_indexed.index <= 1417417980)
    ]
    df2_selected = df2_indexed[
        (df2_indexed.index >= 1417411980) & (df2_indexed.index <= 1417417980)
    ]

    # Concatenate with keys
    concatenated = pd.concat(
        [df2_selected, df1_selected], keys=['bitstamp', 'coinbase']
    )

    # Swap levels to have Timestamp as first level in MultiIndex
    concatenated = concatenated.swaplevel(0, 1).sort_index()

    return concatenated
