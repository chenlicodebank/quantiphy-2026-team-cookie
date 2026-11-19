# q_587: width of the wooden bench (m)

Prior: the black cat's speed is 0.94 m/s. depth_info: none. fps = question_fps = 24.

The view is top-down, so I used one metres-per-pixel scale on the floor plane, set by the black cat's speed.

- **Black cat speed (measure.py, scene tracks):** it walks steadily along +x. The linear-fit slope is 10.94 px/frame for body_cx, 10.96 for cx and 10.98 for the head edge bbox_x1. The mean per-frame step of the body centroid is 10.98. I used 10.97 px/frame, which is 263.3 px/s.
  The scale is 0.94 / 263.3 = 0.003570 m/px.
- **Bench (bench2.py, frame 25, saturation > 110 profiles):**
  - Its long side runs along x: 244–532, so 288–289 px (matches the record's 289).
  - Its short side runs along y: about 172 to 285–291 depending on the column. That gives 114–120 px; the centre column gives 118. The record says 120.
  - Width = the short horizontal extent, about 118 px, so 118 × 0.00357 = **0.42 m**. The length would be 289 px, about 1.03 m.
- **Check:** the scene record's frame-0 box (120 px) gives 0.428 m. Bench proportions of 1.03 × 0.42 m look plausible.
- **Caveat:** the camera has perspective, and the bench top sits higher than the cat's origin, so it may be magnified by a few percent. The camera height is unknown (the wall tops are outside the frame), so I made no correction. A slight correction would bring the answer to about 0.41.

Confidence: moderate to good, about ±5%.
