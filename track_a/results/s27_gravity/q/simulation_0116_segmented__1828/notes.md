# q_1828 – speed of the football at 0.5 s

2D clip, 24 fps (file fps = question_fps = 24), so t = 0.5 s → frame 12. Prior: gravity 9.8 m/s² (the football falls
straight down, so the prior applies directly and sets the scale).

## Method (fit.py)
- Track: scene/tracks/football.csv, mask centroid cy (and bbox_cy as a check), frames 0-31. x is constant
  (±1 px), so the motion is vertical.
- Quadratic fit y(f): pixel acceleration 3.121 px/frame² (fits over frames 0-25, 1-25, 0-31, 5-25, 1-19 all give
  3.109-3.131; rms residual ~0.5 px). Vertex at frame 0.00 ± 0.04 → released from rest at frame 0.
- Scale: 9.8 / (3.121 × 24²) = 0.005450 m/px.
- Speed at frame 12 = backward difference |p(12) − p(11)| × 24:
  - from the fit: 4.70 m/s (all fit windows 4.68-4.71);
  - analytic check: release at frame 0 → v = g × (11.5/24) = 4.696 m/s (scale-independent);
  - raw centroid difference: 40.09 px → 4.59 m/s (single-frame noise ±1 px ≈ ±0.13 m/s), consistent.

## Sanity
Ball long axis ~68 px × 0.00545 = 0.37 m (real American football ~0.28 m; within 40 %, acceptable).

Answer: 4.70 m/s. Confidence high.
