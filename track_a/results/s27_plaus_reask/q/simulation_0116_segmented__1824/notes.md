# q_1824 – length of the football (m); prior: gravity 9.8 m/s^2

2D segmentation clip, 24 fps (file fps = question_fps = 24), 32 frames. The football falls straight down from near rest
(x ≈ 1036), with no bounce, so the gravity prior gives the scale directly at the ball's own depth.

## Scale (gravity)
- `measure.py`: re-made the mask myself (min RGB < 240, largest component in x ≥ 880) and took the centroid y per frame (it matches scene/tracks/football.csv).
- Quadratic fit of cy(t): a = 1798.0 px/s^2 (frames 0-31), 1797.7 (0-25), 1800.0 (3-25), 1792.6 (0-15),
  1828 (16-25, short window), 1798.8 (8-23); rms residual about 0.5 px. Second differences are about 3.1 px/frame^2 throughout.
- Scale = 9.8 / 1798 = 0.005450 m/px.

## Football length in pixels
- The long axis is roughly vertical (axis angle 86-99°). The ball also tilts toward the camera, and the tilt grows
  over the clip: by about frame 20 it looks barrel-shaped, end-on, so its apparent length shrinks.
  The projected length can only be shorter than the true length, so I use the early frames, which show nearly the full length.
- Length along the principal axis, frames 1-15: 65-72 px with threshold 240 (includes anti-aliased edge pixels) and 61-68 px with threshold 200.
  Taking the edge halfway between the two gives about 67-68 px. Frames 16-25 give about 60 px (more foreshortened).
- Width (across) is about 44 px in early frames. A football's length/diameter is about 1.57-1.65, which gives about 70 px for the true length.
  So the measured 68 px means only a small tilt early on.
- Adopted L ≈ 69 px (range 68-70). L = 69 × 0.005450 = 0.376 m (range 0.371-0.382).

## Checks
- Second route: width 44 px × 1.6 (real football aspect ratio) = 70 px → 0.38 m, which agrees.
- Plausibility: a regulation American football is about 0.28 m long. This one comes out about 34% larger,
  which is inside the ±40% tolerance. Gravity gives the scale at the ball's own depth, so I keep the
  gravity-based value. The cabinets (161 px wide, which would be 0.88 m at the same scale) may stand at a different depth, so I did not use them.

Answer: 0.375 m. Confidence: moderate. The pixel length is uncertain by about ±3% (edge threshold and tilt).
If the reference is the model's real-size bounding box (~0.28-0.30 m), this answer would be off by about 25-30%.
