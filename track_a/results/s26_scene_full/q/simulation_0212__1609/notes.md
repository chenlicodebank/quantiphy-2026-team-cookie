# q_1609: height of the table lamp's lampshade (m)

Answer: **0.246 m**

The video is a 3D Blender render, 1920x1080. The file rate and question_fps are both 24 fps, and the camera is static.
The lamp does not move, so all lamp measurements come from frame 48, where it is not hidden.

## Focal length (two routes)
1. **Cat** (`focal.py`). I used the prior speed of 0.94 m/s (0.94 m in 1 s) and the given depths, 4.199 m at frame 0
   and 4.481 m at frame 24. I back-projected the cat's torso-core centroid, (408.5, 842.7) at frame 0 and (869.4, 805.3)
   at frame 24, and solved for the focal length that makes the 3D displacement 0.94 m. Result: f = 2156 px (2143–2168
   when I move the frame-24 point by a few pixels).
2. **Room vanishing points** (`lines.py`). I fitted the two wall–floor lines (back wall y = 909.0 − 0.0751x, right
   wall y = 562.5 + 0.1294x) and took the horizon at y = 540. If the two walls are perpendicular, f = 2117 px.
   I used f = 2136 px; the two routes differ by 2 %.

The camera is level. Treating the cat's feet at frames 0 and 24 and the mirror's bottom centre (1515, 812, at the
given 6.407 m) as floor points gives the same camera height, 0.78 m, each time.

## Depth of the lamp
- The table top is only about 6 px tall in the image (rows 656 to 662). The lamp base's front contact is at row
  661.5, the front edge of the top, and the vase stands at the back edge (row 655). From those rows the top is about
  0.29 m deep. That fits the leg footprint (front and rear legs about 0.34 m apart on the floor).
- The given distance to the closest bench leg is 5.69 m. For the front-left leg (bottom at (1406, 839), top at (1432,
  690)) this gives z = 5.534 m. The floor-row route, using the camera height from the mirror, gives 5.599 m.
- Lamp axis depth = front edge (about 2 cm in front of the leg) + base radius (0.05 m) ≈ 5.64 m, give or take 0.07.

## Lampshade
- Measured in code (`shade.py`, `shade2.py`): the top silhouette is at row 398.3, and the lowest shade pixels are
  at row 495.3. The axis is at x = 1369.5. Half-widths are 28.5 px at the top and 96.5 px at the bottom, so the
  radii are 0.075 m and 0.255 m.
- The shade sits above eye level (its bottom rim is about 0.12 m above the camera), so the camera sees the dark
  inside through the bottom opening. The far side of the bottom rim is the lowest point in the image, and the near
  side shows about 4 px higher (rows 491–492). The rim model predicts that 4 px gap, which supports this reading.
- `final.py` projects the full rim circles and solves for the heights of the top and bottom rims. Result: H = 0.244
  to 0.249 m across f = 2117 to 2156 and the two leg-depth routes. The central value is 0.246 m.
- Sensitivity: each 0.1 m of lamp depth changes H by about 0.0044 m (1.8 %).
- A naive check, 97 px × 5.64 / 2136, gives 0.256 m. It ignores that the top and bottom silhouettes come from rim
  points at different depths, which is why it reads about 4 % high.

## Corrections to the scene record
- The record gives the vase bottom at y = 634. It is actually at about y = 655.
- The shade extent in the record (y 398 to 497) is about right; the precise rows are 398.3 to 495.3.

## Confidence
Moderate to good, about ±4 %. The main uncertainty is the lamp's depth (front-edge position, ±0.07 m) and f (±1 %).
