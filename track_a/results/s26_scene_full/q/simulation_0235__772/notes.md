# Q772: speed of the basketball at t = 0.5 s

- This is a 2D render at 24 fps. question_fps is also 24, so t = 0.5 s is frame 12, and the speed is |p12 − p11| × 24.
- The ball falls straight down (x stays at about 907.3) from rest at frame 0. It bounces between frames 23 and 24, so frame 12 is in the middle of the free fall.
- `measure.py` makes my own HSV mask of the ball for frames 0–24 and records its centroid, bbox and area in `my_track.csv`.
- **Scale:** the prior gives a diameter of 0.282 m.
  - The ball's horizontal width is 108 px (106 px on frames with motion blur).
  - The area-equivalent diameter is about 107.5 px, and the circle fit in the record gives 106.1 px.
  - I use 107 ± 1 px, which gives 0.002636 m/px.
- **Velocity (`fit.py`):** I fitted a quadratic to y(frame) over the fall (residuals 0.13 px) and took the one-frame backward difference at frame 12:
  - It comes out at 15.45 px/frame for my centroid, 15.44 for the bbox centre and 15.44 for the record's circle-fit centre, and barely changes with the fit window (0–23, 2–22, 6–18).
  - The raw differences are noisier: 15.74 for my centroid and 14.93 for the record.
- **Speed:** 15.45 × 24 = 370.8 px/s, and 370.8 × 0.282 / 107 = **0.977 m/s**. With a diameter of 106–108 px the range is 0.968–0.986.
- **Second route:** three independent position estimates and three fit windows all agree within 0.2 %, and the raw differences scatter around the fitted value. The acceleration is 1.34 px/frame², which is about 2.0 m/s² at this scale. That is not real-world gravity, but rendered scenes are not at real scale, so I left it alone.
- **Confidence:** high. The main uncertainty is the ±1 % pixel size of the ball.
