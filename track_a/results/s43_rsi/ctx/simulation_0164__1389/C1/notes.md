# q1389 – acceleration of the bowling ball at t = 1 s (frame 24 at 24 fps; file is 24 fps too)

Answer: 0.41 m/s^2 (size of the deceleration; the ball is slowing down, a ≈ -0.41 m/s^2).

## Method
- Ball track: scene/tracks/ball.csv (circle-fit centres, ±1 px). Frame 24 is before the pin impact (frame 37-38),
  so I used the clean rolling stretch, frames 6-37.
- Vanishing point (vp.py): fitted three bright lane-edge lines on frame 0 (rms 0.3-0.4 px). They meet at
  (5650, 208) ±10 px, and the ball's image path goes through the same point. So the ball rolls along a 3D line
  parallel to the lane.
- 3D reconstruction (line3d.py): pinhole camera, principal point at (960, 540). Line direction = ray to the VP.
  Line anchored by the frame-12 ball ray at 9.391 m (depth_info is given at t = 0.5 s = frame 12). For each frame,
  the position along the line s comes from the closest point between that frame's ray and the line.
- Focal length: f = diam_px × depth / 0.21 = 82.1 × 9.391 / 0.21 ≈ 3670 px. Check: with f ≈ 3600-3700 the
  predicted apparent diameters match the measured ones within 0-3 % (the early frames run about 3 % big; there
  the top of the ball sits against the dark gutter, so the mask is less reliable). The acceleration barely
  depends on f: 3500 → -0.425, 3800 → -0.404.
- Acceleration: quadratic fit of s(t) over frames 6-37 gives a = -0.414 m/s^2 and v(1 s) = 3.59 m/s (f = 3650).

## Checks
- Fit windows: 6-30 → -0.43, 12-36 → -0.42, 16-32 → -0.39; a cubic fit evaluated at 1 s → -0.41.
- VP x shifted by ±70 px → -0.39 / -0.43.
- Residuals of the quadratic fit are ±5 mm (about 1 px), with no trend.
- First attempt (recon.py): ball centres on a horizontal plane with the horizon at y = 205. It gave -0.46, but
  it depends strongly on the assumed horizon. The line/VP method fixes that from measured lines.
- I rejected depth taken from the apparent diameter alone (-0.77): the diameter is biased in the early frames
  (dark gutter behind the ball's top).

Confidence: moderate-good; estimated uncertainty about ±10 %.
