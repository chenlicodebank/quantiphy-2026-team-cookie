# q_2453 – distance travelled by the book (cm)

File fps = question_fps = 24, so no time-base issue. Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).

## Method (geo2.py, geo3.py, path.py)
- Track: scene/tracks/teal_book.csv (full-mask centroid). I checked it against frames 0 and 48. The book rests on the ramp
  for frames 0-18, slides down the ramp for frames 19-29, slides on the table for frames 29-36, and is at rest from frame 36 on.
- Ramp phase: I back-projected the book centre at frame 24 (depth 1.0685 m) and at frame 29 (depth 0.977 m). The 3D line
  through these two points is the slide line, 15.9 cm between them. For every ramp frame I took the point on this line
  closest to the pixel ray, which gives a depth of 1.116 m at the start.
- Table normal: from the table-edge vanishing points (183,333) and (1527,428), which meet at 80 deg. The slope angle of
  the slide line is 28.4 deg. The given slope near/far depths, back-projected at the ramp edge midpoints, give 27.4 deg,
  which agrees.
- Table phase: the book leaves the ramp moving in the horizontal component of the slide direction. That direction is
  86 deg from the ramp's bottom edge, so the book slides off almost straight. I intersected the pixel rays with the
  vertical plane through the frame-29 point. Rest depth is 0.889 m and the rest height is -0.134 m relative to the camera.
  The table surface is at about -0.150 m (the slope_near point is at -0.144 and table_left at -0.155), so the rest height
  is the table plus half the book's thickness (about 1.6 cm), which is consistent.
- The table plane on its own was too badly conditioned to give depths (the camera is only about 15 cm above the table
  top), so I used the vertical-plane intersection instead.
- An independent ramp model built from the slope_far/near depths does not reproduce the book depths (it gives 1.135
  instead of 1.0685), so I did not use it. The given book depths set the scale.

## Results (path length = sum of frame-to-frame 3D displacements)
| track | z-depth convention (method card) | Euclidean ray |
|---|---|---|
| full mask | 39.5 cm (ramp 23.8 + table 15.7) | 38.6 cm |
| cover only (2nd route) | 39.3 cm (with 5-frame smoothing) / 40.3 cm (raw) | 38.4 / 39.4 cm |

The net displacement is 38.9 cm. Check against the prior: on the ramp the speed rises at about 2.2-2.8 m/s^2
(frames 20-23: 2.8 m/s^2). This roughly agrees with the prior of 2.8 m/s^2.

Answer: **39.4 cm**. Confidence: moderate-good. The main uncertainty is the depth at the start and at rest, which is
extrapolated from the two given depths (about ±5%).
