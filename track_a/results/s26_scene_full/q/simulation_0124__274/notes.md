# q_274 – length of the black car (m)

Prior: black car speed = 26.085 m/s. This is a 2D top-down render, so one metres-per-pixel scale comes from the speed. fps = question_fps = 24.

## Scale (from the speed)
- In scene/tracks/dark_car.csv the per-frame centre steps over frames 2–45 are very steady: median 26.97 px/frame,
  mean 27.01, spread ±0.3. Frames 0–1 are a duplicated frame. The edge frames 46–49 are not used.
- Speed = 26.97 × 24 = 647.3 px/s, so the scale is 26.085 / 647.3 = 0.04030 m/px.

## Length in pixels (re-measured)
- `zoom.py` / `measure_len.py`: each frame is rotated so the car's axis is horizontal, using the track centre and heading.
  I then read grey-level profiles along the axis in frames 20, 26 and 40 and looked at 5× crops (frames/z_26.png).
- The dark outline of the body sits at u ≈ −57 (rear) and +56 (front) in all three frames. The outer edge, where the
  values return to road grey, is at about −58.5 and +58. The front edge is a little uncertain because the car's
  shadow falls just ahead of it.
- That gives a length of about 116.5 px (±2), which agrees with the record's 117 px.
- I did not use the background-difference masks: the shadow and the dark road make them unreliable (111–131 px).

## Answer
L = 116.5 px × 0.04030 m/px = **4.70 m**. The range from the ±2 px uncertainty is 4.6–4.8 m.

Check: the road is about 188 px wide, which is 7.6 m at this scale — plausible for a two-lane road. The car is a
little shorter than the silver car (122 px → 4.9 m), and 4.7 m is a plausible length for a sports car.
Confidence: good, about ±3 %.
