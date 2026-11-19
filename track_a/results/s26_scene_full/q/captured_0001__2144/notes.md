# q_2144 – velocity of the ball at 1.5 s (cm/s)

File fps = question_fps = 24, t = 1.5 s -> frame 36. The ball rolls down the ramp, starting at about frame 28; at frame 36 it is
still on the ramp, and it reaches the bottom at about frame 38.

## Method (measure.py, fit2.py)
- Camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360).
- Ball centres come from scene/tracks/ball.csv (mask centroid). I checked them on zoomed crops of frames 35, 36 and 37,
  and they sit on the visible ball.
- 3D anchors: P0 = back-projection of frame 0 at depth 1.1075 m; P36 = back-projection of frame 36 at depth 0.912 m. On the ramp
  the ball moves in a straight line. For each frame I took the point on line P0–P36 that is closest to the pixel ray, which gives the
  arc length s(frame). The line is about 30 deg to the optical axis and about 4 cm off the ramp plane, which I got from the given
  slope-end depths (1.136 / 0.884 m). Both agree with a 3.2 cm ball radius. Ball diameter from frame 0: 44.7 px -> 6.5 cm.
- The per-frame speeds (cm/s) for frames 31 to 37 are 31, 49, 56, 75, 101, **216**, 123. The step from 35 to 36 is about twice
  what its neighbours suggest, so a frame was almost certainly dropped between 35 and 36.
  - If I fit constant acceleration to frames 29–37 with the times after frame 35 shifted by one frame, the RMS residual is
    0.17 cm and a = 3.3–3.4 m/s². This is close to the prior of 3.0 m/s².
  - With the naive timing the RMS residual is 0.83 cm and a ≈ 6 m/s², which contradicts the prior.
- Velocity at frame 36 from the dropped-frame fit: 123–125 cm/s (windows 29–37, 30–37, 31–37).

## Second route / checks
- Local speeds around frame 36: about 108 cm/s on each half of the doubled 35→36 step and 123 cm/s for 36→37.
  Their centred mean is about 116 cm/s. The forward difference used by the reference is 123 cm/s.
- Smoothed differences with the naive timing: (p38−p33)/5 → 120 cm/s and (p38−p34)/4 → 132 cm/s.
- Physics check: accelerating from rest at a = 3.0 m/s² from t0 ≈ 1.17 s gives about 112–125 cm/s at frame 36.
- Ramp travel check: the ball covers about 31.5 cm from frame 28 to frame 38. That needs a = 3.0 m/s² over 11 frame intervals
  (with the dropped frame), compared with 3.6 m/s² over 10.

Answer: **123 cm/s**. The routes give 112–132 cm/s. Confidence is moderate: the main uncertainty is how the reference treated
the dropped frame.
