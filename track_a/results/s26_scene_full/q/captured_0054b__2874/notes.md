# Q2874 – velocity of the green ball at 1.5 s (frame 36, question_fps = file fps = 24)

- The "green ball" is the yellow-green tennis ball (`scene/tracks/yellow_ball.csv`). It is thrown from the left, bounces on the
  floor at frame 37, and is at (687, 467) px at frame 36. I checked this on a zoomed crop (`frames/f36.png`).
- Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- Depth per frame: Z = K / d, where d is a linear-in-time fit of 1/diameter (wid_minor) over frames 20–37. The capture
  skipped between frames 35 and 36 is included in the time axis. K = 1.331 m (given, t = 1.0 s) x d24_fit (38.8 px) = 51.6.
  This implies a ball diameter of 6.76 cm, which matches a real tennis ball (6.7 cm), so the depth model is consistent.
  Z36 ≈ 2.46 m.
- 3D centres come from back-projecting the tracked pixels.
- Prior check (`prior_check.py`): orange basketball at frame 12, depth 2.24 m. A 5-frame position smoothing followed by a
  one-frame difference gives 2.10–2.24 m/s against the prior of 2.21. This reproduces the prior to within a few percent,
  and the reference evidently keeps the skipped-capture jump inside its smoothing window.
- Green ball at frame 36 (`measure.py`):
  - smoothed-position forward difference: 3.05 (pre-bounce depth fit) / 2.92 (split fit)
  - smoothed-position backward difference: 3.42 / 3.72
  - raw forward difference 36→37: 3.24
  - physical speed 35→36 (two capture intervals): 3.47
  - per-frame speeds 30–34 rise steadily: 2.7, 2.9, 3.0, 3.05, 3.36
- Answer: about 3.3 m/s, the centre of these estimates.
- Confidence: moderate (about ±10%). Frame 36 lies between a skipped capture and the floor bounce at frame 37, so the
  result depends on the smoothing window.
