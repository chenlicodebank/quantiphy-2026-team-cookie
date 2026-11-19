# Q606: diameter of the white fur carpet (m)

The prior is "speed of the black cat = 0.94 m/s". scene/ calls this animal a "dog", but it is the only moving black
animal: about 191 px long and walking right. The scene is 2D (top-down camera, fixed), so one metres-per-pixel scale
comes from the prior. fps is 24 and question_fps is 24, so there is no re-timing issue.

## Scale (from the cat)
- I used scene/tracks/dog.csv and checked it again. The motion is steady with no acceleration. The linear-fit slope
  is 10.99 px/frame for torso_cx, 11.00 for mask_cx, 11.01 for the torso bbox centre and 10.98–11.00 for nose_x. The
  mean per-frame |dp| is 11.03–11.10, a little high because of gait jitter. I used 11.0 px/frame = 264 px/s.
- Scale = 0.94 / 264 = 0.003561 m/px. Sanity check: the cat is 0.68 m nose to tail tip, which is plausible.

## Rug diameter (rug2.py)
- I cast radial rays from the approximate centre over the visible left, top and bottom edges. The right side is
  hidden under the sofa. On each ray I took the first crossing of the blurred grey level (σ = 6) below a threshold
  between rug (~155) and carpet (~115), then fitted a circle with an algebraic fit and outlier rejection.
- At threshold 134 the diameter is 479.4 px. Thresholds 128 and 140 give 486 and 472 px. The fit residual SD is
  ~2.7 px and the result is the same in frames 0, 30 and 49. The overlay in frames/rugfit.png matches the edge.
- 479.4 px × 0.003561 = **1.707 m**.

## Second route
The vertical extent of the rug at x ≈ 400 in the scene record is 396–870 (≈ 475 px), which gives 1.69 m and agrees
within 1%. The threshold range (472–486 px) puts the answer between 1.68 and 1.73 m.

Confidence: good (±3%). The main uncertainty is how much of the soft fur fringe the reference bounding box
includes.
