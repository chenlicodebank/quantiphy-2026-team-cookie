# Q1372 – side length of the square earthen platform (simulation_0074)

Answer: **1.99 m**. The fitted model gives 1.99 ± ~0.04 m, so the designed size is most likely 2.0 m.

## Object
The scene/ record does not cover the platform; it lists it only as a "red-brown grate". The platform is the flat square slab on the far
sidewalk at image x ≈ 998–1145 and y ≈ 245–292. It has a pink rim, a grey-brown "earth" top and edges aligned
with the roads. It does not move; I used the median of frames 0/30/60/71. A second, similar but darker tree-grate object
sits at the left image edge (x < 90, y ≈ 520–600). It is cut off by the frame, so I did not use it.
File fps = question_fps = 24.

## Camera (fixed; pinhole, principal point at image centre)
- Kerb lines were fitted in code (kerbs.py, rms 0.2–1.2 px). They give the vanishing points of the two
  orthogonal road directions: VA = (-1393, -285) and VB = (2692, -265). From VA and VB: **f = 1822 px**.
- Independent check (poles.py): 8 vertical poles give a vertical vanishing point Vz = (1069, 4596).
  This gives f = 1822 with VA and 1812 with VB; leaving any one pole out moves f by at most 1795–1832.
  Pitch ≈ 24° down.
- Metric scale: camera height above the far sidewalk, from the pedestrian, whose depth at t = 0.58 s and
  1.58 s is given (ped_height.py). The pelvis lies on the ray at the given depth, vertically above the feet
  ground point. I read the feet on zoomed frames: (936, 243.2) at frame 14 and (891, 232.6) at frame 38. The
  track's bottom_y (258 / 239) is wrong here: it includes the shadow, and the green bin covers the feet.
  The fitted feet line runs parallel to the kerb, which confirms the readings.
  Result: H = 9.51 (frame 14) and 9.49 (frame 38); fitted pelvis height 0.95 m. Moving the feet by ±1.5 px
  or the pelvis fraction between 0.50 and 0.56 changes H by < 0.4 %.
  Cross-check from the cars and the bike: depth × centroid ray, assuming centroid heights of 0.75 / 1.0 / 0.9 m and
  a 0.15 m kerb, gives H_sidewalk = 9.14–9.56 (mean 9.36). This agrees within 1.5 %.

## Platform fit (plat_fit.py, sens.py)
- Edge points come from sub-pixel threshold crossings (51–65 points per edge, line rms 0.1–0.25 px):
  - the two back edges (top face) and the two front edges (where the side faces meet the ground);
  - the left and right silhouette extremes (the vertical corner edges).
- Model: a square slab aligned with the roads, with side s, height h and centre (a, b), placed on the
  sidewalk plane. Fit rms 0.26 px. In units of camera height: s = 0.2095 H and h = 0.0157 H (≈ 0.15 m).
  If the two sides are fitted separately: 0.2085 and 0.2111 (ratio 0.988, so nearly square, which also
  supports f).
- s = 0.2095 × 9.50 = **1.99 m**. The two sides separately give 1.98 and 2.01 m.
- Sensitivity to f: f = 1800 gives 2.02 m and f = 1840 gives 1.97 m. Using the car-based H (second route)
  gives 1.96 m.

Confidence: good (about ±3 %). The main residual uncertainty is f (±1 %) and the scale source (±1.5 %).
