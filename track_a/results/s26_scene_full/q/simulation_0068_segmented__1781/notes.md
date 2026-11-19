# Q1781 – width of the turning yellow (beige) car

2D top-down render, 24 fps (file fps = question_fps, no retiming). Turning car = scene record's `beige_car`; white car = `white_van` (straight, uniformly accelerating).

## Scale (prior: white car acceleration = 4 m/s^2)
`accel.py`: quadratic fit of van y(t). Centroid: 160.8 px/s^2 (full clip, first/second half 160.9 / 161.6); rotated-rect centre 160.5; front edge 161.9. Use 160.8 px/s^2 -> 4/160.8 = 0.02488 m/px.

## Width in pixels
`width.py`: widths across the car axis on straight frames (0-2 heading up, 64-71 heading +x), central half of the car:
- half-max width of the mean profile: 79.4-81.6 px (about 80)
- per-row mask span, threshold 15: median 79-81, max 82-84 (mirrors / anti-aliasing)
- The record's width_px (87, threshold 6, rotated rect) is inflated by soft edges and by turning frames, so I didn't use it.
Chosen value: 81.5 px. It sits between the body width (80) and the width including mirrors (~83), since the bounding box would include the mirrors.

## Answer
81.5 x 0.02488 = 2.03 m (range 1.99 m for the body only to 2.07 m with mirrors).
Second check: the van's width of about 91 px gives 2.26 m and its length of 240 px gives 5.97 m. The assets are on the large side, but the two cars are in a consistent ratio.
Confidence: good. The scale is consistent to within 1%, and the width is uncertain by about 2-3%.
