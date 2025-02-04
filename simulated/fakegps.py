#!/usr/bin/env python3

import random
import math
from time import sleep


def generate_gps_coordinates(lat, lon, speed, direction):
    """Generates a new GPS coordinate based on speed and direction."""
    rad = math.radians(direction)  # Convert direction to radians
    lat_change = math.cos(rad) * speed * 0.0001  # Latitude shift
    lon_change = math.sin(rad) * speed * 0.00015  # Longitude shift
    new_lat = lat + lat_change
    new_lon = lon + lon_change
    return round(new_lat, 6), round(new_lon, 6)


def fake_gps_movement(
        lat=36.944996,
        lon=-76.313332,
        speed=1,
        number_of_updates=86400,
        straight_line=False):

    direction = random.uniform(0, 360)

    for _ in range(number_of_updates):
        if not straight_line:
            direction += random.uniform(-5, 5)  # Slowly change direction
        lat, lon = generate_gps_coordinates(lat, lon, speed, direction)

        print(f"{lat}, {lon}")
        sleep(1)  # Simulate real-time updates


if __name__ == "__main__":
    fake_gps_movement()