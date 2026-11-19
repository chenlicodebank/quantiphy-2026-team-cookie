# q2072: ball speed at 7.00 s

- Scale: prior centre circle radius = 9.15 m. `measure_circle.py` fits the circle line on frame 208 (359 edge points,
  rms 0.17 px) and gets r = 116.92 px (horizontal 116.8 / vertical 117.0). That matches scene.json (116.9). Scale =
  9.15/116.9 = 0.07827 m/px. Sanity check: goal line to goal line is 1309 px, which gives 102.5 m. Plausible.
- Camera: static (drift under 0.1 px per frame). The stabilised ball track from scene/tracks/ball.csv is used. The ball
  rolls smoothly from frame 173 to 262 after the kick, with no contact near 7 s. The per-frame steps are steady,
  about 1.1 px/frame.
- Time base: the file runs at 29.764 fps and the question at 30. At 7.00 s that is frame 208 or 210. The ball is
  slowly decelerating at that point, so both give the same result.
- `speed.py` fits a local line to the positions (±1 to ±8 frames):
  - frame 208 at 29.764 fps: 2.60-2.64 m/s.
  - frame 210 at 30 fps: 2.53-2.61 m/s.
  - Raw forward differences: 2.54 and 2.49 m/s.
- Answer: 2.60 m/s. Confidence: good (about ±3%).
