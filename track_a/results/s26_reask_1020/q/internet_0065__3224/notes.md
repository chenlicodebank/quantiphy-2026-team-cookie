# q3224 – velocity of the ball at 0.50 s

- The video looks top-down at a gym floor. A basketball rolls left to right at nearly constant pixel speed. Nothing falls, so
  the prior (g = 9.8 m/s^2) gives no usable scale: the fitted pixel acceleration is only ~0.19 px/frame^2, which is noise.
- **Scale:** I took it from a regulation basketball instead (size 7, diameter 0.24 m). The ball's diameter across the motion
  (vertical extent, which has no blur) is 258 px. That is the record's median bbox_h. My own column-profile check gives
  253–262 px on frames 9–19 where the seam lines don't break the profile; the other frames dropped out because of the seams.
  So scale = 0.24 / 258 = 9.30e-4 m/px.
- **Time:** t = 0.50 s is frame 15 at question_fps 30 (same as the file's fps).
- **Position:** the centroid stabilised against the background (`cx_est_stab`, `cy_est_stab`). The camera drift is small
  (≤3 px/frame).
- **Velocity:**
  - Forward difference 15→16: 98.1 px/frame. Backward 14→15: 96.4. Mean over frames 13–17: 98.5. Quadratic fit over frames
    5–21: 98.4 px/frame.
  - v = 98.1 × 30 × 9.30e-4 = **2.74 m/s**. The fit route gives 2.75 m/s.
- **Uncertainty:**
  - If the ball is a size 6 (0.229 m), the answer would be 2.61 m/s.
  - If the diameter is taken along the motion including blur (~275 px), it would be 2.57 m/s.
- **Confidence:** moderate. The scale comes from the standard ball size, not from the prior.
