#!/usr/bin/env python3

import random
from time import sleep

def generate_gps_coordinates(lat=36.94496622, lon=-76.31333208, speed=50):
    lat_change = (random.uniform(-1, 1) * speed * 0.000009)  # Small latitude shift
    lon_change = (random.uniform(-1, 1) * speed * 0.000012)  # Small longitude shift
    new_lat = lat + lat_change
    new_lon = lon + lon_change
    return round(new_lat, 6), round(new_lon, 6)


def fake_gps_movement(lat=36.94499622, lon=-76.31333208, speed=50, number_of_updates=600):
    for _ in range(number_of_updates):
        lat, lon = generate_gps_coordinates(lat, lon, speed) 
        print(f"{lat}, {lon}")
        sleep(1)  # Simulates real-time GPS updates (1 update/sec)


def main():
    number_of_updates = 600  # 10 minutes of updates
    fake_gps_movement(number_of_updates=number_of_updates)


if __name__ == "__main__":
    main()
