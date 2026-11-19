# Q150 — height of the car (prior: car length = 5.67 m)

2D side-view render, static camera, fps 24 = question_fps (no re-timing issue; size question anyway).
The car (white Cybertruck-style pickup, lower object) moves right→left; checked visually on frame 33 (frames/car.png).
Scale is taken from the car itself, so height = 5.67 m × (pixel height / pixel length).

Measurements (code):
* `measure.py` — median background + |diff|>12 mask, bbox per frame 3-65: height 43 px constant, length 128-130 px
  near the image centre, rising to 137 px at the image edges (end faces seen off-axis in a perspective render).
  Mask ratio near centre → 1.87-1.90 m.
* `subpix.py` — sub-pixel edges (crossing at half the local contrast, per column/row, so dark wheels and white body
  are each handled), frames 28-45: H = 42.4 px (roof 631.2 → wheel bottoms 673.6), L = 128.4-128.9 px for frames
  33-41 (car centred near x≈960, cleanest side-on view). Ratio × 5.67 = 1.866-1.875 m; median over 28-45 = 1.864 m.

Second route: the threshold-mask bbox (route 1) gives 1.87-1.90 m at the centre; the sub-pixel route gives 1.87 m.
Sanity check: a real Cybertruck is 5.68 m long and about 1.79-1.91 m high, which fits.

Answer: **1.87 m**. Confidence: good (±2 %). The main uncertainty is the slight perspective at the roof and wheels.
