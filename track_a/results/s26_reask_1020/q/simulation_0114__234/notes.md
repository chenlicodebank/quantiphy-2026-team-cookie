# q_234 — length of the plane (m)

2D top-down scene. The yellow plane starts at rest at frame 0 and accelerates straight down the image. The camera is static.
Prior: a = 18 m/s². question_fps = 24.0. The file runs at 24.0024 fps; I used 24.0.

## Method (measure.py)
- I tracked the plane myself with an HSV yellow mask, using the wing-bar row (rows with ≥100 yellow px) for frames 0–75.
- Quadratic fits of y(frame) give a = 0.5971 px/frame² over frames 0–75, 0.5977 over 2–40, 0.5975 over 30–75 and 0.5974 over 10–60.
  Velocity is zero at frame ≈0, so the plane starts from rest. The scene record's ref_y gives 0.5969, and the slope of its per-frame
  speeds gives 0.5973. I took **a = 0.5973 px/f² = 344.0 px/s²** (×24²).
- Scale = 18 / 344.0 = **0.05232 m/px**.
- Nose-to-tail length at frame 0 (sharp, no blur): the mask bbox gives y 108–213 (106 px). The scene record has 108 px (106–214).
  The zoomed crop shows the tail edge at about 108–109 and the nose at about 213–214. I used **107 px**.
- Length = 107 × 0.05232 = **5.60 m** (range 5.55–5.65 for 106–108 px).

## Checks
- The acceleration agrees across four independent frame windows to within 0.1%. The record's track and my own track agree.
- Plausibility: the wingspan is 168 px × 0.0523 = 8.8 m and the length 5.6 m, which fit a light aircraft. The prior is realistic.

Confidence: high (about ±2%).
