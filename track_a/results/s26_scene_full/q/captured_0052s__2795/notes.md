# q_2795 — basketball diameter (cm)

File fps = question_fps = 24. Basketball is static (bottom centre-right, centre ≈ (801, 671) px); camera static.

## Method (lab method card)
f = 0.5959 × 1280 = 762.75 px. Diameter = depth_info distance (1.9365 m) × pixel diameter / f.

## Pixel measurement (measure2.py)
Foreground mask (max BGR difference to the per-row background > 30/40/60, all thresholds give the same result),
in every one of the 49 frames:
- horizontal extent x 756–847 → **92 px** (constant in all frames; widest chord also 92 px)
- vertical extent y 623–719 → 97 px. The bottom row is the image edge, so the bottom may be cut off.
- least-squares circle fit on the free outline: D ≈ 95.1 px (±0.1 over frames); it is pulled by the vertical elongation.
(The first colour-only mask in measure.py missed the dark lower-right part of the ball. Discarded.)

The scene/ record (bbox 756–847, 92 px wide) agrees.

## Result
Width route: 1.9365 × 92 / 762.75 = **23.36 cm** (answer).
Cross-checks:
- circle-fit diameter of 95.1 px → 24.2 cm
- geometric mean of the axes, sqrt(92 × 97) → 24.0 cm
- exact off-axis sphere projection (sphere_proj.py) reproduces the 92 × 97 px aspect from perspective alone (predicted
  height 97.2 px), so the vertical elongation is perspective, not a measurement error. If the depth is Euclidean,
  the exact projection gives 20.7 cm. If the depth is the sensor's z-depth, it gives ≈ 22.8 cm.
These routes give 22.8–24.2 cm, which fits a real basketball (size 6 ≈ 23 cm, size 7 ≈ 24.3 cm). The answer follows
the card convention: the horizontal pixel extent, which is not cut by the image edge.
Confidence: moderate-high (within about ±4%).
