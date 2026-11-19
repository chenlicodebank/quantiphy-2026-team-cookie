# q1565 – speed of magnifying glass at t=0.333 s (frame 8 at 24 fps; file fps = question fps = 24)

Method: used the scene/ track (bbox centre, f0-f10 free fall, crisp ±1-2 px; the values look consistent).
Fitted a 3D pinhole free-fall model (fit.py): start point = back-projection of the f0 pixel with the given depth 4.2401 m,
principal point at the image centre; unknowns: focal f, camera pitch, release time t0, small horizontal velocity;
acceleration fixed to the prior g = 9.8 m/s^2 along world vertical.
Result: f = 2619 px, pitch 17.0 deg, t0 = -0.007 s (released at ~frame 0), rms 0.33 px.
Check: model depth at frame 12 (t=0.5, glass on desk) = 4.430 m vs given 4.4097 m (0.5 pct).
Speed (backward difference |p8-p7| x 24) = 3.072 m/s.
Second route: ideal release from rest at frame 0 -> v = g x 7.5/24 = 3.0625 m/s; the pixel drops
(6, 17, 28, 39, ...) show the first drop ≈ half the per-frame increment, which confirms release at f0.
Answer 3.07 m/s. Confidence high (about ±2 pct).
