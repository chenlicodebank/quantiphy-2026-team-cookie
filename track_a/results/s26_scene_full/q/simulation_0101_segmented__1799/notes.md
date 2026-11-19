# q1799 — length of the shark (m), prior: shark acceleration = 1 m/s^2

2D scene, 24 fps (file fps = question_fps, so no re-timing). The shark swims left, in side view, at a constant y.
The background is white.

## Method (measure.py -> shark_meas.csv)
- Segmentation: non-white threshold 12 in rows 760–1079, largest component. Per frame: snout x (leftmost), tail x (rightmost),
  centroid. Checked on the frame-36 crop (frames/f.png): the snout is at ~1177 and the tail tip at ~1455, matching the mask.
- Pixel acceleration: a quadratic fit x(t) over frames 1–72 (frames 0 and 1 are identical; motion starts at frame 1):
  snout −86.0, centroid −86.0, bbox centre −85.9, tail −85.8 px/s² (rms residual 0.5–0.9 px).
  Sub-windows: 1–36 → 83–85, 36–72 → 82–86, 10–60 → 86–87. I used **86.0 px/s²**.
- Scale: 1 m/s² ↔ 86.0 px/s², so 0.01163 m/px.
- Shark length: horizontal mask extent, median 279 px (mean 279.4; range 277–283 with the tail flap).
  The record in scene/ agrees (279 px).

## Answer
L = 279.4 / 86.0 = **3.25 m**

## Check
The second route uses each reference point's own acceleration (snout, tail, centroid). They all give 85.8–86.0 px/s², so
the length is 3.25 m ± 0.02. The split-window fits (82–87 px/s²) give 3.2–3.4 m. This is a plausible size for a large shark.
Confidence: high. The main uncertainty is the ~2% spread in the acceleration fit.
