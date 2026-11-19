# Q2164: basketball velocity at 1.2 s (m/s)

The video and the question both run at 24 fps, so t = 1.2 s is frame 29. In that frame the ball is falling, one frame before it hits the table at frame 30. It is motion-blurred.

## Method
- I used the ball centres from scene/tracks/ball.csv and checked frames 28 and 29 on zoomed crops with a grid:
  - frame 28: about (565, 335); the record gives (564.1, 335.4)
  - frame 29: about (570, 390); the record gives (571.5, 391.6)
- Camera: f = 763 px, principal point (640, 360). Each centre is back-projected with its camera distance:
  - The depth_info distances are 1.401 m at frame 24 and 1.564 m at frame 29.
  - Model A: linear interpolation between those two distances.
  - Model B: depth = k / diameter. Both given depths imply a ball diameter of 0.210 m, so this model is consistent with them.
- Script: vel.py.

## Results
- Backward difference from frame 28 to 29: 2.85 m/s (model A), 3.00 m/s (model B).
- Quadratic fit over frames 24-29, evaluated at frame 29: 3.07 m/s (A), 3.17 m/s (B). The fitted vertical acceleration is 8.2-8.8 m/s², close to the prior's 9.8.
- Physics check: the 3D drop from the release point (frame 21) to frame 29 is 0.59 m. Free fall over that gives sqrt(2·9.8·0.59) = 3.4 m/s. Starting from release at frame ~20.9, g·t gives about 3.3 m/s.
- The forward difference from frame 29 to 30 (1.4 m/s) is ruined by the impact, so I did not use it.

## Answer and confidence
Answer: 3.1 m/s. Confidence is moderate: the routes give 2.85-3.4 m/s, the blurred centres are uncertain by 5-12 px, and the impact rules out a symmetric smoothing window.
