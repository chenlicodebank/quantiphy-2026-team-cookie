# q1118 – speed of the eagle at t = 1.0 s

The file runs at 25 fps but question_fps is 24, so I used 24 for everything: t = 1.0 s is frame 24, and speed = per-frame displacement × 24.
I used the scene/ record's frame column, not its seconds.

## Scale (prior: eagle length = 0.8 m)
- The eagle flies left to right, almost square to the line of sight: depth changes by only 0.62 m/s, while it moves
  sideways at about 13 m/s. Seen from obliquely above, its wingspan shows up mostly as image height, and its body
  (beak to tail) lies along image x. In frames where the wings are raised (f10–14, f22–24, f47–50; see
  frames/zoom_18_29.png), the x extent is the body length.
- Results from measure_len.py (mask thresholds of 40/60/90 against the background): x extent 25–26 / 25 / 24–25 px
  at f10, 11, 14, 22, 24. len_profile.py, with a stricter half-of-peak threshold, gives 21.5–26.6 px (it loses the
  faint thin tail and beak tips). **I took L = 25 px (±1 px).**
- Sanity check: the shadow's wingspan is about 58 px, and the bird's projected wingspan peaks at about 40 px. Both fit
  an eagle whose wingspan is about 2.3 times its body length, so 0.8 m is the body length.
- Focal length: f = 25 px × 100.14 m / 0.8 m ≈ 3130 px, which gives a horizontal field of view of 17.4°.

## Speed
- speed.py back-projects the track centroids (scene/tracks/bird.csv, checked on frames) with principal point
  (480, 480). Depth is interpolated linearly between the two depth_info values (100.1405 m at frame 24, 99.5206 m at
  frame 48), so the 0.62 m/s radial part is included.
- The mask centroid wobbles with the wingbeat, which lasts about 25 frames. I therefore averaged over one full wing
  cycle centred on frame 24: windows 12→37 and 11→36 both give 12.88 m/s.
- Second-route check: other windows give 12.69 (f0→25), 12.91 (f24→49), 12.95 (f14→34) and 13.05 (f20→28) m/s. The
  raw one-frame difference f23→24 is 13.05 m/s.
- If L is 24 or 26 px, the answer becomes 13.4 or 12.4 m/s (±4%).

**Answer: 12.9 m/s.** Confidence is moderate: the main uncertainty is the eagle's pixel length (±4%).
