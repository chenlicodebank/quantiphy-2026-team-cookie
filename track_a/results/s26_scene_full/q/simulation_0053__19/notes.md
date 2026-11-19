# Q19: speed of the green car at 2.0 s (m/s)

- The green car is scene/ "black_car", the dark green roadster in the right lane. The orange car is the prior's object.
- This is a 2D top-down render at 30 fps (file and question fps match). One m/px scale applies to the road plane.
- Scale (fit.py): I fitted a line to the orange car's per-frame displacements from its template-matched reference
  point, over f25–90. It has slope -0.3478 px/frame² (residual 0.1 px), which is -313.0 px/s².
  Separate fits to the first and second halves give -0.347 and -0.342, and a quadratic fit on y gives -0.3486.
  Scale = 2.86 / 313.0 = 0.009138 m/px. As a sanity check, this makes the lane 4.0 m wide and the car 5.1 m long.
- Green car at t = 2.0 s (frame 60): the backward difference |p60 - p59| is 43.07 px. 43.07 × 30 × 0.009138 = **11.81 m/s**.
  A quadratic fit over f47–80 gives 43.17 px/frame at f60, which is 11.83 m/s.
- Second route (check.py): I took masks from the difference against frame 0 and tracked the car edges.
  - The orange car's leading and trailing edges have accelerations of -0.322 and -0.373 px/f². The blur changes
    the bbox length, so I used their mean, -0.348. This matches the template fit.
  - The green car's edges move at 42.3–42.6 px/frame on average over f47–80, and 42–43 px/frame around f60.
    This is consistent within about 1 %.
- Confidence: high, with an error of about 2 %.
