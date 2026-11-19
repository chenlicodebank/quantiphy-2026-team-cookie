# Q516 – diameter of the bottle's neck (m)

- 2D product render, 60 fps (fps and question_fps agree; no re-timing). Prior: the droplet's acceleration is 9.7 m/s². No depth_info.
- **Scale** (`measure.py`): I took the droplet track from scene/tracks (I inspected it, and frames 2–10 are clean free fall).
  - Centroid, using the speed convention of backward differences: the mean acceleration over frames 3–10 is 113,714 px/s², and a quadratic fit gives 112,801 px/s².
  - The bbox centre gives 114,762 px/s².
  - Scale = 9.7 / 113,714 = 8.53e-5 m/px. The spread between methods is about ±1%.
- **Neck width** (`neck.py`): I averaged frames 11–13 (no drop in view) and, for each row, found the outermost columns that differ from the background.
  - Rows 572–604, the threaded neck: 257–264 px, median about 262 px. The neck runs from x ≈ 1786 to 2050.
  - Rows 612–652, the bottom collar or thread ring: up to about 295 px.
  - Rows above 560 are contaminated by the dropper tube.
  - The bare glass between the threads is about 240 px, by eye on a 2.5x zoom.
- **Answer:** 262 px × 8.53e-5 = 0.0223 m. Using the bbox-centre scale gives 0.0221 m.
- **Check:** the body is 427 px wide, which is 0.0364 m at this scale, plausible for a 30 ml dropper bottle. The neck-to-body ratio is 0.61, which is consistent with the frames.
- **Confidence:** moderate. The main uncertainty is which width counts as "the neck": 240 px with no threads gives 0.0205 m, and 295 px at the collar gives 0.0252 m.
