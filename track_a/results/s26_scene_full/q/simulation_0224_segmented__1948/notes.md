# q_1948 — speed of the red general chess piece at t = 1.5 s

- The record's "block" is actually the Chinese chess piece: a disc lying flat in the ramp trough, seen at a
  grazing angle, so it looks like a pill. Its long image axis lies along the slide direction and equals the disc
  diameter. It is the only moving object.
- fps = question_fps = 24, so t = 1.5 s is frame 36.
- Scale (2D, one scale): the diameter is 81.3 px along the motion axis (record median of frames 0–36, range
  79.6–83.6, with no trend along the ramp). My own difference mask (measure.py) gives a median of 80.6 px. That mask
  clips the shaded lower edge, but that edge does not change the extent along the axis. So 0.097 / 81.3 =
  1.193e-3 m/px.
- Speed:
  - Frame 35 is an exact copy of frame 34, which holds render 35. So the step from frame 34 to frame 36 is one
    render step: 35.01 px/frame, giving 840 px/s and **1.003 m/s**.
  - Second route: a quadratic fit of position along the path against the corrected render index (fit windows
    starting at frames 10, 15 and 20; rms 0.45–0.57 px). The backward step at index 36 is 35.08–35.23 px, giving
    1.005–1.009 m/s.
- Answer: 1.005 m/s. Confidence is good, about ±3%; most of the uncertainty is in the pixel diameter.
