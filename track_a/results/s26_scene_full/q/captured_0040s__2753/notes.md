# q_2753 – distance travelled by white ball, 1.5 s → 1.9 s (cm)

- question_fps = file fps = 24 → frames 36 … 46 (round(1.9·24)=46). Interval contains the 2nd table bounce (frame 41);
  path length = sum of frame-to-frame 3D displacements, so the bounce is simply a vertex of the polyline.
- Centres: scene/tracks/ball.csv cx,cy (mask centroid). Checked on overlays (frames/check.png, check.py) for frames
  35–47: centroids sit on the ball / centre of the blur streak; frames 40–41 slightly affected by the table colour (±3 px).
- Camera: lab card f = 0.5959·1280 = 762.8 px, (cx,cy) = (640,360). Depth from depth_info: 0.7045 m at t=1.5 (f36),
  0.6270 m at t=2.0 (f48), linearly interpolated per frame.
- Back-projection per method card: P = ((u−cx)/f, (v−cy)/f, 1)·depth  → path length **38.1 cm** (measure.py, route B).
- Variants: treating depth as Euclidean range along the ray: 35.8 cm (ball is far right, ray norm up to 1.17, so the
  two readings differ by ~6 %); 3-frame smoothing within each flight segment: unchanged (35.7 cm range reading);
  chord sum 36→41→46: 33.1 cm (lower bound, as expected for curved arcs).
- Per-frame steps 2.5–4.7 cm, consistent with ~0.6–1.1 m/s ball speed.
- Answer: 38.1 cm (method-card convention). Confidence moderate: ±7 % from depth convention / interpolation.
