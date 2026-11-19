# q_2523: tennis-ball velocity at 1.6 s (cm/s)

- t = 1.6 s → frame round(1.6 × 24) = 38. The file and the question both run at 24 fps.
- The tennis ball is the yellow ball. At frame 38 it is still rolling toward the camera on the table top; it leaves the edge around frames 42-43.
- Track: scene/tracks/yellow_ball.csv (circle fit to the top, left and right edges). I checked frame 38 on a zoomed crop (frames/f38.png). The ball spans x ≈ 714-765, so the diameter is ≈ 51 px, which agrees with the record's 50.8 px. I used frames 26-42 only, all on the table, before the fall.
- 3D geometry: f = 0.5959 × 1280 = 763 px, principal point (640, 360). I took the camera distance as dist(k) = 1.19 m × D(38)/D(k), anchored by depth_info at frame 38, with D the apparent diameter. Position = dist × the unit ray through (cx, cy).
- Route 1 (measure.py): I smoothed the diameter with a quadratic fit of 1/D over frames 26-42 (the raw diameter is too noisy to difference). From that:
  - mean of the forward differences over frames 36-40: 74.5 cm/s
  - central difference over ±2 frames: 73.8 cm/s
  - quadratic fit of the 3D position over frames 33-42: 74.0 cm/s
  - With the raw, unsmoothed diameter the values range from 68 to 78 cm/s.
- Route 2 (check2.py): I fitted polynomials of 1/D, cx and cy in time over several windows and took the analytic derivative at frame 38. The results were 69.4-78.5 cm/s, with a median of about 77.
- Answer: **75 cm/s**.
- Caveat: the size prior (6.7 cm) together with D = 50.1 px gives a camera distance of only about 1.04 m, against the given 1.19 m. The white ball shows the same kind of mismatch. If the sensor's depth were offset by a constant rather than proportional, the depth-rate part of the speed would be about 13 % lower, roughly 65 cm/s. I followed the lab method card and used the depth_info scale.
- Confidence: moderate, about ±8 %.
