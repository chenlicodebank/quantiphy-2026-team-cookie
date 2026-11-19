# Q756 – height of the black cat including its tail (m)

2D scene (the cat walks along a desk against a wall, static camera), so I used one metres-per-pixel scale taken from the prior (cat speed 0.714 m/s). fps = question_fps = 24.

## Measurements (measure.py, using scene/tracks/cat.csv, checked on frame 12 at 3x zoom)
- Pixel speed of the cat: linear fit of the torso-centroid x over frames 0–49 gives 8.96 px/frame. The endpoint net speed is 9.11 px/frame. The mean per-frame step is 9.19, but that is inflated by about ±3 px of gait jitter. I used ≈9.03 px/frame = 216.7 px/s.
  Scale = 0.714 / 216.7 = 0.003295 m/px (range 0.00326–0.00332).
- Height including the tail = full-mask bbox height: from the raised tail tip (y≈596–606) to the paws on the desk (y≈742). The median is 145 px (range 137–148, mean 143.4). On frame 12 I read the tail tip at y≈605 and the paws at y≈742, which matches the bbox.
- Height = 145 × 0.003295 ≈ 0.478 m. Using the mean bbox height instead gives 0.472 m.

## Check
- Scales from the fit and from the endpoint speed give 0.481 and 0.474 m.
- The mask centroid gives the same speed (8.95 px/frame).
- Sanity check: the height without the tail is 106 px ≈ 0.35 m, and the desk height is 258 px ≈ 0.85 m. Both are plausible.

Answer 0.477 m. Confidence is fairly high (±3%). The spread comes from the tail pose changing during the gait.
