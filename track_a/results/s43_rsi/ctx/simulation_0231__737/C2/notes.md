# q737 – width of the orange chair next to the blackboard (simulation_0231)

Prior: cat speed = 0.714 m/s. No depth_info. fps = question_fps = 24.

## Object
The orange wooden-seat chair standing against the right wall, under the clock (x≈1600–1795, y≈735–1030).
It faces the camera squarely: its backrest is at the back and the seat runs toward the camera. Its right legs
at x 1752 (back) and 1792 (front) line up on a ray toward the vanishing point (960,540).

## Geometry (perspective matters, so I did not use a single 2D scale)
- The vanishing point / horizon is at y≈540, the image centre. The side edges of four ceiling panels cross x=960 at
  y = 515–575, mean ≈542 (lights2.py). Verticals are vertical, so the camera has no pitch.
- Wall–floor line y = 951.5 (desk.py). The desk top runs from its rear edge at y≈738 (dark contact line,
  flush with the wall) to its front edge at y≈766.5.
- Cat: paws at y = 741 (track median, constant, so the cat walks parallel to the wall). Depth from the desk-top
  plane: Z_cat = 198/201 Z_wall = 0.985 Z_wall.
- Cat pixel speed: linear fit of torso_cx = 8.91 px/frame (cx_dark 9.00, cx_mask 8.99, first–last 8.85)
  → 8.92 px/frame = 214.1 px/s. Scale at the cat: 0.714/214.1 = 0.003335 m/px. At the wall:
  0.003386 m/px. Camera height = 411.5 px × 0.003386 = 1.393 m.
- Chair floor contacts (contrast-enhanced leg bottoms, legs.py / legimg.py): back legs y≈1006 and front legs
  y≈1028. The x-positions give Z_back/Z_front = 832/792 = 1.050 and the y-positions 1.047, which agree.
  Z_back = 0.883 Z_wall and Z_front = 0.843 Z_wall.
- Backrest (orange mask, rows 745–795, backrest.py): x 1601.4 → 1751.9 = 150.5 px. Its depth ≈ Z_back × 1.005
  (the backrest leans back slightly).

## Result
World X from the floor/perspective geometry: X = (x−960)·h_cam/(y_floor−540).
- Backrest left edge X = 1.925 m and right edge X = 2.379 m. The front-right leg's outer edge (1794, y 1028) is at
  X = 2.381 m. The right-hand legs at the back and front give 2.367 and 2.375 m, which confirms that the chair is
  square to the camera and that the horizon is correct.
- **Width, left to right (axis-aligned bounding box) ≈ 0.456 m.** The backrest alone is 0.452 m. The front-leg
  spacing is 0.39 m centre to centre.
- Second route, the same scale applied through depth ratios: 150.5 px × (0.8875/0.985) × 0.003335 = 0.452 m.
  The full extent is 0.455 m.
- Plausibility check with the same scale: chair seat height ≈ 0.42 m, total height ≈ 0.81 m, cat torso
  ≈ 0.49 m. All of these are realistic.
- For comparison, ignoring perspective (one 2D scale at the cat's depth) gives 150.5 × 0.003335 = 0.50 m. I
  rejected this because the chair stands about 12% closer to the camera than the cat.
- Other reading: the chair's front-to-back depth needs the focal length, which is poorly constrained. A rough
  estimate is ~0.3–0.45 m, so I did not use it. I answer with the left-right width across the chair's face.

Answer: 0.455 m. Confidence is moderate-high. The main uncertainties are whether the desk is exactly flush with the
wall (if not, the answer goes up a few %) and the leg contact rows (±1–2%).
