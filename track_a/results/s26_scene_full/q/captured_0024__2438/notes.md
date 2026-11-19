# q_2438 — height of the book (cm)

The "book" is the light-blue notebook that slides down the white board (the only moving object). It lies flat
throughout, so I read **height as its vertical extent, i.e. its thickness**, following the benchmark convention
(height = vertical extent). File fps = question_fps = 24, so the frame numbers are the same under both.
(Other reading: the cover's long side ("height" as in book format) would be roughly 18-20 cm. I did not use it.)

## Camera / scale
f = 0.5959 x 1280 = 762.8 px, principal point (640, 360). The wall-panel seams are almost vertical
(seams.py), so pitch is about 1 deg and roll about 1-2 deg. I treat the camera as level.

## Checking the depth geometry (ramp_plane.py, accel_check.py)
- I back-projected the book centres at f24 (750.6, 397.3) and f29 (670.3, 451.9) with the given depths 1.0685 m and
  0.977 m. This gives the downhill direction (-0.73, 0.41, -0.55), an incline of about 24 deg.
- I built a ramp plane from this line, offset by T/2. It reproduces the given slope distances: the top-left corner
  of the board comes out at 1.241-1.244 m (given 1.243). The lower-left corner comes out at 1.016 m (given 0.99).
- The board's lower edge lies at camera Y = 0.142-0.146 m. The table-left point gives Y = 0.138 at x = -0.29, which
  is consistent with a small roll. Table plane under the final book position: h = 0.146 +- 0.004 m below the
  camera.
- Acceleration along the 3D ramp line, quadratic fit over f20-29: 1.7-1.8 m/s^2. Assuming the book starts from rest
  at f19 instead gives 2.8 m/s^2, which matches the prior. The track is noisy here, so this only roughly confirms the
  scale.

## Route 1 (main): book at rest on the table, frame 48 (thick.py, darklines.py)
For a vertical face at depth Z, its pixel height is dv = f T / Z and its bottom edge is at v_b - cy = f h / Z.
So T = h x dv / (v_b - cy), which does not depend on the depth.
- Top-face edge to bottom edge, median over x 520-600: dv = 14.2 px (13.4 px if measured from the cover-edge dark
  lines, centre to centre 11.9 px + 1.5 px; 15 px if the contact line is included).
- v_b is about 497.
- Ratio dv / (v_b - cy) = 0.098-0.109, central value 0.103. T = 0.146 x 0.103 = 1.50 cm (range 1.43-1.59).

## Route 2: book at rest on the ramp, frame 0 (route2.py)
- I placed the book on the same 3D ramp line where it projects to the f0 centroid. That gives a distance of
  1.12 m.
- The thickness lies along the ramp normal. Projected, 1.6 cm would appear as a vertical offset of about 9.9 px.
- Measured: dark-line spacing 7.5 px, so about 8.6-8.8 px of thickness. That gives T = 1.37-1.42 cm. The front face
  is a little nearer than the centroid, which pushes the value slightly lower.

The two routes agree to within about 7%. Answer **1.5 cm**. Confidence: moderate about the value (+-8%). The main
risk is the meaning of "height": if it means the long side of the cover, this answer is wrong.
