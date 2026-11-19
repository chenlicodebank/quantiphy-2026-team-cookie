# q3105: distance between the ball and the floor at t = 1.50 s

The rate is 30 fps (the file and the question agree), so t = 1.50 s is frame 45. That is the apex of the
throw.

## Scale from the prior (g = 9.8 m/s^2)
`fit.py` fits a parabola to the ball centre y in `scene/tracks/ball.csv`. It uses only the clean free-flight
frames, before the bounce at frame 61:
- Frames 36–60, camera-compensated: a = 3713 px/s^2 (rms 0.6 px). Raw coordinates give 3729 px/s^2.
- Frames 38–58: 3694 px/s^2. Frames 45–60: 3707 px/s^2. Frames 36–50: 3774 px/s^2.
- The mean of the second differences is 3772 px/s^2.
- Adopted value: 3715 px/s^2, so the scale is 9.8 / 3715 = 0.002638 m/px.

## Pixel distance at frame 45
- The ball centre is at y = 304.8 px (raw frame-45 coordinates; the fit gives 304.8–305.2).
- **Floor level at the ball's depth**: this comes from the bounce at frame 61, read from a 3x zoom
  (frames/f61.png). There the ball's bottom touches its reflection at y ≈ 875, and the centre is 827.6 with
  D = 94, which also gives 875. Moving that to frame-45 coordinates with the camera drift (+1.3 px) gives a
  floor y of about 876.
- The walker's foot contact is at y 867–880, which agrees.
- Centre to floor: 876.3 − 304.8 = 571.5 px, which gives **1.51 m**.
- Under the other reading, ball bottom to floor, the gap is 524.5 px = 1.38 m. I answer with centre to floor
  because positions are taken at the object's centre or reference point.

## Check by a second route
- The ball's diameter is 94 px, which is 0.248 m at this scale. A real basketball is about 0.24 m, so the
  scale is consistent to about 3 %.
- Using a 0.24 m ball for the scale instead gives 571.5 × 0.24 / 94 = 1.46 m, within 3 % of the main answer.

## Confidence
Good on the scale (±2 %) and on the pixel distance (±5 px). The main risk is the convention: centre to floor
versus the bottom gap.
