# fakegps.py

## Syntax
```
fakegps.fake_gps_movement(lat, lon, speed, number_of_updates)
```

| Input | Value
|:--|:--|
| `lat` | Starting latitude in DD format (default: `36.94499622`)
| `lon` | Starting longitude in DD format (default: `-76.31333208`)
| `speed` | Speed factored into position change (m/s) (default: `50`)
| `number_of_updates` | How many sample readings to you want. Readings are 1/sec use this to define how many minutes of sample movement you want (default: `600` (10 minutes))

## Starting Coordinates
* Starting coordinates are the Navy Exchange on Norfolk Naval Base.
* Use [this](https://www.google.com/maps/@36.942166,-76.3105843,854m/data=!3m1!1e3?hl=en&entry=ttu&g_ep=EgoyMDI1MDEyOS4xIKXMDSoASAFQAw%3D%3D) and [this](https://latitude.to/map/us/united-states/cities/norfolk-virginia) to get GPS starting coordinates you prefer.

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