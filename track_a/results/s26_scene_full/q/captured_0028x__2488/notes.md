# q_2488 – acceleration of ping pong ball at t = 1.0 s (frame 24 at 24 fps; file fps = question fps = 24)

## Method (lab method card)
- At frame 24 the ball is in free fall: it is released at about frame 20.7 and first bounces at about frame 26.2.
- I re-tracked the ball in a tight crop (x 705–765, y 270–415, gray > 90) for frames 19–25 (`measure.py`). The centroids match scene/tracks/ball.csv to within about 1 px.
- I fitted quadratics to the centroid over windows around frame 24:
  - y acceleration: 8.47 (frames 21–24), 8.62 (21–25), 8.59 (22–25), 7.94 (22–24) and 9.25 (23–25) px/frame²
  - x acceleration: about 0
  - Representative value: **8.6 px/frame²**
  - The top and bottom edges of the blur streak give 7.9–9.4, which is consistent.
- Scale: f = 0.5959 × 1280 = 763 px, depth at t = 1.0 s = 1.805 m (from depth_info).
  a = 8.6 × 1.805 / 763 × 24² = 11.7 m/s² = **≈1170 cm/s²**

## Second route
- Fall from the release apex (cy ≈ 291, frame ≈ 20.7) to contact (centre ≈ 417, frame ≈ 26.2): a = 2 × 126 / 5.5² = 8.3 px/frame², which gives ≈1135 cm/s². This agrees to within 3%.

## Caveat
- The ball's pixel size (≈20 px wide, so 763 × 0.04 / 20 ≈ 1.53 m) suggests the ball is nearer than the given 1.805 m. At that depth the result would be ≈1000 cm/s², close to g.
- I followed the rule that depth_info is the scale, so I answered 1170.
- Confidence: moderate. The answer depends on the reference's depth convention.
