# q3085: height of the green bottle (cm)

Prior: rolling cylinder velocity = 107.3 cm/s. This is an internet video, so I used one planar scale = prior / pixel speed.
Time base: the file's rate (30.013 fps) and question_fps (30) differ by less than 0.05%, so the choice doesn't matter. I used 30.

## Cylinder pixel speed (measure.py, from scene/tracks/cylinder.csv; the camera drift is negligible, and the stabilised centroid was used)
- Mean per-frame speed of the centroid over the fully visible frames 4-30: 1839 px/s (stabilised) and 1834 px/s (raw). The net displacement gives 1835 px/s.
- Leading-edge (bbox_x0) route over the same frames: 1784 px/s.
- The cylinder speeds up slightly: 1720 px/s in frames 4-12 and 1890 px/s in frames 13-30.
- Value used: 1835 px/s, so the scale is 107.3 / 1835 = 0.05847 cm/px.

## Bottle pixel height (frame 44, clean)
- Intensity profiles in columns 955, 959 and 963 put the lip top at y ≈ 147 and the base at y ≈ 723. That gives 576 px; scene/static_objects.json gives 574 px.
- I used 575 px.

## Answer
575 × 0.05847 = 33.6 cm. That is a plausible size for a wine bottle.

## Second-route check and sensitivity
- The leading-edge speed (1784 px/s) gives 34.6 cm.
- The early-only speed gives 35.9 cm, and the late-only speed gives 32.6 cm.
- So the answer is within about ±5%. Confidence: moderate to good.
