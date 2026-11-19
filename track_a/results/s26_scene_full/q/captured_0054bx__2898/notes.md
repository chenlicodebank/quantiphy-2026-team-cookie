# q 2898: velocity of the green ball at 1.5 s (frame 36)

The green ball is the small tennis ball. In scene/ it is called `yellow_ball` (the white one is `white_ball`, the orange one is
the basketball). Both question_fps and the file rate are 24, so t = 1.5 s is frame 36. Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).

## Measurements (scripts in this folder)
- `measure_green.py`: masks the yellow pixels and gives the centre (cx, cy) for each frame. The centres agree with
  scene/ ref_x/ref_y to about 1 px. The overlays in frames/green_*.png were checked by eye.
- `diam_fg.py`: diameter = width of the full foreground (including the pale rim) across the motion direction, at
  the 50 % brightness edge. This avoids the motion-blur streak. W(f24) = 38.5 px (38.2 after smoothing) and W(f36) = 23.5 px.
- Ball size = 1.331 m x 38.2 / 762.8 = 0.0666 m. That matches a tennis ball (6.7 cm), which is a good consistency check.
- Depth at each frame = 0.0666 x f / W, which gives Z(f36) ≈ 2.18-2.20 m. 1/W rises linearly before the bounce, which fits a ballistic
  depth rate of about 1.5 m/s.
- Events: the bounce (lowest image point) is at f37. A recording frame is missing between f35 and f36: the image step
  doubles, and the 1/W trend also needs 2 frames there.

## Prior check (basketball, 0.5 s = f12, prior 2.21 m/s)
With depth interpolated between the given values (2.24 m at f12, 1.81 m at f24), back-projected centres, and the mean
of the per-frame forward speeds over f10-f14, I get 2.20 m/s. That reproduces the prior, so this is the 5-frame smoothing
convention I use. The chord over the same window gives 2.29 m/s.

## Green ball at f36 (velocity.py, fit_green.py)
- Mean of the forward speeds over f34-f38 (the same convention as the prior check): 2.94 m/s. Depth comes from the smoothed diameter.
- Second route: a quadratic 3D fit to the pre-bounce flight, with real time shifted +1 frame for the missing frame
  (rms 1.5-5 mm), gives v(f36) = 2.94 / 3.11 / 3.23 m/s for the windows f30 / f28 / f26-36.
  The post-bounce fit gives 2.4-2.6 m/s just after the bounce.
- The chord estimates are lower (1.9-2.3 m/s) because their window spans the bounce, where the direction reverses.
- Answer: 2.9 m/s. Confidence is moderate. The main uncertainties are the reference's unknown per-frame sensor depth,
  how its smoothing treats the bounce and the missing frame, and the ±1 px diameter (about ±4 % depth).
