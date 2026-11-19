# q_1601 — height of the floor mirror (m)

File fps = question_fps = 24, so frame = round(t*24). Static camera, 3D Blender render, 1920x1080.

## Focal length (focal.py)
Cat torso-centre proxy (scene/tracks/cat.csv) at f0 (407.0, 842.0) and f24 (857.1, 807.6), back-projected with
depths 4.199 m and 4.481 m, principal point (960,540). Constant speed 0.94 m/s => 0.94 m apart after 1 s.
f = 2099 (torso raw), 2084 (torso smoothed), 2143-2163 (mask centroid / bbox centre). Used f ≈ 2110 (hfov ≈ 49°).

## Camera orientation (corner.py)
The vertical wall corner at x ≈ 1693 stays within ±1-2 px of vertical from y=130 to 790, 734 px off-centre
=> pitch < ~0.4°, roll ≈ 0: camera is level, floor normal = image -y, horizon at y = 540.
(A vanishing-point route using the "right wall" line and the cat direction gave a nonsensical 0.14 m
camera height and was discarded; a route using the bench-leg depth as a foot point tilts the floor by 3°, see below.)

## Mirror (edges.py, level.py)
- Bottom centre: floor contact line of the frame (dark contact shadow) at x≈1518, y≈813 (bottom runs from
  ≈(1437,817) to ≈(1600,807)). Back-projected with depth 6.407 m => camera height above floor = 0.80 m (f=2099).
- Top: outer top edge of the frame from intensity profiles, y≈311 at x 1430 to 317 at x 1540; corners ≈(1397,307), (1565,318);
  top centre (1481, 313.5).
- The mirror leans on the back wall. Wall plane = vertical plane through the back-wall/floor line
  y = -0.0753x + 909.2 (back-projected onto the floor). Top-edge ray ∩ wall plane gives depth ≈ 6.74 m.
- Height = top elevation above floor: 1.511 (f=2084), 1.501 (2099), 1.473 (2143), 1.462 (2160).
  Same within 0.004 m using the top-left or top-right corners. Lean: bottom 0.33 m in front of the wall => ~12.5°, plausible.

## Checks
- Cat centre height above floor 0.220 m at t=0 and 0.233 m at t=1 (constant within gait bob) => consistent geometry.
- Cat paw row at f0 (≈965) on the floor gives z ≈ 4.01 m, which matches the cat's depth 4.199 m at u=407 (z≈4.02).
- The bench-leg foot (1408,838) on this floor is at 5.81 m vs the given 5.69 m; the given value probably refers to
  the leg's origin rather than its foot (a 2% difference), so it was not used for scale.
- Ignoring frame thickness changes H by < 0.01 m.

Answer: 1.50 m (range 1.46-1.51 depending on f). Confidence: moderate-good (~±3%).
