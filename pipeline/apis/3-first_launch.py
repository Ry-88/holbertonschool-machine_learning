#!/usr/bin/env python3
"""
Script: 2-first_launch.py

Description:
    This script uses the (unofficial) SpaceX API to retrieve and display
    information about the first (earliest) SpaceX launch.

    The script performs the following steps:
    1. Fetches all launches from the SpaceX API.
    2. Sorts them using the 'date_unix' field (ascending order).
    3. Selects the earliest launch.
    4. Retrieves additional details about the rocket and launchpad
       using their respective IDs.
    5. Prints the result in the required format:

       <launch name> (<date>) <rocket name> -
       <launchpad name> (<launchpad locality>)

Dependencies:
    - requests (HTTP library for Python)

Usage:
    Run the script directly:
        ./2-first_launch.py

    Or:
        python3 2-first_launch.py

Note:
    The script will not execute automatically if imported, due to the
    use of: if __name__ == "__main__"
"""

import requests


def get_first_launch():
    """
    Fetches and prints information about the earliest SpaceX launch.

    Steps:
        - Retrieve all launches
        - Sort launches by 'date_unix'
        - Extract relevant launch details
        - Fetch rocket and launchpad information
        - Format and print the result

    Returns:
        None
    """

    # Retrieve all launches
    # Endpoint that returns all SpaceX launches
    url = "https://api.spacexdata.com/v4/launches"

    # Send GET request and convert response to JSON (list of dictionaries)
    launches = requests.get(url).json()

    # Sort launches by date
    # 'date_unix' is a timestamp (seconds since epoch)
    # Sorting ensures earliest launch appears first
    launches.sort(key=lambda x: x["date_unix"])

    # Select first launch
    # After sorting, index 0 contains the earliest launch
    first_launch = launches[0]

    # Extract basic data
    # These values come directly from the launch object
    launch_name = first_launch["name"]          # Name of the launch
    date_local = first_launch["date_local"]     # Local date/time of launch
    rocket_id = first_launch["rocket"]          # Rocket ID (not name)
    launchpad_id = first_launch["launchpad"]    # Launchpad ID (not name)

    # Retrieve rocket data
    # Use rocket ID to query rocket endpoint
    rocket_url = f"https://api.spacexdata.com/v4/rockets/{rocket_id}"

    # Send request and parse JSON response
    rocket_data = requests.get(rocket_url).json()

    # Extract rocket name
    rocket_name = rocket_data["name"]

    # Retrieve launchpad data
    # Use launchpad ID to query launchpad endpoint
    launchpad_url = f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}"

    # Send request and parse JSON response
    launchpad_data = requests.get(launchpad_url).json()

    # Extract launchpad name and locality
    launchpad_name = launchpad_data["name"]
    launchpad_locality = launchpad_data["locality"]

    # Output result
    # Print formatted string as required
    print(
        f"{launch_name} ({date_local}) "
        f"{rocket_name} - {launchpad_name} ({launchpad_locality})"
    )


if __name__ == "__main__":
    get_first_launch()
