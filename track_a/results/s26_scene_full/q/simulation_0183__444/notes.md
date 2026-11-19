# q_444 – length of the box (tool box / crate), simulation_0183

Prior: acceleration of the tool box after 1.25 s = 1.58 m/s^2. 2D video, static camera, fps 24 (= question_fps).

## Method (measure.py)
- Scale from the prior: the crate slides down the ramp at constant acceleration over frames 22-44 (t = 0.92-1.83 s,
  includes t = 1.25 s = frame 30). Quadratic fit of the along-slope position (28.4 deg direction):
  - scene/ track: 401.5 (22-44), 405.9 (24-40), 401.9 (26-36) px/s^2, residual rms 0.2-0.3 px
  - my own translation-only template tracks (refs at frames 26/30/36): 404-411 px/s^2
  - adopted a_px = 405 px/s^2 -> scale = 1.58 / 405 = 0.00390 m/px
- Length: at frame 0 the crate is axis-aligned against the wall; background-difference mask gives horizontal
  extent 337 px (333-339 depending on threshold; scene record 335). Height 191 px.
- Length = 337 x 0.00390 = 1.315 m.

## Second route
Free fall frames 0-7: pixel acceleration 2491 px/s^2. Taking Blender gravity 9.81 m/s^2 gives 0.00394 m/px ->
length 1.327 m. Agrees with the prior route within 1 %.

## Answer
1.32 m (box length = its long horizontal extent, seen face-on at frame 0). Confidence: high (~3 %).
