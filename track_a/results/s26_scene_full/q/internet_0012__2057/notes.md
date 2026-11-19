# q_2057: average velocity of the truck (m/s)

Prior: lane width = 3.66 m. Internet clip taken top-down by a drone. The camera is static (see the scene record), so I used a single planar scale.

## Scale
- `measure.py` takes the intensity-weighted centroids of the right-carriageway lane-dash lines in frame 0. The adjacent-line spacing is
  96.5 px (y≈2700–2820), 97.1 (y≈3100–3220), 96.0 (2300), 95.8 (1500) and 97.2 (top). Near the left lane at y≈3000 it is 96.6.
- I used 96.5 px, the value near the truck's path. Scale = 3.66 / 96.5 = 0.03793 m/px.
- Sanity check: truck length 457 px × scale = 17.3 m, which is plausible for a semi-truck.

## Displacement
- Truck track (scene/tracks/truck.csv, template match, body centre): from (1318.4, 3323.6) at f0 to (1321.0, 2653.0) at f107,
  a net distance of 670.6 px, travelling up the image.
- Check by eye on zoomed frames:
  - front of cab: 3092 → 2425 (667 px)
  - top of trailer: 3202 → 2530 (672 px)
  - rear of trailer: 3560 → 2882 (678 px; the truck looks slightly longer near the image edge because of lens distortion)
  - These average about 671 px, which agrees with the track.
- 46 of the 108 frames are duplicates (3 in every 7). This does not matter here because I use the net displacement over the whole clip.

## Time base
- The question's rate is 60 fps; the file's is 59.35 fps. The two differ by only 1.1%, and both give plausible truck speeds.
- I used question_fps = 60, so T = 107/60 = 1.783 s.

## Result
- 670.6 px × 0.03793 m/px = 25.43 m; 25.43 / 1.783 s = **14.26 m/s** (about 51 km/h).
- Second route: a linear fit of cy(t) gives 377.2 px/s, which is 14.31 m/s. With the file fps (59.35) the answer would be 14.11 m/s.
- Confidence: good, about ±2%. The main uncertainty is the lane-width pixel reading (95.8–97.2 px).
