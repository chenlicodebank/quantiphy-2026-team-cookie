# Q2048 – average velocity of the ball flying across the net (m/s)

- Static camera (record: phase-correlation shift <= 0.7 px), near-nadir view, so the planar annotator convention applies.
- Ball crossing the net = outgoing shot after the right player's hit, frames 40-91 (scene/tracks/ball.csv). I checked frame 60 on
  a zoomed crop: the streak centre is about (1587, 2333), and the track gives (1587.8, 2326.5). They agree.
- Scale: singles width measured in code (`measure.py`, frame 100, white-line centroids of both singles sidelines at 13 rows):
  1341 px (y=1000) to 1366 px (y=3600). Perspective makes it about 2% wider at the bottom. Mean 1351 px, so 8.23/1351 = 0.00609 m/px.
- Speed: per-frame displacement of the ball centroid is 41-59 px (median ~51). Mean over frames 40-91 = 50.1 px/frame.
- fps: the file runs at 59.83 fps and the question states 60. The difference is 0.3%, which has no practical effect.
- Result: mean of per-frame speeds = 18.3-18.5 m/s (depending on the width reading and the fps). The net displacement over time
  gives the same value (straight path).
- Second route: frames 60-80 around the net crossing (net at y~2870) give 51.9 px/frame, or 19.0 m/s. A linear fit over the
  whole flight gives 18.8 m/s. The ball slows slightly late in the flight.
- Answer 18.4 m/s (about 66 km/h, plausible for a rally shot). Confidence: good, about ±4%.
