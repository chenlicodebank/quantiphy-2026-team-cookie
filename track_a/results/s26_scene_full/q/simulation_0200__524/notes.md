# Q524: horizontal length of the droplet (m)

- 2D simulation, 60 fps (the file and the question agree). A teardrop-shaped drop falls straight down from the dropper tip.
- Scale from the prior (a = 9.7 m/s²): I fitted a quadratic to the drop centre's y track (scene/tracks/drop.csv, frames 1–11 / 2–11 / 3–11):
  the acceleration is 28.78–28.93 px/frame², and per-frame second differences run 27.3–30.2. I used 28.85 px/frame²,
  which is 103,860 px/s², so the scale is 9.7 / 103,860 = 9.34e-5 m/px.
- Width, measured myself (measure.py): a background-difference mask against frame 13 on frames 2–5 gives 54–58 px depending on the
  threshold (56–57 px at threshold 6). Half-max edges of the column profile give about 54–55 px. A zoomed grid view of frame 4 shows x ≈ 1148–1204.
  I adopted 56 px (the scene record says 57).
- Answer: 56 × 9.34e-5 = 0.00523 m (range 0.0051–0.0053 for 55–57 px).
- Second route: the width is consistent across 4 frames and 3 methods, and the acceleration is consistent across fit windows and the raw second differences.
- Confidence: good (±3%). The main uncertainty is the soft, transparent edge of the drop.
