# Q553: speed of the typewriter at t = 0.333 s

- question_fps = 24 = file fps, so t = 0.333 s is frame 8 (still in free fall; impact happens between frames 10 and 11).
- Prior: acceleration = 9.8 m/s^2 before 0.45 s. The scene is 2D-like: the typewriter keeps a constant pixel width of about 291 px through the fall, so its depth is constant. I take the scale from the pixel acceleration.
- fit.py: quadratic fits to the vertical track in scene/tracks/typewriter.csv over frames 0-9, plus variants over frames 0-10, 1-9 and 0-8. I fitted four reference points: bbox centre, bbox top, bbox bottom and the mask centroid.
  - bbox centre: a = 12.6 px/frame^2, and the backward difference at frame 8 is 96.5 px/frame.
  - speed = d8 / a x 9.8 / 24 = 3.12 m/s (3.09 from the fitted curve).
  - The bbox top gives 3.11-3.19, the bbox bottom 3.00-3.16 and the centroid 3.04-3.17.
- Check: an ideal drop from rest at t = 0 gives a backward difference at frame 8 of 9.8 x 7.5/24 = 3.06 m/s. The fits show a small initial velocity, which is consistent with this.
- Answer: 3.1 m/s. Confidence high (about ±3%).
