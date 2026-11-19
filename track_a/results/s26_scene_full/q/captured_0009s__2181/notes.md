# q_2181 — basketball's initial distance from the floor (cm)

File fps = question_fps = 24. Intrinsics: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
Scripts: recon.py (3D track), height.py (height routes). Ball track: scene/tracks/basketball.csv (circle fit; checked against the record's overlays).

## Geometry
- Ball centre at t=0: pixel (483.1, 186.8), back-projected at 1.321 m gives P0 = (-0.260, -0.287, 1.263) m.
- Ball diameter: depth / (pixel-diameter distance) gives 0.225 m (frame 0), 0.215 m (frame 43) and 0.222 m (frame 46), mean 0.221 m. Per-frame depth = R_per_D x 0.221.
- The camera is pitched down by about 28°. The fall from P0 to the bounce centre (frame 37) has camera-frame components dy = 0.98 m and dz = 0.53 m, with almost no x. I used that fall direction as the vertical.
- distance_floor_camera = 2.0285 m is consistent with the floor point under the ball, which is also where it bounces. The bounce contact point estimated from the ball diameter lies about 1.98 m from the camera.

## Routes
1. Walk down the vertical from P0 until the camera distance is 2.0285 m: h = 1.230 / 1.242 / 1.291 m, taking the vertical from bounce frame 36 / 37 / 38.
2. Floor contact Q = ray through the ball-bottom pixel at frame 37, at 2.0285 m. Height = (Q - P0) · vertical = 1.249–1.256 m.
3. Check from the diameter-based depth alone: drop to the bounce centre is 1.117 m, plus radius 0.11 m, giving 1.23 m.
4. Free-fall check with g = 9.8: release at frame 26 and bounce at frame 37–37.5 give 1.14–1.24 m. This is consistent, but the release frame is uncertain by ±1 frame.

## Answer
Height of the ball centre above the floor ≈ 1.245 m = 124.5 cm. If "distance" meant the ball's bottom surface, the value would be about 113.5 cm, but I answer with the centre, following the dataset convention.
Confidence: moderate, about ±5%.
