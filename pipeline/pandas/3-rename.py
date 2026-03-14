#!/usr/bin/env python3
"""
Module that renames and processes a DataFrame column.
"""

import pandas as pd


def rename(df):
    """
    Rename the Timestamp column to Datetime, convert it to datetime
    format, and return only the Datetime and Close columns.

    Args:
        df (pd.DataFrame): DataFrame containing a column named Timestamp.

    Returns:
        pd.DataFrame: Modified DataFrame with Datetime and Close columns.
    """
    # Rename the column
    df = df.rename(columns={"Timestamp": "Datetime"})

    # Convert the column to datetime
    df["Datetime"] = pd.to_datetime(df["Datetime"])

    # Keep only Datetime and Close columns
    df = df[["Datetime", "Close"]]

    return df
