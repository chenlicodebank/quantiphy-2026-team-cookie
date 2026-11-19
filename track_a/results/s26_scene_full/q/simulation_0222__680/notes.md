# q_680 — acceleration of the robot vacuum at t = 2 s

- 2D top-down Blender render, 24 fps (file and question rates agree). t = 2 s -> frame 48.
  a = (s48 - s47) x fps^2 x scale, where s_i = |p_i - p_(i-1)| in px/frame.
- Scale from the prior: diameter 0.438 m. I re-measured the disc with sub-pixel radial edges (half-intensity /
  max-gradient edge, robust circle fit; `track_edge.py`). It gives 120.26 px for frames 44–52. The radial profile
  (`profile.py`) shows the 50 % edge at r ≈ 60 px. The record's mask circle (117.8 px) is about 2 % small because its
  gray > 185 threshold cuts off the antialiased rim. Scale = 0.003642 m/px.
- Positions: my edge track and the record agree to within about 0.1 px over frames 30–66.
- Δs at frame 48: raw 0.485 px/f² (edge track) and 0.458 (record). Local polynomial fits to the speed curve around
  frame 47.5 give 0.50–0.57 (`accel.py`). The neighbouring Δs values are 0.80 (frame 47) and 0.44 (frame 49): the
  robot is accelerating toward a speed peak at frame 51.
- Results: raw gives 0.96–1.02 m/s², smoothed fits give 1.06–1.20. I used Δs ≈ 0.515 px/f², which gives
  0.515 x 576 x 0.003642 ≈ **1.08 m/s²**.
- Check: the two independent trackers agree, and the raw and smoothed routes agree within about ±10 %.
- Confidence: moderate. The Δs value at a single frame carries about ±0.1 px/f² of noise, which is about ±20 %.
