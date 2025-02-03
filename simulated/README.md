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

# Simple
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