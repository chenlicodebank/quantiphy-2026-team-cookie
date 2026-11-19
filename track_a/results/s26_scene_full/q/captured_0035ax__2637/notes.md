# q2637 – soccer ball velocity at t=1.6 s (cm/s)

t=1.6 s -> frame 38 (question_fps 24 = file fps). The ball is rolling away from the camera after bouncing off the basketball (frames 21-47).
Camera: f = 0.5959*1280 = 763 px, principal point (640,360).

depth_info: the second "t=1.6s soccer_ball 2.412 m" entry is taken to be the basketball (it matches the basketball's
size: 2.412*69.0/763 = 21.8 cm, and 2.27*74.1/763 = 22.1 cm at t=0.6). Soccer ball at frame 38: 3.052 m.

## Depth per frame (only one soccer depth near t=1.6)
Route A (floor plane, plane.py): back-projected the four given centres (soccer f14 and f38, basketball f14 and f38). I took them
down by the ball radii (soccer 8.75 cm from its size, 17.5 cm diameter; basketball 11.6 cm) and fitted the floor plane. Results:
camera 1.72 m above the floor, tilted 33° down, residuals ≤1 cm. Soccer-ball depth per frame = ray / plane intersection at height r.
Check: the diameter this implies from the pixel sizes stays at 17.2-17.9 cm over frames 24-46 (consistent).
Route B (apparent size, vel.py): distance ∝ 1/diam, anchored to 3.052 m at f38, with a linear fit of 1/d over frames 24-47.

## Velocity (3D centre, forward differences)
- Plane: mean of forward differences over frames 36-40 = 61.9 cm/s. Linear fit over 36-41 / 36-44 / 36-47 gives 62.4 / 63.9 / 64.3.
  Over the pre-jump frames 29-35 the fit gives 64.9.
- Size (linear 1/d): forward differences over 36-40 = 64.6 cm/s, and 64.5 from the 36-41 displacement. The quadratic 1/d fit gives about 57,
  which is less stable.
- The lateral (image-plane) part alone is about 41 cm/s. The depth part makes up the rest.
- The scene record notes a probable dropped frame at 35->36, where the step doubles. Windows that include it give about 68-72. I excluded it.

Answer: 63.5 cm/s. Confidence: moderate (±7%). The main uncertainty is the depth rate.
