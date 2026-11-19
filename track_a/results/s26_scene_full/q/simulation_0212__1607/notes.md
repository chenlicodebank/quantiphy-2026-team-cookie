# q1607 — length of the wooden bench (m)

The "wooden bench" is the slatted reddish-brown piece with a lower shelf on the right of the frame. The scene record
calls it "side_table". File fps = question fps = 24.

## Scale
- Focal length comes from the cat prior (0.94 m/s) and the depths 4.199 m (t=0, f0) and 4.481 m (t=1 s, f24). I back-projected the
  cat core centroids (408.5,842.7) and (869.4,805.3), with the principal point at the image centre, and solved
  |P1-P0| = 0.94 m. That gives f ≈ 2150 px (2100–2156 depending on the origin proxy), so hfov ≈ 48°  (focal.py).
- Floor geometry (geom2.py, vp.py, bench.py): the vanishing points of the back-wall and right-wall floor lines (perpendicular walls) give a
  horizon at y≈534 for f = 2150, so pitch is ≈0. I used horizon y = 540. The closest leg foot (1408,841) at 5.69 m gives a
  camera height H = 0.77 m.
  - Check: the floor point at the mirror's bottom (≈(1515,809–812)) comes out at 6.33–6.41 m. Given: 6.407 m. ✓
- Bench feet measured in code (wood mask on frame 43, a clear frame; wood.py): front-left (1408,841), rear-left (1330,828) and
  front-right (1627,823). The rear-right foot is hidden in the shadow under the bench, in front of the mirror's bottom rail. The
  diagonal leg seen inside the mirror glass is a reflection.
- The feet, back-projected to the floor, form a rectangle: 0.757 x 0.295 m, corner angle ≈ 90°, yawed 27.6°. The back wall's
  direction, taken from its vanishing point, is 28.3°. So the bench stands parallel to the wall, and its world AABB length
  equals its true length.
- Top board: in the image it runs from x = 1288 (back-left corner) to x = 1667 (front-right corner). I solved for the top's length L and
  width W, centred on the footprint and at the same yaw. Result: **L = 1.005 m**, W = 0.37 m. The model puts the front-left top corner
  at x ≈ 1375, and the apron's corner is observed at ≈1377–1390. ✓

## Sensitivity (bench.py)
| Change | L (m) |
|---|---|
| f = 2100 / 2200 | 1.03 / 0.98 |
| horizon y = 530 / 550 / 560 | 1.005 / 1.004 / 1.004 |
| any foot moved ±2 px | 0.99–1.02 |
| top ends ±2 px | 1.013 |

Answer: **1.0 m**. Confidence: moderate-high, about ±5%. The main uncertainty is the focal length taken from the cat's speed.
