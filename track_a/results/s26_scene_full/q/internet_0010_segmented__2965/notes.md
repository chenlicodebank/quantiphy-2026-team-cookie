# q2965 — ball velocity at 2.00 s (cm/s)

- Time base: t = 2.00 s → frame 60 (fps 30.0003 ≈ question_fps 30). The ball is in free flight after release (frame 46), just before the apex (~frame 66).
- Scale (internet convention, one factor): prior basketball diameter of 24 cm ÷ 17 px. 17 px is the median bbox width over clean frames; the equal-area diameter is 16.7–17.5 px in frames 46–54. That gives 1.412 cm/px.
- Track (measure.py): connected components of non-white pixels, darkness-weighted centroid, frames 46–92. My values match scene/tracks/ball.csv to within 0.5 px.
  The masks in frames 57–62 are deformed (partial or smeared, see frames/crops56_64.png), so the raw one-frame differences there are noisy (353–555 cm/s).
- Method (fit.py): x linear, y quadratic, fitted over the clean frames 46–79, leaving out the deformed frames 57–62, 67, 70 and 80.
  vx = 9.68 px/f, vy = −4.26 px/f at frame 60 → 317 px/s → 448 cm/s (central), 442 cm/s (forward difference 60→61).
- Check: fitted g = 614 px/s² = 8.7 m/s² with this scale. That is close to gravity, so 30 fps and the 17 px diameter hold up.
- Second route, other windows: 46–56 gives 447; 50–70 gives 437; 63–79 gives 463; 52–68 gives 434. The mean forward difference over frames 58→62 is 393 (noisy masks).
- Answer: 445 cm/s. Confidence: moderate (about ±5%). The main uncertainty is the ball's pixel diameter, 16–18 px.
