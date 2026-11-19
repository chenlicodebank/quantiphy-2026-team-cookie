# Q1395 – average speed of the police car (van), simulation_0168

The file and the question both run at 24 fps (80 frames). The camera is static. The prior gives the bike's speed as 5.52 m/s. depth_info gives the bike's distance from the camera as 28.219 m at frame 0 and 25.554 m at frame 12.

## Method (ground-plane model calibrated on the bike)
- **Focal length** (`bikefit.py`): I fitted a constant-velocity straight-line model to the bike track, with |V| = 5.52 and the two given distances as constraints. This gives f ≈ 2650 (bbox centre) to 3020 px (hip). The answer barely depends on f: it changes by less than 0.5 % across that range.
- **Horizon** (`ground.py`): for a ground point moving at constant velocity, 1/(v − y_h) is linear in t. The best y_h is 535 for the bike, 540 for the van's FR contacts and 535 for the van's bbox bottom. The vanishing point of the road lines gives about 516–530. The horizon is close to the image centre, so I treated the camera as level.
- **Ground points**: Z = f·h/(v − y_h) and X = (u − cx)·h/(v − y_h).
- **Camera height**: h is set so that the bike's front-wheel contact point moves at 5.52 m/s over frames 0–79 (linear fit). I read these contact points by hand on gamma-boosted 6× crops at frames 0, 12, 24, 36, 48, 60, 72 and 79 (`pcrops.py`). The record's `ground_x` is the bbox centre, not the wheel, so I did not use it. Result: h ≈ 1.19 m (f = 2850, y_h = 535).
- **Van tyre contacts**: these come from the record and are rigid points on the van. I checked them on 6× crops (`wcrops.py`): FL at frames 4–56 and FR at 28–79 match the visible tyre bottoms to within about 1 px.
- **Van speed** (`final.py`, linear fit of X(t) and Z(t)):
  - FL (frames 0–56): 6.77 m/s
  - FR (frames 28–79): 6.82 m/s
  - RR (frames 40–79): 6.92 m/s
  - Across f = 2650–3020 and y_h = 530–540 the results stay within 6.63–6.95 m/s (mean 6.84).
  - The first half is slightly slower than the second (FL 6.58 → 7.00, FR 6.57 → 6.92 at y_h = 535), so the van may be accelerating a little. That makes the full-clip fit the right estimate of the average speed.

## Second route
I scaled the ground model with the given bike distances at frames 0 and 12 instead of the bike's speed:
- Using the contact distances as they are gives about 6.74 m/s.
- Assuming the bike's origin sits about 0.45 m behind the front-wheel contact gives about 6.64 m/s.

This route agrees within 1–3 %. The speed-calibrated route is the main one because it uses all 80 frames.

## Answer
**6.8 m/s.** Confidence is moderate to good, with an expected error of about ±4 %.
