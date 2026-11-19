# q_277 – smallest distance between the two cars

- 2D top-down render at 24 fps (the file and the question agree). Prior: dark (black) car speed = 26.085 m/s.
- Tracks come from scene/tracks (an.py prints the per-frame separation and steps). The dark car's step is
  26.97 px/frame (median over frames 2–44, mean 27.01, ±0.3), so 647.2 px/s and the scale is 26.085/647.2 = 0.04030 m/px.
- Distance between the centres: 90.6 px at frame 0 and 90.5 px at frame 1. Both cars stand still in these two
  frames (frame 1 repeats frame 0). From frame 2 on the distance only grows: 93.6, 97.3, ... with a local plateau
  of 103.4 px at frame 20, then up to 223 px. The scene record calls 103 px "the minimum", but that is only the
  minimum while the cars are moving; the minimum over the whole clip is at frames 0–1.
- Frame 0 checked by eye (frames/f0.png): the cars are side by side in adjacent lanes, partly above the top edge,
  with the dark car slightly ahead. The entry positions are consistent: the steps in frames 2–4 (26.8–27.3 and
  21.9–22.6 px) match the later steady steps, so the frame-0 centres fit the extrapolated motion.
- Origin offset: both headings are about 36° at frame 0, so any common front/back offset of the rig root cancels
  almost exactly.
- Answer: 90.5 px × 0.04030 = 3.65 m. If the reference counted only the moving frames, the answer would be
  103.4 × 0.0403 = 4.17 m.
- Sanity check: car length 117–122 px ≈ 4.7–4.9 m, which is plausible. Confidence: good (about ±3%).
