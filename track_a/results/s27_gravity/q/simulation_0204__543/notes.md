# Q543 – speed of the magnifying glass at t = 0.125 s

question_fps = file fps = 24 → t = 0.125 s is frame 3; speed = (y3 − y2) × 24 × (m/px).

Scale (2D video): the prior says it falls at 9.8 m/s² before 0.5 s. The vertical pixel acceleration comes from a
quadratic fit to the free-fall frames (0–9 or 0–11, before the impact at about frame 11.2).
- Using my own mask centroid (measure.py, background = frame 29), frames 0–9: a = 12.95 px/frame², max residual 0.3 px.
- Using the record's centroid, frames 0–11: a = 12.90; frames 0–9: a = 12.97. Bbox centre: 12.83–12.93.
  (My frame-11 mask merged with the mat/shadow, so I left that frame out.)
- m/px = 9.8 / (a × 24²) ≈ 1.31e-3 m/px.

Speed at frame 3: the drop from f2 to f3 is 33.0–33.05 px (both centroids), so v = 33.0 × 9.8 / (a × 24) = 1.039–1.046 m/s.
Taking the f3−f2 difference from the fitted parabola instead gives 1.041–1.05 m/s.
Check: the fit puts release at frame ≈ −0.05, essentially at rest at t = 0. An ideal release at exactly t = 0 would
give 9.8 × 2.5/24 = 1.021 m/s, which agrees within 2%.

Answer: 1.04 m/s. Confidence: high (±2%).
