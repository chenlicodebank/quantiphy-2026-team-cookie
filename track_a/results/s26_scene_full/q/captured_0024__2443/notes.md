# q_2443: distance travelled by the book (cm)

The file is 24 fps and question_fps is also 24, so frame = round(t × 24). Lab camera f = 0.5959 × 1280 = 762.8 px, principal point (640, 360).

## Track
I used scene/tracks/blue_notebook.csv (full-mask centroid). I checked it on frames 0 and 48. The book is still for frames 0–18, slides down the
ramp in frames 19–29, lands and slides on the table in frames 30–35, and is at rest from frame 36 onward. I averaged the rest phases to a single point each.

## 3D
- P24 = back-projection of (750.6, 397.3) at 1.0685 m (t = 1.0). P29 = back-projection of (670.3, 451.9) at 0.977 m (t = 1.2).
  |P29 − P24| = 15.8 cm. The ramp direction from these two points agrees within about 6° with the ramp direction from the slope far/near
  depths (1.243 m and 0.990 m, applied to the ramp top and bottom centres) (geo.py).
- Ramp frames 0–29: each centroid ray is intersected with the 3D line P24–P29. The start depth comes out at 1.125 m. Ramp path = **24.4 cm**.
- Table phase: the book centre is placed on the table plane, raised by half the book thickness (8–14 mm). I fitted the plane two ways:
  (a) through the table-left corner at 1.035 m, the ramp foot at 0.99 m and the front table corner at 0.573 m;
  (b) through the table-left corner and the ramp foot, containing the ramp's horizontal width direction (table2.py, table3.py).
  Frames 30–31 are the ramp-to-table transition, so their depth is interpolated.
  - The end depth comes out at 0.87–0.95 m.
  - The table path (frames 29–36) is 14.4–17.2 cm. The straight line from P29 to the rest point is 12.9–16.2 cm.
- I did not use the right table corner taken at 0.573 m: a plane through it passes through the camera, so that pairing is inconsistent.

## Results (fullpath3.py)
- Per-frame path length: 38.9–41.6 cm.
- After 5-frame smoothing: 37.3–40.7 cm.
- Second route, ramp length plus the straight table segment: 37.5–40.5 cm.
- **Answer: 39 cm.**

## Caveats
- A quadratic fit along the ramp gives an acceleration of about 2.0 m/s², not the prior's 2.8 m/s². The ramp scale is fixed by the
  given depths, so I kept it. The prior is probably a noisy second difference.
- The end depth is the main uncertainty: the table is seen at a grazing angle. A book-size check suggested a slightly closer end
  (about 0.83 m), which would make the total about 41 cm.
- Confidence: moderate, about ±8%.
