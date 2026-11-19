# q_678: acceleration of the robot vacuum at t = 1 s

The file and the question both run at 24 fps, so t = 1 s is frame 24. Acceleration = (speed(24) - speed(23)) x fps,
where speed(i) = |p(i) - p(i-1)| x fps.

## Measurement
- `measure.py` fits a circle to the robot disc in frames 8-69. It samples 720 radial rays from a rough centre,
  finds the edge where the brightness crosses 50% (sub-pixel), and runs a robust least-squares circle fit.
  Output: `my_track.csv`.
- The centres agree with scene/tracks (x, y) to within about 0.3 px. SAM 3 ("white disc", frame 24) puts the
  centroid at (1392.0, 378.3); mine is (1391.67, 378.15).
- The raw per-frame step changes are noisy (about ±0.2 px/frame²). Raw speed(24) - speed(23) is 0.15 px/frame² from
  my track and 0.10 from the scene track.
- `accel.py` fits smooth polynomials to x(t) and y(t), or to the speed, over windows of frames 10-38, 12-36, 14-34 and
  16-32 (degree 3-5). It then applies the benchmark convention to the fitted curve. Every fit gives
  dS = 0.19-0.22 px/frame², with a consensus of 0.205. The scene track gives the same values, which is the second
  route. The speed is close to its first peak there (20.5 px/frame at frame 25), so the acceleration is small and
  positive.

## Scale (prior: diameter 0.438 m)
- The radial profile (`edge_check.py`) shows a sharp edge: brightness falls from 198 to 117 between r = 58.5 and
  62 px. The 50% crossing is at r ≈ 60.4, giving a diameter of about 120.7 px at frame 24.
- Across the clip, the 50% edge diameter is 121.6 px at the far right of the image and about 119.8-120.0 px near the
  image centre (frames 45-69). The extra width at the edge of the image is probably the cylinder's side showing
  through perspective. I used D = 120.0 px.
- SAM 3 mask at frame 24: a circle fit to its contour gives 121.3 px (122.2 from its area), versus my 120.7 there.
  That is within 1%, so the two agree.
- The scene record's 117.8 px (threshold at gray > 185) sits inside the 50% edge, so it is biased about 2.5% small.
  The radial profile shows the 50% edge is the real rim.
- Scale = 0.438 / 120.0 = 0.003650 m/px.

## Answer
a = 0.205 px/frame² x 24² x 0.00365 = **0.431 m/s²**.

Range: 0.40-0.46 from the spread of the fits. Using D = 117.8 or 121.3 px gives 0.439 or 0.426.

Confidence is moderate. The value is a small difference of two large speeds, so frame-level noise matters. The
smooth fits are consistent, but a non-smooth true speed curve could make the true value differ by about 10-20%.
