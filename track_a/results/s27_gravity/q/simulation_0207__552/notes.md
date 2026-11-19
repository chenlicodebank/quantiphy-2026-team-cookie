# q_552 — typewriter speed at t = 0.25 s

The typewriter falls freely in frames 0-10 and hits the desk between frames 10 and 11. The prior says its acceleration is 9.8 m/s^2.
question_fps = 24, the same as the file rate. t = 0.25 s is frame 6, so speed = |p6 - p5| x 24.

## Method (measure.py)
- I built a background from frame 0 below y=550 and frame 29 above it, then made a mask with a difference threshold of 30.
- For frames 0-10 I took the box top and bottom (rows with at least 20 mask pixels) and their midpoint.
- I fitted a parabola to frames 0-9, then 1-9 and 0-8, which gives the pixel acceleration a (px/frame^2).
- Scale = 9.8 / (a x 24^2) m/px, so speed (m/s) = (Δy in px/frame / a) x 9.8 / 24.

## Results
- Box midpoint: a = 12.6-12.8 px/f^2; Δy from frame 5 to 6 = 69 px; fitted v(5.5) = 70.1-70.2 px/f.
  This gives 2.20-2.27 m/s.
- Box top: a = 11.9, v = 67.3, giving 2.30. Box bottom: a = 13.4, v = 73.1, giving 2.17-2.24.
  The top and bottom differ because the visible underside/top changes as the object drops.
- The midpoint fit puts the moment of rest at t ≈ 0 (within ±0.06 frame).

## Second route (physics)
The object is released at about t = 0. Under constant g, the backward difference at frame 6 is the velocity at frame 5.5:
9.8 x 5.5 / 24 = 2.246 m/s. This agrees with the pixel measurement (midpoint fit gives 2.26).

Answer: 2.25 m/s. Confidence: high (about ±3 %).
