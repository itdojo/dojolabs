#!/usr/bin/env python3

import random
import math
from time import sleep

def generate_gps_coordinates(lat, lon, speed, direction):
    # Convert direction to radians
    rad = math.radians(direction)
    lat_change = math.cos(rad) * speed * 0.0001
    lon_change = math.sin(rad) * speed * 0.00015
    new_lat = lat + lat_change
    new_lon = lon + lon_change
    return round(new_lat, 6), round(new_lon, 6)


def fake_gps_movement(
        lat=36.94499622, 
        lon=-76.31333208, 
        speed=1, 
        number_of_updates=86400):
        direction = random.uniform(0, 360)  # Pick an initial direction
        for _ in range(number_of_updates):
            #direction += random.uniform(-5, 5)  # Slowly change direction
            lat, lon = generate_gps_coordinates(lat, lon, speed, direction)
            print(f"{lat}, {lon}")
            sleep(1)


if __name__ == "__main__":
    fake_gps_movement()
