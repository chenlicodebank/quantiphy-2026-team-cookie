# Q1528 – width of the pillar with collision-warning (black/yellow hazard) markings

The camera is static and level, with fps 24 = question_fps. The pillar used is the left mid pillar (x 230–430, hazard stripes on its
corners, fire extinguisher on its aisle-side face). The right mid pillar is identical in the image: front face
1532.5–1693.5 = 161 px, base y 772.5. So the answer does not depend on which of the two pillars is meant.

## Measurements (scripts in this folder)
- Horizon: vanishing point of the two ceiling light tubes, fitted to ~250 tube pixels (`horizon.py`), is (959.9, 539.4).
- Pillar (frame 41, `pillars.py`, `pillar2.py`): front face runs from the left silhouette x 230.5 to the front/side corner x 391.5,
  which is **161 px**. The front-face base is at y 773 (dark→floor step). The aisle-side face runs to x 427.5, with its base
  at y 758. The two ratios (568.5/532.5 = 1.068 and 233.6/218.6 = 1.069) agree, so the face is ~0.068·Z deep.
- Tire at t = 0.5 s (frame 12, left front tire, `rimfit.py`, `measure.py`): the rim-ellipse centre is (1657.2, 791.8). The
  tire–floor contact is at y 884. Outer tire diameter = 2 × (884 − 791.8) ≈ **183 px**. Frame 24 gives the same result: centre 793.3,
  top 703.5, bottom 884, so ≈181 px.
- Focal length: f = D_px·Z/0.764 with Z = 11.38/√(1+(697²+252²)/f²). Iterating gives **f ≈ 2623 px** (HFOV ≈ 40°) and Z_tire ≈ 10.95 m.
- Back wall: the wall/floor line is at y ≈ 706.5. The B1 sign is near the optical axis, so Z_wall ≈ 23.43 m.

## Width
For a level camera, the pillar front face is at depth Z_p = f·h/(773 − 539.4), so W = 161·h/233.6.
- Route 1 (prior only): camera height h = (884 − 539.4)·0.764/183 = 1.439 m, giving **W = 0.99 m**.
- Route 2 (depth_info of the B1 wall plus f from the tire): h = 167.1·23.43/2623 = 1.493 m, giving **W = 1.03 m**.
  Equivalently, Z_p = 23.43·167.1/233.6 = 16.8 m and W = 161·16.8/2623 = 1.03 m.
- The tire and wall depths disagree by ~3.5% about the ground-plane geometry. The cause is a horizon or contact-row
  offset of a few px. If the horizon is chosen so that both given depths are reproduced (cy ≈ 548), W = 1.00 m.

The pillar's other horizontal dimension (front to back) is ≈ 0.068·Z_p ≈ 1.1 m, which is the longer one. So under the
"width = shorter horizontal extent" reading and the "width across the face" reading, the answer is the same: the face width.

**Answer: 1.0 m.** The routes give 0.99–1.03 m. Confidence: good, about ±4%.
