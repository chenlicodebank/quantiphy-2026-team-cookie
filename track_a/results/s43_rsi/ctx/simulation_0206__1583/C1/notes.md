# q1583 – length of the letter (paper slip) under the revolver

The file and the question both run at 24 fps. The paper is static, so frame 0 is used.

## Focal length (two routes)
- **Fall fit** (`fitf.py`, `fitf2.py`): typewriter released at t=0 from depth 4.32 m and falling at 9.8 m/s² (the prior).
  Projected its fall on frames 1/2–9/10 and compared with the scene/ track (bbox-centre ref_y, bottom edge, mask centroid).
  Result: f ≈ 2780–3000 px. The gravity direction in camera coordinates is ≈ (0, 0.96, 0.28).
- **Desk geometry** (`desk.py`): desk-top near corner (695,872) at 3.593 m, front-right end (1985,642) at 5.009 m, and the
  revolver (1428,627) at 4.704 m define the desk plane. Requiring the desk's left edge (to corner 470,692) to be
  perpendicular to the front edge gives f ≈ 2950–3000 px. The plane normal (−0.06, 0.957, 0.28) matches the gravity
  direction from the typewriter's fall: P0 (t=0, 4.32 m) → P(t=0.5, 4.501 m) gives (0, 0.96, 0.28). So both routes
  are consistent.
- Chosen value: f ≈ 2950 px, principal point at the image centre.

## Paper
- Segmented the cream paper in code (`paper.py`, overlay in frames/paper_mask.png; contrast-boosted view in frames/boost.png).
  Visible corners: left (1322,625.5) and front (1360,642). The front-right edge runs into the revolver's shadow and ends
  at x≈1413–1416, y≈634 (profile.py). It tapers there, which suggests the right corner. The back edge is hidden by the gun.
- Back-projected onto the desk plane (`size.py`). The paper depth comes out at ≈4.66 m, consistent with the gun's 4.704 m.
  - Short side L–F ≈ 0.090 m.
  - Long side F–R ≈ 0.107–0.114 m (f 2900–3000; R at x 1413–1416).
  - Corner angle is 92–93°, close to rectangular, which supports f and the corners.
- Using a plane through the gun depth (−1.5 cm) instead of the desk-corner plane changes the result by about 1%.

Answer: length (longer side) ≈ 0.11 m. Confidence is moderate. The main uncertainty is where the right corner is, since it
is partly in the gun's shadow and possibly under the gun; that gives about ±5%.
