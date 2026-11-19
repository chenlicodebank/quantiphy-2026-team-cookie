# q_586 — length of the wooden bench (m)

Prior: black cat speed = 0.94 m/s. The clip is a 2D top-down view (Blender render) with a static camera. fps = question_fps = 24, so no re-timing.

## Scale (from the black cat)
- `measure.py` reads scene/tracks/black_cat.csv. The cat walks steadily along +x and its y stays within ±3 px.
  - body centroid: net 10.970 px/frame (linear-fit slope 10.935)
  - head-front edge: 10.980 px/frame (fit 10.978)
  - full-mask centroid: 10.958 px/frame
- I used 10.97 px/frame, which is 263.3 px/s. Scale = 0.94 / 263.3 = 0.003570 m/px.
- The per-frame centroid steps carry ±4 px of gait noise. The rig root moves smoothly, so I used the steady drift rather than the mean of the noisy steps.

## Bench
- `bench.py` masks wood pixels in frame 0 (HSV saturation > 110, hue < 25). The carpet's saturation is about 75–85.
  - Rows y = 190, 230 and 270 span x = 244–531, so the slat top is 288 px long along its long axis (x).
  - Columns span y ≈ 170–289, about 120 px wide.
- The record's static bbox (289 x 120 px) agrees.
- Perspective: a few leg and shadow pixels show at the bottom-right, offset by only about 3–5 px. With the bench about 500 px from the image centre, that means the height-to-camera-height ratio is about 1%, so the magnification is negligible.

## Result
Length = 288 px × 0.003570 m/px = 1.028 m, reported as **1.03 m**.

Second check: the record's independently measured bench width of 289 px and the head-edge speed of 10.98 px/frame give 1.032 m. A bench width of 120 px works out to 0.43 m, which gives a plausible 1.03 × 0.43 m slatted bench.

Confidence: good, about ±3%. The main uncertainty is how the cat's origin speed maps to the prior.
