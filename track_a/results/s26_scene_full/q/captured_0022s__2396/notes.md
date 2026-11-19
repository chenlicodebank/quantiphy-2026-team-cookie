# q_2396 – velocity of ping pong ball at t = 1.2 s (cm/s)

Lab video, 24 fps (file and question fps equal); t = 1.2 s -> frame 29. f = 0.5959*1280 = 763 px, c = (640,360).
depth_info (Euclidean distance): f14 1.751 m, f19 1.687 m, f29 1.526 m.

## Measurements
- Ball centre track from scene/tracks/ball.csv (x_ref,y_ref; core x-mid, top+r). Checked on zoomed frame 29:
  ball at ~(422,455), apparent diameter ~21 px vs 763*0.04/1.526 = 20.0 px expected (consistent with prior).
  My own circle fit (measure.py) agrees for frames 18-29 but breaks after f30 (mask merges), so the record was used.
- 3D points from depth_info: P14, P19, P29 lie on a line within 1-4 mm (rolling on the flat board).

## Routes (measure.py, route2.py)
1. Back-project every frame with interpolated depth, local fit / 5-frame forward-difference mean at f29:
   linear depth (f19-f29) -> 44.8 cm/s; quadratic depth through 3 points -> 49.4-50 cm/s.
2. 3D line of motion from the three depth points; per-frame position along the line from image rays only
   (ray-line closest point, gaps <3 mm); speed at f29: local fits 43.8-45.6, mean fwd-diff 27-31 43.6,
   global quadratic (f14-35) 43.6 cm/s, acceleration only ~6 cm/s^2.
3. Chord check: |P29-P19| / (10/24 s) = 43.7 cm/s (mean over f19-29).
The quadratic-depth route assumes large acceleration that the image motion does not show; routes 2/3 agree.

Answer: ~45 cm/s. Confidence moderate (depth-rate dominated; plausible range 43-50).
Frame 35->36 has an irregular big step (possible capture glitch); not used.
