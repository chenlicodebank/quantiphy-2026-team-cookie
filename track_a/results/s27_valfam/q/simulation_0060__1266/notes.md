# q_1266 – average speed of the bicycle over the whole clip (m/s)

The file rate and question_fps are both 24, so there is nothing to convert. The depths are given at t=0.58 s and
t=1.58 s, which are frames 14 and 38.

## Method
- Pixel tracks come from scene/tracks: `white_van.csv`, where ref is the wheel midpoint, and `cyclist.csv`, where
  ref is the centre of the bbox. I checked them on frame 14: the cyclist's bbox centre is about (1547, 383).
- Pinhole camera with the principal point at the image centre (1080, 540). The focal length is unknown.
- **Focal length from the prior** (`focal.py`):
  - For a trial f, back-project the van at frames 14 and 38 using the given depths (22.7254 and 21.5370 m). This
    gives a 3D line of travel.
  - Map every frame's van pixel point onto that line (the point closest to its ray) to get s(t).
  - Fit a quadratic to s(t) to get the acceleration, then solve for acceleration = 4 m/s².
  - Results:
    - f = 2279 px fitting frames 28–71
    - f = 2276 px fitting frames 2–27
    - f = 2292 px fitting frames 2–71
    - f = 2300 px fitting frames 10–60
    - Varying the van point vertically (axle, ground or body centre) changes f by less than 5 px.
  - Taking f ≈ 2285 px (horizontal FOV about 50.5°), a linear fit of the van's per-frame speeds gives 4.03 m/s². That
    reproduces the prior.
  - A first guess that the van starts from rest at frame 1 gave f = 2530. I rejected it: the van already moves at
    about 0.4 m/s at frame 2, so it was not at rest there.
- **Bicycle** (`bike.py`):
  - Back-project with the given bike depths (23.5534 and 23.2262 m) to get its 3D line.
  - Project all frames onto that line. Frames 61–71 are hidden behind the van, so they use the record's
    constant-velocity extrapolation.
  - Take the per-frame backward-difference speeds.

## Results (f = 2285 px)
- Chord speed from frame 14 to 38: 5.06 m/s.
- Mean of the per-frame speeds over frames 2–71: 5.05 m/s.
- Mean over frames 1–71: 4.98 m/s. Frames 0 and 1 of the video are identical, so the speed at frame 1 is 0.
- Sensitivity: across f = 2275–2300 the result moves by ±0.6%. Changing the bike's vertical reference point
  (bbox centre, ground or hip) moves it by less than 0.2%.

## Answer
**5.0 m/s.** This lies between 4.98 (counting the zero speed at frame 1) and 5.05 (excluding it). The motion is a
constant-speed ride.

## Confidence
High: the answer should be within about 2%.
