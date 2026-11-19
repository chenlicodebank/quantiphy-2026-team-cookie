# Q687 – speed of the moving red general at t = 1.5 s (m/s)

Prior: chess piece diameter = 0.097 m. 2D scene (top-down board), static camera. question_fps = file fps = 24,
so t = 1.5 s → frame 36; speed = |p(36) − p(35)| × 24.

## Position (frame 35 → 36)
Frame pair (34, 35) is a duplicated image; per the record, frame 35's image is its own position (frame 34 is the
wrong one), and the following steps confirm it (35→36 38.0, 36→37 39.0, 37→38 40.0 px: smooth +1 px/frame growth).
- Record (silhouette centroid): 811.34 → 849.32 = 37.98 px
- My half-max edge centres (diameter.py): 811.32 → 849.29 = 37.97 px
- My background-difference mask (measure.py, frame 44 as background): bbox-centre 37.5, centroid 37.76 px
- SAM 3 masks (frames 35, 36): centroid 811.87 → 849.53 = 37.66 px
→ step = 37.9 px/frame (spread ±0.3 px, <1 %). x is constant (959.2–959.6).

## Scale (diameter in pixels)
- Half-max edge profiles through the centre (diameter.py): moving general 84.4 (horiz) / 85.0 (vert); static
  soldiers/cannon 84.1–85.9 px.
- Record silhouette bbox: 86–87 px.
- SAM 3: vertical 86–87 px, but horizontal 94 px. Zoomed overlay (frames/mask36.png) shows the SAM mask has spurious
  side lobes at mid-height outside the disc edge, so 94 is wrong; the half-max lines hug the visible rim.
- Used D = 85.5 px (between half-max 84.7 and mask-bbox 86.5) → 0.097/85.5 = 1.1345e-3 m/px.

## Answer
v = 37.9 × 24 × 1.1345e-3 = 1.032 m/s → **1.03 m/s**.
Range from diameter choice: 1.02 (86.5 px) – 1.04 (84.7 px).

## Second route
Constant acceleration check: clean steps 30→31 32.8, 31→32 33.8, 32→33 34.8, (33→35)/2 36.3 avg, 35→36 38.0,
36→37 39.0, 37→38 40.0 px — linear growth ≈1 px/frame², so the backward difference at 36 (38.0 px) is consistent with
the trend, not a frame-duplication artifact.

Confidence: high (≈2 % uncertainty, dominated by edge definition of the diameter).
