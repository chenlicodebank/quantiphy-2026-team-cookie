# q_3185 – ball velocity at 2.50 s (frame 75, 30 fps; file fps = question fps)

Prior: g = 9.8 m/s^2. Scale from the ball's pixel vertical acceleration (2D, one scale).

## Measurements (scene/tracks/ball.csv, camera-compensated cx_bg/cy_bg; frame 75 centre checked on a zoomed frame: ~(547,100) raw, matches)
- Parabola fit of cy_bg over frames 66-97 (truncated frames 77-80 excluded): a_y = 5.51 px/frame^2 = 4956 px/s^2
  -> scale = 9.8/4956 = 1.977e-3 m/px. (Raw, uncompensated cy: 5.48 px/f^2 — agrees.)
  Local windows: 5.92 (66-76), 5.65 (66-90), 5.27 (81-97); the ball shrinks slightly (~125 -> 121 px), a mild
  perspective/recession effect, and vx falls 50 -> 45 px/f. Annotator convention = one global scale, so the global fit is used.
- Speed at frame 75: forward difference |p76 - p75| = 52.3 px/frame; local quadratic fit at 75 gives
  (vx, vy) = (48.4, -22.3) -> 53.3 px/f; global fit (46.7, -22.3) -> 51.8 px/f.
- v = 52.3 px/f x 30 x 1.977e-3 = 3.10 m/s; fit routes give 3.07-3.16 m/s; with the local a_y (5.76) 2.97-3.03 m/s.

## Answer
3.08 m/s (range of routes 2.97-3.16). Confidence: moderate-high (~5%).
