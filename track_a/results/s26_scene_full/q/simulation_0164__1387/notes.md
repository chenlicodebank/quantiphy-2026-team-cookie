# q1387 – acceleration of the bowling ball at t = 0.5 s (frame 12 at 24 fps; file fps = question fps = 24)

## Method (3D, pinhole)
- Ball track: scene/tracks/ball.csv (circle-fit centres, ±1 px). Checked frame 12 visually: the ball is at (440, 643)
  rolling freely on the lane, well before the pin impact at frame ~38.
- Focal length: f = diam_px × depth / D. The smoothed apparent diameter at frame 12 is 81.9 px (quadratic fit of 1/diam,
  frames 6-37), so f = 81.9 × 9.391 / 0.21 ≈ 3664 px (hfov 29°). The diameter from mask height (~83.4 px) would give
  f ≈ 3730, which changes the result by about 1 %.
- Lane direction: vanishing point from the four clean edge lines at frame 0 (two cyan lines, the lane bottom edge and
  the return-cap edge; each line rms < 0.2 px), see vp.py. Result: VP ≈ (5650, 207) ± 40 px. It lies on the ball's
  image path (y = −0.0832x + 678.6).
- 3D line: it passes through P12 = 9.391 m × the unit ray through the ball centre at frame 12, with its direction set by
  the VP ray. For each frame, the position s along the line is taken where the centre ray comes closest to the line
  (final.py). Check: the diameters predicted from these depths match the measured ones within about ±2 px.
- Acceleration: quadratic fit of s(frame) over frames 6-37 (free rolling, before impact), a = 2·p2·fps².

## Key results
- Circle centres, frames 6-37: a = −0.413 ± 0.009 m/s², v(12) = 3.79 m/s. Sub-windows give 6-24: −0.420,
  10-30: −0.439 and 16-37: −0.397, so the deceleration is roughly constant.
- Second route: the blue-mask centroid instead of the circle centre gives −0.415. A linear fit of the per-frame speeds
  gives −0.412 to −0.414.
- Sensitivity: VP x ±50 px changes a by ±0.015. f ±10 % changes a by ∓0.025.
- The per-frame backward-difference speeds are too noisy (±0.15 m/s) to difference directly at frame 12. The
  constant-deceleration fit is used as the acceleration at t = 0.5 s.

## Answer
The ball decelerates at about 0.41 m/s² (magnitude; the scalar speed is falling). Confidence: moderate-high,
roughly ±7 %.
