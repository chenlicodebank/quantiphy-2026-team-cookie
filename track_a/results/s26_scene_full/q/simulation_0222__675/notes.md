# q_675 — speed of the robot vacuum at t = 0.5 s

- 2D overhead render, 24 fps (the file and the question agree), so t = 0.5 s is frame 12. Speed = |p12 − p11| × 24.
- Scale from the prior: diameter = 0.438 m. I re-measured the disc on frames 9–15 (`measure.py`: mask = diff vs frame 79
  and gray > 185, robust circle fit). Area-equivalent diameter = 119.0–119.1 px, bbox = 119–120 px, circle fit through
  the contour pixel centres + 1 px = 119.2 px. The record's 117.8 is the fit through the pixel centres, which leaves out
  the 1 px edge. I used 119.05 px, so the scale is 0.003679 m/px.
- Circle-fit centres: f11 = (1612.68, 410.24), f12 = (1600.73, 408.09). The step is 12.14 px; scene/tracks gives
  12.17 px, which agrees.
- Speed = 12.14 × 24 × 0.438 / 119.05 = **1.072 m/s**.
- Check: the steps rise smoothly (10.25, 11.29, 12.14, 13.35, 14.32 px/frame), so frame 12 is not an outlier. A centred
  estimate (frames 11–13) would give about 1.09 m/s. With the record's diameter of 117.8 px the answer would be
  1.083 m/s. Confidence: high, ±2 %.
