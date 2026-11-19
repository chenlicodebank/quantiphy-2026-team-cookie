# q_2247 — length of the pen (cm)

The question and file are both 24 fps. The pen is static, so I averaged frames 0, 5, 40 and 48.
Prior (ball acceleration) is not needed; scale comes from depth_info: pen at 1.6725 m (t=0), f = 0.5959*1280 = 762.8 px.

## Pixel extent (pen2.py, pen3.py; zoom frames/pen3.png, frames/penleft.png)
- Pen axis from a weighted PCA of the deviation-from-wood mask: angle -5.9 deg (nearly horizontal in the image), centre (467, 438.5).
- Profile along the axis with a 50 % threshold: ends at (434.6, 441.9) and (501.0, 435.0), giving **66.8 px**.
  - Right end: the silver end cap; the edge is sharp at x≈501.5.
  - Left end: the black body ends at x≈441. A thin dark tip (the writing tip / cone, 1–2 px wide) continues to x≈435,
    right at the table's left edge (green background begins at x≈433). I included the tip.
  - The scene record gave 68 px (bbox 434–501), which agrees.
- Excluding the tip: 60.7 px (13.3 cm via the card).

## Size
- Method card: 1.6725 * 66.8 / 762.8 = **14.64 cm**.
- Second route: I fitted the table plane through the 3D back-projected centres of the pen, book and cookie (their given
  depths), then intersected the rays of both pen ends with that plane. Result: **14.06 cm**. This handles the off-axis
  ray length (Euclidean depth vs z, about 3 %) and the foreshortening; the pen lies almost parallel to the image plane.
- The two routes differ by 4 %. Answer: **14.3 cm**, between the two and within about 2 % of each. A typical pen is 14–15 cm,
  which is consistent.

Confidence: moderate-good. The left-end location is ±2 px (±0.4 cm).
