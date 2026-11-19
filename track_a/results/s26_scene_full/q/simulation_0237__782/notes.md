# q_782 — length of the brown horse (m)

Prior: speed of the horse at the back = 0.874 m/s. Only one horse in the clip (the chestnut horse walking right
below the house), so the prior and the question refer to the same animal. 2D top-down scene, fps 24 = question_fps.

## Scale (from the prior)
- Track scene/tracks/horse.csv (trunk reference point, template matched, verified static camera):
  mean per-frame step 2.658 px (median 2.669, net/49 = 2.641). Steady walk, no acceleration.
- Pixel speed = 2.658 x 24 = 63.8 px/s -> scale = 0.874 / 63.8 = 0.01370 m/px.

## Length in pixels (measure.py)
- Rump (red body mask left end) to nose tip (end of white blaze), every 4th frame: 140–144 px, median 142;
  overlays frames/ov_0/24/48.png confirm rump and nose tip. Scene record's clean-frame bbox_w ≈ 143–149 (best 145)
  includes grass specks. Using 143 px.

## Answer
length = 143 px x 0.01370 m/px = 1.96 m (range 1.92–1.99 for 140–145 px).

Check: second route with net displacement (2.641 px/frame) gives scale 0.01379 -> 1.97 m; consistent.
Confidence: moderate-high (±3 %); main uncertainty is the true rig-root speed vs trunk speed and tail/nose extent.
