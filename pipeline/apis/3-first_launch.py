#!/usr/bin/env python3
import requests


def get_first_launch():
    # Step 1: Get all launches
    url = "https://api.spacexdata.com/v4/launches"
    launches = requests.get(url).json()

    # Step 2: Sort launches by date_unix
    launches.sort(key=lambda x: x["date_unix"])

    # Step 3: Get the first launch
    first_launch = launches[0]

    # Step 4: Extract needed data
    launch_name = first_launch["name"]
    date_local = first_launch["date_local"]
    rocket_id = first_launch["rocket"]
    launchpad_id = first_launch["launchpad"]

    # Step 5: Get rocket name
    rocket_url = f"https://api.spacexdata.com/v4/rockets/{rocket_id}"
    rocket_data = requests.get(rocket_url).json()
    rocket_name = rocket_data["name"]

    # Step 6: Get launchpad details
    launchpad_url = f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}"
    launchpad_data = requests.get(launchpad_url).json()
    launchpad_name = launchpad_data["name"]
    launchpad_locality = launchpad_data["locality"]

    # Step 7: Print result in required format
    print(f"{launch_name} ({date_local}) {rocket_name} - {launchpad_name} ({launchpad_locality})")


if __name__ == "__main__":
    get_first_launch()
