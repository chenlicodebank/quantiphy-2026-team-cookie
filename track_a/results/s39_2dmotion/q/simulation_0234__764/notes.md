# q_764 — speed of the basketball at t = 0.5 s (m/s)

The file fps and question_fps are both 24, so t = 0.5 s is frame 12. Speed = |p(12) − p(11)| × 24 (one-frame backward difference).
This is a 2D scene, so the scale comes from the prior: ball diameter = 0.282 m.

## Measurements (measure.py, compare.py)
- My HSV mask with a least-squares circle fit to the contour reproduces scene/tracks/ball.csv exactly:
  - frame 11: centre (986.68, 795.97)
  - frame 12: centre (986.59, 806.77)
  - The step is 10.80 px. The motion is purely vertical.
- Ball diameter in px:
  - Circle fit: 74.4–74.9 (frames 0–12, mean 74.6). The mean over frames 0–25 is 74.9, but frames near the bounce are slightly larger.
  - Half-maximum saturation edge profile, horizontal through the centre: 73.6–73.8.
  - Mask bbox width: 74–75.
  - I used **D = 74.4 px** → 0.003790 m/px.
- SAM 3 check:
  - Mask on frame 11: bbox 80 × 79, equivalent diameter 78.3.
  - Mask on frame 12: bbox 80 × 78, equivalent diameter 77.9.
  - The SAM masks are about 5 % larger than mine. On the overlay and a zoomed crop (frames/f12.png), the SAM outline sits outside the soft, anti-aliased edge, adding a 2–3 px halo. I take my half-max / circle-fit edge as correct and did not use the SAM size.
  - SAM centroids: 795.8 → 806.9, a step of 11.1 px. This is within 3 % of my 10.8 px.

## Result
speed = 10.80 px × 24 × 0.282 / 74.4 = **0.983 m/s**. Using D = 74.9 gives 0.976.

## Second route
A parabola fitted to y over frames 0–22 (the descent, before the bounce) gives a backward difference at frame 12 of 0.981 m/s, which is consistent. The instantaneous speed at frame 12 is 1.02 m/s, but the convention is the backward difference.

Confidence: high (±1.5 %).
