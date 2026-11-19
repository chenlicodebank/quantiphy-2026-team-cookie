# Q1969: length of the brown horse (m)

The "animal" in scene/ is the brown horse, seen from above with its white muzzle at the right (leading) end. It moves right along a horizontal line. This is a 2D video, so one m/px scale applies. fps = question_fps = 24.

- Speed (measure.py, my own segmentation of non-white pixels below y=748, mask checked on frames/ov*.png):
  linear-fit slopes are x0 2.645, x1 2.659 and centroid 2.674 px/frame. The scene record gives 2.62-2.68.
  I used 2.655 px/frame = 63.7 px/s.
- Scale = 0.874 / 63.7 = 0.01372 m/px.
- Length = horizontal mask extent, nose to rump. It is 141-160 px over the gait cycle, with mean 148.9 and median 148 px.
  - Median: 148 px x 0.01372 = 2.03 m.
  - Range over the gait cycle: 1.93-2.20 m.
- Second route: using the centroid slope (2.674 px/frame) gives a scale of 0.01362 and a length of 2.02 m. Using the scene record's PCA axis_len (mean ≈149) gives 2.04 m.
- This is plausible for a horse (about 2-2.4 m).
- Confidence: moderate-high. The main uncertainty is pose variation (±5%).

Answer: 2.03 m
