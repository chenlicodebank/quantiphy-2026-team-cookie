# Q1783 – length of the white car (m)

2D top-down render, 24 fps (file fps = question fps). The white car is the white van in scene/ (left, drives straight up from rest, uniformly accelerating). Prior: its acceleration = 4 m/s^2.

## Scale from prior (fit.py)
Quadratic fit of centroid y(t) from scene/tracks/white_van.csv:
- frames 0-71: a = 160.8 px/s^2 (centroid), 160.5 (rotated-rect centre)
- sub-windows 0-40: 160.3/160.8; 30-72: 162.0/161.5; 10-60: 160.4/159.9
=> a ≈ 160.6 px/s^2 → scale = 4 / 160.6 = 0.02491 m/px.

## Length in pixels (length.py)
Vertical extent of the van (darkness 255-min(RGB) ≥ 10 over the body columns), frames 0..71:
248, 245, 246, 246, 242, 239, 238, 238, 244 px (mean 243). Rotated-rect lengths in the record: 236-246, median 240.
The slight variation with image position (smaller mid-frame) is matched by averaging over the same frames as the acceleration fit. Use 243 px.

## Answer
243 × 0.02491 = 6.05 m. Range across length readings (238-248 px): 5.9–6.2 m.
Check: the two independent position references (centroid and rect centre) and several fit windows give the same acceleration to within 1%.
Confidence: good (≈ ±3%).
