#!/usr/bin/env python3
"""
Module to fetch available starships based on passenger capacity
"""

import requests


def availableShips(passengerCount):
    """
    Returns a list of starships that can hold at
    least passengerCount passengers

    Args:
        passengerCount (int): Minimum number of passengers

    Returns:
        list: Names of starships that meet the requirement
    """
    url = "https://swapi.dev/api/starships/"
    ships = []

    while url:
        response = requests.get(url)
        data = response.json()

        for ship in data.get("results", []):
            passengers = ship.get("passengers", "0")

            # تنظيف البيانات
            if passengers in ["unknown", "n/a"]:
                continue

            # إزالة الفواصل
            passengers = passengers.replace(",", "")

            try:
                passengers = int(passengers)
            except ValueError:
                continue

            # المقارنة
            if passengers >= passengerCount:
                ships.append(ship.get("name"))

        # الصفحة التالية
        url = data.get("next")

    return ships
