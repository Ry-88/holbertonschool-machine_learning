#!/usr/bin/env python3
"""
Module that renames and processes a DataFrame column.
"""

import pandas as pd


def rename(df):
    """
    Rename Timestamp column to Datetime, convert it to datetime,
    and keep only Datetime and Close columns.

    Args:
        df (pd.DataFrame): DataFrame containing a Timestamp column.

    Returns:
        pd.DataFrame: Modified DataFrame.
    """
    # Rename column
    df = df.rename(columns={"Timestamp": "Datetime"})

    # Convert timestamp (seconds) to datetime
    df["Datetime"] = pd.to_datetime(df["Datetime"], unit='s')

    # Keep only required columns
    df = df[["Datetime", "Close"]]

    return df
