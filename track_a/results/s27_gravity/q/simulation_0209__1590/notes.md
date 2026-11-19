# q_1590 – speed of the typewriter at t = 0.333 s

- question_fps = file fps = 24, so t = 0.333 s is frame 8. Speed = |p(8) - p(7)| x 24 (backward difference).
- Prior: the typewriter falls with a = 9.8 m/s^2 before 0.45 s (free fall; it lands at about frame 10).
- The prior fixes the metric scale, so I only need the time since release. `fit_release.py` fits the pixel track
  (scene/tracks/typewriter.csv) with y = A + (k0 + k1 n) * 0.5 (n - n_r)^2. The linearly varying scale k absorbs
  perspective: depth grows from 4.32 m, and the camera looks down.
  - bottom edge y1, frames 0-9: n_r = -0.07 frames, max residual 0.23 px
  - y1, frames 1-9: n_r = -0.05
  - bbox centre, frames 2-9: n_r = -0.20 (centre is less reliable: bbox_h grows while it falls)
  - top edge, frames 2-9: n_r = -0.29
  So it starts from rest at frame 0 (within about 0.1 frame). This is the same pattern as Blender rigid-body
  start-up.
- Fall is vertical: horizontal pixel drift is under 2 px/frame against 70-80 px/frame vertical.
- Speed: 0.5 g [(8+0.05)^2 - (7+0.05)^2] / 24^2 x 24 = 3.08 m/s. With release exactly at frame 0 it is
  3.06 m/s. The instantaneous g t would be 3.27 m/s, but the benchmark uses the backward difference.
- Second route: the y1 increments d(n)/(n - 0.5) are smooth (12.0 to 10.1 px/frame^2, decreasing with perspective),
  with no sign of an initial velocity.
- Answer 3.08 m/s. Confidence: high, assuming the reference uses the stated backward-difference convention.
