# Q42 – width of the turning yellow (peach) car

2D orthographic top-down render, fps 24 (= question_fps). Scale from prior: car length 5.44 m.

Measurements (measure.py, paint mask R−B>22 & R>180, row/column profiles ≥3 px, frames where the car is
axis-aligned):
- f0, f1 (heading up): width 81 px, length 218 px.
- f66–71 (heading right): width 80 px, length 218–220 px.
- Scene record (PCA extents, all frames): length 220 (median), width 82; minAreaRect 219 x 81.
- Side mirrors add ~1–2 px each side beyond the body.

Width/length ratio: body only 80.5/218.5 = 0.368; with mirrors ~83/219 = 0.379; record 82/220 = 0.373.
Width = 5.44 × ~0.371 ≈ 2.02 m (range 2.00–2.06).

Second route: two independent orientations (vertical at f0, horizontal at f71) give the same ratio within 1 px,
and the scene record's PCA numbers agree. Confidence: high (±3%).
