# q_249 — length of the book (m)

Prior: toy car speed = 0.05 m/s. Top-down, static, near-orthographic camera; car and book both lie on the table plane, so one m/px scale applies (2D treatment).

## Scale (measure.py)
- Car centroid track (scene/tracks/toy_car.csv, checked): linear fit of cx vs frame = 2.609 px/frame; rear edge 2.615, front edge 2.603; mean of per-frame |Δ| = 2.621 (includes noise). Taken as 2.613 px/frame. y drift is 0.003 px/frame, so the motion is purely along image x.
- fps 24.003 (file) vs 24.0 (question): the 0.01% difference doesn't matter. 2.613 × 24.003 = 62.72 px/s, so the scale is 0.05 / 62.72 = 7.97e-4 m/px.
- Sanity check: car length 130 px works out to 0.104 m (plausible toy) and the table 868 × 665 px to 0.69 × 0.53 m.

## Book (book2.py, frame 60; mask drawn in frames/bookmask.png)
- White-page mask inside a polygon ROI, threshold V>200 and S<40, then the convex hull. minAreaRect = 215.0 × 156.7 px, rotated 4.4° in the image (the 215 px side runs along image x). Thresholds of 200 and 215 agree to within 1 px. Corners are about (216,222), (429,238), (418,391), (204,374), which matches scene.json.
- The axis-aligned extent in the image is 226 × 170 px.
- Possible readings:
  - Book's own long side: 215 px, giving 0.171 m.
  - World-axis AABB, if image axes equal world axes (the car moves exactly along image x): 226 px, giving 0.180 m.
- These two differ by 5%. I answered at the midpoint (≈220 px, giving 0.175 m), which is within 3% of both readings.

## Second route
I took the car speed in px/frame three independent ways (centroid, rear edge and front edge), and they agree within 0.5%. The book extent agrees across thresholds and with the pre-recorded scene.json value (214 px).

## Answer
0.175 m. Confidence: moderate-high. The main uncertainty is whether the reference used the rotated AABB or the book's own length (±3%). A small perspective effect from the car's origin sitting above the table plane is ignored (≈1–2%).
