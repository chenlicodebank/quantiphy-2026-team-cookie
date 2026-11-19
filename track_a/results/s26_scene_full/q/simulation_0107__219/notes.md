# Q219: distance between the two viruses at t = 1.0 s

- 2D render at 24 fps (question_fps is also 24), so t = 1.0 s is frame 24.
- Scale comes from the prior (right/large virus speed = 1.7393 m/s). The large virus moves at a constant rate. A
  linear fit of its body-fit centre over frames 2–35 gives a step of (13.733, −0.761) px/frame, which is
  13.754 px/frame or 330.1 px/s. Scale = 1.7393 / 330.1 = 0.005269 m/px.
  (The raw step from frame 23 to 24 is 13.56 px. The fitted value is used because the motion is uniform.)
- Positions at frame 24 (body-sphere centres from the circle fit; checked on frames/f24.png): small (367.5, 585.5),
  large (1623.1, 599.7).
- Distance = 1255.6 px (raw) or 1254.9 px (from the linear fits), which is **6.616 m** (6.612 m from the fits).
- Second route: the template-match centres and the template-based step give 6.641 m (0.4 % higher).
- Answer: 6.616 m. Confidence is high (about ±1 %). The main uncertainty is whether the origin is exactly the body
  centre.
