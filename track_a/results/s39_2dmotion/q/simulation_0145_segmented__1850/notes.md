# q_1850: average speed of the rocket (m/s), prior: rocket length = 2.9 m

The video is 2D, with a static camera, 24 fps (file rate = question_fps) and 29 frames. The rocket leaves the launcher pod and flies in a straight line along a 39° axis. Its nose is visible from frame 3 and it is gone from frame 26 on.

## Method
- `measure.py`: rocket mask = |frame − frame 28| > 40, inside a ±14 px band around the launch axis, then a 3×3 opening. For each frame it records the nose, tail and centroid positions along the axis, written to `my_track.json`. These agree with scene/tracks/rocket.csv to within about 1 px.
- Rocket length in px:
  - Mine: 219.2 px. This is the 0.2–99.8 percentile extent, median over frames 15–20 and 22. Trimming the percentiles shaves the thin nose cone slightly.
  - SAM 3 masks (frames 16, 18 and 20, measured in `sam_len.py`): 218.2, 223.6 and 222.9 px by percentiles, and 221–227 px from max − min. The SAM outline is dilated by about 1–2 px at each end.
  - Scene record: 221.9 px.
  - All of these are within 3% of each other, so no conflict. **L = 221.5 px**, giving 2.9 / 221.5 = 0.01309 m/px.
- Centre = nose − L/2 for frames 4–22 and tail + L/2 for frames 13–25. The step to frame i is c(i) − c(i−1).
  - Per-frame steps from frame 5 to 25: 20, 17, 18, 29, 27, 32, 33, 37, 41, 43, 43, 46, 50, 52, 53, 56, 61, 55, 63, 57, 64 px.
  - The speed rises roughly steadily: acceleration about 2.2–2.4 px/frame², with no bounce or turn.
- `fit.py`: quadratic fit to the centre (combined nose- and tail-based series), giving v(i) = 1.2108(2i − 1) + 8.435 px/frame.

## Result
- Average of the per-frame speeds:
  - **Route 1 (fit):** over the whole clip (frames 1–28) or over the visible frames (4–25), which share the same midpoint 14.5: 42.34 px/frame, which is 1016 px/s and gives **13.30 m/s**.
  - **Route 2 (measured steps, no fit):** mean over frames 5–25 gives 13.43 m/s at L = 221.5.
- Answer: **13.35 m/s**.

## Sensitivity and confidence
- The interval is ambiguous. Taking only the frames where the whole rocket is visible (13–22) would give about 15.6 m/s. Because the motion is close to uniformly accelerated, the whole-clip and visible-span averages are the same.
- The scale is uncertain by about 1.5% (the spread in L).
- Confidence: medium-high, provided the reference averages over the full clip.
