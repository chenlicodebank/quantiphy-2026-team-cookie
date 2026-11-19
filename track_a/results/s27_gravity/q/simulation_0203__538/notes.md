# Q538 – speed of the magnifying glass at t = 0.333 s

- 2D simulation, 24 fps (file and question_fps agree). t = 0.333 s -> frame 8. Speed = |p(8) - p(7)| x 24 (backward difference).
- Glass falls freely frames 0-10 (impact between 10 and 11), so the prior (a = 9.8 m/s^2 before 0.5 s) sets the scale.
- measure.py: difference mask vs. frame 12 (glass already on desk, upper area clean), largest blob, frames 0-10.
  Quadratic fits of y(frame) for several reference points:
  - mask centroid: a = 12.964 px/frame^2, residuals <= 0.3 px; step 7->8 = 97.55 px (fit 97.87)
  - ring centroid: a = 12.84; step 96.74 (fit 97.01)
  - bbox centre: a = 12.96; step 96.5 (fit 98.1)  (bbox top/bottom individually noisy due to tilt)
- Scale: 9.8 m/s^2 = 9.8/576 m/frame^2 -> m/px = 0.017014 / 12.96 = 1.313e-3 m/px.
- Speed = step/a x 9.8/24: centroid 3.07-3.08, ring 3.08, bbox centre 3.04-3.09 m/s.
- Second route (physics): fit gives release at rest at ~frame 0 (step/a = 7.55 frames), so the ideal backward
  difference at frame 8 is 9.8 x 7.5/24 = 3.06 m/s; agrees.
- Answer 3.08 m/s (instantaneous value would be 3.27; the benchmark convention is the backward difference). Confidence high (~2 pct).
