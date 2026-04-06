#!/usr/bin/env python3
"""
Module to fetch home planets of sentient species
"""

import requests


def sentientPlanets():
    """
    Returns a list of names of home planets of all sentient species

    Returns:
        list: Names of planets
    """
    url = "https://swapi.dev/api/species/"
    planets = []

    while url:
        response = requests.get(url)
        data = response.json()

        for species in data.get("results", []):
            classification = species.get("classification", "").lower()
            designation = species.get("designation", "").lower()

            # تحقق إذا الكائن عاقل
            if "sentient" in classification or "sentient" in designation:
                homeworld_url = species.get("homeworld")

                if homeworld_url:
                    planet_res = requests.get(homeworld_url)
                    planet_data = planet_res.json()

                    planet_name = planet_data.get("name")
                    if planet_name:
                        planets.append(planet_name)

        # الصفحة التالية
        url = data.get("next")

    return planets
