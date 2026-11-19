# q_1244 – width of the purple car (m)

The purple car is the parked dark-purple Mercedes sedan (rear view, near the centre-right). The scene/ record calls it the
"dark Mercedes". It is static. The file rate and question_fps are both 24.

## Pixel extents (frame 0, merc_width.py, merc_prof.py, zoomed crops)
- Rear bumper chrome: x 1254–1524 at row ~786 (270 px). Rear body at the tail-light row 760: 1255–1517 (262 px).
- Side mirrors at row ~656: left 1252, right 1484–1485 (they sit about 1.5–2 m ahead of the rear axle).
- Rear tyres: outer edges 1257.5 / 1504, ground contact rows 825 / 829 (I used 827 for the axle).
- The left flank goes almost straight to the main-road vanishing point (1253, 422.5), so the image width is the width of the rear face.

## Camera model (geom.py, accel.py, curbs.py)
- Principal point is taken as the image centre. The horizon is at row 422.5 (pitch). The main road's direction comes from its vanishing point.
- Each origin = depth_info distance × the unit ray through the box centre. Camera height H = the height at which the ground ray (the object's
  contact row) reaches the origin's forward coordinate.
- Focal length f, from independent routes:
  - The prior (white van, a = 4 m/s²): the van moves along the cross street at a fixed forward/height line set by its two depths, and a
    quadratic fit gives 4.0 m/s² at f ≈ 2200 (rear-edge track) to 2230 (centre track).
  - The van's path is perpendicular to the main road (no forward drift between t = 0.58 and 1.58 s) at f ≈ 2230. The bike's path gives f ≈ 2020.
  - The vanishing point of the four cross-street curbs (measured in background_final.png): f = 1972, 2089, 2172, 2180.
  - Chosen f ≈ 2170 (the prior-based route is weighted most).
- Camera height from the bike (both times) and the pedestrian: H = 2.82–2.95 m for f = 2200–2100, and these agree within 0.03 m.
- Mercedes rear axle: ground about 15.4 m ahead of the camera.

## Width (merc3d.py, mirror.py)
- Rear bumper width, with a 1.0 m rear overhang behind the axle (this gives a plausible bumper height of 0.44–0.46 m):
  1.824 (f = 2100), 1.786 (f = 2150), 1.748 (f = 2200). Overhang ±0.1 m changes it by ±0.7%.
- Mirror-to-mirror span (mirrors 1.5–2.0 m ahead of the axle): 1.84–1.89 (f = 2100), 1.80–1.85 (f = 2150), 1.76–1.81 (f = 2200).
- The world bounding box includes the mirrors, so its width ≈ the mirror span ≈ 1.81 m at f ≈ 2170. The body alone (bumper) is ≈ 1.77 m.
  The real W123 body width is 1.786 m, which is a sanity check only.

Answer: **1.81 m**. Confidence: moderate. The main uncertainty is f (±4% between routes), which scales the result about 1:1.
