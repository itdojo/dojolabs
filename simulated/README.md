# Contents

* [fakegps.py](#fakegpspy)
* [doorstatus.py](#doorstatuspy)


***

# fakegps.py

Generates simulated GPS data for a device in motion. Meant for importing into python scripts where you need simulated GPS input (lat/lon in [DD format](https://www.maptools.com/tutorials/lat_lon/formats)).

The 'pattern' produced by this directional, but not in a straight line.  The After the initial direction is randomly chosen, the path slowly drifts, producing a gradually changing path.  All I wanted was to simulate motion without having to go driving around.

## Syntax

```
fakegps.fake_gps_movement(lat, lon, speed, number_of_updates, direction)
```

| Input | Value | Default | Data Type
|:--|:--|:--|:--|
| `lat` | Starting latitude in DD format<sup>*</sup> | `36.942872` | float
| `lon` | Starting longitude in DD format<sup>*</sup> | `-76.309913` | float
| `speed` | Speed factored into position change (m/s) | `1.4` (~10 mph) | float
| `number_of_updates` | How many sample readings to you want. Readings are 1/sec use this to define how many minutes of sample movement you want | `86400` (24 hours) | int
| `direction` | 0-360 (degrees). Determines initial direction of travel. | random | float

## <sup>*</sup>Starting Coordinates

* Default starting coordinates are around the parking lot of the Navy Exchange on Norfolk Naval Base.
* Use [this site](https://www.google.com/maps/place/36%C2%B056'34.6%22N+76%C2%B018'35.6%22W/@36.9406491,-76.3097768,1308m/data=!3m1!1e3!4m4!3m3!8m2!3d36.942942!4d-76.309882?entry=ttu&g_ep=EgoyMDI1MDEyOS4xIKXMDSoASAFQAw%3D%3D) and [this site](https://latitude.to/map/us/united-states/cities/norfolk-virginia) to get GPS starting coordinates you prefer.

***

## Speed Suggestions

| Real Speed | Equivalent (Approximate) `speed` parameter
|:--|:--|
| Walking (~3 mph = 1.34 m/s) | speed ≈ 0.2
| Jogging (~6 mph = 2.68 m/s) | speed ≈ 0.4
| Cycling (~28 mph = 6.7 m/s) | speed ≈ 1
| 10 mph (4.47 m/s) | speed ≈ 1.4
| 15 mph (6.7 m/s) | speed ≈ 1.7
| 30 mph (13.4 m/s) | speed ≈ 4.2
| 50 mph (22.4 m/s) | speed ≈ 7
| 55 mph (24.6 m/s) | speed ≈ 7.8
| 70 mph (31.3 m/s) | speed ≈ 9.8
| 100 mph (44.7 m/s) | speed ≈ 14
| 500 mph (223.5 m/s) | speed ≈ 70

***

## `fakegps.py` Usage
```python
import fakegps

# Simple Usage
fakegps.fake_gps_movement()


# Control all inputs
fakegps.fake_gps_movement(lat=36.942872, lon=-81.685997256, speed=14, number_of_updates=600, direction=45.5)
```

### Sample output
```
36.938279, -81.679251
36.943189, -81.682568
36.945242, -81.688129
36.948757, -81.681512
36.948966, -81.679992
36.952845, -81.68056
36.947602, -81.675186
36.945541, -81.675131
```

***

# doorstatus.py

Simulated open/close events for a door (or anything else that opens/closes).  This is primarily intended for use by importing into other scripts but you can execute it directly, too.  

The open/close transitions are intended to be random and typically range from a few seconds to well over a minute.

You can control the frequency of open/close transitions (but still random-ish) with `threshhold`.
* Lower (i.e. `3`) = More frequent open/close transitions (door opens and closes more often).
* Higher (i.e. `5`) = Less frequent open/close transitions (door opens and closes less often).

## `doorstatus.py` Syntax & Usage

Returns a dict in the form: `{"door_status": "open/closed", "old_status": "open/closed", "time_in_previous_state": "seconds (string)"}`

```python
import doorstatus

for event in emulate_door_state_transition():
    print(f"Door status: {event['door_status']}, Old status: {event['old_status']}, Time in previous state: {event['time_in_previous_state']}s")
```

Example output:

```python
>>> import doorstatus
>>> for door_event in doorstatus.emulate_door_state_transition():
...     door_event
... 

{'door_status': 'open', 'old_status': 'closed', 'time_in_previous_state': '3.01'}
{'door_status': 'closed', 'old_status': 'open', 'time_in_previous_state': '34.14'}
{'door_status': 'open', 'old_status': 'closed', 'time_in_previous_state': '7.03'}
{'door_status': 'closed', 'old_status': 'open', 'time_in_previous_state': '5.02'}
{'door_status': 'open', 'old_status': 'closed', 'time_in_previous_state': '37.14'}
{'door_status': 'closed', 'old_status': 'open', 'time_in_previous_state': '28.11'}
{'door_status': 'open', 'old_status': 'closed', 'time_in_previous_state': '33.12'}
{'door_status': 'closed', 'old_status': 'open', 'time_in_previous_state': '53.22'}
{'door_status': 'open', 'old_status': 'closed', 'time_in_previous_state': '4.01'}
{'door_status': 'closed', 'old_status': 'open', 'time_in_previous_state': '15.05'}
{'door_status': 'open', 'old_status': 'closed', 'time_in_previous_state': '51.20'}
{'door_status': 'closed', 'old_status': 'open', 'time_in_previous_state': '69.26'}
```