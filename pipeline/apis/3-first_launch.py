#!/usr/bin/env python3
"""Module to display the first SpaceX launch using the SpaceX API."""
import requests
from datetime import datetime


def get_first_launch():
    """Fetch and display the first SpaceX launch by date_unix.

    Queries the SpaceX API for all launches, sorts them by date_unix
    (ascending), and prints the earliest launch in the format:
    <launch name> (<date>) <rocket name> - <launchpad name> (<locality>)
    """
    url = "https://api.spacexdata.com/v4/launches/upcoming"
    response = requests.get(url)
    launches = response.json()

    first_launch = min(launches, key=lambda x: x["date_unix"])

    name = first_launch["name"]
    date_unix = first_launch["date_unix"]
    rocket_id = first_launch["rocket"]
    launchpad_id = first_launch["launchpad"]

    local_date = (datetime.fromtimestamp(date_unix)
                  .strftime("%Y-%m-%dT%H:%M:%S%z"))

    rocket_url = "https://api.spacexdata.com/v4/rockets/{}".format(
        rocket_id
    )
    rocket_data = requests.get(rocket_url).json()
    rocket_name = rocket_data["name"]

    launchpad_url = "https://api.spacexdata.com/v4/launchpads/{}".format(
        launchpad_id
    )
    launchpad_data = requests.get(launchpad_url).json()
    launchpad_name = launchpad_data["name"]
    launchpad_locality = launchpad_data["locality"]

    print("{} ({}) {} - {} ({})".format(
        name, local_date, rocket_name, launchpad_name, launchpad_locality
    ))


if __name__ == '__main__':
    get_first_launch()
