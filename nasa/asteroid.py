#!/usr/bin/python3
import os
from sys import maxsize
import requests
from dotenv import load_dotenv
from styling import Color

# Load environment variables from .env file
load_dotenv()

## Define URL
URL = "https://api.nasa.gov/neo/rest/v1/feed?"


# this function grabs our credentials
# it is easily recycled from our previous script
def return_creds():
    api_key = os.getenv("API_KEY")

    ## if we don't have an API key, error out
    assert api_key is not None

    ## remove any newline characters from the api_key
    nasa_creds = "api_key=" + api_key.strip("\n")
    return nasa_creds


# this is our main function
def main():
    ## first grab credentials
    nasa_creds = return_creds()

    ## update the date below, if you like
    start_date = "start_date=2019-11-11"

    ## the value below is not being used in this
    ## version of the script
    # end_date = "end_date=END_DATE"

    # make a request with the request library
    api_request = requests.get(URL + start_date + "&" + nasa_creds, timeout=10)

    # strip off json attachment from our response
    data = api_request.json()

    for date, asteroids in data["near_earth_objects"].items():
        biggest_diameter: float = 0.0
        biggest_idx: int = -1

        fastest_speed: float = 0.0
        fastest_idx: int = -1

        closest_distance: float = maxsize
        closest_idx: int = -1

        for idx, asteroid in enumerate(asteroids):
            curr_diameter = float(
                asteroid["estimated_diameter"]["miles"]["estimated_diameter_max"]
            )
            if biggest_diameter < curr_diameter:
                biggest_diameter = curr_diameter
                biggest_idx = idx

            curr_speed = float(
                asteroid["close_approach_data"][0]["relative_velocity"][
                    "miles_per_hour"
                ]
            )
            if fastest_speed < curr_speed:
                fastest_speed = curr_speed
                fastest_idx = idx

            curr_distance = float(
                asteroid["close_approach_data"][0]["miss_distance"]["miles"]
            )

            if closest_distance > curr_distance:
                closest_distance = curr_distance
                closest_idx = idx

        print(f"{Color.BLUE}Date: {date}{Color.RESET}")
        print(
            f"The {Color.CYAN}biggest{Color.RESET} asteroid was {Color.YELLOW}{asteroids[biggest_idx]['name']}{Color.RESET}"
            f" with a diameter of {Color.GREEN}{biggest_diameter:,.5f} miles{Color.RESET}."
        )
        print(
            f"The {Color.CYAN}fastest{Color.RESET} asteroid was {Color.YELLOW}{asteroids[fastest_idx]['name']}{Color.RESET}"
            f" with a speed of {Color.GREEN}{fastest_speed:,.2f} miles per hour{Color.RESET}."
        )
        print(
            f"The {Color.CYAN}closest{Color.RESET} asteroid was {Color.YELLOW}{asteroids[closest_idx]['name']}{Color.RESET}"
            f" with a distance of {Color.GREEN}{closest_distance:,.2f} miles{Color.RESET}."
        )
        print("\n")


if __name__ == "__main__":
    main()
