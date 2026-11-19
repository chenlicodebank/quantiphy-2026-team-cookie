# Q361 – length of the turtle (m); prior: turtle acceleration = 2.639 m/s^2

2D side-view scene, static camera, 24 fps (file fps = question_fps, so no re-timing).

## Scale from the prior (fit.py)
- Carapace track `shell_x` from scene/tracks/turtle.csv (template matching, match 0.90-0.99). The per-frame dx grows
  linearly, i.e. constant acceleration starting from rest.
- Linear fit of dx vs frame: slope -0.924 px/frame^2 over frames 1-47 -> 532 px/s^2; 1-24: 529; 24-47: 536;
  10-40: 536. Quadratic fit of x(t): 534 px/s^2. Taken as a_px = 533 px/s^2 (spread ±0.7 %).
- Scale = 2.639 / 533 = 0.00495 m/px.

## Pixel length
- Full-mask bbox x extent in the near-rest pose, frames 39-46: 283-310 px, mostly ~305 (frames 44-46: 305-306);
  frames 21-36: 305-326 px (flippers swing). I checked crops of frames 24, 36, 42 and 45: the far-side front flipper
  reaches ~30 px ahead of the head, and the rear flipper tip is the back end.
- Head plus shell to the rear flipper tip without the forward flipper: ~275-290 px.
- I used the world-AABB reading (all mesh parts, rest-like pose) = 305 px.

## Answer
305 px x 0.00495 m/px = 1.51 m.
Other readings: body only (~283 px) -> 1.40 m; stroke-pose bbox (~318 px) -> 1.57 m.
Second route: the acceleration measured over the two half-windows separately (529 and 536 px/s^2) changes the
result by less than 1 %. The main uncertainty is which pose and extent define "length" (±7 %).
