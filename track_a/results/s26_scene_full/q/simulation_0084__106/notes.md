# q_106: distance between the yellow car and the black-and-white car at 1.0 s

- 2D top-down render at 24 fps (question_fps is also 24), so t = 1.0 s is frame 24.
- Scale from the prior (yellow car speed 5.07 m/s):
  - `measure.py` re-measured the yellow car's bumper-to-bumper midpoint in frames 12–40. A linear fit gives a step of −9.886 px/frame, which agrees with the record's −9.90.
  - That is 237.3 px/s, so the scale is 5.07 / 237.3 = 0.02137 m/px.
- Positions at frame 24:
  - My mask gives yellow cx = 1651.5 and dark cx = 532.5. The record gives 1653.5 and 533.5.
  - That makes dx = 1119–1120 px.
  - `yext.py` gives the lane centrelines: yellow y = 525.5 and dark y = 637.5, so dy = 112 px.
  - The in-plane distance is sqrt(1119.5² + 112²) = 1125.1 px, which is **24.04 m**.
- Second-route check:
  - Using the raw backward-difference step at frame 24 (exactly 10 px, which is affected by rounding) gives 23.8 m.
  - Using the record's centres with the 9.90 px step gives 24.0 m.
- Perspective: the cars' top surfaces set both the speed and the distance measurements, and both cars are at the same height, so the scale effect cancels.
- Confidence: high, within about 1–2%.
