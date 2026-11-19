# Q262: speed of the left first ball (ball1) at 0.5 s

- This is a 2D Newton's cradle render. The prior is a ball diameter of 2 m.
- Time base: file fps = 30.0075 and question_fps = 30. Both give frame round(0.5 × fps) = 15, and they differ by only 0.03 %, so I used 30.0075.
- Speed = |p15 − p14| × fps (one-frame backward difference of the ball centre).

## Scale
- Ball diameter = 163 px (from the scene record). I checked it on ball5 at rest in frame 0: its right edge is 82 px from its centre in the background-difference image, so the radius is about 82 px.
- Scale = 2 m / 163 px = 0.01227 m/px.

## Measurements
- **Route 1 (scene record, ball1.csv):** p14 = (374.35, 713.80), p15 = (388.56, 721.43).
  - Step = 16.13 px, so speed = 5.94 m/s.
  - The neighbouring steps are 14.84 px and 17.08 px, so the motion is smooth (the ball is accelerating down its arc).
- **Route 2 (my own fit, rimfit.py):** fixed-radius (81.5 px) rim fit on |frame − frame1|, ignoring the dark loop and rods.
  - My centres sit at a constant offset of about (−1.5, −0.9) px from the record's.
  - Step 14→15 = 16.51 px, so speed = 6.08 m/s. The neighbouring steps are 14.87 px and 17.17 px.
- **Smoothed:** the midpoint of the neighbouring steps is 15.96 px (record) and 16.02 px (mine). A consensus step is about 16.2 px.
  - Speed = 16.2 × 0.01227 × 30.0075 = 5.96 m/s.
- measure.py is a crude threshold-blob check. It is unreliable because the loop occludes the ball, and I discarded it.

## Answer
**5.95 m/s.** The two routes span 5.94–6.08 m/s.

Confidence: high, with an error of about ±2 %.
