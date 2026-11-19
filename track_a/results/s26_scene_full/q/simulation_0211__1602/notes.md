# q1602 — length of the floor mirror (simulation_0211)

File fps = question_fps = 24, so t=0 is frame 0 and t=1.0 s is frame 24.

## Focal length
- Route 1 (cat, focal.py / focal2.py): I used the torso centre from scene/tracks/cat.csv at frames 0 and 24,
  (407,842) and (857,808), with the given distances 4.199 m and 4.481 m. I took the walk as steady and straight,
  so the cat covers 0.94 m between t=0 and t=1. Solving |P24 − P0| = 0.94 gives f ≈ 2099 px.
  Other reference points gave: mask centroid 2161, bbox centre 2145, feet row 2082, quadratic-smoothed track 2087.
  Changing the distance by ±0.02 m moves f by about ±50 px.
- Route 2 (walls, wall.py): I back-projected the back-wall/floor and right-wall/floor lines onto the floor plane.
  The floor height comes from the mirror's bottom centre at 6.407 m, which gives a camera height of about 0.80 m.
  The angle between the two walls is 89.2° at f=2100 and 90.0° at about f=2130. This agrees with route 1.
- Value used: f ≈ 2110 px, principal point (960,540). The camera is close to level: a pitch of 0° makes the two side
  edges of the mirror equal in length, while 1° does not. The cat's origin comes out about 0.22 m above the floor,
  which is plausible.

## Mirror (mirror3d.py, final.py)
- Outer corners of the frame's front face on frame 0, read from 4x zooms: TL (1394,306), TR (1562,317.5),
  BL (1437.5,819), BR (1609,806). The bottom centre is (1523,812.5) at 6.407 m.
- I intersected the bottom corners with the floor plane through the bottom centre. The top corners come from
  requiring the sides to be perpendicular to the bottom edge. The rectangle closes well: top edge = bottom edge,
  and left side = right side to within 2 mm.
- At f = 2100–2130: the bottom edge (width across the face) is 0.644–0.650 m and the frame's long side is
  1.48–1.50 m. The mirror leans about 7.6° and is turned 26.8° from the camera, which is parallel to the back wall
  (28°). It stands about 0.33 m from the wall line.
- Axis-aligned box in wall-aligned axes: horizontal along the wall 0.645–0.655 m, horizontal depth 0.20–0.21 m,
  vertical 1.47–1.48 m.

## Reading of "length"
- The convention is that length = the longer horizontal extent. Here that is the extent along the wall, about
  **0.65 m**, which is also the frame's width across its face. This is the answer.
- Other reading: the mirror's long dimension, 1.49 m along the frame (1.48 m vertical extent).
- Real-world check: about 1.5 m × 0.65 m is a normal size for a floor mirror.

## Confidence
- The focal length is uncertain by about ±3%, and the corners by about ±2 px out of 172 px, so the measurement
  is good to about ±4%.
- The main risk is which reading of "length" the reference uses.
