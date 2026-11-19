# q_677 — speed of the vacuum cleaner at t = 1 s

2D top-down Blender render, 24 fps (file fps = question_fps = 24). t = 1 s -> frame 24; speed = |p(24) - p(23)| x 24.
Prior: vacuum diameter = 0.438 m -> scale = 0.438 / diameter_px (vacuum is on the floor, as is its whole path).

## Measurements (measure.py, own_track.json)
- Own method: 180 radial rays from the disc centre; edge = half-level crossing between disc and floor grey,
  sub-pixel; robust least-squares circle fit. Frames 20-30 diameter 120.3-121.0 px, median 120.6 px.
- Centres: f23 (1411.66, 380.76), f24 (1391.59, 378.25) -> step 20.22 px/frame.
  scene/ record (circle fit to a gray>185 mask): f23 (1412.29, 380.55), f24 (1392.24, 378.01) -> 20.21 px. Agree.
- Neighbouring steps (f22-f27): 19.76, 20.10, 20.22, 20.45, 20.36, 20.39 px — smooth, no event near frame 24.

## Diameter: three estimates
- scene/ record: 117.9 px (threshold gray>185 sits inside the soft rim, since the left/top edges ramp over about 6 px).
- Own half-level edge: 120.6 px (raw profiles through the centre at f24: edges at x≈1330.7 / 1452.5 and y≈317.8 / 438).
- SAM 3 (box prompt "white disc", f23/f24): bbox 127-128 px, circle fit 126 px, centroid (1391.58, 377.88) at f24,
  which matches my centre within 0.4 px. The diameter is 4.5 pct larger than mine. I checked a 4x zoomed overlay
  (frames/overlay_f24.png): the SAM outline is blocky and lies outside the visible rim, on the floor and shadow,
  while my green circle sits on the rim. So SAM over-estimates the size; I use 120.6 px. The SAM centres
  confirm the step (centroid step f23->f24 = 20.25 px).

## Result
speed = 20.22 px x 24 / 120.6 px x 0.438 m = 1.763 m/s.
Second route: the record's diameter (117.9 px) and step (20.21 px) give 1.80 m/s, which is 2 pct higher. That
gap is how far I can trust the rim definition. The half-level edge is the standard silhouette estimate, so I
answer 1.76 m/s.
Confidence: high (about ±2 pct).
