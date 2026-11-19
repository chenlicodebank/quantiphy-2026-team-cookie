# q_849 — speed of the soccer ball at t = 1 s (m/s)

Prior: ball diameter = 0.344 m. 2D scene, static camera; file fps = question_fps = 24, so t = 1 s -> frame 24.
Speed = |p(24) - p(23)| x 24 (backward difference), motion is horizontal.

## Scale
- Scene record: free-radius silhouette circle fit, median diameter 50.0 px.
- SAM 3 mask at frame 24 (`masks/soccer_ball_f24_k0.png`): principal extents 50.8 x 49.4 px (mean 50.1),
  box 46.7 x 47.9 (horiz/vert px 52/49); SAM track boxes median 49 x 49 px over frames 3-48 (x1-x0, i.e. ~50 inclusive).
- Zoomed frame 24 (frames/f24b.png): edges ~717-761 x ~531-579, ~48-50 px.
- My own diff-mask (measure.py) gives width 50-52 px but includes the shadow; its vertical extent is unreliable
  (the bright top of the ball barely differs from the wall). All within 3 pct of 50 px -> D = 50 px,
  scale = 0.344/50 = 0.00688 m/px. (49 px would raise the answer by 2 pct.)

## Velocity (speed.py)
Backward difference cx(24) - cx(23), px/frame:
- scene circle-fit track: raw 29.75; quadratic fit over 14-34: 29.72; over 4-48: 29.75; linear 18-30: 29.64
- SAM track: raw 30.60 (noisy), quadratic fits 29.64-29.65
- own diff-mask centroid / box centre: 30.1-30.5 (includes shadow, noisier)
Adopted 29.72 px/frame -> 29.72 x 24 x 0.00688 = 4.91 m/s.

## Check
SAM route independently: 29.65 px/frame with its own 49-50 px diameter -> 4.90-4.99 m/s. Agreement within ~2 pct.

Answer: 4.91 m/s. Confidence: high (±3 pct, dominated by the pixel diameter).
