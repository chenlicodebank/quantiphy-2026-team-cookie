# Q403 — speed of the astronaut at t = 1 s (m/s)

- 2D render, static camera, 24 fps (file fps = question_fps, so no re-timing). t = 1 s → frame 24;
  speed = |p(24) − p(23)| × 24.
- Scale from prior (height 2.2 m): my own mask (measure.py, crop excluding the moon) gives a vertical extent of
  91 px at frame 0 (90–92 px across thresholds 15/25/40 and frames 0/12/24; matches scene record 91 px).
  → 2.2 / 91 = 0.02418 m/px.
- Pixel speed (intensity-weighted mask centroid, 3 thresholds):
  - raw step 23→24: 4.60–4.66 px/frame (scene track also 4.66);
  - linear fit of the steps over frames 20–28 evaluated at frame 24: 4.44 px/frame; net (20→28)/8 = 4.50.
  The motion is a smooth ease-in, so the raw step's +0.15 px is mostly centroid jitter (arm/tilt changes, ~0.2–0.5 px).
  Adopted 4.52 px/frame (between smoothed and raw).
- Speed = 4.52 × 24 × 0.02418 ≈ 2.62 m/s (range 2.58–2.70 for the raw/smoothed alternatives).
- Second route: the scene record's independent centroid track gives 4.66 px/frame raw → 2.70 m/s; its 5-frame mean ≈4.45 → 2.58. Consistent.
- (Phase correlation on the crop was dominated by the static moon and was discarded.)
- Confidence: good, ±3–4 %.
