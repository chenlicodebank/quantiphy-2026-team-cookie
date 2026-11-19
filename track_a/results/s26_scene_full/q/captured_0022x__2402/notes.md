# q_2402 – velocity of ping pong ball at t=1.2 s (frame 29 at 24 fps; file fps also 24)

Method (scripts m1.py, m2.py):
- Camera: f = 0.5959*1280 = 763 px, principal point (640,360).
- Ball centre track from scene/tracks/ball.csv (checked it is the white ball rolling toward the camera; frames 12–45 rolling on table).
  Both cx/cy and cx_box/cy_box were used.
- Back-projected centres at the three depth_info frames (14, 19, 29) with the given depths. The three 3D points are collinear
  to 5 mm, so the ball rolls on a straight 3D line. Fitted that line, and for every frame took the 3D point on the line closest
  to the pixel's camera ray (this gives a depth per frame; it reproduces the given depths to within 5 mm: 1.756/1.680/1.528 vs 1.751/1.687/1.526).
- Speed = |ΔP| * 24 per frame.

Results at frame 29:
- Forward-difference speeds averaged over 5 frames (27–31): 46.9 cm/s (cx), 47.4 cm/s (box centre).
- Quadratic fit of position along the line over windows 20–35, 22–35, 24–34, then derivative at frame 29: 44.1–44.6 cm/s.
- Second route, using the given depths only: the 3D distance between the back-projected points at f19 and f29 is 0.182 m over 10 frames,
  so the mean is 43.8 cm/s (centred at f24). With the small measured acceleration (~0.1–0.2 m/s^2), that gives about 45–46 cm/s at f29.
- Note: the 35→36 step is double length (a dropped capture frame). It lies outside the window that was used.

Answer: 45.5 cm/s (spread across the routes is 44–47). Confidence: moderate-good (±5%).
