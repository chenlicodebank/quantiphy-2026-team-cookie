# q 2975 — initial distance passer ↔ receiver (m)

- Passer = A (leftmost, kicks the ball at frame 0); receiver = E (taller of the right pair, heads the ball at frame 39).
- File fps 30.0003, question_fps 30; frame indices used directly (t=0 → frame 0).
- Scale from prior (gravity 9.8 m/s²): my own ball track (`measure.py`, connected components, frames 3–38),
  quadratic fit of y → 834.8 px/s² (mean second difference 830.8 px/s², consistent; scene record 834.8).
  Scale = 9.8 / 834.8 = 0.011740 m/px. Camera: static apart from ≤4 px vertical drift (scene record); raw pixels used.
- Frame 0 horizontal separation (people stand on same ground row, y≈351–361):
  - mask centroids: A 456.8, E 832.0 → 375.2 px → 4.40 m (chosen)
  - A torso/standing-leg centroid 452.3 → 379.7 px → 4.46 m
  - bbox centres: 365.5 px → 4.29 m; head tops: 391.5 px → 4.60 m
- Answer 4.4 m. Sanity: E's height 146 px → 1.71 m, plausible adult.
- Confidence: moderate; main uncertainty is which reference point the annotator clicked (spread ±4%).
