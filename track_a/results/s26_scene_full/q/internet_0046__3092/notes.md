# q_3092: velocity of the cup at 1.20 s

- Time base: 30 fps (the file and the question agree). t = 1.20 s is frame 36. The camera is static (see scene/notes.md).
- Scale: the prior says the cup height is 10.5 cm. Measured rim to base, the body is 570-576 px tall in frames 33-37
  (my measure.py gives 574 at frame 36; the scene record's median is 570). Using 572 px gives 1.836e-4 m/px.
- Motion: forward difference of the body centre (scene/tracks/mug.csv). Frame 36 to 37 is 1220.8 to 1347.6, so
  126.8 px/frame, or 3804 px/s.
  v = 3804 x 0.105 / 572 = **0.698 m/s**.
- Second route: my own background-difference left-edge tracker (measure.py) gives 121.2 px/frame for 36 to 37, which is 0.667 m/s.
  A central difference of the centre (frames 35 to 37) gives 125.2 px/frame, which is 0.69 m/s. The right edge gives 131.6 px/frame, but that edge is blurry.
  The edge steps differ because the measured width changes with motion blur. The centre is the most robust point.
- Answer: 0.70 m/s. Confidence: good (about ±5 %).
