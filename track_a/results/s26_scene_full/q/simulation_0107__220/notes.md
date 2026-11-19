# q_220 — distance between the two viruses at 2.0 s

- 2D render, 24 fps (fps = question_fps). t = 2.0 s -> frame 48.
- Prior: right (large) virus speed 1.7393 m/s. Its motion is a constant straight line. Fitting body-circle
  centres over the reliable frames 2–35 gives (+13.733, −0.761) px/frame = 330.10 px/s, so the scale is
  0.0052690 m/px.
- At frame 48 the large virus's centre has left the frame (it is out from frame 46). The small virus is
  partly clipped. So both positions come from linear fits over the reliable body-fit frames (small 2–40,
  large 2–35; residuals about 0.25 px), extrapolated to frame 48:
  small (28.3, 589.4), large (1952.6, 581.0). The separation is 1924.3 px, which is 10.14 m.
- Second route: the record's trailing-edge-based centres at frame 48 give 1921.8 px, which is 10.13 m. The two
  routes agree to within 0.15 %.
- Answer: 10.13 m. Confidence is high; the main uncertainty is extrapolating outside the frame, under 0.5 %.
- Script: measure.py
