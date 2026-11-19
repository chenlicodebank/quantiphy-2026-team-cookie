# Q645: speed of the small robot at t = 1 s (frame 24). Prior: big robot (tank) speed = 5.924 m/s

fps = question_fps = 24, so no re-timing.

## Measurements
- Small robot (body axis, the cup under the dome, from scene/tracks): steady leftward motion. Linear fit
  -8.40 px/frame over the whole clip and -8.43 over frames 14-34. The backward difference at frame 24 is 8.3 px.
  Per-frame differences scatter by about ±0.5 px with the gait. I use 8.4 px/frame.
- Tank: rigid parts tracked with NCC from frame 12 (`tank_parts.py`). The near-side track frame and rear plate move
  at 50.75 px/frame (residual 0.1-0.9 px). The body cylinder moves at 51.8 and the drill arm or tip at about 54;
  the arm is animated. Track bottom: y = 894 in every frame.
- Perspective: the camera is level. The wall pillars are vertical, and the floor lane markings perpendicular to the
  wall meet at about (955, 535), so the horizon is y_h ≈ 538. The robot is nearer than the tank: its feet reach
  y ≈ 972, and its centre's ground point is about y ≈ 965. The tank's near track touches the ground at y = 894.
  On a ground plane, Z ∝ 1/(y - y_h), so Z_robot / Z_tank-near-side = 356/427 = 0.834 (range 0.82-0.85).

## Answer
v = 5.924 × (8.4 / 50.75) × 0.834 = 0.818 m/s, which I round to **0.82 m/s**.

Second route and sensitivity: using the body cylinder (51.8 px/frame) as the tank reference instead gives 0.80.
Moving the horizon by ±20 px changes the result by about ±1%. Without the depth correction, a single 2D scale would
give 0.96-0.98. I did not use that, because the robot is clearly nearer the camera than the tank.

Confidence: moderate, about ±5%. The main uncertainty is the robot's ground-contact depth.
