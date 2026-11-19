# Q820 – height of the antelope (m)

- I took the "antelope" to be the large horned creature that walks left to right. The 2D convention applies: static camera, motion parallel to the image plane, and one m/px scale.
- Scale comes from the prior, speed = 1.277 m/s. The creature's image speed is taken from the landmark tracks (measure.py): shoulder net 6.603 px/frame (linear fit 6.610), hip 6.73 px/frame, body_mid 6.38 px/frame. I used about 6.61 px/frame (shoulder; the most stable track, and close to the mean of hip and shoulder), which gives 198.3 px/s.
  - That gives 1.277 / 198.3 = 0.00644 m/px.
- Height comes from the bbox, horn tip to hooves: median 421 px (p10–p90 410–426), with the top at y ≈ 1124–1138 and the hooves at ≈ 1547. A zoom on frame 30 roughly agrees on the top. I used about 418 px, so 418 × 0.00644 = 2.69 m, answered as 2.70 m.
- Cross-check: using the hip speed (6.73 px/frame) gives 2.65 m; using the median height of 421 px gives 2.71 m. The range is 2.65–2.75 m.
- Plausibility: the creature is a fantasy ibex/deer with very long horns, so a total height of 2.7 m including the horns is credible. The rabbit (73 px long) comes out at about 0.47 m, which is a little large but within the plausible range.
- Confidence: moderate-high (±5%).
