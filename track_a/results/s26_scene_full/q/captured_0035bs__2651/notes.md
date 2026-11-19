# q_2651 — basketball velocity at t = 1.4 s (cm/s)

- question_fps = file fps = 24; t = 1.4 s -> frame 34 (round(33.6)).
- depth_info has two "soccer_ball" entries at 1.4 s (typo). 2.6020 m is the basketball: the basketball's apparent
  diameter grows from 61.6 px (frame 22, given 2.7777 m) to 65.1 px (frame 34); 2.7777 x 61.6/65.1 = 2.62 m. Both anchors
  imply the same true diameter (22.29 / 22.30 cm with f = 763 px, vs ruler prior 23.2 cm): consistent.
- Centres from scene/tracks/basketball.csv (RANSAC circle fits); frame 34 checked visually (centre ~ (528, 463), diameter ~65 px).
- 3D centre = back-projection with f = 0.5959 x 1280 = 762.8 px, principal point (640, 360), depth per frame either
  (a) linear interpolation between the two given depths or (b) from apparent size scaled to the anchors (vel.py).
- Per-frame speeds around frame 34 (both depth models): ~105-112 cm/s (frames 29-35, 36-40), i.e. physical ≈ 110 cm/s.
- Frame 35->36 is a doubled step (dropped source frame, see scene notes): 207 cm/s for that one step. Any smoothing
  window centred on/forward from frame 34 includes it: 5-frame windows give 123-133 cm/s (fit ±2: 128, ±3: 125, ±4: 122).
  Backward/clean windows give 108-113.
- Answer 117 cm/s: between the clean physical speed (~110) and the smoothed-through-dropped-frame value (~125),
  within ~7 % of either reading. Confidence moderate (convention ambiguity dominates; measurement itself ±3 %).
