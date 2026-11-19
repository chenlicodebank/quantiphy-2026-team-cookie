# Q539 – length of the table (m)

File fps = question fps = 24.

## Scale from the prior (fit.py)
Quadratic fit to the magnifier's y position over the free-fall frames 0-11 (scene/tracks/magnifier.csv):
a = 12.90 px/frame² (centroid) / 12.93 px/frame² (bbox centre), which is 7435 px/s² ± 0.2 %, residual 0.3-0.5 px.
So the scale at the magnifier's depth is s_m = 9.8 / 7435 = 1.318e-3 m/px.
Sanity check: lens diameter 103 px → 0.136 m, total length 162 px → 0.21 m, typewriter about 0.41 m wide. All plausible.

## Table geometry (edges.py, lens.py)
- I traced the table silhouette against the wall row by row (frame 29) and fitted lines to the side edges:
  left x = -1.948 y + 2114, right x = 1.810 y + 83.6. They meet at (1062, 540.4), which is the image centre, so the
  camera looks horizontally and the horizon is at v = 540.4.
- The back top edge is at v ≈ 946.5. The corners from the extrapolated side lines are at x = 270.8 and 1797.2, so the
  back edge is **1526 px** long.
- The table is clearly in perspective and its back edge lies farther away than the magnifier, so I used the ground
  plane rather than a single 2D scale. A point on the table at depth Z projects at v - 540.4 ∝ 1/Z.
  The magnifier at rest lies flat with its lens at the same x and the same pixel diameter (103 px) as in flight, so
  it is at the same depth as during the fall. The rim's top ellipse spans y 992-1010 and the rim bottom front is at
  1029, which puts the table contact under the lens centre at v_c ≈ 1020.
- Depth ratio Z_back / Z_magnifier = (1020 - 540.4) / (946.5 - 540.4) = 1.181.

## Answer
L = 1526 px × 1.318e-3 m/px × 1.181 = **2.37 m**. This is the longer horizontal extent: the front edge lies beyond
the image, but the side-to-side extent is the length.

Second route (not fully independent): the top ellipse of the lens has an axis ratio of 18/103, giving an elevation of
about 10°. That gives f ≈ 2620 px (horizontal field of view about 44°), Z_m = 3.45 m, camera 0.63 m above the table,
Z_back = 4.08 m, and L = 1526 × 4.08 / 2620 = 2.38 m.
Under a naive single 2D scale (no perspective) the length would be 2.01 m.
Confidence: moderate-good. The main uncertainties are v_c (±5 px, about ±1 %), the corner positions (±5 px) and
whether the outer silhouette is the table (I assumed it is).
