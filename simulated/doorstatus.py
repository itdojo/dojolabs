#!/usr/bin/env python3

import time
import random


def read_door_status():
    return random.choice(["open", "closed"])


def emulate_door_state_transition():
    door_status = "closed"  # Initial state
    threshold = 4  # Lower to have more frequent open/close events, increase to have less frequent events
    consecutive_count = 0
    last_reading = None
    current_state_start_time = time.monotonic()

    while True:
        new_status = read_door_status()

        if new_status == last_reading:
            consecutive_count += 1
        else:
            consecutive_count = 1

        last_reading = new_status

        # Confirm a stable transition (same state 4 times in a row)
        if consecutive_count == threshold and new_status != door_status:
            old_status = door_status
            door_status = new_status
            time_in_previous_state = f"{time.monotonic() - current_state_start_time:.2f}"
            current_state_start_time = time.monotonic()

            #yield door_status, old_status, time_in_previous_state
            yield {"door_status": door_status, "old_status": old_status, "time_in_previous_state": time_in_previous_state}
        time.sleep(1)


if __name__ == "__main__":
    for event in emulate_door_state_transition():
        print(f"Door status: {event['door_status']}, Old status: {event['old_status']}, Time in previous state: {event['time_in_previous_state']}s")
