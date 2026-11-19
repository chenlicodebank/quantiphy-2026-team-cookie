# q29 — width of the green car (simulation_0054)

- Scene: 2D top-down view of a road with a static camera. The car the scene record calls "black_car" is actually **dark green** (checked on a zoomed crop, frame 45). It is the only non-orange car, so it is the green car.
- fps: 30.003 (file) vs 30.0 (question). The difference is negligible (0.01%).

## Scale from the prior (orange car acceleration = -2.86 m/s^2)
I fitted a quadratic to the orange car's centre y over frames where it is fully in view (`fit.py`). The fit residuals are about 0.5 px rms:
- bbox centre: -163.0 (f16-90), -163.5 (f25-90), -163.0 (f40-90), -161.5 (f16-60), -162.0 (f50-90) px/s^2
- mask centroid: -159.5 to -161.7 px/s^2
- cubic fit: acceleration -161.5 to -164.5 px/s^2 across the window, so it is essentially constant.
- Adopted value: -162 px/s^2, giving a scale of 2.86/162 = 0.01765 m/px.

## Green car width
I measured the green car over frames 38-70 (fully in view) with my own background-difference masks (`width.py`). The overlay in frames/mask55.png covers the whole car.
- Mask bbox x-extent: 122 px at threshold 40 (close to the half-contrast edge); 128 at threshold 25 (picks up blur/anti-aliasing); 118 at threshold 60.
- Scene record: wid_px median 121 (119-122) and bbox width 121.
- Adopted: 121.5 px across the car (the full extent, as an axis-aligned bounding box would measure it).

Width = 121.5 x 0.01765 = **2.15 m**.

## Checks
- The green car's length is 292 px, which converts to 5.15 m. The orange car's 293 px converts to 5.17 m. Both are consistent with a 2.15 m width at the same scale; the scene is not at real-world scale.
- Sensitivity: the edge threshold (118-128 px) gives 2.08-2.26 m; the acceleration fit (160-163.5) moves the answer by about ±1%.
- Confidence: good, with an expected error of about 3-5%.
