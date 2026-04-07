#!/usr/bin/env python3
"""
    This script uses the (unofficial) SpaceX API to calculate and display
    the number of launches per rocket.
"""

import requests


def launches_per_rocket():
    """
    Fetches launch data from the SpaceX API and prints
    the number of launches per rocket.

    Process:
        - Retrieve all launches
        - Count occurrences of each rocket_id
        - Fetch rocket names from rocket endpoint
        - Sort and print results

    Returns:
        None
    """

    # Step 1: Retrieve all launches
    url = "https://api.spacexdata.com/v4/launches"

    launches = requests.get(url).json()

    # Step 2: Count launches per rocket_id

    rocket_count = {}

    # Iterate over all launches
    for launch in launches:
        rocket_id = launch["rocket"]

        # Increment count if rocket already seen
        # Otherwise initialize count to 1
        if rocket_id in rocket_count:
            rocket_count[rocket_id] += 1
        else:
            rocket_count[rocket_id] = 1

    # Step 3: Retrieve rocket names
    # Dictionary to map rocket_id -> rocket_name
    rocket_names = {}

    # For each unique rocket_id, call API to get its name
    for rocket_id in rocket_count:
        rocket_url = f"https://api.spacexdata.com/v4/rockets/{rocket_id}"

        # Request rocket data and parse JSON
        rocket_data = requests.get(rocket_url).json()

        # Store rocket name
        rocket_names[rocket_id] = rocket_data["name"]

    # Step 4: Combine names with counts
    # Create a list of tuples:
    result = []

    for rocket_id, count in rocket_count.items():
        name = rocket_names[rocket_id]
        result.append((name, count))

    # Step 5: Sort results
    # Sorting rules:
    #   1. Descending by launch count  -> -x[1]
    #   2. Ascending alphabetically    -> x[0]
    result.sort(key=lambda x: (-x[1], x[0]))

    # Step 6: Print results
    for name, count in result:
        print(f"{name}: {count}")


if __name__ == "__main__":
    launches_per_rocket()
