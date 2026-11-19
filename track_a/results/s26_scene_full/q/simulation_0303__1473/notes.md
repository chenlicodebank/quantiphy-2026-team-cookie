# q_1473 — displacement of the plane, 0.5 s → 1.0 s

File fps 24, question_fps 25 → I use the frame indices at 25 fps: t=1.0 s → frame 25; t=0.5 s → round(12.5) = frame 12
(Python half-to-even) or 13 (half-up).

## Method (fit.py)
- Used the scene/ track (craft = the plane, one object, static camera; frame 1 duplicates frame 0, so I used frames 2–71).
- Fitted a 3D pinhole model: principal point (1280,720), unknown f, with the plane's origin moving on a straight line,
  either constant velocity or with a quadratic term. Constraints: image track plus the two given depths
  (102.6664 m at frame 25, 121.8263 m at frame 50).
  - Linear, bbox centre: f ≈ 3297 px, rms 0.56 px, speed 22.39 m/s at 25 fps. That is within 1% of the prior 22.16, so
    the 25 fps time base and the constant-speed straight-line motion both check out.
  - Quadratic fits: speed changes only by about 1.5% over the whole clip, so the motion is effectively uniform. In those
    fits, displacement over 12→25 divided by (speed × 13/25) = 0.999, which means a straight path.
  - f is poorly constrained (3300–11300 px depending on the model and the reference point). The prior speed sets the
    scale instead.
- So the displacement = prior speed × number of frames / 25:
  - frames 12→25 (13 frames): 22.16 × 0.52 = 11.52 m
  - frames 13→25 (12 frames): 22.16 × 0.48 = 10.64 m
  - 0.5 s × 22.16 = 11.08 m, which is within 4.2% of both readings.
- Answer: **11.08 m**.

## Second-route check
The independent 3D fit with the depths gives 11.64 m (12→25) or 10.75 m (13→25) when unscaled. Its own speed is
22.39 m/s, which is consistent with the prior-based numbers above.

## Confidence
High that the answer is in the 10.6–11.5 m range. The remaining uncertainty is mostly the rounding of frame 12.5.
