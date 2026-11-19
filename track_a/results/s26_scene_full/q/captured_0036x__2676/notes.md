# q2676 — ping pong ball velocity at 0.9 s (cm/s)

- t = 0.9 s -> frame 22 (question_fps = file fps = 24). Depths given: frame 22 Z = 1.010 m, frame 34 (1.4 s) Z = 0.716 m.
- Lab camera: f = 0.5959*1280 = 762.8 px, principal point (640, 360).
- Ball centres from scene/tracks/ball.csv (frames 13-35, rolling on table); frame 22 checked on a zoomed crop
  (centre about (567-570, 453-455), matches the track).
- Size check: 4 cm ball at 1.01 m -> 30.2 px predicted; measured about 28 px tall / 24-31 px at frames 21-23 (consistent).
- Script: vel.py. 3D points = unit ray x range (depth_info treated as camera-centre distance).
  - Route A: depth linear in time through the two given depths. Per-frame speeds near frame 22: 75-81 cm/s;
    centred +-2/+-3 frame differences 78.6/78.4; linear fit over 18-26: 78.3; quadratic over 17-27: 78.3 cm/s.
  - Route B: ground-plane depth model Z = k/(cy - v_h) fitted to the two given depths (v_h = 324.7, matching the
    table vanishing point at y ≈ 330 in the scene record). Noisier per frame; fits over 17-27 / 18-26 give 82.7-83 cm/s.
- Answer ≈ 80 cm/s (between the routes; components at frame 22 about 56 cm/s sideways, 55-61 cm/s toward the camera).
- Confidence: moderate-high (±5 %). Main uncertainty: the local rate of depth change at frame 22.
