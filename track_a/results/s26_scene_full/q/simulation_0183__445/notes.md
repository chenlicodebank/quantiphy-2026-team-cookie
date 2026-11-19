# q445 – height of the box (tool box / crate), simulation_0183

2D video, 24 fps (file fps = question_fps, no re-timing).

Scale from prior (acceleration 1.58 m/s^2 at t = 1.25 s, frame 30, steady slide on the ramp):
- Pixel acceleration along the slide path from scene/tracks/crate.csv (template fit, checked against frames):
  linear fit of per-frame speed, frames 22–44: 390; 24–44: 403; 26–40: 407; quadratic fit of arc length,
  frames 22–44 / 24–44: 401 / 400 px/s^2. I used 400 px/s^2.
- Scale = 1.58 / 400 = 0.00395 m/px.

Box height: frame 0, where the box is axis-aligned against the wall. Background differencing against frame 30
gives rows 236–425 = 190 px (the scene record has 190 px too; read by eye on the grid it is about 237–424).
Height = 190 x 0.00395 = 0.750 m.

Second route: the free fall in frames 0–7 gives 2491 px/s^2, and 2491 x 0.00395 = 9.84 m/s^2, which is about g.
The scale from gravity alone (9.81/2491 = 0.003938 m/px) gives 0.748 m. The two routes agree.
A small part of the 190 px may be the top lid seen from slightly above (about 3 px), which would give about 0.74 m.

Answer: 0.75 m. Confidence: high (within about 3%).
