# Q329 – speed of the cup at t = 1 s (m/s)

Prior: cup diameter = 0.087 m. 2D video, file fps = question_fps = 24, so t = 1 s is frame 24 and
speed = |x(24) - x(23)| x 24 x (m/px).

## Pixel speed (measure.py: my own HSV blue mask, frames 8-34)
Backward difference 24-23, in px/frame:
- mask centroid 33.07; mean of row midpoints 33.11; left edge 32; right edge 33; bbox centre 32.5
- SAM 3 masks (frames 23 and 24): centroid 1097.5 -> 1130.3 = 32.8
- scene/ minAreaRect centre gives 28.6, but that is a glitch: the rect centre jumps at frames 22-25
  (40.1, 34.0, 28.6, 34.9). The smooth sequence from the centroid is 34.6, 33.1, 31.4 (frames 23, 24, 25), so I
  did not use the rect value.
-> 33.0 ± 0.4 px/frame = 792 px/s.

## Scale (width_check.py, edge_profile.py, width_green.py)
The diameter is the cup's widest extent, at the rim (rows ~528-545). I measured it three ways:
- HSV mask: 120 px. This misses the dark, low-saturation outline pixels at the edges.
- Raw edge profiles, and sub-pixel half-level crossings in the green channel: 123.3 px at frame 24 and 122.9 px
  at frame 23 (122.5-123.4 over frames 22-24).
- SAM mask: 125 px at most (122 at row 540). It is slightly wider than the half-level edge.
On the raw pixel rows at frame 24, y = 540, the left edge sits at about x = 1072.1 and the right edge at
about x = 1195.4, so the width is about 123 px. My HSV mask (120) is too small and SAM (125) is about 1.5 % too
large. I used **123.0 px**.

The width shrinks from 128.7 px (frame 9, x≈284) to 123 px (frame 24, x≈1130). This matches perspective, a
1/cosθ widening off-axis, with f ≈ 2250 px: frame 13 predicts 124.9 and I measured 124.9. Frame 24 is only
170 px from the image centre, so the correction there is 0.3 %, which is negligible. Pixel displacement of the
origin maps linearly to world displacement on the motion plane.

Scale = 0.087 / 123.0 = 7.07e-4 m/px.

## Answer
v = 792 px/s x 7.07e-4 m/px = **0.560 m/s**

Second check: a smoothed speed (mean of frames 23-25, 33.0 px/frame) gives the same value.
- Width 120 px would give 0.574.
- Width 125 px (SAM) would give 0.551.
Confidence: high, about ±3 %.
