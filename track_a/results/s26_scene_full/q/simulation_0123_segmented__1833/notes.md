# q_1833 — diameter of the rolling cup (m)

- 2D top-down render, 24 fps (file fps = question_fps, so no re-timing). The "cup" is the teal object (scene record's
  "teal_block"): 42 px along the motion (x) by 78 px across (y). It is the cup lying on its side, rolling to the right,
  so its diameter is the x extent (42 px) and 78 px is the cup's length along its axis.
- Speed: a linear fit of the centroid x over frames 2–71 (scene track) gives 14.536 px/frame. The mean per-frame dx is
  14.534. My own centroids (measure.py) give (1415.04 − 543.25)/60 = 14.530 px/frame. That is 348.9 px/s.
- Scale: 0.338 / 348.9 = 9.688e-4 m/px.
- Diameter in pixels (measure.py, sub-pixel teal-fraction row widths): 42.0 px max width at rest (frames 0–1); the
  median row is 41.1–41.5 px. Moving frames read 42.4–43.7 px because of motion blur, so I used the rest frame.
- Diameter = 42.0 × 9.688e-4 = 0.0407 m (the range 41.5–42.5 px gives 0.0402–0.0412 m).
- Second-route check: the speed from my own centroid tracking matches the scene track to 0.03%. The width is the
  same (±1 px) in all 7 frames I sampled.
- Confidence: high (about ±3%).
