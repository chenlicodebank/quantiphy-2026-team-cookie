# q_289: length of the blue car (m)

The video is a 2D top-down render with a static camera, at 24 fps (the file rate and question_fps agree). The prior is a bike speed of 24 m/s,
which is 1.000 m per frame.

## Scale
- Cyclist pixel speed from the scene track (chained NCC, frames 2–53): mean 31.64 px/frame.
- Independent check (`cyc_check.py`): direct NCC over 20 frames gives 31.87 px/frame (frames 20→40) and 31.83 (30→50).
  The 20→50 match failed and was discarded. Value used: 31.7 ± 0.15 px/frame.
- Scale = 1 m / 31.7 px = 0.03155 m/px.

## Car length in pixels
- Scene record: 236 px at frame 12, where the rear sits under the canopy shadow.
- Re-measured (`edges.py`) from column colour profiles over rows 295–340, compared with a background frame (50):
  - Frame 20: rear outline outer edge ≈1454, blue body ends at ≈1692.5 (the shadow lies beyond it). Length ≈ 238.5 px.
  - Frame 24: rear ≈1554, front ≈1793. Length ≈ 239 px.
  - A visual read of a 3x crop at frame 20 gives 1456–1696, about 240 px.
- Value used: 238 ± 3 px.

## Answer
238 / 31.7 = **7.5 m** (7.46 if I use 236 px). The error comes mostly from the edge reading, about ±1.5%.

## Plausibility
At this scale the bike is 85 px = 2.7 m long, and the car is 7.5 m. Both are about 1.5x real size: the true bike speed
would be about 16 m/s. A 24 m/s (86 km/h) bike is itself unrealistic, so following the rules the scene is taken as
scaled to the exact prior, and I keep the prior's scale. If the bike length (about 1.8 m) were used for the scale instead,
the car would come out at about 5.0 m.
