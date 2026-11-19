# Q2668 - ping pong ball displacement 0.9 s -> 1.4 s (cm)

- question_fps = file fps = 24. t=0.9 -> frame 22, t=1.4 -> frame 34 (ball rolling on the table, before the edge at frame 36).
- Ball centres (scene/tracks/ball.csv, white edges + contact-shadow method; checked on zoomed crops frames/f09.png, f14.png):
  frame 22 (569.0, 457.0), frame 34 (838.0, 513.0) px.
- Camera: f = 0.5959*1280 = 762.75 px, principal point (640,360). depth_info treated as Euclidean distance along the ray:
  1.010 m (frame 22), 0.716 m (frame 34).
- Back-projected 3D displacement: **41.6 cm** (3-frame smoothed centres: 41.6; treating depth as z instead: 40.6).
- Checks: prior size reproduced - vertical diameter 31 px x 1.010/f = 4.10 cm, 45 px x 0.716/f = 4.22 cm (prior 4 cm).
  Second route with depths from the 4 cm prior (0.984 m, 0.678 m): displacement 41.7 cm. Routes agree within 0.3%.
- Confidence: high (~ +-3%).
