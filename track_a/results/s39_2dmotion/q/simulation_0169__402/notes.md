# Q402 — acceleration of the astronaut at t = 0.5 s

2D render, 24 fps (file fps = question_fps = 24). t = 0.5 s → frame 12. Acceleration = (speed(12) − speed(11)) × fps.

## Scale (prior: astronaut height 2.2 m)
- Own threshold mask (measure.py, gray > 25 + merged fragments): upright bbox height 90–91 px on frames 0–5.
- SAM 3 "astronaut": vert_px 90 (frame 0), 90 (frame 11), 87 (frame 12). The frame-12 SAM mask is 3.4 pct shorter;
  on the overlay it trims the dark visor/helmet top, so my threshold mask (91) is the better extent there. Frames 0/11
  agree within 1 px.
- Height = 90.5 px → 0.02431 m/px.

## Motion
- Own centroid track for all 80 frames (my_track.csv); agrees with scene/tracks/astronaut.csv. Raw per-frame steps are
  noisy (±0.5 px), so differences of differences need a model.
- The path fits a Blender ease-in/ease-out (smoothstep 3u²−2u³) between frames ≈ −0.25 and 78.2 with
  displacement (16.1, −274.2) px; RMS residual 0.49 px over 80 frames (peak speed 5.25 px/frame matches the
  observed plateau).
- Discrete acceleration from the fit at frame 12: 0.191 px/frame² = 110.1 px/s² (intensity-weighted centroid: 109.1).
- Second route: cubic polynomial fit of raw path distance over frames 4–20, 2nd derivative at 11.5: 108.6 / 109.4 px/s².
  Continuous smoothstep value at frame 12: 106 px/s².
- SAM centroids at frames 11/12 (1296.4,503.0)/(1296.8,498.2) are biased by the trimmed helmet on frame 12
  and not used for motion (SAM track also jumped to the moon mid-clip).
- Adopted 109.5 px/s² × 0.02431 m/px = **2.66 m/s²**.

## Confidence
Good: model fits well, two routes agree within ~2 pct; scale uncertain by ~1 px of 90 (~1 pct).
