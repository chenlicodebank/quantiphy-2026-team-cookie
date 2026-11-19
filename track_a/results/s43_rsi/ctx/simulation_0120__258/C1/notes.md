# Q258 — length of the TV (m). Prior: robot cleaner speed = 1 m/s

## Scale from the prior
Vacuum track (scene/tracks/robot_vacuum.csv, checked): straight line, linear fit slope 8.410 px/frame (mean step 8.415),
x 24.0078 fps (file rate; question_fps 24.0 differs by only 0.03 %) = 201.9 px/s, so 201.9 px/m in the vacuum's plane (floor level).
Vacuum diameter 68.8 px / 201.9 = 0.34 m, a realistic size, which supports this scale.

## TV
This is the black panel on the left wall (clock image with "12" and "3"), at x 147–216 and y 387–795 px in frame 0. It is a vertical
face seen at a steep angle from the top-down camera. It shows as a strong trapezoid: the upper edge (x = 147.5) spans 409 px and the
lower edge (x = 215.5) spans 338 px. Its side edges run along radial lines from the image centre (slopes 0.382/0.390 and
-0.647/-0.650). So the principal point is at (540, 540), and **one 2D scale would be wrong here**: 409/201.9 = 2.03 m and
338/201.9 = 1.67 m disagree.
For a vertical plane at horizontal distance X from the camera nadir, the y-extent divided by the x-offset (540 - x) equals ΔY / X.
Measured in code (trap.py), this ratio is 1.045 ± 0.002 in every column from 148 to 214.

## Finding X (edges.py, fire.py)
- The low white plinth in front of the wall (it holds the linear fireplace and the plush toy) has its front face from x = 285 (top
  edge) to x = 295.8 (floor). That puts the floor-level front at X = 244.2 / 201.9 = 1.210 m, and the plinth-top scale at
  255 / 1.210 = 210.8 px/m.
- The marble TV wall meets the plinth top at x = 219 (offset 321), so the wall is at X_w = 321 / 210.8 = 1.522 m.
  Check: at the plinth-top scale, the fireplace frame (340 px, no trapezoid, so horizontal) is 1.61 m long, matching the TV width.
- The TV stands off the wall. A grey strip at x 138–151 is the top of the panel and its back box, so the face is about 2–5 cm in
  front of the wall: X_wall / X_face = 1.035 at most (402 / 388.5). I used the midpoint: X_face ≈ 1.485 m.
- The tracked vacuum feature is the top of the vacuum, which sits a few cm above the floor, so the floor scale is about 1 % lower:
  +1 % on the result.

## Result
L = 1.045 × 1.485 × 1.01 ≈ **1.57 m**. Without the stand-off from the wall it would be 1.61 m; with the full 5 cm, 1.55 m.
Second-route check: assuming a 16:9 screen, the trapezoid gives a focal length of about 1100–1160 px (horizontal FOV about 50°),
a camera height of about 5.6 m, a plinth height of about 0.23 m and a TV bottom about 0.5 m above the floor. All of these are
plausible, and the matching 1.6 m fireplace below the TV agrees.
Confidence: moderate (±5 %). The main uncertainty is the wall junction and plinth edge pixels (±1 px each, about 1 %) and how far
the TV stands off the wall (±2 %).
