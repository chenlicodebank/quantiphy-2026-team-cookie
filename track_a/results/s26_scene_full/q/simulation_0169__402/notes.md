# Q402 — acceleration of the astronaut at t = 0.5 s (frame 12)

- 2D render, 24 fps (file fps = question_fps; no re-timing issue). Static camera, single moving astronaut.
- Scale: prior height 2.2 m; upright astronaut at frame 0 is 91 px tall (bbox_h 90-91 over frames 0-30, checked on a
  zoomed frame f0.png: y≈475→565). 2.2/91 = 0.02418 m/px.
- Track: scene/tracks/astronaut.csv mask centroid (checked consistent; path nearly straight, perpendicular deviation
  <1.5 px). Projected onto the path direction.
- Main route (fit.py): smoothstep (Blender ease-in/ease-out Bezier, 3t²-2t³) fitted to all 80 positions:
  D = 274.8 px, keys at frame -0.3 → 78.2, rms residual 0.27 px (excellent fit). Benchmark convention
  (speed(12)-speed(11))·fps on the fitted curve: 109.7 px/s² → 2.65 m/s². Analytic at frame 11.5: 2.61 m/s².
- Second route: local polynomial fits of raw positions around frame 12 (various windows, deg 2-3): 2.57-2.64 m/s²;
  linear slope of raw per-frame steps over frames 6-18: 2.78 m/s² (noisier).
- Answer: 2.64 m/s². Confidence: good (~±4%), dominated by the 91 px height reading (±1 px ≈ 1%) and fit choice.
