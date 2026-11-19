# q_910: table width (longer side), simulation_0260

Answer: **1.36 m** (likely range 1.30 to 1.40 m). Planar, no-perspective value: 1.62 m.

## Scale from the prior (the mug's free fall)
- I fitted a quadratic to scene/tracks/mug.csv over frames 5-15, which are before the impact at frame 16 (t = 0.53 s), at question_fps 30 (the file is also 30 fps). Script: `accel.py`.
  - ref_y gives 6110-6155 px/s²; the bottom edge gives 6130-6205 px/s². I used **6150 px/s²**.
  - The fit puts zero velocity at t ≈ 0, so the mug falls from rest. The residuals are about 0.5 px.
- This gives s_m = 9.8 / 6150 = **1.593 mm/px in the mug's plane**.
- Plausibility checks at this scale:
  - Mug: 48 px body width = 7.6 cm, 55 px height = 8.8 cm. Realistic.
  - LG outdoor air-conditioner unit (against the wall): 506 px = 0.81 m. Realistic.

## Table in pixels (`table_edges.py`, `legs.py`, `cols.py`)
- The front face of the tabletop and the legs run from **x = 518.5 to 1538.5, so 1020 px**. The left leg occupies x 519-548 and the right leg x 1507-1538. The edges are sharp to about ±1 px.
- Vertical positions:
  - Front top edge: y = 895.5.
  - Back edge of the top (meeting the wall): y ≈ 865.
  - The mug's contact line at rest: y = 868.5. So the mug stands near the BACK of the table, and the measured edges are nearer the camera than the mug.

## Perspective correction (this is the scene record's main gap: it treated the scene as purely 2D)
- **Inner side faces of the legs.** They are visible: 7 px wide at the right leg and 5 px at the left.
  - These give a vanishing point at x ≈ 948 and D_f/(D_f + d_leg) = 0.9875.
  - Assuming a square leg (front face 30.5 px), this gives f ≈ 2400 px.
- **Apparent mug height against image y** (`hfit.py`, `hfit2.py`).
  - The model is H_app = H_side + (48/f)·|y − y_horizon|. Seen from below, the base ellipse adds height, and it disappears near the horizon.
  - The flight slope alone gives f ≈ 1800-2100. Fitting with the rest frames as well gives y_horizon ≈ 690-750.
- **Front-plane factor.** For points on the tabletop, depth is proportional to 1/(y − y_h). So D_mug/D_front = (895.5 − y_h)/(868.5 − y_h), multiplied by (1 + R/f) for the contact point.
  - For f = 1700-2800 this ratio is **1.16-1.25**, so the width is **1.30-1.40 m**.
  - I used f ≈ 2000-2400, which gives a ratio of about 1.19 and a width of **1.36 m**.
- **Consistency of the geometry.** D_mug = f·s_m ≈ 3.2-3.8 m. The table's depth from the front edge to the mug is about 0.55-0.65 m, and the camera is about 0.2 m above the tabletop. A table about 1.36 x 0.65 m is plausible.

## Second route and confidence
- **The two f estimates agree** (legs: ≈ 2400; mug height: ≈ 1700-2100), and the width varies by only ±3.5 % over that range.
- **The direct planar reading (1020 px × 1.593 mm/px) would be 1.62 m.** I rejected it because the table's front edge is clearly closer to the camera than the mug's plane: the top surface is visible as a 30 px band and the mug stands at its back.
- **A fit I discarded.** Fitting the curvature of the base ellipse (`ellipse.py`) was too noisy: it put the horizon at about 810 px, which would imply an implausible table more than 1.2 m deep.
- **Confidence: moderate.** The main uncertainty is the horizon height.
