# Q79 – distance walker ↔ bike at t = 0.5 s (frame 12, 24 fps; file fps = question fps)

Scene: static top-down camera, cyclist (lower lane) and walker (upper lane) both moving -x. Prior: bike length 1.7 m.

## Measurements (frame 12)
- Bike: front tip x 1056, rear tip x 1469, axis y 649 → centre (1262.5, 649). Tip-to-tip 412–414 px (scene record checked on the frame).
- Walker: hair-blob centroid (1756.7, 437.0) (scene record checked against a zoomed crop).
- Perspective (handlebar.py): the handlebar grips (~1.0 m high) shift against the front wheel tip (~0.34 m)
  by 0.0356 px per px of image position over frames 4–32. That gives a camera height of D ≈ 19.5 m (18–22.5 m depending on
  the assumed bike geometry) and f ≈ 4600 px (HFOV ≈ 23°). The bike's length also changes with position (slope 0.0065), which matches
  this parallax. Check by eye: at frame 17 the head sits ~65 px right of the feet, and at frame 68 (near the image centre) about 0 px; the model predicts ~57 and ~0.
- I back-projected the head to world XY at hair height (~1.68 m), taking the pelvis to be vertically below it, and the bike centre at tip height.
  The horizontal pelvis–bike distance is **2.005 m** (range 1.99–2.03 over the geometry variants; distance.py).

## Other conventions
- 3D distance with the bike root at axle height: 2.08–2.14 m. With the root on the ground: 2.21–2.27 m.
- One naive scale (412 px = 1.7 m) applied to the head point: 2.22 m.

## Answer
This is a 2D-type video (top-down view, motion in the plane facing the camera), so the in-plane distance (~2.01 m) is
the main estimate. While walking the pelvis tends to sit slightly behind the head, which makes the distance a bit larger, and the
reference may be 3D. Answer: **2.1 m**, which is within ~5% of the in-plane value, the axle-height 3D value and the naive single-scale value.
Confidence: moderate (the main uncertainty is which convention the reference used).
