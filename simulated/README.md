# Contents

* [fakegps.py](#fakegpspy)
* [doorstatus.py](#doorstatuspy)


***

# fakegps.py

Generates simulated GPS data for a device in motion. Meant for importing into python scripts where you need simulated GPS input (lat/lon in [DD format](https://www.maptools.com/tutorials/lat_lon/formats)).

The 'pattern' produced by this is erratic; it does not follow roads and does not respect anything on the map.  It produces output more like someone moving around otherwise aimlessly.  

## Syntax
```
fakegps.fake_gps_movement(lat, lon, speed, number_of_updates)
```

| Input | Value
|:--|:--|
| `lat` | Starting latitude in DD format (default: `36.94499622`)
| `lon` | Starting longitude in DD format (default: `-76.31333208`)
| `speed` | Speed factored into position change (m/s) (default: `30`)
| `number_of_updates` | How many sample readings to you want. Readings are 1/sec use this to define how many minutes of sample movement you want (default: `600` (10 minutes))

## Starting Coordinates
* Starting coordinates are the Navy Exchange on Norfolk Naval Base.
* Use [this](https://www.google.com/maps/@36.942166,-76.3105843,854m/data=!3m1!1e3?hl=en&entry=ttu&g_ep=EgoyMDI1MDEyOS4xIKXMDSoASAFQAw%3D%3D) and [this](https://latitude.to/map/us/united-states/cities/norfolk-virginia) to get GPS starting coordinates you prefer.

## Speed
| Value | Approximation
|:--|:--|
| `1` | A human walking around
| `2-4` | A human running/jogging
| `8` | A person riding a bike (~20 MPH)
| `13` - `29` | ~Range of various DJI drone top speeds (~30-65MPH)
| `25` | ~55 PMH
| `31` | ~70 MPH
| `44` | ~100 MPH
| `53`-`70` | Fastest FPV drones I have heard of
| `223` | ~500 MPH
| `342` | ~Speed of sound (~767 MPH)

## Usage
```python
import fakegps

# Simple Usage
fakegps.fake_gps_movement()


# Control all inputs
fakegps.fake_gps_movement(lat=30.489831374, lon=-81.685997256, speed=600, number_of_updates=86400)
```

### Sample output
```
36.944998, -76.31338
36.945394, -76.31366
36.945639, -76.313505
36.945968, -76.31354
36.945939, -76.313164
```

***

# doorstatus.py

Simulated open/close events for a door (or anything else that opens/closes).  This is primarily intended for use by importing into other scripts but you can execute it directly, too.  

The open/close transitions are intended to be random and typically range from a few seconds to well over a minute.

You can control the frequency of open/close transitions (but still random-ish) with `threshhold`.
* Lower (i.e. `3`) = More frequent open/close transitions (door opens and closes more often).
* Higher (i.e. `5`) = Less frequent open/close transitions (door opens and closes less often).

## Syntax & Usage

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