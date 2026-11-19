# q_1842 — width of the black car (m)

2D top-down simulation, 24 fps (the file's fps and question_fps agree). Prior: black car speed = 26.085 m/s (constant).

## Scale from speed
- Track: scene/tracks/car_dark.csv, template-fit centres. Per-frame steps from frame 2 to 47: mean 27.19 px/frame,
  median 27.29, scatter about ±1 px (the speed is constant). With a 5-frame moving-average path: 27.05 px/frame
  (this cuts the curve slightly). Adopted 27.15 px/frame = 651.6 px/s.
- Scale = 26.085 / 651.6 = 0.04003 m/px.

## Pixel width (measure.py, measure2.py)
- Minimum-area rectangle of the mask at RGB min ≤ 235, over 37 clean frames: median width 49.4 px. This threshold
  includes anti-aliased pixels, so it runs ~1 px large.
- Near-vertical frames 12–14, rows thresholded at 50 % (mean < 150): widest row 48 px (mirrors included), body about 46–47 px.
- Median row width along the car axis is 45.6 px (body only, without mirrors).
- Adopted the full bounding-box width including mirrors: 48.5 px. The reference uses the world bounding box, which includes the mirrors.

## Answer
48.5 px × 0.04003 = 1.94 m. Range: 1.98 (49.4 px) down to 1.83 (body only, 45.6 px). Answer **1.95 m**.
Check: the length is 115.8 px × 0.04 = 4.64 m, so the car is 4.6 × 1.95 m, a plausible real car (and in proportion).
Confidence: moderate-high (±4 %). The main uncertainty is whether the mirrors count in the width.
