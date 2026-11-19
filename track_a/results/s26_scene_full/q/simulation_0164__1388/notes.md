# q_1388 – speed of the ball at t = 1 s (frame 24 at question_fps 24; file fps also 24)

Prior: ball diameter 0.21 m. depth_info: camera–ball distance 9.391 m at t = 0.5 s (frame 12).

## Method (recon.py, sens.py, local.py)
- Ball centres and apparent diameters from scene/tracks/ball.csv (circle fit; I checked frame 24 visually: ball at (1004, 596), ~73 px).
- Focal length: f = diam_px(12) × 9.391 / 0.21. Raw diam 82.1 px gives 3671 px; the smoothed diam gives 3664 px; a global fit of
  f·0.21/D to all diameters in frames 6-37 gives 3635-3655 px. I used 3640-3665 px (HFOV ≈ 29°).
- Route 1 (main): the ball rolls along a 3D line in the lane direction. That direction comes from the vanishing point of the cyan lane/floor
  lines (pairwise intersections x = 5645, 5703, 5770; the ball's image path passes through the same point). The line is anchored at
  the frame-12 position (9.391 m along the frame-12 ray). Each frame's centre ray is intersected with this line to get a 3D position.
- Speed at frame 24: a local linear or quadratic fit of path length over frames 24±3, ±4 and ±6 gives 3.53–3.60 m/s across the f and VP ranges.
  The central value is about 3.565–3.58. The raw one-frame backward difference is 3.50 (per-frame noise ±0.15).
  The ball slows gently over the clip, from about 3.9 m/s (frame 7) to about 3.4 m/s (frame 37).
- Route 2 (check): distance = f·0.21 / diameter, using a smoothed diameter, times the unit ray. This gives 3.67 m/s at frame 24
  (3.73 averaged over frames 20-28). It depends on diameter noise and motion blur.
  The diameter-only fit prefers a slightly nearer vanishing point, which would give about 3.65. The two routes differ by about 3%.

## Answer
3.58 m/s (route 1, nudged slightly toward route 2). Confidence: about ±4%.
