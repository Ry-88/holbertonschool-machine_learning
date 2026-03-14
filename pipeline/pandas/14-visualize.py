#!/usr/bin/env python3
"""
Module to clean, process, and aggregate cryptocurrency DataFrame for plotting.
"""


def visualize(df):
    """
    Transform the DataFrame for plotting:
        - Remove Weighted_Price
        - Rename Timestamp to Date and convert to datetime
        - Set Date as index
        - Fill missing values
        - Aggregate daily from 2017 onward:
            High: max, Low: min, Open: mean, Close: mean
            Volume_(BTC): sum, Volume_(Currency): sum

    Args:
        df (pd.DataFrame): Input DataFrame

    Returns:
        pd.DataFrame: Transformed DataFrame ready for plotting
    """
    # Remove Weighted_Price column if it exists
    if "Weighted_Price" in df.columns:
        df = df.drop(columns=["Weighted_Price"])

    # Rename Timestamp to Date
    df = df.rename(columns={"Timestamp": "Date"})

    # Convert Timestamp to datetime (assuming it's in seconds)
    df["Date"] = pd.to_datetime(df["Date"], unit='s')

    # Set Date as index
    df = df.set_index("Date")

    # Fill missing Close values with previous row
    df["Close"] = df["Close"].fillna(method="ffill")

    # Fill missing High, Low, Open with the same row's Close
    for col in ["High", "Low", "Open"]:
        if col in df.columns:
            df[col] = df[col].fillna(df["Close"])

    # Fill missing Volume columns with 0
    for col in ["Volume_(BTC)", "Volume_(Currency)"]:
        if col in df.columns:
            df[col] = df[col].fillna(0)

    # Filter data from 2017 onwards
    df = df[df.index.year >= 2017]

    # Aggregate daily
    daily = df.resample("D").agg({
        "High": "max",
        "Low": "min",
        "Open": "mean",
        "Close": "mean",
        "Volume_(BTC)": "sum",
        "Volume_(Currency)": "sum"
    })

    return daily
