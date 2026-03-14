#!/usr/bin/env python3
"""
Module that creates a pandas DataFrame from a dictionary.
"""

import pandas as pd

# Dictionary containing the data
data = {
    "First": [0.0, 0.5, 1.0, 1.5],
    "Second": ["one", "two", "three", "four"]
}

# Row labels
rows = ["A", "B", "C", "D"]

# Create the DataFrame
df = pd.DataFrame(data, index=rows)
