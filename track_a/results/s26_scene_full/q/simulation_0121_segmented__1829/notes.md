# q_1829: speed of the left first ball at 0.5 s

- This is a 2D Newton's-cradle style scene at 30 fps (the file and the question agree). t = 0.5 s is frame 15. The "left first ball" is the striker, ball_left.
- Scale: the prior gives a ball diameter of 2 m. The measured diameter is 164 px (scene record median; my own circle fits near f15 give radius 82.0–82.4 px). That makes the scale 2/164 = 0.012195 m/px.
- Tracking (measure.py): for each frame, mask pixels with min RGB < 235 and x < 720, take the convex hull, sample its outline densely, then do an algebraic circle fit with outlier rejection. The centres match scene/tracks/ball_left.csv to within about 0.5 px (f14 (372.97, 714.71), f15 (386.91, 722.25)).
- Route 1, the raw backward difference |p15 − p14| = 15.84 px/frame, gives 5.80 m/s.
- Route 2 (speed.py): fit a circle to the path (pivot about (643, 231), R 554 px) and fit polynomials to angle vs frame over several windows (8–22 cubic, 10–20 quadratic, 6–24 quartic, 11–19 quadratic). The difference between f15 and f14 comes out at 15.90–16.10 px/frame, which is 5.82–5.89 m/s. The neighbouring raw differences (15.23, 15.84, 17.62) show about ±1 px of noise per frame.
- Answer: 5.85 m/s, using the smoothed value, which agrees with the raw value to within 1%. Confidence: high, with an error of about 2–3%.
