# q_568 – height of the vase (prior: black cat speed 0.94 m/s)

fps = question_fps = 24, so no re-timing issue. The camera is static and level.

## Scale at the cat's depth
- From scene/tracks/cat.csv (I checked the mask on the frames): linear fits of x(frame) over frames 0–49, 0–45 and 4–48 for the mask
  centroid, nose (front_x) and rear bbox edge all give 17.74–17.83 px/frame. The speed is constant (steady walk), so I used
  426.7 px/s.
- s_cat = 0.94 / 426.7 = 2.203 mm/px.

## Perspective (the vase is deeper than the cat)
This 2D-labelled scene has clear perspective: the table feet are at y≈1005 and the cat's paws at y≈1030, and the table-top
slats converge toward a vanishing point.
- Horizon: I fitted the slat-gap lines on the table top (slats2.py) and, with cx = 960, they meet at y_h = 537.6
  (5 lines, 528–542). This matches a level camera with the principal point at the centre, so y_h = 540.
- Floor point: y − y_h = f·H/Z. Cat paws at y=1030 give camera height H = 490 · s_cat = 1.080 m.
- Table (legs.py, profiles): front feet y=1005 and tabletop front edge y=808.5 give K = H/(H−h_table) = 1.732.
  The back feet (y=975) and the back edge (y=790.5) give 1.737, so the legs don't splay front-to-back. Table height is 0.457 m.
- The vase base sits on the tabletop: s_vase = (H/K)/(y_base − 540).
- Vase (the large front vase; the small one behind it is shorter, so an AABB of both has the same height). Column
  profiles (vase_profile.py) put the top at y=586.5 and the base contact at y=800.5, so it is 214 px tall.
  - Raw: s_vase = 2.390 mm/px (1.085 × s_cat), giving a height of 0.511 m.
  - Correcting the rim and base ellipses to the vase-centre depth (assumed r/Z≈0.01) gives 0.509 m.

## Checks
- The second route, the back legs and back edge instead of the front ones, gives K = 1.737 and changes the height by under 0.3 %.
- Moving the horizon to 538 (the slat fit) changes it by under 0.1 %.
- If the lowest paw is the near-side paw (a few cm in front of the origin), the height could be about 1 % higher.
- A naive single scale with no depth correction would give 214 × 2.203 mm = 0.471 m. That is rejected, because the vase is
  clearly behind the cat's plane.

Answer: 0.51 m. Confidence is moderate to high (about ±4 %). The main risk is whether the reference used a no-perspective
single scale (0.47).
