# q1131 – walking speed of the person at t = 1.0 s (frame 30 at question_fps 30; file fps 30.005)

## Scale (metres per pixel at the person's depth, kh = Zh/f)
- Orange car acceleration prior -2.86 m/s^2. I fitted a quadratic to the car's axle-midpoint x over frames 10-53, which gives
  0.52 px/frame^2 (470 px/s^2). Fits over frames 25-53 give 0.51. So kc = Zc/f = 0.0061-0.0062 m/px; adopted 0.00613.
- Depth difference check: with the car origin at the bbox centre (axle midpoint + ~18 px), x(0) ≈ 1524 and x(30) ≈ 565.
  sqrt(D0^2 - D1^2) / sqrt(du0^2 - du1^2) = 0.00613. This agrees with the prior.
- Focal length from the car's D(t=1) = 10.432: f ≈ 1640-1670 px (depends on the car origin's height).
- Person: Zh = D_h(t=1) / sqrt(1 + (du^2 + dv^2) / f^2), using pelvis u ≈ 185 and v ≈ 765, so kh = Zh/f = 0.0079-0.0082. Adopted 0.00803.
- Independent route (ground-row ratio, level camera): kh = kc * (982 - cy) / (871 - cy) = 0.0081-0.0082 for cy = 520-540, which matches.
  Sanity check: the person is ~218 px tall, which gives 1.75 m.

## Pixel speed (scripts: mask.py, torso.py; tracks: mask_track.csv)
- The head is hidden by the lamp post around frames 25-41. The pixel speed rises slowly through the clip:
  - head f0→30: 1.67 px/frame
  - head f15→45: 1.95 px/frame (one gait cycle centred on f30)
  - head f23→53: 2.08 px/frame
  - torso back edge f22→37 (unoccluded): 1.87 px/frame
- Gait step ≈ 15 frames. At f30 the head is at its high point, where the phase speed is slightly above the cycle mean. Adopted 1.97 px/frame.
- Speed = 1.97 × 30 × 0.00803 ≈ 0.475 m/s.

## Confidence
About ±10%. The main uncertainty is the instantaneous pelvis speed within the gait cycle (a one-frame difference in the reference answer); the scale is about ±2%.
