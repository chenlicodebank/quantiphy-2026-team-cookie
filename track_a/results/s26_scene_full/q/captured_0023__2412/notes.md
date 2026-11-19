# q_2412: length of the slope (cm)

File fps = question_fps = 24, 1280x720. Lab camera: f = 0.5959*1280 = 762.8 px, principal point (640, 360).

## Method
- The slope is the white board leaning on the table. Far end = top edge, near end = bottom (foot) edge.
- Top edge measured on frame 46, where the book is off the ramp: the gradient of the vertical profile is at
  y = 356.5 (median over columns 530-650; the blurred edit blob at x 580-610 was ignored). Row extent x 516-660.
- Bottom edge measured on frame 5, before the book covers the foot: y = 482.5 (median over columns 520-650).
  Row extent x 494-676.
- Each edge midpoint is back-projected along its pixel ray to the depth_info distance (the distance is a ray
  length, not z): far 1.201 m, near 0.9555 m.
  - Top: (-0.082, -0.005, 1.198) m.
  - Bottom: (-0.068, 0.151, 0.941) m.
- Slope length = |P_top - P_bottom| = 0.3014 m. The incline is about 31 deg. Moving the edge by ±2 px changes
  the result by about ±0.2 cm.

## Checks
- If the board is rectangular, its width should be the same at both ends. Top: 144 px * 1.201 / f = 22.7 cm.
  Bottom: 182 px * 0.9555 / f = 22.8 cm. They agree, so the two given depths and the focal length are consistent
  with the edges I picked.
- Physics: g sin(31 deg) = 5.0 m/s^2 is above the prior book acceleration of 2.8 m/s^2. That is plausible with
  friction.

## Answer
30.1 cm. Confidence: good, about ±1.5 cm, mostly from where the depth points sit on the edges.
