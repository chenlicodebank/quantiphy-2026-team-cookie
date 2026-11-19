# q_2926: width of the blue shopping bag (cm). Answer: 42.0 cm

The file and the question both run at 24 fps, so no time conversion was needed. The bag doesn't move, so the measurements use frames 10, 20, 34 and 48 (t = 1.4 s is frame 34).

## Object
The blue shopping bag is the dark-blue tote with the round orange "MARINE" logo, lying flat on the floor at about (835,330) px (`blue_tote_bag` in scene/). Its handles come out of the upper-right edge, so that edge is the bag's opening.
- In the image its corners are about L(770,315), T(827,297), R(894,349) and B(844,370).
- **Width = the edge along the opening (T-R, with the parallel edge B-L).** This is the bag's horizontal extent across its face when it hangs upright, and it is also its longer side. The other side (L-T / R-B) is the bag's height, about 33-35 cm.

## Method (lab camera: f = 0.5959 x 1280 = 763 px, principal point (640,360))
1. **Floor plane orientation from the white board.** The board is a rigid rectangle lying flat on the floor.
   - `board_edges.py` fits sub-pixel lines to its four edges in frames 24-48 and gets the two vanishing points. The floor normal is the cross product of the two directions.
   - The two edge directions come out orthogonal in every frame (d1·d2 ≈ 0), which supports f = 763.
   - Mean normal: pitch 37.5° ± 0.6°, roll 10° ± 1.3°.
   - Check: the board measures a constant 77.5 x 58.5 cm in every frame on this plane, so the normal is consistent.
2. **Plane offset from depth_info.** The bag centre pixel is back-projected at 3.307 m and the floor plane is put through that point. Camera height comes out at 1.71 m.
3. **Bag on the floor plane.**
   - (a) `bag_corners.py`, visual corners intersected with the plane: T-R = 41.0 cm, B-L = 41.5 cm, short sides 35.5 / 31.6 cm, corner angles 87-94°.
   - (b) `bag_topdown.py` + `topdown_profile.py`, a metric top-down rectification (2 mm/px) of the bag, using half-maximum extents of the blue mask along the opening direction. Results by saturation threshold:

     | saturation threshold | width (along opening) | height (across) |
     |---|---|---|
     | S ≥ 80 | 43.6 cm | 35.4 cm |
     | S ≥ 100 | 42.6-43.0 cm | 34.4-35.0 cm |
     | S ≥ 120 | 41.4-42.0 cm | 32.6-33.0 cm |

     Frames 10, 20, 34 and 48 agree.
   - Final width: 42.0 cm. Routes (a) and (b) span 41-43.6 cm.

## Checks and uncertainty
- **Sensitivity to the floor normal:** pitch ±2° changes the width by about ±1.5 cm, and roll ±3° by about 1 cm.
- **The other given depths, predicted from this plane:**
  - mario/plush toy: 2.00 m (given 2.016)
  - board centre at frame 34: 2.67 m (given 2.815)
  - white box/carton: 2.26 m (given 2.082)

  So the depths are noisy at about ±5-9%, scattered in both directions around this solution.
  - The "trashbin" depth (2.303) can't belong to the blue bin at the back of the room, which is about 3.9 m away, so I ignored it.
  - A plane forced to fit the board's given depth exactly (pitch about 40-42°) gives a width of about 40-41 cm.
- **Velocity prior:** on this plane the board's speed is about 1.4-1.7 m/s around t = 1.4 s, against the prior of 1.934 m/s. The reference velocity comes from noisy per-frame depth back-projection, so it isn't a clean scale check. I didn't use it.
- **Simple card formula (no foreshortening):** 3.307 x about 87 px / 763 = 37.7 cm. This underestimates, because the floor is seen obliquely.
- **Other reading of "width":** taken as the shorter side of the bag lying flat, the width would be about 33-35 cm. I answered with the dimension across the bag's face along the opening, which is the conventional bag width.

Confidence: moderate. The plane geometry gives about ±5%, and the depth noise could add 5%.
