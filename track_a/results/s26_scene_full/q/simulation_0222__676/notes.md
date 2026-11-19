# Q676 — acceleration of the robot vacuum at t = 0.5 s

- 2D top-down render, 24 fps (file fps = question_fps, so no re-timing). t = 0.5 s → frame 12. The camera is static.
- Scale comes from the prior: diameter 0.438 m. Measured diameter is 118.7 px from my own circle fit (measure.py,
  frames 8–29), bbox 119 px, and 117.8 px from the record's circle fit. I used 118.5 px, giving 0.003696 m/px.
- Track: I re-measured frames 4–29 (measure.py, background = frame 79). The positions agree with
  scene/tracks/robot_vacuum.csv to within 0.3 px.
- Per-frame speed (px/frame): f10 10.21, f11 11.29, f12 12.19, f13 13.31, f14 14.31. The robot speeds up smoothly
  until about frame 25.
- Raw backward difference at frame 12: 0.88–0.90 px/frame². This is noisy, because the frame-to-frame differences
  swing between 0.7 and 1.5.
- Smoothed (fit.py): polynomial fits of speed or arc length over frames 6–18, 8–16, 5–19 and 4–20 give
  1.02–1.06 px/frame², with a central value of 1.04.
- a = 1.04 px/frame² × 24² × 0.003696 m/px = 2.21 m/s². Using 117.8 px as the diameter gives 2.23.
- Second route: an arc-length polynomial fit gives 1.03–1.04, which agrees with the speed fits.
- Answer: 2.22 m/s². Confidence is moderate, about ±5%. The main uncertainty is whether the reference used the
  smooth value (about 1.04) or a noisier raw one (about 0.9, which would give 1.9).
