# q_2674 — width of the table (m)

File fps = question fps = 24. Lab camera: f = 0.5959·1280 = 762.8 px, principal point (640, 360).

## Method (3D plane reconstruction; `edges.py`, `geom.py`, `check.py`)
1. Frame 48 (ball gone): wood mask → line fits. Left side x=-1.5765y+1112.0, right side x=1.6377y+24.3 (rows
   455–585, so the rounded corners are left out), back edge y=0.02119x+431.4, front top-surface edge y≈0.0071x+587.8
   (the bright-to-dark transition into the front band). Corners are the line intersections: BL(418,440) BR(757,447)
   FL(183,589) FR(999,595).
2. The side edges meet at the depth vanishing point (578.5, 338.4) → the front-to-back direction d1. The plane
   normal is d1 × (front-edge direction, taken ⟂ d1); the back edge and the ball's path give the same normal
   (pitch ≈1.5°).
3. Scale from depth_info: the ball centre is 1.010 m away at frame 22 and 0.716 m at frame 34, back-projected along
   the centroid rays. Both points sit at the same height relative to the plane (0.1507 / 0.1482–0.1507), so the
   camera is ≈0.169 m above the table top (ball centre minus the 2 cm radius).
4. The corners are back-projected onto the table-top plane.
   - Left-right: 0.546–0.550 m (front edge 0.546, back edge 0.550).
   - Front-to-back: 0.72 m (left side 0.717–0.737, right side 0.715–0.730, depending on how the normal is taken).

## Reading of "width"
Width is the shorter horizontal extent, so the answer is **0.546 m** (left-right). The longer extent (length) is the
front-to-back 0.72 m. Under the desk "front-to-back depth" reading the answer would be about 0.72 m. I used the
rule given for tables (length = longer side, width = shorter side).

## Second-route check
- Depth from the ball's apparent diameter (minus about 1.5 px of segmentation halo) against the depth predicted by
  the plane at frames 0, 28, 31 and 34: ratios 0.98, 0.98, 1.00 and 0.95. This independently confirms the metric
  scale within about 2–5 %.
- The front and back edges give the same left-right length (0.546 vs 0.550), so the table is consistent with a
  rectangle.
- Moving the back or front edge by ±2 px changes left-right by <0.1 %, front-to-back by about ±3.5 %.

Confidence: good for 0.546 m (±3 %). The main risk is the width-naming convention.
