# Q761: length (horizontal width) of the white backboard. Prior: ball diameter = 0.282 m

fps 24 = question_fps, so no retiming issue (static-size question anyway).

## Measurements (frame 0; scripts m1-m4.py)
- Backboard: the left and right edges sit at x = 794.5 / 1152.5 (max gradient) in every row from y 80 to 150, so the edges are
  vertical (no keystone). **Width = 358 px**, which confirms the scene record.
- Ball: circle-fit diameter **74.66 px** (mean over frames 0-15, no motion blur; 74.75 over all frames). This matches the record.
- Single 2D scale: 358 / 74.66 x 0.282 = **1.352 m**. This assumes the ball and the board are at the same depth, but they are not:
  - The corner-three lines on the floor (left and right edges of the image) meet at a vanishing point of (960.8, 541.4), which is the image
    centre. So the camera is level and faces the wall square-on, and the horizon is at y = 541.4.
  - The ball touches the floor at y = 1004.24 + 37.4 = 1041.6 (frame 24, its lowest point). The wall/floor junction is at
    y = 981.38 (teal to orange transition, sd 0.14 over 60 columns). Floor depth is proportional to 1/(y - horizon), so
    Z_wall / Z_ball = 500.2 / 440.0 = 1.137. The ball falls about 12% of its distance in front of the wall.
  - The board stands off the wall: the dark mounting bracket under it gets narrower from 331.4 px (where it meets the board's lower
    edge, y 281) to 320.2 px at its far end (y 318.5). Its centre stays at x ≈ 973, which fits the vanishing point. So
    Z_far / Z_board = 1.035. Assuming the far end of the bracket is on the wall: Z_board / Z_ball = 1.137 / 1.035 = 1.0985.
- **Board length = 1.352 x 1.0985 ≈ 1.485 m.**

## Checks and alternatives
- The scale cancels the focal length, so only the depth ratio matters.
- Bounds: board flat on the wall gives 1.537 m; board at the ball's depth (pure single 2D scale) gives 1.352 m.
- Contact point: if the ball's centre had reached the parabola-extrapolated 1010.8, the depth ratio would be 1.151 and the answer 1.50 m.
  The measured lowest centre was used.
- Confidence: moderate. The main uncertainty is the assumption that the bracket's far end is on the wall, and whether the
  reference used a plain single 2D scale (1.35).
