# Q1205 — distance between the left pillar of the near door and the right pillar of the far door

Answer: **3.56 m**. File fps = question fps = 33, so there was no time-base issue.

## Objects
- Near door = the arched wooden door of the grey stone building (right side of the frame, nearer the camera,
  because the street recedes to the left). Its left pillar = the stone post with a ball finial at x 1490-1545,
  y 387 (ball top) to 656.5 (base). A stone pilaster at x 1510-1560 stands behind it.
- Far door = the brown door of the green house. Its right pillar = the white pilaster at x 1086-1121
  (capital top y 236). The other reading is the stoop's right newel post on its stone pedestal
  (x 1021-1066, y 440-649).

## Camera (scripts: vp.py, lsd.py, vp2.py, vvp.py, model*.py, wheel*.py)
- Street vanishing point from 91 LSD facade and ground lines: (-2707, 571). Vertical vanishing point from
  132 vertical segments: (640, -24288). Perpendicular vanishing point from the phone booth's side face and
  the sign alcove: about (1790, 495).
- With the principal point at the image centre, these give f ≈ 1740-1860 px. The cyclist moves parallel to
  the street at f ≈ 1890. The bike-wheel ellipse aspect (0.90) needs f ≈ 1650-1860.
- f = 3010 is impossible: it is what the prior gives if the pedestrian's given depths are used. At that f the
  booth faces could not be orthogonal (the bound is f ≤ 2250), and the predicted wheel aspect would be 0.77.
- Final value: f = 1840 (range 1800-1880).

## Scale
- Camera height from the bike's depth_info at t = 1 s and t = 2 s: 1.09 m above the road. The two times
  agree within 1%.
- The curb face is 0.12 m tall, so the sidewalk plane sits 0.966 m below the camera.
- Check against the prior: the pedestrian's feet on the sidewalk plane give a walking speed of 1.225 m/s,
  against the prior of 1.236 (1% off). So the bike depths and the speed prior give the same scale.
- The pedestrian's own depth_info (15.87 / 16.67 m) does not fit his body. His feet are at about 12.9 m, and
  using his depths would also make him walk at 1.69 m/s. His origin seems to be offset from his body, so his
  depths were not used.
- The final distances were rescaled so that the pedestrian speed equals 1.236 exactly. After that they do
  not depend on f (3.459-3.461 for f = 1800-1880).

## Geometry (answer.py, rail.py, cheek3d.py, stairs.py)
- The post bases and the stoop pedestal sit on the sidewalk's back line, about 12.8-13.15 m out
  (perpendicular distance from the camera).
- Facade plane: about 14.05 m out. Two routes give this: the end of the right stair rail (13.97-14.06) and the
  back edge of the cheek face (14.14). Both stoops have 5 risers of 0.17 m; the rail slope of 35° gives a run
  of about 0.24 m.
- Origins are taken as box centres.

## Distances under each reading (rescaled to the speed prior)
- post to green right pilaster: 3.62 m (pilaster running to the ground) / 3.73 m (to the landing).
  Moving the facade by ±0.25 m changes this by about ±0.15 m.
- post to green right newel and pedestal: 3.46 m.
- arched left pilaster to green right pilaster: 3.49 m.
- 3.56 m is chosen because it lies within 5% of every reading.

## Confidence
Moderate. The scale is well supported: the bike depths and the speed prior agree within 1%. The largest
uncertainty is which object counts as a "pillar" (about ±4%), followed by the facade depth.
