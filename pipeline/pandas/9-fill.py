#!/usr/bin/env python3
"""
Module that fills missing values and removes unnecessary columns
in a cryptocurrency DataFrame.
"""


def fill(df):
    """
    Remove the Weighted_Price column, fill missing values according
    to specified rules, and return the modified DataFrame.

    Rules:
        - Close: fill NaN with previous row's value
        - High, Low, Open: fill NaN with the Close value in the same row
        - Volume_(BTC), Volume_(Currency): fill NaN with 0

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: Modified DataFrame.
    """
    # Remove the Weighted_Price column if it exists
    if "Weighted_Price" in df.columns:
        df = df.drop(columns=["Weighted_Price"])

    # Fill missing Close with previous row's value
    df["Close"] = df["Close"].fillna(method="ffill")

    # Fill missing High, Low, Open with Close value in the same row
    for col in ["High", "Low", "Open"]:
        if col in df.columns:
            df[col] = df[col].fillna(df["Close"])

    # Fill missing volumes with 0
    for col in ["Volume_(BTC)", "Volume_(Currency)"]:
        if col in df.columns:
            df[col] = df[col].fillna(0)

    return df
