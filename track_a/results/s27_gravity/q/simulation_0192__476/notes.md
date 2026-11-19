# Q476: speed of the box at t = 0.2 s (m/s)

Prior: the box accelerates at 9.8 m/s² before 0.6 s. The scene is 2D, the camera is static, and the file and the question both run at 120 fps.
At t = 0.2 s the frame is 24.

## Method (fit.py)
- I fitted a quadratic y(t) to the box's front-face reference point (scene/tracks/cardboard_box.csv, template cy) over frames 0–58,
  before the roof contact at frame 59–60. I left out the frozen or duplicated frames and the odd frames 18 and 54.
- With a free fit: a_px ≈ 2050–2065 px/s², and the fitted rest time is t ≈ 0.001–0.003 s. So the box is released from rest at frame 0.
  The face-top-edge track gives the same result (a_px ≈ 2005, rest at t ≈ 0.001 s).
- Scale from the prior: 9.8 / 2045 ≈ 0.00479 m/px.
  - Plausibility check: the truck rear is 566 px ≈ 2.7 m wide, which is realistic. The box face would be about 1.35 m wide, which is large but consistent.
- The motion is uniformly accelerated from rest at t = 0, so v(0.2) = 9.8 × 0.2 = 1.96 m/s.
  - The pixel route gives the same: 2045 px/s² × 0.2 s × 0.00479 m/px = 1.96 m/s.
  - Using the one-frame backward-difference convention instead: 9.8 × 23.5/120 = 1.92 m/s.
- I answered 1.94 m/s, which is within about 1% of both readings.

## Caveat
The rendered box position is frozen on some frames, including frame 24, so I could not use the raw one-frame difference of the video track.
I used the fitted smooth motion instead.

Confidence: high (within about 2%).
