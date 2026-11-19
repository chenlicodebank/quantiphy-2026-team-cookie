# Q686 – acceleration of the moving red general at t = 1 s

- 2D scene seen from above, static camera, 24 fps (file fps = question_fps, no re-timing). t = 1 s → frame 24.
- Scale: prior diameter 0.097 m; the general's disc diameter is 86.5 px (scene record bbox 86–87 px, frames 0–39)
  → 1.121e-3 m/px.
- Track: my own re-measurement (measure.py: median-background difference mask, centroid y) agrees with
  scene/tracks/red_general.csv to within ~1 px (constant offset from a slightly looser mask).
  Duplicated frames (9,11,18,20,28,34 show the next frame's image) were excluded.
- Motion is uniformly accelerated: quadratic fit over clean frames 2–39 gives 1.079 px/frame² (rms 0.69 px);
  sub-windows 2–20: 1.110, 14–30: 1.078, 20–40: 1.039 px/frame².
- a = 1.079 × 24² × 0.097 / 86.5 = 0.697 m/s².
- Second route: clean one-frame speed increments around frame 24 (diffs 22→27: 24.21, 25.42, 26.54, 27.43, 28.56 px/frame)
  average 1.09 px/frame² → 0.70 m/s²; the single increment at frame 24 alone (1.21) is noisier (0.78).
- Answer: 0.70 m/s². Confidence: good (±5 %, mostly from the diameter pixel size 84–87 px).
