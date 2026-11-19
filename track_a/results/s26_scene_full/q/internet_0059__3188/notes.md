# q_3188 – displacement of ball 2.50 s -> 3.00 s (frames 75 -> 90 at 30 fps; file fps = question fps = 30)

Method (internet convention, one planar scale from the prior g = 9.8 m/s^2):
- Ball track from scene/tracks/ball.csv (cx_bg, cy_bg = camera-drift-corrected centre). Frames 75 and 90 are clean
  (not truncated); frame 90 centre checked visually on a zoomed crop (frames/f90.png): ~(1231, 406) image, matches.
- Pixel displacement f75 -> f90: dx = 695.1, dy = 293.7 px -> 754.6 px (raw image coords without drift correction: 749.6 px).
- Vertical acceleration in px/s^2 from quadratic fits of cy_bg (truncated apex frames 77-80 excluded):
  frames 66-97: 4956 -> 1.492 m; frames 70-95 / 72-93 / 75-90: ~4900 -> 1.509-1.511 m.
  Median second difference: 4860 px/s^2 -> 1.52 m.
- The rising part (66-76) gives 5330 and falling part (81-97) 4750 px/s^2; ball area shrinks ~11% over the flight,
  so the ball recedes slightly from the camera (perspective); single scale still used per convention.
- Second route: fitted-trajectory displacement (linear x, quadratic y) gives 1.497 m; image coords without drift
  correction give 1.490 m.

Answer: 1.50 m (range 1.49-1.52). Confidence: good (~3%).
