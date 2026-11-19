# q_2962: average speed of the speedboat (prior: sailboat length = 12 m)

- The speedboat is the small dark object near the bottom edge (scene's `bottom_object`). It enters at frame 179 and is fully in view from frame 184 to 239. The sailboat is the large ketch.
- Measurements are in `measure.py` (writes track.json with a min(RGB)<200 mask, the watermark excluded, and connected components) and `speed.py`.
- Scale: the sailboat's horizontal extent (the hull at deck level is its widest part, checked on a 5x crop at frame 120) has a median of 100 px. Hull bottom rows give 98 px. I used 12 m / 100 px = 0.12 m/px, one planar scale as the annotators did.
- Time base: the file is 24 fps and question_fps is 30. The speedboat's per-frame steps repeat as ~7, 7, 7, 14 px. That is the signature of a 30 fps original with 1 frame in every 5 dropped, so the real duration is kept. 24 fps on this file gives the same px/s as 30 fps on the original (9.0 px/frame x 24 = 7.2 px/frame x 30 ≈ 216 px/s). I used fps = 24.
- Speedboat speed over the visible frames:
  - centroid path (mean of per-frame 2D steps, frames 184-239): 215.6 px/s → 25.9 m/s
  - centroid net displacement: 215.4 px/s → 25.85 m/s
  - front edge (frames 179-239): 214.4 px/s → 25.7 m/s
  - rear edge (frames 184-239): 213.8 px/s → 25.7 m/s
- Answer: **25.9 m/s**. The routes agree within 1%. The main uncertainty is the scale: 98 vs 100 px for the sailboat changes the answer by about 2%. The camera motion cannot be checked because the background was removed, so the speed is relative to the frame. The speedboat is in the foreground, so perspective is ignored, following the single-scale convention.
