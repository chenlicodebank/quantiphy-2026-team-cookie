# Q560: speed of the typewriter at t = 0.333 s

- 2D scene, file fps = question_fps = 24. t = 0.333 s -> frame 8; speed = |p(8) - p(7)| x 24.
- Prior: the free fall before 0.45 s (frames 0-10, impact between frames 10 and 11) has a = 9.8 m/s^2. I use it as the scale:
  I fit a quadratic to the vertical track of the typewriter centre (scene/tracks/typewriter.csv, airborne frames), which gives
  a_px in px/frame^2. Then m/px = 9.8 / (a_px x 576). The fall is purely vertical (cx is constant).
- fit.py: I tried several fit windows (0-10, 0-9, 0-8, 2-10, 2-9) and several reference points (bbox centre, mask centroid, top and bottom edges).
  - bbox centre, frames 0-9: a = 12.64 px/f^2, so 1 px = 1.346 mm. Speed at frame 8 from the fit's backward difference is 3.08 m/s, and from the raw difference (97 px) it is 3.13 m/s.
  - Mask centroid: 3.07-3.11 m/s. The motion blur biases the edges in opposite directions (top edge 3.14-3.2, bottom edge 2.93-3.1), and the centres fall between them.
  - Second-route check: since a is fixed at 9.8, speed = 9.8 x (time since zero velocity). The parabola's vertex lies near frame 0 (the frame 0->1 drop is 8 px), which gives about 9.8 x 7.6/24 = 3.1 m/s. This agrees with the fits.
- Answer: 3.08 m/s. Confidence high (about ±3%).
